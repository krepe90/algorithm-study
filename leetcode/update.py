#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.14"
# dependencies = ["requests"]
# ///

import argparse
import datetime as dt
from pathlib import Path

import requests

URL = "https://leetcode.com/graphql/"
QUERY = """
query ($filters: QuestionListFilterInput) {
  questionList(categorySlug: "", limit: 20, skip: 0, filters: $filters) {
    data { questionFrontendId title titleSlug difficulty }
  }
}
"""


def main(numbers: list[int]) -> None:
    for number in numbers:
        response = requests.post(
            URL,
            json={
                "query": QUERY,
                "variables": {"filters": {"searchKeywords": str(number)}},
            },
            timeout=10,
        )
        response.raise_for_status()
        problems = response.json()["data"]["questionList"]["data"]
        problem = next(
            (p for p in problems if p["questionFrontendId"] == str(number)), None
        )
        if problem is None:
            print(f"{number}: not found")
            continue

        path = Path(__file__).parent / "python" / f"P{number}.py"
        if path.exists() and path.stat().st_size:
            print(f"{number}: skipped ({path})")
            continue

        path.parent.mkdir(exist_ok=True)
        path.write_text(
            f"# https://leetcode.com/problems/{problem['titleSlug']}/\n"
            f"# {dt.date.today()} / {number}. {problem['title']} / "
            f"{problem['difficulty']}\n\n",
            encoding="utf-8",
        )
        print(f"{number}: added ({path})")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("number", type=int, nargs="+")
    main(parser.parse_args().number)
