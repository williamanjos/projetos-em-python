import random

def escolher palavra():
    palavras = ["python", "programação", "computador", "i.a", "dados"  ]
    return = random.choice(palavras)

def jogo_da_forca():
    palavra = escolher_palavra()
    letras_corretas = set(palavra)
    letras_digitadas = set()
    tentativas = 6

    print("bem vindo ao jogo da forca!")

    while tentativas > 0:
        palavra_oculta = ''.join([letra if letra in letras_digitadas else '_' for letra in palavra])
        print (f"palavra: {palavra_oculta}")
        print (f"tentativas restantes: {tentativas}")

        letra = imput("digite uma letra: ").lower()
        if letra in letras_digitadas:
            print ("você já digitou essa letra.")
        elif letra in letras_corretas:
            print ("boa!!! você acertou uma letra! continue assim!!.")
        else:
            letras_digitadas.add(letra)
            tentativas -= 1 
            print ("ops! letra errada. tente novamente.")
        if letras_corretas.issubet(letras_digitadas):
            print (f"parabens!!! Você acertou uma palavra completa: {palavra}")
            break
        else:
            print ("ffim de jogo!!! a palavra era: {palavra}")	

jogo_da_forca()        
