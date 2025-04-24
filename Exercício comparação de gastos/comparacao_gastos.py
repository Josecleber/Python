gastos_joao = [300, 500, 200, 800]
gastos_pedro = [200, 400, 500, 700]

total_gastos_joao = sum(gastos_joao)
total_gastos_pedro = sum(gastos_pedro)

if total_gastos_joao > total_gastos_pedro:
    print("João gastou mais que Pedro")
elif total_gastos_pedro > total_gastos_joao:
    print("Pedro gastou mais que João")
else:
    print("João e Pedro gastaram o mesmo valor")
