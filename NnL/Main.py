import os
import time as tm

alfabeto = 'abcdefghijklmnopqrstuvwxyz'.upper()
alf_largura = len(alfabeto)
continuar = True
cenário = 'menu'
vidas = 5


def aviso(mensagem = 'mensagem não recebida', tempo = 1.5):
    res = input(mensagem + "\n")
    tm.sleep(tempo)
    os.system('cls')
    return res

def começar():
    os.system('cls')

    global alfabeto
    global alf_largura
    global continuar
    global cenário
    global vidas

    cenário = 'jogando'
    vidas = 5


    palavra = input("\n digite uma palavra(pode ser qualquer b#st#, quem vai jogar é você mesmo) (sem números, simbolos ou letras acentuadas --- ou tu se lascou ;) ) \n\n ?> ").upper()
    os.system('cls')
    print(palavra + "\n\n")

    largura = len(palavra)

    count = 0
    while count != largura and continuar and cenário == 'jogando':
        resposta = input("n: ")

        if resposta.isnumeric():
            resposta = int(resposta)
            if resposta < (alf_largura):

                if alfabeto[resposta] == palavra[count] and continuar:
                    count += 1
                    print(f"sucesso!: {str(resposta)}: {alfabeto[resposta]} \n")

                    if count == largura:
                        aviso(f"\n parabéns!!! você venceu \n palavra: {palavra} \n tamanho: {largura} \n terminou com {vidas} vidas \n\n confirmar?> ")
                        cenário = 'menu'

                else:
                    vidas -= 1
                    print(f"incorreto... vidas: {vidas} \n {str(resposta)}: {alfabeto[resposta]} \n")

                    if vidas == 0:
                        aviso("\n fim de jogo :skull:")
                        cenário = 'menu'

            else:
                pass
        else:
            pass
    pass



while continuar:
    if cenário == 'menu':
        os.system('cls')
        print(f"{'  ' * 5}Números não Letras - NNL - Numbers and Letters")
        resposta = input("\n começar [A] \n\n fechar [B] \n\n info [C] \n\n poucas escolhas né? XD [nenhum] \n\n ?> ")

        if resposta == 'start' or resposta == 'A':
            começar()

        elif resposta == 'fechar' or resposta == 'B':
            continuar = False

        elif resposta == 'poucas escolhas né? XD' or resposta == 'nenhum':
            aviso("sério?? ;-; \n")

        elif resposta == 'info' or resposta == 'C':
            print("""
eu fiz isso aqui cansado, não sou de dormir, então eu fiz algo mínimo, meio que um esboço, então não espere muita coisa, mas caso eu fique com vontade eu crio novas versões com as mecânicas que eu pensei (olha só, eu realmente pensei kk)

quando começar o jogo você vai ter que digitar uma sequência de letras "normais" do alfabeto felícia (a, b, c... etc. nada de números ou simbolos ou letras acentuadas), mas é melhor digitar uma palavra que existe
                  
depois de digitar, você vai ter que responder por cada caractere que tem na sua palavra, vai começar da primeira letra até a ultima e o padrão é:
                  
 A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
 0 1 2 3 4 5 6 7 8 9 10 - e assim por diante

por exemplo a palavra "gato"

a sequência é 6 - 0 - 19 - 14

e você vai ter que responder uma de cada vez, começando do G até o O


                  """)
            aviso("[digita qualquer coisa ai para voltar pro menu inicial rsrsr]")

        else:
            os.system('cls')