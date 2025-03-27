import os
os.system("cls | clear")
l_num=[1, 2, 3, 8, 0, 0]
l_negatives=[-9, -6, -3, 0]
for i in range(4):
 p_num=int(input("digite um numero inteiro: "))
 l_num.append(p_num)
 l_num[4] = 9

print()
for i in range(4):
 num=int(input("digite um numero inteiro negativo \n(pode escrever positivo, serao negativados): "))
 neg_num=num*(-1)
 l_negatives.append(neg_num)
 l_negatives[1] = -3

print()
print(f"tabela de numeros inteiros positivos: {l_num}")
print()
print(f"tabela de numeros inteiros positivos: {l_negatives}")

p_tamanho=len(l_num)
print(f" qauntidade da tabela positiva {p_tamanho}")
print()
n_tamanho=len(f" quantidade da tabela negativa {l_negatives}")
print(n_tamanho)



