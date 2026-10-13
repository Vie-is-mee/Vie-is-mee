"""Generate repository activity and cache public profile cards for the README."""
import json
import os
import re
import urllib.request
from datetime import datetime, timedelta, timezone
from html import escape
from pathlib import Path
from urllib.parse import urlencode
from xml.etree import ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "assets" / "dashboard"
OWNER = os.environ.get("PROFILE_USERNAME", "Vie-is-mee")
PROJECTS = ["UIT-ChatBot", "OneVoice-Lab", "SolarOpt"]
COLORS = ["#58a6ff", "#bc8cff", "#3fb950"]


def download(url, github=False):
    headers = {"User-Agent": "An-Vi-Profile-Dashboard"}
    if github and os.environ.get("GITHUB_TOKEN"):
        headers["Authorization"] = "Bearer " + os.environ["GITHUB_TOKEN"]
    request = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(request, timeout=45) as response:
        return response.read()


def weekly_activity(now):
    today = now.date()
    monday = today - timedelta(days=today.weekday())
    start = monday - timedelta(weeks=11)
    series = []
    for project in PROJECTS:
        counts = [0] * 12
        page = 1
        while True:
            query = urlencode({"since": start.isoformat() + "T00:00:00Z", "until": now.isoformat(), "per_page": 100, "page": page})
            commits = json.loads(download(f"https://api.github.com/repos/{OWNER}/{project}/commits?{query}", github=True))
            for commit in commits:
                # GitHub's commit date is the committer timestamp, not the author timestamp.
                timestamp = datetime.fromisoformat(commit["commit"]["committer"]["date"].replace("Z", "+00:00"))
                index = (timestamp.astimezone(timezone.utc).date() - start).days // 7
                if 0 <= index < 12 and timestamp <= now:
                    counts[index] += 1
            if len(commits) < 100:
                break
            page += 1
        series.append({"repository": project, "weeks": counts})
    return start, series


def activity_svg(start, series, now):
    parts = ['<svg xmlns="http://www.w3.org/2000/svg" width="1000" height="458" viewBox="0 0 1000 458" role="img" aria-labelledby="title description">',
             '<title id="title">Featured projects: commits by week</title>',
             '<desc id="description">Twelve weeks of default-branch repository commits, all contributors. The current week is partial. Commit volume is activity, not a completion percentage.</desc>',
             '<rect x="1" y="1" width="998" height="456" rx="16" fill="#0d1117" stroke="#30363d"/>',
             '<style>text{font-family:Segoe UI,Arial,sans-serif;fill:#e6edf3}.muted{fill:#8b949e;font-size:13px}.label{font-size:17px;font-weight:600}</style>',
             '<text x="30" y="40" font-size="23" font-weight="600">Project activity</text>',
             '<text x="30" y="66" class="muted">12 weeks · default-branch commits · all contributors · current week partial</text>']
    for row, (item, color) in enumerate(zip(series, COLORS)):
        top = 94 + row * 100
        total = sum(item["weeks"])
        maximum = max(max(item["weeks"]), 1)
        parts += [f'<text x="30" y="{top + 25}" class="label">{escape(item["repository"])}</text>',
                  f'<text x="30" y="{top + 49}" class="muted">{total} commits in this window</text>']
        for week, count in enumerate(item["weeks"]):
            x = 262 + week * 58
            height = 46 * count / maximum
            date = start + timedelta(weeks=week)
            parts.append(f'<rect x="{x}" y="{top + 54 - height:.2f}" width="34" height="{max(height, 2):.2f}" rx="3" fill="{color if count else "#21262d"}"><title>Week of {date}: {count} commits</title></rect>')
            parts.append(f'<text x="{x + 17}" y="{top + 47 - height:.2f}" text-anchor="middle" class="muted">{count}</text>')
            if row == 2:
                parts.append(f'<text x="{x + 17}" y="{top + 77}" text-anchor="middle" class="muted">{date:%d/%m}</text>')
    parts += ['<text x="30" y="421" class="muted">Each row uses its own scale. Activity does not measure project completion or individual skill.</text>',
              f'<text x="30" y="444" class="muted">Source: GitHub REST API · Updated {now:%Y-%m-%d %H:%M} UTC</text>', '</svg>']
    return "\n".join(parts)


def main():
    OUTPUT.mkdir(parents=True, exist_ok=True)
    now = datetime.now(timezone.utc).replace(microsecond=0)
    start, series = weekly_activity(now)
    svg = activity_svg(start, series, now)
    ET.fromstring(svg)
    (OUTPUT / "project-activity.svg").write_text(svg, encoding="utf-8")
    (OUTPUT / "project-activity.json").write_text(json.dumps({"updated_at": now.isoformat(), "first_week": str(start), "scope": "default branch, all contributors, committer timestamp", "projects": series}, indent=2) + "\n", encoding="utf-8")
    cards = {
        "stats.svg": "https://github-readme-stats.vercel.app/api?" + urlencode({"username": OWNER, "custom_title": "An Vi's GitHub Stats", "show_icons": "true", "include_all_commits": "true", "hide_rank": "false", "theme": "dracula", "hide_border": "false", "border_color": "e4e2e2", "border_radius": 6, "disable_animations": "true"}),
        "languages.svg": "https://github-readme-stats.vercel.app/api/top-langs/?" + urlencode({"username": OWNER, "layout": "compact", "langs_count": 6, "theme": "dracula", "hide_border": "false", "border_color": "e4e2e2", "border_radius": 6, "card_width": 360, "disable_animations": "true"}),
        "streak.svg": "https://streak-stats.demolab.com/?" + urlencode({"user": OWNER, "theme": "github-dark-blue", "hide_border": "true"}),
    }
    failed = []
    for name, url in cards.items():
        try:
            data = download(url)
            tree = ET.fromstring(data)
            words = " ".join(tree.itertext())
            if not tree.tag.endswith("svg") or re.search(r"something went wrong|rate limit exceeded|could not fetch|error fetching|service unavailable", words, re.I):
                raise ValueError("Provider returned an error card")
            normalized = "\n".join(line.rstrip() for line in data.decode("utf-8").splitlines()) + "\n"
            (OUTPUT / name).write_text(normalized, encoding="utf-8")
            print("Updated", name)
        except Exception as error:
            # A provider outage must not overwrite the last usable card.
            failed.append(name)
            print(f"Kept existing {name}: {type(error).__name__}")
    print("Updated project activity:", ", ".join(f'{s["repository"]}={sum(s["weeks"])}' for s in series))
    if failed:
        raise SystemExit("Some profile cards could not refresh; existing snapshots were preserved.")


if __name__ == "__main__":
    main()
