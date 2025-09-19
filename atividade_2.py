def analisar_situacao_aluno():
    print("--- Análise da Situação do Aluno ---")

    # 1. Coleta de dados de frequência
    while True:
        try:
            num_aulas_semestre = int(input("Digite o número total de aulas do semestre: "))
            if num_aulas_semestre <= 0:
                print("O número de aulas deve ser positivo. Tente novamente.")
            else:
                break
        except ValueError:
            print("Entrada inválida. Por favor, digite um número inteiro para as aulas.")

    while True:
        try:
            num_faltas_aluno = int(input("Digite o número de faltas do aluno: "))
            if num_faltas_aluno < 0 or num_faltas_aluno > num_aulas_semestre:
                print(
                    f"O número de faltas não pode ser negativo ou maior que o número total de aulas ({num_aulas_semestre}). Tente novamente.")
            else:
                break
        except ValueError:
            print("Entrada inválida. Por favor, digite um número inteiro para as faltas.")

    # Cálculo da frequência
    percentual_presenca = ((num_aulas_semestre - num_faltas_aluno) / num_aulas_semestre) * 100
    frequencia_aprovada = percentual_presenca >= 75

    # 2. Coleta das notas das provas
    while True:
        try:
            nota_p1 = float(input("Digite a nota da P1: "))
            if not (0 <= nota_p1 <= 10):
                print("A nota da P1 deve estar entre 0 e 10. Tente novamente.")
            else:
                break
        except ValueError:
            print("Entrada inválida. Por favor, digite um número para a nota da P1.")

    while True:
        try:
            nota_p2 = float(input("Digite a nota da P2: "))
            if not (0 <= nota_p2 <= 10):
                print("A nota da P2 deve estar entre 0 e 10. Tente novamente.")
            else:
                break
        except ValueError:
            print("Entrada inválida. Por favor, digite um número para a nota da P2.")

    # Cálculo da média inicial
    media_inicial = (nota_p1 + nota_p2) / 2

    nota_recuperacao = None
    situacao_final = ""

    # Avaliação da situação baseada nas notas e frequência
    if not frequencia_aprovada:
        situacao_final = "REPROVADO POR FREQUÊNCIA"
    elif media_inicial >= 7.0:
        situacao_final = "APROVADO POR MÉDIA"
    elif 5.0 <= media_inicial < 7.0:
        print(f"\nO aluno obteve média {media_inicial:.2f} e precisa fazer a prova de recuperação.")
        while True:
            try:
                nota_recuperacao = float(input("Digite a nota da Prova Complementar (Recuperação): "))
                if not (0 <= nota_recuperacao <= 10):
                    print("A nota da recuperação deve estar entre 0 e 10. Tente novamente.")
                else:
                    break
            except ValueError:
                print("Entrada inválida. Por favor, digite um número para a nota da recuperação.")

        media_final_recuperacao = (media_inicial + nota_recuperacao) / 2
        if media_final_recuperacao >= 5.0:
            situacao_final = "APROVADO NA RECUPERAÇÃO"
        else:
            situacao_final = "REPROVADO NA RECUPERAÇÃO"
    else:  # media_inicial < 5.0
        situacao_final = "REPROVADO POR MÉDIA"

    # Exibição dos resultados
    print("\n--- Resultados Finais ---")
    print(f"Número de aulas do semestre: {num_aulas_semestre}")
    print(f"Número de faltas do aluno: {num_faltas_aluno}")
    print(f"Percentual de presença do aluno: {percentual_presenca:.2f}%")
    print(f"\nPrimeira nota (P1): {nota_p1:.2f}")
    print(f"Segunda nota (P2): {nota_p2:.2f}")
    if nota_recuperacao is not None:
        print(f"Nota complementar (recuperação): {nota_recuperacao:.2f}")
    else:
        print("Nota complementar (recuperação): Não aplicável")
    print(f"Situação final do aluno: {situacao_final}")


# Executa a função principal
analisar_situacao_aluno()