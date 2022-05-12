import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt

filepath_conversions = "conversiones.csv"
filepath_navegacion = "navegacion.csv"

conversions = pd.read_csv(filepath_conversions, sep=";", parse_dates=True)
navegacion = pd.read_csv(filepath_navegacion, sep=";", parse_dates=True)

#! Analisis dataset
print(conversions.head())
print(navegacion.head())

print(conversions.columns)
print(navegacion.columns)

conversion_data = conversions.groupby("result")["result"].count()
conversion_excel_filename = "excels/conversion_data.xlsx"
pd.DataFrame(conversion_data).to_excel(conversion_excel_filename)

sns.barplot(x=conversion_data.index, y=conversion_data.values)
conversion_data_filename = "plots/conversion_data"
plt.savefig(conversion_data_filename)

conversion_rate = conversion_data.at["Positivo"] / len(conversions.index)
print(f"La tasa de conversión de llamadas es de {conversion_rate * 100}%")
print(f'(Ver tabla "{conversion_excel_filename}" y "{conversion_data_filename}")')

type_data = conversions.groupby("lead_type")["lead_type"].count()
type_excel_filename = "excels/type_data.xlsx"
pd.DataFrame(type_data).to_excel(type_excel_filename)

sns.barplot(x=type_data.index, y=type_data.values)
type_data_filename = "plots/type_data"
plt.savefig(type_data_filename)

call_rate = type_data.at["CALL"] / len(conversions.index)
call_n, form_n = type_data.at["CALL"], type_data.at["FORM"]
print(f"El número de llamadas fue de {call_n}, mientras que la tasa de forularios fue de {form_n}")
print(f'Ver tabla "{type_excel_filename} y {type_data_filename}')


recurrent_data = navegacion.groupby("user_recurrent")["user_recurrent"].count()
recurrent_excel_filename = "excels/recurrent_data.xlsx"
pd.DataFrame(recurrent_data).to_excel(recurrent_excel_filename)

recurrent_data_adapted = recurrent_data.copy()
recurrent_data_adapted.index = ["No recurrente", "Recurrente"]
sns.barplot(x=recurrent_data_adapted.index, y=recurrent_data_adapted.values)
recurrent_data_filename = "plots/recurrent_data"
plt.savefig(recurrent_data_filename)

recurrent_rate = recurrent_data.at[True] / len(navegacion.index)
print(f"El porcentaje de usuarios recurrents fue de {recurrent_rate*100:.2f}%")
print(f'(Ver tabla "{recurrent_excel_filename}" y "{recurrent_data_filename}"')


gclid_analisis = navegacion.groupby("gclid")["gclid"].count()
gclid_analisis_sorted = gclid_analisis.sort_values()
print(gclid_analisis_sorted)
print(gclid_analisis_sorted.shape)

