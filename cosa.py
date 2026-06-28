# %% Dinero curso python
capital = float(input("Ingrese su saldo inicial: "))

transporte = 10
comida = 200
material = 50

dias = int(input("Por cuantos dias quiere calcular los gastos: "))

suma = dias * (transporte + comida + material)

total = capital - suma

print(
    f"Con un saldo inicial de {capital}, su saldo final tras los gastos de {dias} dia/s es : {total}"
)
