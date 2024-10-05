import pandas as pd

datos = {'Nombre': ['Alice', 'Bob', 'Charlie'],
         'Edad': [25, 30, 35],
         'Ciudad': ['A', 'B', 'C']}

df = pd.DataFrame(datos)


data = {'state': ['Ohio', 'Ohio', 'Ohio', 'Nevada', 'Nevada', 'Nevada'],
        'year': [2000, 2001, 2002, 2001, 2002, 2003],
        'pop': [1.5, 1.7, 3.6, 2.4, 2.9, 3.2]}
frame = pd.DataFrame(data)
print(frame)