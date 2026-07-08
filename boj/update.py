#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "requests",
# ]
# ///

from typing import Any
import os
import argparse
import datetime as dt

import requests  # pyright: ignore[reportMissingModuleSource]


LEVEL_NAME = [
    "UNRATED",
    "Bronze V",
    "Bronze IV",
    "Bronze III",
    "Bronze II",
    "Bronze I",
    "Silver V",
    "Silver IV",
    "Silver III",
    "Silver II",
    "Silver I",
    "Gold V",
    "Gold IV",
    "Gold III",
    "Gold II",
    "Gold I",
    "Platinum V",
    "Platinum IV",
    "Platinum III",
    "Platinum II",
    "Platinum I",
    "Diamond V",
    "Diamond IV",
    "Diamond III",
    "Diamond II",
    "Diamond I",
    "Ruby V",
    "Ruby IV",
    "Ruby III",
    "Ruby II",
    "Ruby I",
]
CODE_DIR_PYTHON = "python"
CODE_TEMPLATE_PYTHON = """# https://www.acmicpc.net/problem/{code}
# {date} / {code}. {title} / {level_name}

import sys
input = lambda: sys.stdin.readline().rstrip()
# print = sys.stdout.write

# T = int(input())
# N, M = map(int, input().split())

"""


def get_problem(p_id: int | str) -> dict[str, Any] | None:
    # https://solvedac.github.io/unofficial-documentation/#/operations/getProblemById
    resp = requests.get(f"https://solved.ac/api/v3/problem/show?problemId={p_id}")
    if resp.status_code != 200:
        return

    data = resp.json()
    return data


def append_readme(*args: str):
    for code in args:
        p = get_problem(code)
        if not p:
            continue
        title: str | None = p.get("titleKo")
        level: str | None = p.get("level")

        if title is None or level is None:
            print(f"Problem {code} data error!!")
            continue

        code_file_path = os.path.join(CODE_DIR_PYTHON, f"P{code}.py")
        if os.path.exists(code_file_path):
            print(
                f"{LEVEL_NAME[level]:12s} - [{code}. {title}] / skip!! (file already exists)"
            )
            continue
        with open(code_file_path, "w", encoding="utf-8") as f:
            f.write(
                CODE_TEMPLATE_PYTHON.format(
                    code=code,
                    title=title,
                    date=dt.date.today(),
                    level_name=LEVEL_NAME[level],
                )
            )
        print(f"{LEVEL_NAME[level]:12s} - [{code}. {title}] added!! ({code_file_path})")


def edit_readme(*args):
    with open("README.md", "r", encoding="utf-8") as f:
        lines = f.readlines()
        idx = lines.index("<!-- TABLE START -->\n")

        for line in lines[idx + 3 :]:
            data = line[1:-1].split("|")
            print(data[2])


def generate_markdown(*args):
    # args: code(문제 번호) 있는 list
    for code in args:
        p = get_problem(code)
        if not p:
            continue
        title: str | None = p.get("titleKo")
        level: str | None = p.get("level")
        if title is None or level is None:
            print(f"Problem {code} data error!!")
            continue
        with open(f"docs/P{code}.md", "w", encoding="utf-8") as f:
            f.write(
                f"# {code}. {title} ({LEVEL_NAME[level]})\n[소스코드(Python)]({CODE_DIR_PYTHON}/P{code}.py)"
            )


def edit_readme_markdown():
    pass


def download_icons():
    for i, name in enumerate(LEVEL_NAME):
        with open(os.path.join("icon", f"{i}.svg"), "wb") as f:
            resp = requests.get(f"https://static.solved.ac/tier_small/{i}.svg")
            if resp.status_code != 200:
                print(f"ERROR: {resp.status_code}")
                continue
            data = resp.content
            if not isinstance(data, bytes):
                print("ERROR: 알 수 없는 오류")
                continue
            f.write(data)
            print(f"다운로드 완료: {resp.url}")


def main():
    pass


if __name__ == "__main__":
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument(
        "-m", "--markdown", help="Markdown file generate mode", action="store_true"
    )
    arg_parser.add_argument(
        "number", help="BOJ problem code numbers", type=int, nargs="+"
    )
    args = arg_parser.parse_args()
    if args.markdown:
        edit_readme_markdown()
    else:
        append_readme(*args.number)
    # edit_readme()
