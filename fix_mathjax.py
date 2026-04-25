import os, glob

for f in glob.glob('*.html'):
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Replace single backslash escaped version
    content = content.replace(r"inlineMath:[['\\(','\\)']]\",", r"inlineMath:[['$','$'], ['\\(','\\)']],")
    content = content.replace("inlineMath:[['\\\\(','\\\\)']],", "inlineMath:[['$','$'], ['\\\\(','\\\\)']],")
    
    with open(f, 'w', encoding='utf-8') as file:
        file.write(content)
print("MathJax fixed in all HTML files.")
