import pandas as pd
import seaborn as sns

# Part.3
# 3-1
df = pd.read_csv(R'C:\Users\dbgya\OneDrive\바탕 화면\CODE\KDT\[2]Pandas\WORK\auto-mpg.csv', header=None)

df.columns = ['mpg','cylinders','displacement','horsepower','weight',
                'acceleration','model year','origin','name']


print(df.head())
print()

print(df.tail())
print()

print(df.shape)
print()

df.info() 
print()

# 3-2
print(df.dtypes)
print()


print(df["mpg"].dtypes)
print()


print(df.describe())
print()

print(df.describe(include='all'))
print()

print(df.count())
print()

print(type(df.count()))
print()

unique_values = df['origin'].value_counts() 
print(unique_values)
print()

unique_values_ratio = df['origin'].value_counts(normalize=True) 
print(unique_values_ratio)
print()

unique_values_percentage = (df['origin'].value_counts(normalize=True) * 100 ).round(1)
print(unique_values_percentage)
print()

# 3-3
print(df.median(numeric_only=True))
print('\n')
print(df['mpg'].median())

print(df.max(numeric_only=True))
print('\n')
print(df['mpg'].max())

print(df.min(numeric_only=True))
print('\n')
print(df['mpg'].min())

print(df.std(numeric_only=True))
print('\n')
print(df['mpg'].std())

print(df.corr(numeric_only=True))
print('\n')
print(df[['mpg','weight']].corr())

# Part.5
# 5-1
df = sns.load_dataset('titanic')

print(df['deck'].value_counts(dropna=False) )
print()

print(df.head().isnull())
print()

print(df.head().notnull())
print()

print(df.head().isnull().sum(axis=0))
print()

ser1 = pd.Series([1, 2, None])
print(ser1)
print()

ser2 = pd.Series([1, 2, None], dtype="Int64")
print(ser2)
print()

# 5-2
print(df.isnull().sum(axis=0))
print()

df_thresh = df.dropna(axis=1, thresh=500)  
print(df_thresh.columns)
print()

df_age = df.dropna(subset=['age'], how='any', axis=0)  
print(len(df_age))
print()

df_age_deck = df.dropna(subset=['age', 'deck'], how='all', axis=0)  
print(len(df_age_deck))
print()

# 5-3
print(df['age'].head(10))
print()

mean_age = df['age'].mean(axis=0)
df['age'] = df['age'].fillna(mean_age) 
print(df['age'].head(10))
print()

# 5-4
print(df['embark_town'][825:830])
print()

most_freq = df['embark_town'].value_counts(dropna=True).idxmax()   
print(most_freq)
print()

most_freq2 = df['embark_town'].mode()[0]   
print(most_freq2)
print()

df['embark_town'] = df['embark_town'].fillna(most_freq)
print(df['embark_town'][825:830])
print()

# 5-5
df2 = df.copy()
print(df['embark_town'][825:831])
print()

df['embark_town'] = df['embark_town'].ffill()
print(df['embark_town'][825:831])
print()

df2['embark_town'] = df2['embark_town'].bfill()
print(df2['embark_town'][825:831])
print()

# 5-6
df = pd.DataFrame({
    'c1':['a', 'a', 'b', 'a', 'b'],
    'c2':[1, 1, 1, 2, 2],
    'c3':[1, 1, 2, 2, 2]
})

df_dup_first = df.duplicated()
print(df_dup_first)
print()

df_dup_last = df.duplicated(keep='last')
print(df_dup_last)
print()

df_dup_false = df.duplicated(keep=False)
print(df_dup_false)
print()

col_dup = df['c2'].duplicated()
print(col_dup)
print()

col_dup2 = df.duplicated(subset=['c2'])
print(col_dup2)
print()

# 5-7
df2 = df.drop_duplicates()
print(df2)
print()

df3 = df.drop_duplicates(keep='last')
print(df3)
print()

df4 = df.drop_duplicates(keep=False)
print(df4)
print()

df5 = df.drop_duplicates(subset=['c2', 'c3'])
print(df5)
print()

df6 = df.drop_duplicates(subset=['c2', 'c3'], keep=False)
print(df6)
print()