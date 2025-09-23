import re
import sys
import os

# Read learning.md
try:
    with open('learning.md', 'r', encoding='utf-8') as f:
        learning_content = f.read().rstrip()
except FileNotFoundError:
    print("ERROR: learning.md not found", file=sys.stderr)
    sys.exit(1)

# Read README.md
readme_path = 'README.md'
if os.path.exists(readme_path):
    with open(readme_path, 'r', encoding='utf-8') as f:
        readme = f.read()
else:
    readme = ''

# Markers
start_marker = '<!--START_SECTION:learning-->'
end_marker = '<!--END_SECTION:learning-->'
replacement = f"{start_marker}\n{learning_content}\n{end_marker}"

pattern = re.compile(re.escape(start_marker) + r'.*?' + re.escape(end_marker), re.DOTALL)

if pattern.search(readme):
    new_readme = pattern.sub(replacement, readme)
else:
    if readme and not readme.endswith('\n'):
        readme += '\n'
    new_readme = readme + '\n' + replacement

if new_readme != readme:
    with open(readme_path, 'w', encoding='utf-8') as f:
        f.write(new_readme)
    print("README.md updated")
else:
    print("No changes needed")
