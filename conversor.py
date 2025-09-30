print("Conversor decimal para hexadecimal")
num = int(input("Digite um Número Decimal = "))
res_H = ""

if num == 0:
    res_H = "0"
else:
    num_D = num
    while num_D > 0:
        resto = num_D % 16
        num_D = num_D // 16
        if resto < 10:
            res_H = str(resto) + res_H
        elif resto == 10:
            res_H = "A" + res_H
        elif resto == 11:
            res_H = 'B' + res_H
        elif resto == 12:
            res_H = 'C' + res_H
        elif resto == 13:
            res_H = 'D' + res_H
        elif resto == 14:
            res_H == 'E' + res_H
        elif resto == 15:
            res_H = 'F' + res_H
        else:
            res_H = ""
print(f"O valor '{num}' em hexadecimal corresponde à: {res_H}!")
