#!/usr/bin/env python3
from __future__ import annotations

import os
from pathlib import Path
from playwright.sync_api import sync_playwright

URL = os.environ.get("GITHUB_PAGES_URL", "https://realagiorganization.github.io/dolphin-ios/")
OUTPUT = Path(os.environ.get("SCREENSHOT_PATH", "docs/website_screenshots/github-pages.png"))


def main() -> None:
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page(viewport={"width": 1440, "height": 900})
        page.goto(URL, wait_until="networkidle")
        page.wait_for_timeout(2000)
        page.screenshot(path=str(OUTPUT), full_page=True)
        browser.close()
    print(f"Saved screenshot to {OUTPUT}")


if __name__ == "__main__":
    main()
