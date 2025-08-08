
class Banco_de_dados:
    def salvar_tarefas(self,tarefas):
        with open ("banco_de_dados.txt","w") as arquivos:
            for tarefa in tarefas:
               arquivos.write(tarefa)
        print("lista de tarefas salva com sucesso!")