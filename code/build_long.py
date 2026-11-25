import glob, re, os, openpyxl, pandas as pd
SRC = '/mnt/user-data/attachments/5ed52829-823d-5802-846d-3e50f577c3a4/'
OUT = os.path.dirname(os.path.abspath(__file__))
recs = []
files = sorted(glob.glob(SRC + '*.xlsx'))
for f in files:
    base = os.path.basename(f)
    fam = re.sub(r'[-_]?\d*\.xlsx$', '', base.split('-', 1)[1]) if '-' in base else base
    ws = openpyxl.load_workbook(f, read_only=True).active
    rows = list(ws.iter_rows(values_only=True))
    hdr = rows[0]
    cols = [(i, str(h).strip()) for i, h in enumerate(hdr) if i >= 2 and h not in (None, '')]
    parent = None; code = None
    for r in rows[1:]:
        label = r[0]
        if label is None or str(label).strip() == '':
            continue
        label = str(label).strip()
        if label == 'Indicator':
            continue
        if label.startswith('↳'):
            segment = label.lstrip('↳ ').strip()
            ind, ic = parent, code
        else:
            parent, code = label, (str(r[1]).strip() if r[1] else None)
            segment = 'All'
            ind, ic = parent, code
        for i, ch in cols:
            v = r[i]
            if v is None: continue
            sv = str(v).strip()
            num = None
            try: num = float(sv)
            except ValueError: pass
            m = re.match(r'^(.*?)\s*\((\d{4})\)$', ch)
            if m: place, year = m.group(1), int(m.group(2))
            else: place, year = ch, None
            recs.append(dict(family=fam, file=base, indicator_code=ic, indicator=ind,
                             segment=segment, place=place, year=year,
                             value_raw=sv, value=num))
df = pd.DataFrame(recs)
df.to_csv(os.path.join(OUT, 'long_raw.csv'), index=False)
print('rows', len(df), 'files', len(files))
print(df.family.value_counts())
print('non-numeric values:', df.value.isna().sum())
print(df.value_raw[df.value.isna()].value_counts().head(10))
