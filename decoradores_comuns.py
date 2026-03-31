#@classmethod
#@staticmethod

class MinhaClasse:
    valor = 10 

    def __init__(self, nome) -> None:
        self.nome = nome

    def metodo_instancia(self):
       return f"Método de instancia chamado para {self.nome}"
    
    @classmethod
    def metodo_class(cls):
        return f"Método de classe chamado para valor={cls.valor}"
    
    @staticmethod
    def metodo_estatico():
        return "Método estático chamado"
    
obj = MinhaClasse(nome="Classe Exemplo")
print(obj.metodo_instancia())
print(MinhaClasse.valor)
print(MinhaClasse.metodo_class())


        