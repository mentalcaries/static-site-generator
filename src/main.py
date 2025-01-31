import os
import shutil
from textnode import TextNode, TextType
from copystatic import copy_static
from generate_page import generate_page

source_path = "./static"
destination_path = "./public"

def main():

    if os.path.exists(destination_path):
        shutil.rmtree(destination_path)
        print('Public directory deleted')
    
    copy_static(source_path, destination_path)
    generate_page('content/index.md', 'template.html', 'public/index.html')

main()
