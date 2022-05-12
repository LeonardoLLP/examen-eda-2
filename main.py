import pandas as pd
import seaborn as sns

filepath_conversions = "conversiones.csv"
filepath_navegacion = "navegacion.csv"

conversions = pd.read_csv(filepath_conversions, sep=";", parse_dates=True)
navegacion = pd.read_csv(filepath_navegacion, sep=";", parse_dates=True)

print(conversions.head())
print(navegacion.head())

print(conversions.columns)
print(navegacion.columns)