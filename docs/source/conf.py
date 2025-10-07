# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys
sys.path.insert(0, os.path.abspath('.'))

# -- Project information -----------------------------------------------------

project = 'Jimit Vyas - CAE & Automation Specialist'
copyright = '2025, Jimit Vyas'
author = 'Jimit Vyas'
release = '1.0'

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.githubpages',
    'sphinx.ext.todo',
    'sphinx_design',
    'sphinx_copybutton',
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'furo'

# Add any paths that contain custom static files (such as style sheets) or
# theme-specific static files, here, relative to this directory. They are
# copied after the builtin static files, so a file named "default.css" will
# overwrite the builtin "default.css".
html_static_path = ['_static']

# Custom CSS files
html_css_files = [
    'css/custom.css',
]

# The master toctree document.
master_doc = 'index'

# HTML theme options
html_theme_options = {
    "sidebar_hide_name": True,
    "navigation_with_keys": True,
    "light_css_variables": {
        "color-brand-primary": "#1a2332",
        "color-brand-content": "#475569",
        "color-admonition-background": "#f8fafc",
        "color-sidebar-background": "#f1f5f9",
        "color-link": "#64748b",
        "color-link--hover": "#1a2332",
    },
    "dark_css_variables": {
        "color-brand-primary": "#e2e8f0",
        "color-brand-content": "#cbd5e1",
        "color-admonition-background": "#1e293b",
        "color-sidebar-background": "#0f172a",
        "color-link": "#94a3b8",
        "color-link--hover": "#e2e8f0",
    },
    "announcement": "🚀 Professional CAE Engineer & Automation Specialist | 9+ Years Experience | Available for Projects",
    "footer_icons": [
        {
            "name": "Email",
            "url": "mailto:jimit.vyas@outlook.com",
            "html": """
                <svg stroke="currentColor" fill="currentColor" stroke-width="0" viewBox="0 0 24 24">
                    <path d="M20 4H4c-1.1 0-1.99.9-1.99 2L2 18c0 1.1.89 2 2 2h16c1.1 0 2-.9 2-2V6c0-1.1-.9-2-2-2zm0 4l-8 5-8-5V6l8 5 8-5v2z"/>
                </svg>
            """,
            "class": "fas fa-envelope",
        },
        {
            "name": "LinkedIn",
            "url": "https://linkedin.com/in/jimit04",
            "html": """
                <svg stroke="currentColor" fill="currentColor" stroke-width="0" viewBox="0 0 24 24">
                    <path d="M20.447 20.452h-3.554v-5.569c0-1.328-.027-3.037-1.852-3.037-1.853 0-2.136 1.445-2.136 2.939v5.667H9.351V9h3.414v1.561h.046c.477-.9 1.637-1.85 3.37-1.85 3.601 0 4.267 2.37 4.267 5.455v6.286zM5.337 7.433c-1.144 0-2.063-.926-2.063-2.065 0-1.138.92-2.063 2.063-2.063 1.14 0 2.064.925 2.064 2.063 0 1.139-.925 2.065-2.064 2.065zm1.782 13.019H3.555V9h3.564v11.452zM22.225 0H1.771C.792 0 0 .774 0 1.729v20.542C0 23.227.792 24 1.771 24h20.451C23.2 24 24 23.227 24 22.271V1.729C24 .774 23.2 0 22.222 0h.003z"/>
                </svg>
            """,
            "class": "fab fa-linkedin",
        },
    ],
}

# HTML context
html_context = {
    'display_github': True,
    'github_user': 'jimitvyas',
    'github_repo': 'personal-website',
    'github_version': 'main',
    'conf_py_path': '/docs/source/',
}

# Source file extensions
source_suffix = {
    '.rst': 'restructuredtext',
    '.md': 'markdown',
}

# Enable TODOs
todo_include_todos = True

# Copy button configuration
copybutton_prompt_text = r">>> |\.\.\. |\$ |In \[\d*\]: | {2,5}\.\.\.: | {5,8}: "
copybutton_prompt_is_regexp = True