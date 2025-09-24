import os
os.system("cls || clear")

class carro:
  def __init__(self,modelo):
    self.modelo=modelo
  def freiar(self):
    return f"o {self.modelo}"
  def acelerar(self):
    return f"o {self.modelo}"

freio=carro("ce parou de dirigir")
acelera=carro("Eu vou dirigir, Depois de beber. O veadinho ali, Só sabe correr. Se multar, Não vou me importar, Vou atropelar. O meu tanque ta Lotado mermão, Cê tá ferrado na minha mão, Te pulveriza Com minha carreta É o meu Bergentrück. Truck")

print(f" Freio: \n{freio.freiar()}")
print()
print()
print(f" Acelelerar: \n{acelera.acelerar()}")
