#!/usr/bin/env python3
"""Scan email copy for spam trigger words.

Usage:
    python spam_check.py emails.csv phrases.txt
    python spam_check.py emails.xlsx phrases.txt --sheet "Emails"

emails:  CSV or XLSX. Every text column is scanned (or pass --columns).
phrases: one spam word or phrase per line. Build it from a public list,
         e.g. https://mailmeteor.com/blog/spam-words

Matches are whole words, case-insensitive, and include simple plurals.
Prints a count per phrase and column, with one example for each.
"""
import argparse, collections, csv, re, sys


def load_rows(path, sheet=None):
    if path.lower().endswith(('.xlsx', '.xlsm')):
        import openpyxl  # pip install openpyxl
        wb = openpyxl.load_workbook(path, data_only=True)
        ws = wb[sheet] if sheet else wb.active
        it = ws.iter_rows(values_only=True)
        header = [str(h) for h in next(it)]
        return [dict(zip(header, r)) for r in it]
    with open(path, newline='', encoding='utf-8-sig') as f:
        return list(csv.DictReader(f))


def compile_phrases(path):
    phrases = sorted({p.strip() for p in open(path, encoding='utf-8') if p.strip()}, key=len, reverse=True)
    out = []
    for p in phrases:
        pre = r'(?<![A-Za-z0-9])' if p[0].isalnum() else ''
        post = r'(?:s|es)?(?![A-Za-z0-9])' if p[-1].isalnum() else ''
        out.append((p, re.compile(pre + re.escape(p) + post, re.I)))
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('emails')
    ap.add_argument('phrases')
    ap.add_argument('--sheet')
    ap.add_argument('--columns', nargs='*', help='only scan these columns')
    a = ap.parse_args()

    rows = load_rows(a.emails, a.sheet)
    pats = compile_phrases(a.phrases)
    cols = a.columns or [k for k in rows[0] if any(isinstance(r.get(k), str) for r in rows)]
    counts, example = collections.Counter(), {}
    dirty = 0
    for r in rows:
        hit = False
        for c in cols:
            text = r.get(c)
            if not isinstance(text, str):
                continue
            for p, rx in pats:
                m = rx.search(text)
                if m:
                    hit = True
                    counts[(p, c)] += 1
                    s = max(0, m.start() - 40)
                    example.setdefault((p, c), text[s:m.end() + 40].replace('\n', ' '))
            if re.search(r'[\u2013\u2014]', text):
                hit = True
                counts[('em/en dash', c)] += 1
                example.setdefault(('em/en dash', c), text[:80])
        dirty += hit
    print(f'{dirty} of {len(rows)} rows have at least one hit\n')
    for (p, c), n in counts.most_common():
        print(f'{n:5}  {c:<14} [{p}]  ...{example[(p, c)]}...')
    sys.exit(1 if counts else 0)


if __name__ == '__main__':
    main()
