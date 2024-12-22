# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

import sphinx_rtd_theme

# 扩展配置
extensions = [
    "nbsphinx",
    "myst_parser"
]

# 设置主题
html_theme = 'sphinx_rtd_theme'
html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]

# Jupyter notebook 配置
nbsphinx_execute = 'never'  # 控制是否在构建时执行 Jupyter Notebook，可以设为 'always' 或 'never'

# 其他可能需要的配置
source_suffix = ['.rst', '.md', '.ipynb']  # 支持 Markdown 和 Jupyter Notebook

project = 'myresearch'
copyright = '2024, jiash'
author = 'jiash'
release = '0.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_static_path = ['_static']

html_use_index = True
html_domain_indices = True
    
html_theme_options = {
    "description": "A light, configurable Sphinx theme",
    "github_user": "sphinx-doc",
    "github_repo": "alabaster",
    "fixed_sidebar": True,
    "github_banner": True,
}