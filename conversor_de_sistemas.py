print("Conversor de sistemas")
import threading

def num_bin(num,resultado):
    if num == 0:
        resultado = "0"
    else:
        num_D = num
        while num_D > 0:
            resto = num_D%2
            num_D = num_D // 2
            resultado = str(resto) + resultado
    print(f"Número em Binário: {resultado}")
def num_hex(num,resultado):
    if num == 0:
        resultado = "0"
    else:
        num_D = num
        while num_D > 0:
            resto = num_D % 16
            num_D = num_D // 16
            if resto < 10:
                resultado = str(resto) + resultado
            elif resto == 10:
                resultado = "A" + resultado
            elif resto == 11:
                resultado = "B" + resultado
            elif resto == 12:
                resultado = "C" + resultado
            elif resto == 13:
                resultado = "D" + resultado
            elif resto == 14:
                resultado = "E" + resultado
            elif resto == 15:
                resultado = "F" + resultado
            else:
                resultado = ""
    print(f"Número em hexadecimal: {resultado}")

num = int(input("Digite o Número Decimal = "))
resultado = ""
print(f"Número em decimal: {num}")
t1 = threading.Thread(target= num_bin, args= (num,resultado))
t2 = threading.Thread(target= num_hex, args= (num,resultado))

t1.start()
t2.start()

t1.join()
t2.join()
