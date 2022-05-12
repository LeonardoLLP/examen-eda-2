import pandas as pd
import seaborn as sns

filepath_conversions = "conversiones.csv"
filepath_navegacion = "navegacion.csv"

conversions = pd.read_csv(filepath_conversions, sep=";", parse_dates=True)
navegacion = pd.read_csv(filepath_navegacion, sep=";", parse_dates=True)

#! Analisis dataset
# print(conversions.head())
# print(navegacion.head())

# print(conversions.columns)
# print(navegacion.columns)

conversion_data = conversions.groupby("result")["result"].count()
print(conversion_data)

conversion_rate = conversion_data.at["Positivo"] / len(conversions.index)
conversion_rate_filename = "excels/conversion_rate.xlsx"
pd.DataFrame(conversion_data).to_excel(conversion_rate_filename)

print(f"La tasa de conversión de llamadas es de {conversion_rate * 100}%")
print(f'(Ver tabla "{conversion_rate_filename}")')



