const express = require('express');
const fs = require('fs');
const path = require('path');
const app = express();
const PORT = process.env.PORT || 10000;

// ============================================================
// CONFIG
// ============================================================
const ADMIN_PASSWORD = "Noobster@2024";
const TELEGRAM_CHANNEL = "https://t.me/firebase1991";

// ============================================================
// LOAD HTML FROM FILE (no escaping issues!)
// ============================================================
const pageHTML = fs.readFileSync(path.join(__dirname, 'panel-otp.html'), 'utf-8');

// ============================================================
// ROUTES
// ============================================================
app.get('/', (req, res) => res.send(pageHTML));
app.get('/admin', (req, res) => res.send(pageHTML));
app.get('*', (req, res) => res.send(pageHTML));

app.listen(PORT, '0.0.0.0', () => {
    console.log(`✅ Server running on port ${PORT}`);
    console.log(`🌐 Panel: http://localhost:${PORT}/`);
    console.log(`🔐 Admin: http://localhost:${PORT}/admin?admin=1`);
    console.log(`🔑 Password: ${ADMIN_PASSWORD}`);
});
