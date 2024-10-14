import os
import sys
sys.path.insert(0, os.path.abspath('.'))

project = 'CliFin'
author = 'IMPACT Lab'

extensions = []  # 확장이 필요할 경우 추가

templates_path = ['_templates']
exclude_patterns = []

# Furo 테마 설정
html_theme = 'furo'

# 테마 옵션 설정 (GitHub 아이콘과 다크모드 포함)
html_theme_options = {
    "light_css_variables": {
        "color-brand-primary": "#007BFF",  # 메인 색상
        "color-brand-content": "#2E2E2E",  # 본문 색상
    },
    # GitHub 아이콘을 상단에 추가
    "header_icons": [
        {
            "name": "GitHub",
            "url": "https://github.com/IMPACTlab-CliFin/CliFin",  # GitHub 리포지토리 링크
            "class": "fa fa-github",  # FontAwesome GitHub 아이콘 사용
        },
    ],
    "navigation_with_keys": True,  # 키보드로 사이드바 탐색 가능
}

# 소스 코드 링크 표시
html_show_sourcelink = True

# Static 경로 설정
html_static_path = ['_static']

# 사용자 정의 CSS 파일 추가 (추가로 스타일을 적용할 때)
html_css_files = [
    'custom.css',
]
