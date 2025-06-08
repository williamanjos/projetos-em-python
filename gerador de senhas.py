import random
import string


def gerar_senha(tamanmho=12):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    senha = '' .join(random.choice(caracteres) for _ in range (tamanho))
    return senha 
tamanho = int(input("digite o tamanho da senha: desejada  "))
print(f"senha gerada: {gerar_senha(tamanho)}")