class dados:
    def __init__(self,nome,rg):
        self.__nome = nome
        self.__rg = rg
    def get__nome(self):
        return f' {self.__nome}'
    def get__rg(self):
        return f' {self.__rg}'
    def set__nome(self,novo__nome):
      self.__nome=novo__nome
    def set__rg(self,novo__rg):
        self.__rg=novo__rg
        
dados1=dados('rogerio', '232.455.677-98')
print("DADOS1\n")
print(dados1.get__nome())
print(dados1.get__rg())
print("\nDADOS2\n")
dados1.set__nome('julia')
dados1.set__rg('321.456.788-87')
print(dados1.get__nome())
print(dados1.get__rg())
