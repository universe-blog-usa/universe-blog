#!/usr/bin/env python3
"""Replace the legacy site URL with the GitHub Pages URL across static site files."""

from pathlib import Path

OLD = "https://universe-blog.net"
NEW = "https://universe-blog-usa.github.io/universe-blog"
TEXT_EXTENSIONS = {".html", ".xml", ".json", ".js", ".css", ".txt", ".xsl"}


def main() -> None:
    updated_files = []
    for path in Path(".").rglob("*"):
        if not path.is_file():
            continue
        if path.suffix.lower() not in TEXT_EXTENSIONS:
            continue

        try:
            text = path.read_text(encoding="utf-8")
        except (UnicodeDecodeError, OSError):
            continue

        if OLD not in text:
            continue

        path.write_text(text.replace(OLD, NEW), encoding="utf-8")
        updated_files.append(str(path))

    if not updated_files:
        print("No files with the legacy URL were found.")
        return

    print("Updated files:")
    for file_path in updated_files:
        print(file_path)


if __name__ == "__main__":
    main()
