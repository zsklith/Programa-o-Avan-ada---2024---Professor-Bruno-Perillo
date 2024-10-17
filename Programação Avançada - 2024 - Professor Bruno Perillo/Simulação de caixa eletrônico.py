def inicializar_caixa():
    """Inicializa o caixa com a quantidade inicial de cédulas."""
    cedulas = {
        100: int(input("Digite a quantidade de cédulas de R$ 100: ")),
        50: int(input("Digite a quantidade de cédulas de R$ 50: ")),
        20: int(input("Digite a quantidade de cédulas de R$ 20: ")),
        10: int(input("Digite a quantidade de cédulas de R$ 10: ")),
        5: int(input("Digite a quantidade de cédulas de R$ 5: ")),
        2: int(input("Digite a quantidade de cédulas de R$ 2: ")),
        1: int(input("Digite a quantidade de cédulas de R$ 1: ")),
    }
    return cedulas

def realizar_saque(cedulas, valor_saque):
    """Realiza o saque do valor informado utilizando o menor número possível de cédulas."""
    cedulas_usadas = {}
    valor_restante = valor_saque
    
    for valor_cedula in sorted(cedulas.keys(), reverse=True):
        quantidade_cedulas = min(valor_restante // valor_cedula, cedulas[valor_cedula])
        if quantidade_cedulas > 0:
            cedulas_usadas[valor_cedula] = quantidade_cedulas
            valor_restante -= quantidade_cedulas * valor_cedula
    
    if valor_restante == 0:
        for valor_cedula, qtd in cedulas_usadas.items():
            cedulas[valor_cedula] -= qtd
        print("Saque realizado com sucesso:")
        for valor_cedula, qtd in cedulas_usadas.items():
            print(f"{qtd} cédula(s) de R$ {valor_cedula}")
        return True
    else:
        print("Não há cédulas suficientes para realizar o saque.")
        return False

def realizar_deposito(cedulas):
    """Realiza o depósito de cédulas no caixa."""
    for valor_cedula in sorted(cedulas.keys(), reverse=True):
        qtd_deposito = int(input(f"Digite a quantidade de cédulas de R$ {valor_cedula} para depósito: "))
        cedulas[valor_cedula] += qtd_deposito
    print("Depósito realizado com sucesso!")

def exibir_cedulas(cedulas):
    """Exibe a quantidade atual de cédulas no caixa."""
    print("Cédulas restantes no caixa:")
    for valor_cedula, qtd in sorted(cedulas.items(), reverse=True):
        print(f"R$ {valor_cedula}: {qtd}")

def main():
    cedulas = inicializar_caixa()
    
    while True:
        operacao = int(input("Digite o tipo de operação (0: saque, 1: depósito, -1: encerrar): "))
        
        if operacao == -1:
            print("Operação encerrada.")
            break
        elif operacao == 0:
            valor_saque = int(input("Digite o valor do saque: "))
            if realizar_saque(cedulas, valor_saque):
                exibir_cedulas(cedulas)
        elif operacao == 1:
            realizar_deposito(cedulas)
            exibir_cedulas(cedulas)
        else:
            print("Operação inválida, tente novamente.")

if __name__ == "__main__":
    main()
