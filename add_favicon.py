import os
import re

# Directory containing the HTML files
template_dir = r'c:\Users\DELL\Desktop\school_proj\core\templates\core'

# Favicon line to add
favicon_line = '    <link rel="icon" type="image/png" href="{% static \'core/images/school_logo.png\' %}">\n'

# Get all HTML files
html_files = [f for f in os.listdir(template_dir) if f.endswith('.html')]

for html_file in html_files:
    file_path = os.path.join(template_dir, html_file)
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Check if favicon is already present
    if 'rel="icon"' in content or 'favicon' in content.lower():
        print(f"Skipping {html_file} - favicon already present")
        continue
    
    # Add favicon after the title tag
    pattern = r'(\s*<title>.*?</title>\n)'
    replacement = r'\1' + favicon_line
    
    new_content = re.sub(pattern, replacement, content, count=1)
    
    if new_content != content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Added favicon to {html_file}")
    else:
        print(f"Could not add favicon to {html_file}")

print("\nDone!")
