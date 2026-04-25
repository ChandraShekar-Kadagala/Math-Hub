import os
import glob
import subprocess

# 1. Create manifest.json for PWA
manifest_content = """{
  "name": "MAT 223 Hub",
  "short_name": "Math Hub",
  "description": "Complete Exam Preparation Hub for MAT 223",
  "start_url": "/index.html",
  "display": "standalone",
  "background_color": "#0b0f1a",
  "theme_color": "#7c6dfa",
  "icons": [
    {
      "src": "https://cdn-icons-png.flaticon.com/512/3501/3501061.png",
      "sizes": "512x512",
      "type": "image/png"
    }
  ]
}"""
with open('manifest.json', 'w', encoding='utf-8') as f:
    f.write(manifest_content)

# 2. Advanced CSS
advanced_css = """
/* ── 30-Year Expert Level Upgrades ── */

/* Active Recall Mode (Blur answers) */
body.active-recall-mode .qa-body {
  filter: blur(8px);
  opacity: 0.7;
  transition: all 0.3s ease;
  cursor: pointer;
  user-select: none;
}
body.active-recall-mode .qa-body:hover {
  filter: blur(4px);
  opacity: 0.9;
}
body.active-recall-mode .qa-body.revealed {
  filter: blur(0);
  opacity: 1;
  cursor: default;
  user-select: auto;
}

/* Study Timer Widget */
.timer-widget {
  margin: 0.75rem;
  background: linear-gradient(135deg, rgba(124,109,250,0.1), rgba(56,189,248,0.1));
  border: 1px solid rgba(124,109,250,0.3);
  border-radius: var(--radius);
  padding: 1rem;
  text-align: center;
}
.timer-display {
  font-size: 2rem;
  font-weight: 800;
  font-variant-numeric: tabular-nums;
  color: var(--accent2);
  margin: 0.5rem 0;
  text-shadow: var(--glow);
}
.timer-controls button {
  background: var(--surface2);
  border: 1px solid var(--border);
  color: var(--text);
  padding: 4px 12px;
  border-radius: 6px;
  cursor: pointer;
  font-weight: 700;
  margin: 0 4px;
}
.timer-controls button:hover { background: var(--accent); color: white; }

/* Scroll to Top FAB */
.fab {
  position: fixed;
  bottom: 2rem;
  right: 2rem;
  width: 50px;
  height: 50px;
  border-radius: 50%;
  background: linear-gradient(135deg, var(--accent), var(--accent2));
  color: white;
  border: none;
  font-size: 1.5rem;
  cursor: pointer;
  box-shadow: 0 10px 20px rgba(0,0,0,0.3);
  opacity: 0;
  visibility: hidden;
  transform: translateY(20px);
  transition: all 0.3s ease;
  z-index: 1000;
}
.fab.visible {
  opacity: 1;
  visibility: visible;
  transform: translateY(0);
}
.fab:hover { transform: translateY(-3px) scale(1.05); }

/* Topbar utility buttons container */
.topbar-actions {
  display: flex;
  align-items: center;
  gap: 10px;
}

/* Print Styles (Ctrl+P to get clean PDF) */
@media print {
  .sidebar, .topbar, .theme-btn, .menu-btn, .fab, .progress-widget, .timer-widget { display: none !important; }
  .main { margin: 0 !important; width: 100% !important; background: white !important; color: black !important; }
  body { background: white !important; color: black !important; }
  .card, .qa-block { border: 1px solid #ccc !important; break-inside: avoid; background: white !important; box-shadow: none !important; }
  * { color: black !important; -webkit-text-fill-color: black !important; }
  .page-title span { background: none !important; color: black !important; }
  mjx-container { overflow: visible !important; }
}
"""

with open('styles.css', 'a', encoding='utf-8') as f:
    f.write(advanced_css)

# 3. Advanced JS
advanced_js = """
// ── 30-Year Expert Level JS Upgrades ──

document.addEventListener('DOMContentLoaded', () => {
    // 1. Scroll to Top
    const fab = document.createElement('button');
    fab.className = 'fab';
    fab.innerHTML = '↑';
    document.body.appendChild(fab);
    
    window.addEventListener('scroll', () => {
        if (window.scrollY > 300) fab.classList.add('visible');
        else fab.classList.remove('visible');
    });
    
    fab.addEventListener('click', () => {
        window.scrollTo({ top: 0, behavior: 'smooth' });
    });

    // 2. Active Recall Mode
    const activeRecallBtn = document.getElementById('recall-btn');
    if(activeRecallBtn) {
        let recallMode = localStorage.getItem('recallMode') === 'true';
        
        const updateRecallUI = () => {
            if(recallMode) {
                document.body.classList.add('active-recall-mode');
                activeRecallBtn.innerHTML = '🧠 Recall: ON';
                activeRecallBtn.style.background = 'var(--accent)';
                activeRecallBtn.style.color = 'white';
            } else {
                document.body.classList.remove('active-recall-mode');
                activeRecallBtn.innerHTML = '🧠 Recall: OFF';
                activeRecallBtn.style.background = 'var(--surface2)';
                activeRecallBtn.style.color = 'var(--text)';
            }
        };
        
        updateRecallUI();
        
        activeRecallBtn.addEventListener('click', () => {
            recallMode = !recallMode;
            localStorage.setItem('recallMode', recallMode);
            updateRecallUI();
        });
        
        // Reveal on click
        document.querySelectorAll('.qa-body').forEach(body => {
            body.addEventListener('click', () => {
                if(document.body.classList.contains('active-recall-mode')) {
                    body.classList.add('revealed');
                }
            });
        });
    }

    // 3. Pomodoro Timer
    const minDisplay = document.getElementById('t-min');
    const secDisplay = document.getElementById('t-sec');
    const playBtn = document.getElementById('t-play');
    const resetBtn = document.getElementById('t-reset');
    
    if(minDisplay && secDisplay && playBtn && resetBtn) {
        let timeLeft = 25 * 60;
        let timerId = null;
        let isRunning = false;
        
        const updateTimerUI = () => {
            const m = Math.floor(timeLeft / 60).toString().padStart(2, '0');
            const s = (timeLeft % 60).toString().padStart(2, '0');
            minDisplay.textContent = m;
            secDisplay.textContent = s;
        };
        
        playBtn.addEventListener('click', () => {
            if(isRunning) {
                clearInterval(timerId);
                playBtn.textContent = '▶️';
            } else {
                playBtn.textContent = '⏸️';
                timerId = setInterval(() => {
                    if(timeLeft > 0) {
                        timeLeft--;
                        updateTimerUI();
                    } else {
                        clearInterval(timerId);
                        alert("Pomodoro Session Complete! Take a 5 minute break.");
                        playBtn.textContent = '▶️';
                        isRunning = false;
                    }
                }, 1000);
            }
            isRunning = !isRunning;
        });
        
        resetBtn.addEventListener('click', () => {
            clearInterval(timerId);
            isRunning = false;
            timeLeft = 25 * 60;
            updateTimerUI();
            playBtn.textContent = '▶️';
        });
    }
});
"""

with open('app.js', 'a', encoding='utf-8') as f:
    f.write(advanced_js)

# 4. Update HTML Files
timer_html = """
  <div class="timer-widget">
    <p>⏱️ Pomodoro Timer</p>
    <div class="timer-display"><span id="t-min">25</span>:<span id="t-sec">00</span></div>
    <div class="timer-controls">
      <button id="t-play">▶️</button>
      <button id="t-reset">🔄</button>
    </div>
  </div>
"""

for file in glob.glob("*.html"):
    with open(file, 'r', encoding='utf-8') as f:
        html = f.read()
        
    # Add manifest
    if '<link rel="manifest"' not in html:
        html = html.replace('<head>', '<head>\n<link rel="manifest" href="manifest.json">\n<meta name="theme-color" content="#7c6dfa">')
        
    # Add Timer to sidebar
    if 'timer-widget' not in html:
        html = html.replace('</nav>', timer_html + '</nav>')
        
    # Restructure topbar to accommodate Active Recall button
    if 'recall-btn' not in html:
        # Find the theme-btn and wrap in topbar-actions
        if '<button class="theme-btn" id="theme-btn">☀️ Light Mode</button>\n    <button class="menu-btn"' in html:
            old_btns = '<button class="theme-btn" id="theme-btn">☀️ Light Mode</button>\n    <button class="menu-btn" id="menu-btn" style="margin-left:10px; background:var(--surface2); color:var(--text); border:1px solid var(--border); padding:0.55rem 1rem; border-radius:99px; font-weight:600; cursor:pointer; display:none;">☰ Menu</button>'
            new_btns = f'<div class="topbar-actions"><button class="theme-btn" id="recall-btn" style="margin-right:10px;">🧠 Recall: OFF</button>{old_btns}</div>'
            html = html.replace(old_btns, new_btns)
        elif '<button class="theme-btn" id="theme-btn">☀️ Light Mode</button>' in html:
            old_btns = '<button class="theme-btn" id="theme-btn">☀️ Light Mode</button>'
            new_btns = f'<div class="topbar-actions"><button class="theme-btn" id="recall-btn" style="margin-right:10px;">🧠 Recall: OFF</button>{old_btns}</div>'
            html = html.replace(old_btns, new_btns)
            
    with open(file, 'w', encoding='utf-8') as f:
        f.write(html)

# 5. Commit and Push
subprocess.run(['git', 'add', '.'], check=True)
subprocess.run(['git', 'commit', '-m', 'Add expert level features: Active Recall, Pomodoro Timer, Print PDF support, and PWA manifest'], check=True)
subprocess.run(['git', 'push', 'origin', 'main'], check=True)

print("Ultimate Upgrade Complete!")
