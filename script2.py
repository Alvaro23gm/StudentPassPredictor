# Sistema que calcula diariamente cómo crece el dinero de clientes de un banco

import numpy as np
import pandas as pd

saldos = np.array([1000, 2500, 500, 3200, 4500])

tasa = 10

saldoFinal = (saldos * tasa / 100) + saldos

#print(saldos)
#print(saldoFinal)

# Los 2 clientes con mayor saldo final
print(f"Los dos mayores saldos son: {np.sort(saldoFinal)[-2:]}")

record1 = pd.Series({'Name': 'Alvaro', 'Class':'Math', 'Score': 100})


