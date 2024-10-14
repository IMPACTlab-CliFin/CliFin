import os
import sys
sys.path.insert(0, os.path.abspath('.'))

project = 'CliFin'
author = 'IMPACT Lab'

extensions = []

templates_path = ['_templates']
exclude_patterns = []

# 테마 설정
html_theme = 'furo'  # Furo 테마로 변경

# 선택: 추가적인 테마 설정 (색상, 폰트 등 커스터마이징)
html_theme_options = {
    "light_css_variables": {
        "color-brand-primary": "#007BFF",  # 메인 색상
        "color-brand-content": "#2E2E2E",  # 본문 색상
    },
}

html_static_path = ['_static']
