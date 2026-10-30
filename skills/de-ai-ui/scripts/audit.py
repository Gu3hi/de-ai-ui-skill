#!/usr/bin/env python3
"""de-ai-ui audit: machine-checkable subset of the slop checklist.

Scans CSS / HTML / JSX-like files for signals that can be detected
mechanically. It does NOT judge taste: optical alignment, copy quality,
icon consistency etc. still need the human/agent checklist in
references/slop-checklist.md.

Usage:
    python3 audit.py <file-or-dir> [<file-or-dir> ...] [--strict]

Exit code: 0 normally; 1 with --strict when any finding is reported.
Stdlib only, no dependencies.
"""
import os
import re
import sys

EXTS = {".css", ".scss", ".html", ".htm", ".jsx", ".tsx", ".vue", ".svelte"}

SLOP_FONTS = ["Instrument Serif", "Space Grotesk", "Bricolage Grotesque"]
PURPLE_HEXES = ["#8b5cf6", "#a855f7", "#9333ea", "#7c3aed", "#6366f1", "#818cf8"]
GRADIENT_WORDS = ["purple", "violet", "fuchsia"]


def iter_files(paths):
    for p in paths:
        if os.path.isfile(p):
            yield p
        elif os.path.isdir(p):
            for root, _dirs, names in os.walk(p):
                for n in sorted(names):
                    if os.path.splitext(n)[1].lower() in EXTS:
                        yield os.path.join(root, n)


def audit_file(path):
    with open(path, encoding="utf-8", errors="ignore") as fh:
        text = fh.read()
    # Strip comments so headers / notes don't trigger content rules.
    text = re.sub(r"/\*.*?\*/", "", text, flags=re.S)
    text = re.sub(r"<!--.*?-->", "", text, flags=re.S)
    findings = []  # (rule, detail)

    # Purple / blue-purple gradients
    for m in re.finditer(r"(linear|radial|conic)-gradient\([^)]*\)", text, re.I):
        seg = m.group(0).lower()
        if any(w in seg for w in GRADIENT_WORDS) or any(h in seg for h in PURPLE_HEXES):
            findings.append(("purple-gradient", m.group(0)[:80]))

    # Slop fonts
    for font in SLOP_FONTS:
        if font.lower() in text.lower():
            findings.append(("slop-font", font))

    # Font sizes: too many steps / below 12px
    sizes = sorted({float(x) for x in re.findall(r"font-size\s*:\s*([0-9.]+)px", text)})
    if len(sizes) > 4:
        findings.append(("font-size-count", f"{len(sizes)} sizes: {sizes}"))
    small = [s for s in sizes if s < 12]
    if small:
        findings.append(("font-size-too-small", f"below 12px: {small}"))

    # Middle-dot separator in markup text
    if "·" in text:
        findings.append(("middle-dot-separator", "found '·' character"))

    # All-caps small headings
    if re.search(r"text-transform\s*:\s*uppercase", text):
        findings.append(("uppercase-transform", "text-transform: uppercase"))

    # Card left accent bar: thick colored border-left
    for m in re.finditer(r"border-left\s*:\s*([2-9]|[1-9][0-9])px\s+solid\s+(#[0-9a-fA-F]{3,8}|[a-z]+)", text):
        if m.group(2).lower() not in ("transparent", "inherit", "currentcolor"):
            findings.append(("card-left-accent-bar", m.group(0)[:80]))

    # Mixed border widths (1px and 0.5px on borders in one file)
    widths = set(re.findall(r"border(?:-[a-z]+)?\s*:\s*([0-9.]+)px", text))
    if "1" in widths and "0.5" in widths:
        findings.append(("mixed-border-widths", f"border widths in file: {sorted(widths)}"))

    return findings


def main(argv):
    strict = "--strict" in argv
    paths = [a for a in argv[1:] if not a.startswith("--")]
    if not paths:
        print(__doc__)
        return 2
    total = 0
    for path in iter_files(paths):
        findings = audit_file(path)
        for rule, detail in findings:
            total += 1
            print(f"{path}: [{rule}] {detail}")
    print(f"\n{total} finding(s). Manual checklist: references/slop-checklist.md")
    return 1 if (strict and total) else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
