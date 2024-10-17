import os
import sys
sys.path.insert(0, os.path.abspath('.'))

project = 'CliFin'
author = 'IMPACT Lab, Dr. Wonchan Lee'

extensions = []

templates_path = ['_templates']
exclude_patterns = []

# Sphinx Book Theme 사용
html_theme = 'sphinx_book_theme'
html_title = 'CliFin Project'

html_theme_options = {
    # 기존 옵션들...
    "repository_url": "https://github.com/IMPACTlab-CliFin/CliFin",
    "repository_branch": "main",
    "path_to_docs": "docs",
    "use_repository_button": True,
    "use_issues_button": True,
    "use_edit_page_button": True,
    "use_fullscreen_button": True,
    "use_download_button": True,
    # 오른쪽 사이드바 설정
    "toc_title": "On this page",  # 사이드바 제목 (원하는 대로 변경 가능)
    "toc_levels": "1-3",  # 표시할 헤딩 레벨 (1은 제목, 2는 섹션, 3은 하위 섹션)
    "show_navbar_depth": 1,  # 좌측 내비게이션 깊이
    "show_toc_level": 2,  # 오른쪽 사이드바에서 표시할 최대 헤딩 레벨
}

html_show_sourcelink = True
html_static_path = ['_static']
html_css_files = ['custom.css']
