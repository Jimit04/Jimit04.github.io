# Configuration file for the Sphinx documentation builder.
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------
import os
import sys
from pathlib import Path
sys.path.insert(0, os.path.abspath('.'))

# -- UTF-8 YAML helper -------------------------------------------------------
import yaml
def load_yaml(path: Path):
    with path.open(encoding='utf-8') as f:
        return yaml.safe_load(f)

# -- Branding -----------------------------------------------------------------
HERE = Path(__file__).parent
brand = load_yaml(HERE / '_data' / 'branding.yaml')

html_theme_options = {
    "sidebar_hide_name": True,
    "light_css_variables": {
        "color-brand-primary": brand['colors']['primary'],
        "color-brand-content": brand['colors']['secondary'],
        "color-sidebar-background": brand['colors']['highlight'],
        "color-link": brand['colors']['accent'],
        "color-link--hover": brand['colors']['primary'],
    },
    "dark_css_variables": {
        "color-brand-primary": brand['dark_mode']['primary'],
        "color-brand-content": brand['dark_mode']['secondary'],
        "color-sidebar-background": brand['dark_mode']['highlight'],
        "color-link": brand['dark_mode']['accent'],
        "color-link--hover": brand['dark_mode']['primary'],
    },
    "footer_icons": [
        {
            "name": item['name'],
            "url": item['url'],
            "html": item['icon'],
        }
        for item in brand['social']
    ],
}

# -- Data layer --------------------------------------------------------------
data = {
    'experiences': load_yaml(HERE / '_data' / 'experience.yaml'),
    'projects':    load_yaml(HERE / '_data' / 'projects.yaml'),
    'skills':      load_yaml(HERE / '_data' / 'skills.yaml'),
    'brand':       brand,
    'social':      brand['social'],
    'hero': {
        'title': 'Jimit Vyas',
        'subtitle': 'CAE & Automation Specialist',
        'description': '9+ years driving simulation efficiency via Python, TCL & AI integration.',
        'primary_label': 'View Portfolio',
        'primary_url': 'portfolio.html',
        'secondary_label': 'Get In Touch',
        'secondary_url': 'contact.html',
    },
}

html_context = {**data, **{
    'display_github': True,
    'github_user': 'jimitvyas',
    'github_repo': 'personal-website',
    'github_version': 'main',
    'conf_py_path': '/docs/source/',
}}

# -- Jinja2 setup ------------------------------------------------------------
# import jinja2
# jinja2_env_kwargs = {
#     'loader': jinja2.FileSystemLoader(HERE / '_templates'),
# }

# -- Contexts exposed to sphinx-jinja --------------------------------------
jinja_contexts = {
    name: {'data': payload}
    for name, payload in data.items()
}


# -- Project information -----------------------------------------------------
project = 'Jimit Vyas'
copyright = '2025, Jimit Vyas'
author = 'Jimit Vyas'
release = '1.0'

# -- General configuration ---------------------------------------------------
extensions = [
    'sphinx.ext.githubpages',
    'sphinx.ext.todo',
    'sphinx_design',
    'sphinx_copybutton',
    'sphinx_jinja',
]

exclude_patterns = []
source_suffix = {'.rst': 'restructuredtext'}
master_doc = 'index'
todo_include_todos = True

# -- HTML output -------------------------------------------------------------
html_theme = 'furo'
html_static_path = ['_static']
html_css_files = ['css/custom.css']
html_js_files = [
    'js/main.js',
    'js/timeline.js',
    'js/portfolio.js',
    'js/contact.js',
]