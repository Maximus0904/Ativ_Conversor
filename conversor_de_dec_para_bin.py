print("Conversor de sistemas")
num = int(input("Digite o Número Decimal = "))
resultado = ""
if num == 0:
    resultado = "1"
else:
    num_D = num
    while num_D > 0:
        resto = num_D % 2
        num_D = num_D // 2
        resultado = str(resto) + resultado
print(f"O valor de '{num}'em binário corresponde a: {resultado}")
