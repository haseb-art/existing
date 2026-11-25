import pandas as pd, re
df = pd.read_csv('long_raw.csv', keep_default_na=False, dtype=str)
df = df[(df.year != '') & (df.value != '')]           # country-level rows with a numeric value
df['year'] = df.year.astype(float).astype(int)
df['value'] = df.value.astype(float)
df['indicator'] = df.indicator.str.replace(r'\s+', ' ', regex=True).str.strip()
df['segment'] = df.segment.str.strip()
key = ['place', 'year', 'indicator_code', 'segment']
df = df.drop_duplicates(subset=key + ['value'])     # identical copies across files
dup = df.duplicated(subset=key, keep=False)
print('conflicting country-level duplicates remaining:', int(dup.sum()))
df = df.drop_duplicates(subset=key)
def slug(s): return re.sub(r'[^A-Za-z0-9]+', '_', s).strip('_')[:40]
df['var'] = df.indicator_code + df.segment.map(lambda s: '' if s == 'All' else '__' + slug(s))
long = df.rename(columns={'place': 'economy', 'year': 'survey_year'})[
    ['economy', 'survey_year', 'family', 'indicator_code', 'indicator', 'segment', 'var', 'value']]
long.to_csv('country_panel_long.csv', index=False)
wide = df.pivot_table(index=['place', 'year'], columns='var', values='value', aggfunc='first').reset_index()
wide = wide.rename(columns={'place': 'economy', 'year': 'survey_year'}).sort_values('economy')
wide.to_csv('country_panel_wide.csv', index=False)
dic = (df.groupby(['indicator_code', 'family', 'indicator', 'segment', 'var'])
         .agg(economies_nonmissing=('place', 'nunique')).reset_index())
dic.to_csv('indicator_dictionary.csv', index=False)
print('economies:', wide.economy.nunique(), ' survey years:', sorted(wide.survey_year.unique())[:3], '...', sorted(wide.survey_year.unique())[-3:])
print('wide shape:', wide.shape, ' indicator-variables:', dic.shape[0])
print('segments:', sorted(df.segment.unique()))
