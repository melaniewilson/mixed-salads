
# INDEX
# First, get the template files
top_template = open('templates/top.html').read()
bottom_template = open('templates/bottom.html').read()

# Read in index HTML code
content = open('content/index.html').read()

# Combine template HTML code with content HTML code
index_html = top_template + content + bottom_template
open('index.html', 'w+').write(index_html)

# ABOUT
top_template = open('templates/top.html').read()
bottom_template = open('templates/bottom.html').read()

# Read in index HTML code
content = open('content/about.html').read()

# Combine template HTML code with content HTML code
about_html = top_template + content + bottom_template
open('about.html', 'w+').write(about_html)

# BLOG
top_template = open('templates/top.html').read()
bottom_template = open('templates/bottom.html').read()

# Read in index HTML code
content = open('content/blog.html').read()

# Combine template HTML code with content HTML code
blog_html = top_template + content + bottom_template
open('blog.html', 'w+').write(blog_html)

# PROJECTS
top_template = open('templates/top.html').read()
bottom_template = open('templates/bottom.html').read()

# Read in index HTML code
content = open('content/projects.html').read()

# Combine template HTML code with content HTML code
projects_html = top_template + content + bottom_template
open('projects.html', 'w+').write(projects_html)
