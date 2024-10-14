import os
import sys
sys.path.insert(0, os.path.abspath('.'))

project = 'CliFin'
author = 'IMPACT Lab'

extensions = []

templates_path = ['_templates']
exclude_patterns = []

# docs/conf.py

html_theme = 'furo'

# GitHub 아이콘 및 링크 추가
html_theme_options = {
    "light_css_variables": {
        "color-brand-primary": "#007BFF",
        "color-brand-content": "#2E2E2E",
    },
    "footer_icons": [
        {
            "name": "GitHub",
            "url": "https://github.com/IMPACTlab-CliFin/CliFin.git",  # GitHub 리포지토리 링크
            "html": """
                <svg stroke="currentColor" fill="currentColor" stroke-width="0" viewBox="0 0 1024 1024" height="1.2em" width="1.2em" xmlns="http://www.w3.org/2000/svg">
                    <path d="M511.6 76.3C264.3 76.3 64 277 64 524.5c0 198 128.7 365.6 307.4 424.8 22.5 4.1 30.7-9.8 30.7-21.7v-85c-124.8 27.1-150.8-53.9-150.8-53.9-20.5-52.1-50.1-66-50.1-66-40.9-27.9 3.1-27.3 3.1-27.3 45.2 3.2 69 46.3 69 46.3 40.2 68.9 105.5 49 131.2 37.4 4-29.1 15.7-49 28.5-60.2-99.6-11.3-204.4-49.8-204.4-221.8 0-49 17.5-89 46.1-120.4-4.6-11.3-20-57 4.4-118.8 0 0 37.6-12 123.2 45.9 35.8-10 74.2-15 112.4-15s76.6 5.1 112.4 15c85.6-57.9 123.2-45.9 123.2-45.9 24.4 61.8 9 107.5 4.4 118.8 28.6 31.4 46.1 71.4 46.1 120.4 0 172.6-104.9 210.3-204.8 221.3 16.2 14.4 30.6 42.9 30.6 86.5v128c0 12 8 25.9 30.7 21.7 178.7-59.2 307.4-226.9 307.4-424.8 0-247.5-200.3-448.2-447.6-448.2z"></path>
                </svg>
            """,
            "class": "",
        },
    ],
}
