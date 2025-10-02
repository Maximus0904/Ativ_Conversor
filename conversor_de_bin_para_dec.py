print("Conversor de sistemas")
num = input("Digite o Número Binário = ")
def bin_para_dec(num):
    if num == "":
        return 0
    else:
        return int(num[0]) * (2 ** (len(num)-1)) + bin_para_dec(num[1:])
resultado = bin_para_dec(num)
print(resultado)
