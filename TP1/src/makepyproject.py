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
    name = "sentilexpt"

    v = jjcli.qx(f"grep name '{name}'.py")
    print('debug',len(v))
    version = "0.0.1"

    pp = jinja2.Template('''
    [build-system]
    requires=["flit_core >=3.2,<4"]
    build-backend = "flit_core.buildapi"

    [project]
    name = "{{ name }}"
    authors = [
        {% for author in authors %}
        {name = "{{author.name}}", email = "{{author.email}}"},
        {% endfor %}
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
        "pt_core_news_lg @ https://github.com/explosion/spacy-models/releases/download/pt_core_news_lg-3.7.0/pt_core_news_lg-3.7.0-py3-none-any.whl"
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
        authors = data["authors"]

    out = pp.render({"version":version, "name":name, "authors":authors})
    print("debug",out)
    
    # Write generated output to pyproject.toml
    with open("pyproject.toml", "w") as file_output:
        file_output.write(out)
        
if __name__ == "__main__":
    main()
    
    # print(pp_template.render(name="myproject", author="me", email="pg52669@alunos.uminho.pt"))