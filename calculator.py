def calculator():

    while True:

        operador = int(input('Digite um operador: \n1.Soma\n2.Subtração\n3.Multiplicação\n4.Divisão\n0.Sair\n'))
        
        if operador == 1 or operador == 2 or operador == 3 or operador == 4:
            num_1 = int(input('Digite um número: \n'))
            num_2 = int(input('Digite outro número: \n'))
        elif operador == 0:
            break
        else:
            print('Essa opção não existe.')
            continue

        if operador == 1:
            print(f'{num_1} + {num_2} é igual a :', num_1 + num_2)
            sair = int(input('Deseja sair? 0 para sim 1 para não.'))
        elif operador == 2:
            print(f'{num_1} - {num_2} é igual a :', num_1 - num_2)
            sair = int(input('Deseja sair? 0 para sim 1 para não.'))
        elif operador == 3:
            print(f'{num_1} * {num_2} é igual a :', num_1 * num_2)
            sair = int(input('Deseja sair? 0 para sim 1 para não.'))
        elif operador == 4:
            print(f'{num_1} / {num_2} é igual a :', num_1 / num_2)
            sair = int(input('Deseja sair? 0 para sim 1 para não.'))
        else:
            print(f'Operador {operador} inválido, digite outro operador (1, 2, 3 ou 4 )')

        if sair == 0:
            break
        elif sair == 1:
            continue    

        question_continue = int(input('Digite 0 para sair ou 1 para continuar: \n'))
        if question_continue != 0 or question_continue != 1:
            print('Digite uma opção válida: 0 para parar e 1 para continuar.')
        elif question_continue == 1:
            continue
        else:
            break

calculator()