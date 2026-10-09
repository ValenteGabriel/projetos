print('=== GERENCIADOR DE TAREFAS===')

tasks = []

while True:

    print('\n------ Escolha uma das opções: ')
    print('1. Adicionar tarefas')
    print('2. Listar tarefas ')
    print('3. Concluir tarefas')
    print('4. Sair')

    opcao = input('Informe a opção desejada: ')
        
    if opcao == '4':
        print('Operação concluída.')
        break

    elif opcao == '1':

        description = input('Tarefa: ')
        task = {
                    
            'description': description,
            'completed': False            
        }
        tasks.append(task)
        print('Tarefa cadastrada com sucesso.')

    elif opcao == '2':
        
        if not tasks:
            print('Nenhuma tarefa cadastrada.')
        else:
            for number, task in enumerate(tasks, start=1):
                if task['completed']:
                    print(f'{number}. {task['description']}: Concluída')
                else:
                    print(f'{number}. {task['description']}: Pendente')
        