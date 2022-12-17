import jinja2
import os
import sys
import argparse
from pathlib import Path
from jinja2 import Environment, FileSystemLoader, TemplateNotFound
import datetime


TEMPLATES_FOLDER="./templates/"
OUTPUT_FOLDER="./cover_letters"
DEFAULT_TEMPLATE="template1.html.j2"
DEFAULT_NAME="Animesh Sengupta"

def create(role,org,template=DEFAULT_TEMPLATE,name=DEFAULT_NAME):
    date = f"{datetime.datetime.now():%m/%d/%y}"
    try:
        environment = Environment(loader=FileSystemLoader(TEMPLATES_FOLDER))
        template = environment.get_template(DEFAULT_TEMPLATE)
        rendered_ouput=template.render(
            role=role,
            org=org,
            name=name,
            date=date)
        print (rendered_ouput)
    except TemplateNotFound as e:
        print("Error 404: Template File/Folder Not found",e)




create("Data Engineer","Google")


# parser = argparse.ArgumentParser()

# parser.add_argument("path")

# args = parser.parse_args()

# target_dir = Path(args.path)

# if not target_dir.exists():
#     print("The target directory doesn't exist")
#     raise SystemExit(1)

# for entry in target_dir.iterdir():
#     print(entry.name)