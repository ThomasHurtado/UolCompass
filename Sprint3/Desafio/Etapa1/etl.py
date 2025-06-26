import pandas as pd

if __name__ == "__main__":
    db = pd.read_csv('concert_tours_by_women.csv')

    db2 = db.copy()

    db2 = db2.drop(['Peak', 'All Time Peak', 'Ref.'], axis=1)

    db2['Actual gross'] = db2['Actual gross'].str.replace(r',', '', regex=False)
    db2['Actual gross'] = db2['Actual gross'].str.extract(r'\$(\d+\.?\d*)')
    db2['Actual gross'] = db2['Actual gross'].astype(float)

    db2['Adjustedgross (in 2022 dollars)'] = db2['Adjustedgross (in 2022 dollars)'].str.replace(r',', '', regex=False)
    db2['Adjustedgross (in 2022 dollars)'] = db2['Adjustedgross (in 2022 dollars)'].str.extract(r'\$(\d+\.?\d*)')
    db2['Adjustedgross (in 2022 dollars)'] = db2['Adjustedgross (in 2022 dollars)'].astype(float)

    db2['Average gross'] = db2['Average gross'].str.replace(r',', '', regex=False)
    db2['Average gross'] = db2['Average gross'].str.extract(r'\$(\d+\.?\d*)')
    db2['Average gross'] = db2['Average gross'].astype(float)

    db2['Start year'] = db2['Year(s)'].str.replace(r'-\s*.*$', '', regex=True)

    db2['End year'] = db2['Year(s)'].str.extract(r'-\s*(\d+)')
    db2['End year'] = db2['End year'].fillna(db2['Start year'])

    db2.to_csv('/dados/csv_limpo.csv', index=False)

