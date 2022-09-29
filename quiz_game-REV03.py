from time import sleep

perguntas = {
    "Pergunta 1": {"pergunta": "Quem inventou a lâmpada?",
                   "respostas": {"A": "Albert Einsten",
                                 "B": "Thomas Edison",
                                 "C": "Graham Bell"},
                   "resposta_certa": "B"},
    "Pergunta 2": {"pergunta": "Quem pintou a Monaliza?",
                   "respostas": {"A": "Leonardo di Caprio",
                                 "B": "Michelangelo",
                                 "C": "Leonardo Da Vinci"},
                   "resposta_certa": "C"},
    "Pergunta 3": {"pergunta": "Quantos ossos temos em nosso corpo? ",
                   "respostas": {"A": "226",
                                 "B": "206",
                                 "C": "236"},
                   "resposta_certa": "B"},
    "Pergunta 4": {"pergunta": "Qual o planeta mais próximo do sol?",
                   "respostas": {"A": "Mercúrio",
                                 "B": "Marte",
                                 "C": "Saturno"},
                   "resposta_certa": "A"},
    "Pergunta 5": {"pergunta": "O que os pandas comem?",
                   "respostas": {"A": "Peixe",
                                 "B": "Bambu",
                                 "C": "Mel"},
                   "resposta_certa": "B"}
            }


def inicio_quiz():
    print("-=" * 20)
    print("Bem vindo ao meu Quiz!")
    print("-=" * 20)
    sleep(1.5)
    print("Carregando perguntas...")
    sleep(2)
    print("Vamos lá!!!")
    sleep(3)


def jogar(dados_perguntas):
    resp_certas = 0
    for pk, pv in dados_perguntas.items():
        print(f"{pk}: {pv['pergunta']}")
        sleep(1)
        # Acessando key: respostas e value: A B C com cada alternativa
        for rk, rv in pv['respostas'].items():
            print(f"{rk}: {rv}")
        escolha = pegar_resp()
        resp_certas += aprovando_resposta(escolha, pv['resposta_certa'])
        sleep(1)
    fim_de_jogo(resp_certas, perguntas)


def fim_de_jogo(acertos, tot_perguntas):
    print("\n")
    print("FIM de JOGO!")
    sleep(0.5)
    print(f"Você acertou {acertos} perguntas")
    porcentagem = (acertos / len(tot_perguntas)) * 100
    print(f"Sua taxa de acerto foi de {porcentagem}%")
    sleep(1)


def pegar_resp():
    while True:
        escolha = input("Sua resposta: ").strip().upper()
        if escolha in 'ABC':
            break
        else:
            print("Resposta invalida! Tente Novamente!")
    return escolha


def aprovando_resposta(resposta_usu, gabarito):
    if resposta_usu == gabarito:
        print('Resposta Certa!')
        return 1
    else:
        print('Resposta Errada!')
        return 0


def main():
    jogar_denovo = ''
    while jogar_denovo != 'N':
        inicio_quiz()
        jogar(perguntas)
        print('Deseja jogar novamente?')
        jogar_denovo = input('Digite "s" para sim e "n" para não: ').strip().upper()


if __name__ == "__main__":
    main()
