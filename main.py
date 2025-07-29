# Used for jinja-type macros

import requests


def define_env(env):
    @env.macro
    def contributors(repo="mcloughlan/algo-notes"):
        try:
            url = f"https://api.github.com/repos/{repo}/contributors"
            resp = requests.get(
                url, headers={"Accept": "application/vnd.github+json"}, timeout=10)

            if resp.status_code == 404:
                return f"<p style='color:red;'>Error: GitHub repo '{repo}' not found.</p>"

            if resp.status_code == 403:
                return "<p style='color:red;'>Error: GitHub API rate limit exceeded. Try again later.</p>"

            if not resp.ok:
                return f"<p style='color:red;'>Error: GitHub API returned status {resp.status_code}.</p>"

            users = resp.json()
            if not isinstance(users, list):
                return "<p style='color:red;'>Error: Unexpected response format from GitHub API.</p>"

            html = ""
            for u in users:
                if "login" not in u:
                    continue  # Skip invalid user object
                username = u["login"]
                html += (
                    f'<a href="https://github.com/{username}" title="{username}">'
                    f'<img src="https://github.com/{username}.png?size=50" alt="{username}" '
                    f'style="border-radius: 50%; margin: 5px;"></a>\n'
                )
            return html or "<p>No contributors found.</p>"

        except requests.exceptions.RequestException as e:
            return f"<p style='color:red;'>Error contacting GitHub: {e}</p>"
