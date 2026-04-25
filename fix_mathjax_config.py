import glob
import re
import subprocess

correct_mathjax = "<script>MathJax={tex:{inlineMath:[['$','$'], ['\\\\(','\\\\)']],displayMath:[['\\\\[','\\\\]']]},options:{skipHtmlTags:['script','noscript','style','textarea']}}</script>"

for file in glob.glob("*.html"):
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Replace any corrupted MathJax config with the correct one
    # Regex to catch variations like [['$','\['] or [['\[','\[']
    content = re.sub(r'<script>MathJax=\{tex:\{inlineMath:\[\[.*?\]\],displayMath:\[\[.*?\]\]\},options:\{skipHtmlTags:\[.*?\]\}\}</script>', correct_mathjax, content)
    
    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)

subprocess.run(['git', 'add', '.'], check=True)
subprocess.run(['git', 'commit', '-m', 'Fix corrupted MathJax configuration breaking rendering across files'], check=True)
subprocess.run(['git', 'push', 'origin', 'main'], check=True)
print("MathJax Config Reset and Pushed!")
