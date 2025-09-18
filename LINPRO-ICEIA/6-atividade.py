class carro:
  def __init__(self,modelo):
    self.modelo=modelo
  def freiar(self):
    return f"o {self.modelo}"
  def acelerar(self):
    return f"o {self.modelo}"

freio=carro("ce parou de dirigir")
acelera=carro("Eu vou dirigir, Depois de beber. O veadinho ali, Só sabe correr. Se mul tar, Não vou me importar, Vou atropelar. O meu tanque ta Lotado mermão, Cê tá ferrado na minha mão, Te pulveriza Com minha carreta É o meu Bergentrück. Truck")

print(freio.freiar())
print()
print()
print(acelera.acelerar())
