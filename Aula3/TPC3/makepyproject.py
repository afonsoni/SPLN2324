# !/usr/bin/env python3
"""
python3 makepyproject.py
"""

import jjcli
import jinja2
from glob import glob
import json
import os

__version__ = "0.0.1"

def main():
    #project name
    modes = glob("*.py")
    if len(modes)==1:
        name = modes[0].replace(".py","")
    elif len(modes)>1:
        print(modes)
        name = input("Modulo?").replace(".py","")
    else:
        name = input("Modulo?").replace(".py","")
    

    v = jjcli.qx(f"grep name '{name}'.py")
    print('debug',len(v))
    version = "0.0.1"

    pp = jinja2.Template('''
    [build system]
    requires=["flit_core >=3.2,<4"]
    build-backend = "flit_core.buildapi"

    [project]
    name = "{{ name }}"
    authors = [
        {name = "{{ author }}", email = "{{ email }}"}, number = "{{ number }}",
    ]

    version = "{{ version }}"

    Classifiers = [
        "License :: OSI Approved :: MIT License",
    ]

    requires-python = ">=3.8"
    dynamic = ["description"]

    dependencies = [
        "jjcli",
        "jinja2"
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
        autor = data.get("Username", "")
        email = data.get("Email", "")
        numero = data.get("Number", "")

    out = pp.render({"version":version, "name":name, "author":autor, "email":email, "number":numero})
    print("debug",out)
    
    # Write generated output to pyproject.toml
    with open("pyproject.toml", "w") as file_output:
        file_output.write(out)
        
if __name__ == "__main__":
    main()
    
    # print(pp_template.render(name="myproject", author="me", email="pg52669@alunos.uminho.pt"))