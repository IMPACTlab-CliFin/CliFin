import os
import sys
sys.path.insert(0, os.path.abspath('.'))

project = 'CliFin'
author = 'IMPACT Lab'

extensions = []

templates_path = ['_templates']
exclude_patterns = []

# docs/conf.py

# Furo 테마 설정
html_theme = 'furo'

# Furo 테마 옵션 설정
html_theme_options = {
    "light_css_variables": {
        "color-brand-primary": "#007BFF",  # 메인 색상
        "color-brand-content": "#2E2E2E",  # 본문 색상
    },
    # 사이드바 토글 버튼 및 깃허브 아이콘 설정
    "navigation_with_keys": True,  # 키보드로 사이드바 탐색 가능
    "header_icons": [  # 상단에 GitHub 아이콘 추가
        {
            "name": "GitHub",
            "url": "https://github.com/IMPACTlab-CliFin/CliFin",  # 깃허브 리포지토리 링크
            "class": "fa fa-github",  # FontAwesome 아이콘 사용
        },
    ],
}

# 소스 코드 링크 표시 (RST 파일 다운로드 가능)
html_show_sourcelink = True

# Static 경로 설정 (custom.css 추가 가능)
html_static_path = ['_static']

# 사용자 정의 CSS 추가
html_css_files = [
    'custom.css',
]
