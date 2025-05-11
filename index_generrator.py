import os

def generate_index_html(base_path):
    # Get all child directories
    child_dirs = [d for d in os.listdir(base_path) if os.path.isdir(os.path.join(base_path, d))]

    # Start building the HTML content
    html_content = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Index</title>
</head>
<body>
    <h1>Games</h1>
    <ul>
"""

    # Add links to child directories
    for child in child_dirs:
        html_content += f'        <li><a href="{child}/">{child}</a></li>\n'

    # Close the HTML tags
    html_content += """    </ul>
</body>
</html>
"""

    # Write the HTML content to index.html
    with open(os.path.join(base_path, "index.html"), "w") as f:
        f.write(html_content)

# Specify the base path (current directory)
if __name__ == "__main__":
    base_path = os.path.dirname(os.path.abspath(__file__))
    generate_index_html(base_path)