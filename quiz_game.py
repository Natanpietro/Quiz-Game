from time import sleep
print("-=" * 20)
print("Bem vindo ao meu Quiz!")
print("-=" * 20)
sleep(1.5)
playing = str(input("Você gostaria de jogar? [Sim/ Não] ")).upper().strip()
if playing != 'SIM':
    quit()
print("Carregando perguntas...")
sleep(2)
print("Vamos lá!!!")
sleep(3)

corretas = incorretas = 0
perguntas = 5
while True:
    pergunta_1 = input("Quem inventou a lâmpada?\nA) Albert Einsten\nB) Thomas Edison\n"
                       "C) Graham Bell\n"
                       "Resposta: ").strip().upper()
    # criar função para validação de da resposta
    if pergunta_1 in 'AaCc':
        incorretas += 1
        print("Resposta Incorreta! Vamos para próxima pergunta...")
        break
    elif pergunta_1 in 'Bb':
        corretas += 1
        print("Resposta Correta! Vamos para próxima pergunta")
        break
    elif pergunta_1 not in 'AaBbCc':
        print("Resposta Invalida! Tente Novamente")
        continue

sleep(2)
while True:
    pergunta_2 = input("Quem pintou a Monaliza?\nA) Leonardo Di Caprio\nB) Michelangelo\n"
                       "C) Leonardo Da Vinci\n"
                       "Resposta: ").strip().upper()
    # criar função para validação de da resposta
    if pergunta_2 in 'AaBb':
        incorretas += 1
        print("Resposta Incorreta! Vamos para próxima pergunta...")
        break
    elif pergunta_2 in 'Cc':
        corretas += 1
        print("Resposta Correta! Vamos para próxima pergunta")
        break
    elif pergunta_2 not in 'AaBbCc':
        print("Resposta Invalida! Tente Novamente")
        continue

sleep(2)
while True:
    pergunta_3 = input("Quantos ossos temos em nosso corpo?\nA) 226\nB) 206\n"
                       "C) 236\n"
                       "Resposta: ").strip().upper()
    # criar função para validação de da resposta
    if pergunta_3 in 'AaCc':
        incorretas += 1
        print("Resposta Incorreta! Vamos para próxima pergunta...")
        break
    elif pergunta_3 in 'Bb':
        corretas += 1
        print("Resposta Correta! Vamos para próxima pergunta")
        break
    elif pergunta_3 not in 'AaBbCc':
        print("Resposta Invalida! Tente Novamente")
        continue

sleep(2)
while True:
    pergunta_4 = input("Qual o planeta mais próximo do sol?\nA) Mercúrio\nB) Marte\n"
                       "C) Saturno\n"
                       "Resposta: ").strip().upper()
    # criar função para validação de da resposta
    if pergunta_4 in 'BbCc':
        incorretas += 1
        print("Resposta Incorreta! Vamos para próxima pergunta...")
        break
    elif pergunta_4 in 'Aa':
        corretas += 1
        print("Resposta Correta! Vamos para próxima pergunta")
        break
    elif pergunta_4 not in 'AaBbCc':
        print("Resposta Invalida! Tente Novamente")
        continue

sleep(2)
while True:
    pergunta_5 = input("O que os pandas comem?\nA) Peixe\nB) Bambu\n"
                       "C) Mel\n"
                       "Resposta: ").strip().upper()
    # criar função para validação de da resposta
    if pergunta_5 in 'AaCc':
        incorretas += 1
        print("Resposta Incorreta! Vamos para próxima pergunta...")
        break
    elif pergunta_5 in 'Bb':
        corretas += 1
        print("Resposta Correta! Vamos para próxima pergunta")
        break
    elif pergunta_5 not in 'AaBbCc':
        print("Resposta Invalida! Tente Novamente")
        continue
print("-=" * 20)
print("Quiz encerrado!")
sleep(1.5)
porcentagem = (corretas / perguntas) * 100
print(f"Sua porcentagem de acerto foi de {porcentagem}%")
print("-=" * 20)
