# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = '计算机网络：自顶向下'
copyright = '2025, Jim Kurose/Keith Ross'
author = 'Jim Kurose/Keith Ross'
release = '1.0'



# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

# extensions
# https://www.sphinx-doc.org/en/master/usage/extensions/index.html
extensions = [
    'sphinx.ext.intersphinx',
    'sphinx.ext.autodoc', 
    'sphinx.ext.todo', 
    'sphinx.ext.coverage',
    'sphinxcontrib.youtube',
    'sphinx_copybutton',
    'sphinx_inline_tabs',
    'sphinx_togglebutton',
]

templates_path = ['_templates']
exclude_patterns = []

language = 'zh_CN'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

# html_theme = 'furo'
html_theme = 'sphinx_book_theme'
html_theme_options= {
    "repository_url": 'https://github.com/hellowac/computer-net-zh-cn',
    "use_repository_button": True
}
html_static_path = ['_static']
html_css_files = [
    'mystyles.css',
]
html_title='计算机网络: 自顶向下'

highlight_language = 'python'  # 默认语言（可选）
pygments_style = 'sphinx'  # Sphinx 默认样式

togglebutton_hint = '原文'
togglebutton_hint_hide = '收起'
