import os
import sys
sys.path.insert(0, os.path.abspath('.'))

project = 'CliFin'
author = 'IMPACT Lab'

extensions = []

templates_path = ['_templates']
exclude_patterns = []

# Sphinx Book Theme 사용
html_theme = 'sphinx_book_theme'

html_theme_options = {
    "repository_url": "https://github.com/IMPACTlab-CliFin/CliFin",
    "repository_branch": "main",  # 기본 브랜치 이름으로 변경
    "path_to_docs": "docs",       # 문서 디렉토리로 변경
    "use_repository_button": True,
    "use_issues_button": True,
    "use_edit_page_button": True,
    "use_fullscreen_button": True,
    "use_download_button": True,
}

html_show_sourcelink = True
html_static_path = ['_static']
html_css_files = ['custom.css']
