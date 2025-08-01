
tarefas = []
confere= []

while True:
    print("""

    -------------------------------------------------------------------------------  
    | _      _     _              _               __                               |
    || |    (_)   | |            | |             / _|                              |
    || |     _ ___| |_ __ _    __| | ___    __ _| |_ __ _ _______ _ __ ___  ___    |
    || |    | / __| __/ _` |  / _` |/ _ \  / _` |  _/ _` |_  / _ \ '__/ _ \/ __|   |
    || |____| \__ \ || (_| | | (_| |  __/ | (_| | || (_| |/ /  __/ | |  __/\__ \   |
    ||______|_|___/\__\__,_|  \__,_|\___|  \__,_|_| \__,_/___\___|_|  \___||___/   |
    -------------------------------------------------------------------------------                                                                         
                                                                                """)
    print("""
    -------------------------------------
    |                                   |
    | 1 : Inserir terefa.               |
    | 2 : Listar tarefa.                |
    | 3 : marcar como concluido.        |
    | 4 : Remover tarefa.               |
    | 0 : sair.                         |
    -------------------------------------
        
        """)

    numero_da_lista= int(input("olá bom dia, insira um número para iniciar sua lista de afazeres."))

    if  numero_da_lista == 1:
        print ("você escolheu o numero 1.")
        a_fazer=(input("insira que  afazeres você tem."))
        tarefas.append(a_fazer)
        
    
    elif numero_da_lista == 2:
        print ("você escolheu o numero 2 , com isso vamos listar oque você tem para fazer.")
        print ("listando....")
        
        for itens in tarefas:
            print(f"{itens}")
        for itens_2 in confere:
            print(f"{itens_2}")

    elif numero_da_lista == 3:
        print ("você escolheu o numero 3.")
        oque_deseja= input("quais tarefas vc concluio")
        confere.append(f"(x){a_fazer}")
        tarefas.remove(a_fazer)





    elif numero_da_lista == 4:
        print("você escolheu o numero 4.")
        pergunta=input("oque vc deseja retirar da lista.....")
        tarefas.remove(pergunta)

    elif numero_da_lista == 0:
        print("você escolheu o numero 0 saindo....")
        break

