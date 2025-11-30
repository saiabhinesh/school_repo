import os

# Directory containing the HTML files
template_dir = r'c:\Users\DELL\Desktop\school_proj\core\templates\core'

# Files to update
files_to_update = [
    'contact.html',
    'services.html',
    'student_list.html',
    'login.html'
]

# Favicon line to add
favicon_line = '    <link rel="icon" type="image/png" href="{% static \'core/images/school_logo.png\' %}">\n'

for html_file in files_to_update:
    file_path = os.path.join(template_dir, html_file)
    
    if not os.path.exists(file_path):
        print(f"File not found: {html_file}")
        continue
    
    try:
        # Try different encodings
        content = None
        for encoding in ['utf-8', 'utf-8-sig', 'latin-1', 'cp1252']:
            try:
                with open(file_path, 'r', encoding=encoding) as f:
                    content = f.read()
                break
            except:
                continue
        
        if content is None:
            print(f"Could not read {html_file}")
            continue
        
        # Check if favicon is already present
        if 'rel="icon"' in content or 'favicon' in content.lower():
            print(f"OK - {html_file} already has favicon")
            continue
        
        # Find the title tag and add favicon after it
        lines = content.split('\n')
        new_lines = []
        added = False
        
        for line in lines:
            new_lines.append(line)
            if '<title>' in line and '</title>' in line and not added:
                new_lines.append(favicon_line.rstrip())
                added = True
                print(f"ADDED - {html_file}")
        
        if added:
            new_content = '\n'.join(new_lines)
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
        else:
            print(f"SKIP - No title tag in {html_file}")
            
    except Exception as e:
        print(f"ERROR - {html_file}: {str(e)}")

print("Done!")
