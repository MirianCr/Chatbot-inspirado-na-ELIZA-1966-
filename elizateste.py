import random
import re

# Regras simples (padrão -> respostas)
regras = [
    (r"eu estou (.*)", [
        "Por que você está {0}?",
        "Há quanto tempo você está {0}?",
        "Como você se sente ao estar {0}?"
    ]),
    (r"eu sinto (.*)", [
        "Por que você sente {0}?",
        "Você costuma sentir {0} com frequência?",
        "O que faz você sentir {0}?"
    ]),
    (r"porque (.*)", [
        "Isso realmente explica tudo?",
        "Que outras razões podem existir?",
        "Você acha que essa é a única causa?"
    ]),
    (r"(.*) mae(.*)", [
        "Fale mais sobre sua mãe.",
        "Como é sua relação com sua mãe?",
        "Sua mãe influencia muito você?"
    ]),
    (r"(.*) pai(.*)", [
        "Fale mais sobre seu pai.",
        "Como é sua relação com seu pai?"
    ]),
    (r"(.*) trabalho(.*)", [
        "Fale mais sobre seu trabalho, como está indo.",
        "Como é sua relação com isso?"
    ]),
    (r"(.*)", [
        "Interessante... continue.",
        "Entendo. E o que mais?",
        "Pode me explicar melhor?"
    ])
]

def responder(frase):
    frase = frase.lower()
    for padrao, respostas in regras:
        match = re.match(padrao, frase)
        if match:
            resposta = random.choice(respostas)
            if "{0}" in resposta:
                return resposta.format(match.group(1), nome)
            return resposta.format("",nome)

nome = input("ELIZA 🤖: Olá! Qual é o seu nome?\nVocê: ")

print(f"ELIZA 🤖: Prazer em te conhecer, {nome}! Como você está se sentindo hoje?")

while True:
    entrada = input("Você: ")
    if entrada.lower() in ["sair", "tchau", "exit"]:
        print("ELIZA 🤖: Foi bom conversar com você. Até mais!")
        break
    print("ELIZA 🤖:", responder(entrada))