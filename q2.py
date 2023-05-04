import pandas as pd
import matplotlib.pyplot as plt

url = 'https://en.wikipedia.org/wiki/Minnesota'
dfs = pd.read_html(
    url,
    match = "Largest cities or towns in Minnesota"
)
df = dfs[0]
# df = df.iloc[0:-2]
# df = df[ ['Name','Pop.'] ].astype('int')
# print(df.info())
# df.plot(x = 'Name.', y = 'Pop.', kind = 'bar')
# plt.show()
print(df.info())