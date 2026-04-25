import os

styles_path = 'styles.css'
with open(styles_path, 'r', encoding='utf-8') as f:
    styles = f.read()

expert_css = """
/* ── Expert UI Polish ── */
/* Animations */
@keyframes fadeInUp {
  from { opacity: 0; transform: translateY(15px); }
  to { opacity: 1; transform: translateY(0); }
}
.card, .qa-block, .formula, .table-responsive {
  animation: fadeInUp 0.5s cubic-bezier(0.16, 1, 0.3, 1) both;
}
.card:nth-child(1) { animation-delay: 0.05s; }
.card:nth-child(2) { animation-delay: 0.1s; }
.card:nth-child(3) { animation-delay: 0.15s; }
.card:nth-child(4) { animation-delay: 0.2s; }

/* Enhanced Typography & Spacing */
h1.hero { font-size: 3rem; font-weight: 800; line-height: 1.1; margin-bottom: 1rem; letter-spacing: -1px; }
h1.hero span { 
  background: linear-gradient(135deg, #7c6dfa, #38bdf8);
  -webkit-background-clip: text; -webkit-text-fill-color: transparent;
}
.eyebrow { font-size: 0.85rem; font-weight: 700; color: var(--accent); text-transform: uppercase; letter-spacing: 2px; margin-bottom: 0.5rem; }

/* Responsive Overrides */
@media (max-width: 900px) {
  .topbar { flex-wrap: wrap; gap: 15px; }
  .topbar-info h2 { font-size: 1.1rem; }
  h1.hero { font-size: 2.2rem; }
  .page-title { font-size: 1.7rem; line-height: 1.2; }
  .card { padding: 1.25rem; }
  .qa-header { padding: 1rem; }
  .qa-body { padding: 1rem; }
  .formula { padding: 1rem; font-size: 0.85rem; }
  .section-label { font-size: 0.7rem; }
  .table-responsive { margin: 1rem -1.5rem; width: calc(100% + 3rem); border-radius: 0; border-left: none; border-right: none; }
  .data-table th, .data-table td { padding: 0.6rem 0.8rem; font-size: 0.8rem; }
  
  /* Make sure math containers don't break flex/grid layouts on mobile */
  mjx-container { overflow-x: auto; overflow-y: hidden; max-width: 100%; display: block; padding: 0.5rem 0; -webkit-overflow-scrolling: touch; }
}

/* Scrollbar styling for entire page */
::-webkit-scrollbar { width: 8px; height: 8px; }
::-webkit-scrollbar-track { background: var(--bg); }
::-webkit-scrollbar-thumb { background: rgba(255,255,255,0.15); border-radius: 8px; }
::-webkit-scrollbar-thumb:hover { background: rgba(255,255,255,0.25); }
[data-theme="light"] ::-webkit-scrollbar-thumb { background: rgba(0,0,0,0.15); }
[data-theme="light"] ::-webkit-scrollbar-thumb:hover { background: rgba(0,0,0,0.25); }
"""

if '/* ── Expert UI Polish ── */' not in styles:
    styles += expert_css
    
with open(styles_path, 'w', encoding='utf-8') as f:
    f.write(styles)

# Commit and push
import subprocess
subprocess.run(['git', 'add', '.'], check=True)
subprocess.run(['git', 'commit', '-m', 'Apply expert-level UI polish, fix mobile table cutoff, add animations and typography enhancements'], check=True)
subprocess.run(['git', 'push', 'origin', 'main'], check=True)

print("Expert CSS polish applied and pushed successfully!")
