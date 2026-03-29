from __future__ import annotations

import html
import os
from datetime import datetime, timezone
from pathlib import Path

import feedparser


FEED_URL = os.getenv("FEED_URL", "").strip()
SOURCE_NAME = os.getenv("SOURCE_NAME", "newsletter").strip()
MAX_ITEMS = int(os.getenv("MAX_ITEMS", "8"))
OUTPUT_PATH = os.getenv("OUTPUT_PATH", "output/briefing.md").strip()

if not FEED_URL:
    raise SystemExit("FEED_URL is empty. Please set it in the workflow env.")
if not OUTPUT_PATH:
    raise SystemExit("OUTPUT_PATH is empty. Please set it in the workflow env.")


def clean_text(text: str) -> str:
    text = html.unescape(text or "")
    text = text.replace("\r", " ").replace("\n", " ").strip()
    while "  " in text:
        text = text.replace("  ", " ")
    return text


def main() -> None:
    feed = feedparser.parse(FEED_URL)

    if getattr(feed, "bozo", False) and not getattr(feed, "entries", None):
        raise RuntimeError(f"Failed to parse feed: {FEED_URL}")

    entries = feed.entries[:MAX_ITEMS]
    now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")

    md_path = Path(OUTPUT_PATH)
    md_path.parent.mkdir(parents=True, exist_ok=True)

    lines: list[str] = []
    lines.append(f"# {SOURCE_NAME} Daily Briefing")
    lines.append("")
    lines.append(f"- Generated at: {now}")
    lines.append(f"- Feed: {FEED_URL}")
    lines.append(f"- Items: {len(entries)}")
    lines.append("")

    if not entries:
        lines.append("No new items found.")
    else:
        for idx, entry in enumerate(entries, start=1):
            title = clean_text(getattr(entry, "title", "Untitled"))
            link = getattr(entry, "link", "")
            summary = clean_text(getattr(entry, "summary", ""))[:300]

            published = ""
            if getattr(entry, "published", None):
                published = clean_text(entry.published)
            elif getattr(entry, "updated", None):
                published = clean_text(entry.updated)

            lines.append(f"## {idx}. {title}")
            lines.append("")
            if published:
                lines.append(f"- Published: {published}")
            if link:
                lines.append(f"- Link: {link}")
            lines.append("")
            if summary:
                lines.append(summary)
            else:
                lines.append("_No summary available._")
            lines.append("")

    md_path.write_text("\n".join(lines), encoding="utf-8")
    print(f"Wrote {md_path}")


if __name__ == "__main__":
    main()
