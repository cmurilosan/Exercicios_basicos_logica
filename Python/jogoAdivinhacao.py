# Faça um jogo de adivinhação, onde o usuário tenta adivinhar um numero escolhido pela maquina
import random

total_tentativas = 3  # variavel inicializa com 3 e mantem caso seja no nivel facil porem aumenta para outros niveis
nivel = 0
taxa = 0
pontuacao = 1000  # jogador começa com 1000 pontos e vai diminuindo conforme perde tentativas
while nivel < 1 or nivel > 3:
    print("=" * 20)
    print("JOGO DE ADIVINHAÇÃO")
    print("=" * 20)
    nivel = int(input("[1] Facil\n"
                      "[2] Medio\n"
                      "[3] Dificil\n"
                      "Escolha o nivel: "))
    if nivel == 1:
        dif = 10
    elif nivel == 2:
        dif = 25
        total_tentativas = 8  # aqui damos ao jogador o mesmo indice de chance cerca de 30%
    elif nivel == 3:
        dif = 50
        total_tentativas = 15  # aqui damos ao jogador o mesmo indice de chance cerca de 30%
    else:
        print("Nivel inválido, tente novamente")
        continue

    while total_tentativas > 0:
        n = int(input("Insira um numero de 1 a {}: ".format(dif)))
        r = random.randint(1, dif)
        acertou = n == r
        maior = n > r
        menor = n < r
        if n < 1 or n > dif:
            print("O seu numero não está na faixa entre 1 e {}, tente novamente!\n".format(dif))
            continue
        if acertou:
            print("Parabens voce acertou, seu numero foi {}, e o da maquina foi {}\n".format(n, r))
            print("Sua pontuação é: ", pontuacao * 100)  # se jogador acerta seus pontos são aumentado em 100 pontos
            break
        else:
            if maior:
                print("Você ERROU, seu numero {} foi maior do que o da maquina {}\n".format(n, r))
            else:
                print("Você ERROU, seu numero {} foi menor do que o da maquina {}\n".format(n, r))
        total_tentativas -= 1
        taxa = abs((n - r) * 10)  # aqui pegamos o numero absoluto da diferença entre os numeros
        # e multiplicamos por 10 como taxa para a redução da pontuação
        pontuacao -= taxa
        print("Você possui {} pontos!".format(pontuacao))
        if pontuacao <= 0:
            print("Voce ainda possuia {} tentativas mas sua pontuação zerou.".format(total_tentativas))
            break   # programa para quando a pontuação fica menor ou igual a zero.
        if total_tentativas > 0:
            print("Voce ainda possui {} de {:.0f} tentativas".format(total_tentativas, dif * 0.3))
            # informa ao jogador quantas tentativas ainda possui
        else:
            print("Voce esgotou todas as suas tentativas")
print("GAME OVER")