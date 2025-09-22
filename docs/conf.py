# Configuration file for the Sphinx documentation builder.

# -- Project information -----------------------------------------------------
project = 'DamuBPM'
copyright = '2025, B-Apps'
author = 'Yeldar Saumbayev'
release = '0.1.111'

# -- General configuration ---------------------------------------------------
extensions = [
    'sphinx.ext.autodoc',      # автоматическая документация из docstring
    'sphinx.ext.napoleon',     # поддержка Google-style и NumPy-style docstring
    'sphinx.ext.viewcode',     # добавляет ссылки на исходный код
    'myst_parser',             # поддержка Markdown (.md файлов)
]

templates_path = ['_templates']
exclude_patterns = []

# -- Options for HTML output -------------------------------------------------
html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']

# Если у тебя корень документации в `docs/`, то источник:
# (index.rst или index.md должен быть в этом каталоге)
