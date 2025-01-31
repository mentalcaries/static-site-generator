from os import path, mkdir, listdir, getcwd
from markdown_blocks import markdown_to_html_node, extract_title

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    markdown_file = open(from_path, 'r')
    markdown = markdown_file.read()
    markdown_file.close()

    template_file = open(template_path, 'r')
    template = template_file.read()
    template_file.close()

    html_content = markdown_to_html_node(markdown).to_html()
    page_title = extract_title(markdown)

    output_doc = template.replace("{{ Title }}", page_title).replace("{{ Content }}", html_content)

    if not path.exists(path.dirname(dest_path)):
        mkdir(path.dirname(dest_path))
    open(dest_path, 'w').write(output_doc)