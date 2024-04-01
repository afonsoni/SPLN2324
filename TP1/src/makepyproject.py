# !/usr/bin/env python3
"""
python3 makepyproject.py
"""

import jjcli
import jinja2
from glob import glob
import json
import os

__version__ = "0.1.0"

def main():
    name = "sentilexpt"

    v = jjcli.qx(f"grep name '{name}'.py")
    print('debug',len(v))
    version = "0.1.0"

    pp = jinja2.Template('''
    [build-system]
    requires=["flit_core >=3.2,<4"]
    build-backend = "flit_core.buildapi"

    [project]
    name = "{{ name }}"
    authors = [
        {name = "{{ author1 }}", email = "{{ email1 }}"},
    ]

    version = "{{ version }}"

    Classifiers = [
        "License :: OSI Approved :: MIT License",
    ]

    requires-python = ">=3.8"
    dynamic = ["description"]

    dependencies = [
        "jjcli",
        "jinja2",
        "vaderSentiment",
        "spacy",
        "nltk",
        "codecs",
        "json",
        "os",
        "re"
    ]

    [project.scripts]
    {{ name }} = "{{ name }}:main"
    ''')

    metadata_path = "METADATA.json"
    
    # Check if the METADATA.json file exists
    if not os.path.exists(metadata_path):
        print("Error: METADATA.json not found.")
        return
    
    # Load metadata from METADATA.json
    with open(metadata_path, 'r') as file:
        data = json.load(file)
        autor1 = data.get("name1", "")
        email1 = data.get("email1", "")
        numero1 = data.get("number1", "")
        autor2 = data.get("name2", "")
        email2 = data.get("email2", "")
        numero2 = data.get("number2", "")
        autor3 = data.get("name3", "")
        email3 = data.get("email3", "")
        numero3 = data.get("number3", "")

    out = pp.render({"version":version, "name":name, "author1":autor1, "author2":autor2, "author3":autor3, "email1":email1, "email2":email2, "email3":email3, "number1":numero1, "number2":numero2, "number3":numero3})
    print("debug",out)
    
    # Write generated output to pyproject.toml
    with open("pyproject.toml", "w") as file_output:
        file_output.write(out)
        
if __name__ == "__main__":
    main()
    
    # print(pp_template.render(name="myproject", author="me", email="pg52669@alunos.uminho.pt"))