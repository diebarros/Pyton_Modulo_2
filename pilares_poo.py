print("\nExemplo de herança:")
class animal:
    def __init__(self, nome) -> None:
        self.nome = nome

    def andar(self):
        print(f"O animal {self.nome} andou")
        return
    
    def emitir_som(self):
        pass

class cachorro(animal):
    def emitir_som(self):
        return "Au, au!"

class gato(animal):
    def emitir_som(self):
        return "Miau!"
    
dog = cachorro(nome="Rex")
cat = gato(nome="Felix")

print("\nExemplo de polimofirmo")
animais = [dog, cat]

for animal in animais:
    print(f"{animal.nome} faz: {animal.emitir_som()}")

print("\nExemplos de encapsulamento:")
class ContaBancaria:
    def __init__(self, saldo) -> None:
        self.__saldo = saldo 

    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
    
    def sacar(self, valor):
        if valor > 0 and valor <= self.__saldo:
            self.__saldo -= valor

    def consultar_saldo(self):
        return self.__saldo
    
conta = ContaBancaria(saldo=1000)
print(f"Saldo da conta bancária: {conta.consultar_saldo()}")
conta.depositar(valor=500)
print(f"Saldo da conta bancária: {conta.consultar_saldo()}")
conta.depositar(valor=-500)
print(f"Saldo da conta bancária: {conta.consultar_saldo()}")
conta.sacar(valor=200)
print(f"Saldo da conta bancária: {conta.consultar_saldo()}")

print("\nExemplo de abstração:")
from abc import ABC, abstractmethod

class veiculo(ABC):

    @abstractmethod
    def ligar(self):
        pass

    @abstractmethod
    def desligar(self):
        pass

class carro(veiculo):
    def __init__(self) -> None:
        pass

    def ligar(self):
        return "Carro ligado usando a chave"
    
    def desligar(self):
        return "Carro desligado usando a chave"
    
carro_amarelo = carro()
print(carro_amarelo.ligar())
print(carro_amarelo.desligar())
        