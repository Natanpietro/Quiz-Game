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
# Acessando key: Pergunta (Nº) e values:
acertos = erros = 0
for pk, pv in perguntas.items():
    print(f"{pk}: {pv['pergunta']}")
    # Acessando key: respostas e value: A B C com cada alternativa
    for rk, rv in pv['respostas'].items():
        print(f"{rk}: {rv}")

    resposta_usuário = input("Sua resposta: ").strip().upper()
    if resposta_usuário == pv['resposta_certa']:
        acertos += 1
        print("Resposta CORRETA!")
    else:
        erros += 1
        print("Resposta INCORRETA!")
    sleep(1.5)
    if acertos + erros < len(perguntas):
        print("Próxima pergunta...")
    sleep(1.5)

print(f"Você acertou {acertos} e errou {erros}")
porcentagem = (acertos / len(perguntas)) * 100
print(f"Sua taxa de acerto foi de {porcentagem}")
