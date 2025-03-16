import os
os.system("cls || clear")


while True:
    num=int(input("digite um numero positivo: "))
    
    if num <0:
        print("Numero negativo inserido, codigo encerrado")
    
        break
    elif num == 0:
      print("zero")
    else:
        print("numero positivo")
    