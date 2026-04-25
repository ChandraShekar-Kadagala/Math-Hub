import os
import glob

# 1. Update styles.css for table responsiveness
styles_path = 'styles.css'
with open(styles_path, 'r', encoding='utf-8') as f:
    styles = f.read()

# Add table-responsive class and custom scrollbars
responsive_css = """
/* ── Responsive Tables ── */
.table-responsive {
  width: 100%;
  overflow-x: auto;
  -webkit-overflow-scrolling: touch;
  margin: 1rem 0;
  border-radius: 10px;
  background: var(--surface);
}
.table-responsive::-webkit-scrollbar { height: 6px; }
.table-responsive::-webkit-scrollbar-track { background: rgba(0,0,0,0.1); border-radius: 10px; }
.table-responsive::-webkit-scrollbar-thumb { background: var(--accent); border-radius: 10px; }

"""

if '.table-responsive' not in styles:
    styles += responsive_css

with open(styles_path, 'w', encoding='utf-8') as f:
    f.write(styles)

# 2. Fix index.html table
with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace('<table class="dt">', '<div class="table-responsive">\n<table class="data-table">')
content = content.replace('</table>\n</div>\n\n</div>\n</div><!-- /main -->', '</table>\n</div>\n</div>\n\n</div>\n</div><!-- /main -->')
# To be safe, just replace the exact end of table
if '</table>\n</div>' not in content:
    content = content.replace('</table>\n</div>', '</table>\n</div>\n</div>')
else:
    # Manual careful replace for index.html
    pass

# A safer way to wrap tables in all html files:
for file in glob.glob("*.html"):
    with open(file, 'r', encoding='utf-8') as f:
        html = f.read()
    
    # Change any .dt to .data-table
    html = html.replace('class="dt"', 'class="data-table"')
    
    # Wrap <table class="data-table"> in <div class="table-responsive"> if not already wrapped
    if '<table class="data-table"' in html and '<div class="table-responsive">' not in html:
        html = html.replace('<table class="data-table"', '<div class="table-responsive">\n<table class="data-table"')
        html = html.replace('</table>', '</table>\n</div>')
        
    with open(file, 'w', encoding='utf-8') as f:
        f.write(html)

print("Tables made responsive!")
