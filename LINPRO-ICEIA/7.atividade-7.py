class dados:
    def __init__(self,nome,rg):
        self.__nome = nome
        self.__rg = rg
    def get__nome(self):
        return f' {self.__nome}'
    def get__rg(self):
        return f' {self.__rg}'
nome= input("Digite vosso nome: ")
print()
rg= input("Degite o seu RG: ")
print()
dados1 = dados(nome, rg)
print(dados1.get__nome())
print(dados1.get__rg())
