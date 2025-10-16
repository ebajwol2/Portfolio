const { app, BrowserWindow } = require('electron');
const WebSocket = require('ws');
const { execSync } = require('child_process');

function createWindow() {
  const win = new BrowserWindow({ width: 420, height: 300 });
  win.loadURL('data:text/html;charset=utf-8,' + encodeURIComponent(`
    <html>
      <body style="font-family: -apple-system, sans-serif; padding: 16px;">
        <h3>NeuroDesk Focus</h3>
        <div>Attention: <span id="score">--</span></div>
        <div id="status">Connecting...</div>
        <script>
          const ws = new WebSocket('ws://localhost:8765');
          ws.onopen = () => document.getElementById('status').textContent = 'Connected';
          ws.onmessage = (ev) => {
            const d = JSON.parse(ev.data);
            const s = (d.score || 0).toFixed(2);
            document.getElementById('score').textContent = s;
          };
        </script>
      </body>
    </html>
  `));
}

function setDoNotDisturb(on) {
  try {
    // macOS Shortcuts: create two shortcuts named "Focus On" and "Focus Off"
    const name = on ? 'Focus On' : 'Focus Off';
    execSync(`shortcuts run "${name}"`, { stdio: 'ignore' });
  } catch {}
}

function attachAutomation() {
  const ws = new WebSocket('ws://localhost:8765');
  let lastState = null;
  ws.onmessage = (ev) => {
    const { score } = JSON.parse(ev.data);
    const focused = score >= 0.6;
    if (lastState === null || focused !== lastState) {
      setDoNotDisturb(!focused);
      lastState = focused;
    }
  };
}

app.whenReady().then(() => {
  createWindow();
  attachAutomation();
});

app.on('window-all-closed', () => {
  if (process.platform !== 'darwin') app.quit();
});

const { app, BrowserWindow, nativeTheme } = require(electron);
const WebSocket = require(ws);
const { execSync } = require(child_process);

function createWindow() {
  const win = new BrowserWindow({ width: 420, height: 300 });
  win.loadURL(data:text/html
