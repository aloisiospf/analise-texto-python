palavras_positivas = {
    "bom", "ótimo", "excelente", "feliz", "maravilhoso", "gostei", "incrível"
}

palavras_negativas = {
    "ruim", "péssimo", "triste", "horrível", "odiei", "problema", "terrível"
}


def classificar_texto(texto):
    palavras = texto.lower().split()

    pontuacao_positiva = sum(1 for palavra in palavras if palavra in palavras_positivas)
    pontuacao_negativa = sum(1 for palavra in palavras if palavra in palavras_negativas)

    if pontuacao_positiva > pontuacao_negativa:
        return "positivo"
    elif pontuacao_negativa > pontuacao_positiva:
        return "negativo"
    else:
        return "neutro"


def main():
    texto = input("Digite um texto: ")
    resultado = classificar_texto(texto)
    print("Classificação:", resultado)


if __name__ == "__main__":
    main()
