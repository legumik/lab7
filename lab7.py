import pandas as pd

url_data_temperatura = (r'https://raw.githubusercontent.com/legumik/lab7-winf/refs/heads/master/pomiary_wilgotno%C5%9Bci_kranowki.csv')
url_data_wilgotnosc = (r'https://raw.githubusercontent.com/legumik/lab7-winf/refs/heads/master/pomiary_temperatury.csv')

tempreatura_csv = pd.read_csv(url_data_temperatura)
wilgotnosc_csv = pd.read_csv(url_data_wilgotnosc)

print("Dane csv temperatura:")
print(tempreatura_csv)
print("Dane csv wilgotność:")
print(wilgotnosc_csv)