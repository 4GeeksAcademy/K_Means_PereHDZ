import pandas as pd

url = "https://raw.githubusercontent.com/4GeeksAcademy/k-means-project-tutorial/main/housing.csv"

df = pd.read_csv(url)

df.to_csv('housing.csv', index=False)
print("Dataset saved as 'housing.csv'")