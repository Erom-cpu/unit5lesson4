import pandas as pd
import matplotlib.pyplot as plt

url = 'https://en.wikipedia.org/wiki/New_York_City#Demographics'
dfs = pd.read_html(
    url,
    match = "Historical population"
)
df = dfs[0]
df = df.iloc[0:-2]

df = df[['Year','Pop.']].astype('int')
print(df)
df.plot('Year', y = 'Pop.', kind = 'bar')
plt.show()
print(df.info())