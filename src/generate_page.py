from os import path, mkdir, listdir, getcwd
from pathlib import Path
from markdown_blocks import markdown_to_html_node, extract_title


def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    
    markdown_file = open(from_path, "r")
    markdown = markdown_file.read()
    markdown_file.close()

    template_file = open(template_path, "r")
    template = template_file.read()
    template_file.close()

    html_content = markdown_to_html_node(markdown).to_html()
    page_title = extract_title(markdown)

    output_doc = template.replace("{{ Title }}", page_title).replace(
        "{{ Content }}", html_content
    )

    if not path.exists(path.dirname(dest_path)):
        mkdir(path.dirname(dest_path))
    open(dest_path, "w").write(output_doc)


def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    path_contents = listdir(dir_path_content)
    for content in path_contents:
        src_path = path.join(dir_path_content, content)
        dest_path = path.join(dest_dir_path, content)

        if path.isfile(src_path) and content.endswith(".md"):
            file_name = (Path(content).stem)
            dest_file_path = f"{path.join(dest_dir_path, file_name)}.html"
            generate_page(src_path, template_path, dest_file_path)
            print(f"Generating {dest_file_path}")
        else:
            mkdir(dest_path)
            generate_pages_recursive(src_path, template_path, dest_path)
