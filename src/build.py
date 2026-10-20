"""Rebuild ../index.html from template.html + portsmouth.json.

Usage:  python3 src/build.py
"""
import json, pathlib

here = pathlib.Path(__file__).resolve().parent
data = json.loads((here / "portsmouth.json").read_text())
page = (here / "template.html").read_text().replace(
    "__DATA__", json.dumps(data, separators=(",", ":"))
)
html = (
    '<!doctype html>\n<html lang="en">\n<head>\n<meta charset="utf-8">\n'
    '<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n'
    + page.replace("</style>\n", "</style>\n</head>\n<body>\n", 1)
    + "</body>\n</html>\n"
)
(here.parent / "index.html").write_text(html)
print("wrote index.html", len(html), "bytes")
