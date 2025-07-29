# Used for jinja-type macros

import requests


def define_env(env):
    @env.macro
    def contributors(repo="mcloughlan/algo-notes"):
        USERS = requests.get(
            f"https://api.github.com/repos/{repo}/contributors").json()
        html = ""
        for u in USERS:
            html += f'<a href="https://github.com/{u["login"]}"><img src="https://github.com/{u["login"]}.png?size=50" alt="{u["login"]}" style="border-radius: 50%; margin: 5px;"></a>\n'
        return html
