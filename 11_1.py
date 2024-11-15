import requests
import pandas as pd
import numpy as np

# Requests - библиотека для упрощения обработки HTTP запросов в языке Python

url = 'https://www.sports.ru'
response = requests.get(url)

print(response.text)


# pandas - используется для обработки данных и анализа

data = {'Имя': ['Алексей', 'Нина', 'Светлана', 'Николай'],
        'Возраст': [21, 19, 42, 38],
        'Город': ['Сызрань', 'Астана', 'Стамбул', 'Воркута']}

df = pd.DataFrame(data)
print(df.head())

# Numpy - Библиотека для работы с числовыми данными и массивами

array = np.random.rand(6)
print(array)
array = array * 2
print(array)