def meu_decorador(fun):
    def wrapper():
        print("Antes da função ser chamada")
        fun()
        print("Depois da função ser chamada")
    return wrapper

@meu_decorador
def minha_funcao():
    print("Minha função foi chamada")

minha_funcao()