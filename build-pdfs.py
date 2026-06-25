#!/usr/bin/env python3
"""Convert Nerva OS markdown docs to PDFs using Chrome headless."""
import os
import subprocess
import sys
from pathlib import Path

import markdown

ROOT = Path(__file__).parent
PDF_DIR = ROOT / "docs-pdf"
PDF_DIR.mkdir(exist_ok=True)

CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"

CSS = """
<style>
  @page { margin: 18mm 16mm 18mm 16mm; }
  body {
    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif;
    font-size: 11pt;
    line-height: 1.55;
    color: #1a1a1a;
    max-width: 100%;
    margin: 0;
    padding: 0;
  }
  h1 {
    font-size: 24pt;
    border-bottom: 2px solid #333;
    padding-bottom: 6px;
    margin-top: 0;
    margin-bottom: 18px;
  }
  h2 {
    font-size: 16pt;
    border-bottom: 1px solid #ccc;
    padding-bottom: 4px;
    margin-top: 28px;
    margin-bottom: 12px;
  }
  h3 { font-size: 13pt; margin-top: 20px; margin-bottom: 8px; }
  h4 { font-size: 12pt; margin-top: 16px; margin-bottom: 6px; }
  p { margin: 8px 0; }
  ul, ol { margin: 8px 0; padding-left: 24px; }
  li { margin: 4px 0; }
  code {
    background: #f4f4f6;
    padding: 2px 5px;
    border-radius: 3px;
    font-family: 'SF Mono', Monaco, Menlo, Consolas, monospace;
    font-size: 9.5pt;
  }
  pre {
    background: #f4f4f6;
    padding: 12px;
    border-radius: 5px;
    overflow-x: auto;
    border-left: 3px solid #888;
    font-size: 9.5pt;
    line-height: 1.4;
  }
  pre code { background: none; padding: 0; }
  blockquote {
    border-left: 3px solid #888;
    padding-left: 12px;
    color: #555;
    margin: 12px 0;
  }
  table {
    border-collapse: collapse;
    width: 100%;
    margin: 12px 0;
    font-size: 10pt;
  }
  th, td {
    border: 1px solid #ddd;
    padding: 8px 10px;
    text-align: left;
  }
  th {
    background: #f4f4f6;
    font-weight: 600;
  }
  hr { border: none; border-top: 1px solid #ddd; margin: 24px 0; }
  a { color: #0a5cc6; text-decoration: none; }
  strong { font-weight: 600; }
  .footer {
    margin-top: 40px;
    padding-top: 12px;
    border-top: 1px solid #ddd;
    color: #888;
    font-size: 9pt;
    text-align: center;
  }
</style>
"""

HTML_TEMPLATE = """<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <title>{title}</title>
  {css}
</head>
<body>
{body}
<div class="footer">Nerva OS &mdash; {filename}</div>
</body>
</html>
"""

# Files to convert
FILES = [
    ROOT / "WELCOME.md",
    ROOT / "README.md",
    ROOT / "INSTALL.md",
    ROOT / "docs" / "01-getting-started.md",
    ROOT / "docs" / "02-your-first-conversation.md",
    ROOT / "docs" / "04-the-skill-system.md",
    ROOT / "docs" / "09-troubleshooting.md",
    ROOT / "docs" / "GLOSSARY.md",
]


def md_to_pdf(md_path: Path) -> Path:
    """Convert one markdown file to PDF via HTML + Chrome headless."""
    text = md_path.read_text(encoding="utf-8")
    html_body = markdown.markdown(
        text,
        extensions=["tables", "fenced_code", "toc", "sane_lists", "nl2br"],
    )
    title = md_path.stem.replace("-", " ").title()
    full_html = HTML_TEMPLATE.format(
        title=title, css=CSS, body=html_body, filename=md_path.name
    )

    tmp_html = PDF_DIR / f".{md_path.stem}.html"
    tmp_html.write_text(full_html, encoding="utf-8")

    pdf_out = PDF_DIR / f"{md_path.stem}.pdf"

    subprocess.run(
        [
            CHROME,
            "--headless",
            "--disable-gpu",
            "--no-pdf-header-footer",
            f"--print-to-pdf={pdf_out}",
            f"file://{tmp_html.absolute()}",
        ],
        check=True,
        capture_output=True,
    )

    tmp_html.unlink()
    return pdf_out


def main():
    print(f"Converting {len(FILES)} files to PDF...")
    print(f"Output: {PDF_DIR}")
    print("---")
    for md in FILES:
        if not md.exists():
            print(f"  SKIP: {md} (missing)")
            continue
        try:
            pdf = md_to_pdf(md)
            size = pdf.stat().st_size / 1024
            print(f"  OK:   {pdf.name} ({size:.0f} KB)")
        except subprocess.CalledProcessError as e:
            print(f"  FAIL: {md.name} — {e}")
            sys.exit(1)
    print("---")
    print(f"Done. {len(list(PDF_DIR.glob('*.pdf')))} PDFs in {PDF_DIR}")


if __name__ == "__main__":
    main()
