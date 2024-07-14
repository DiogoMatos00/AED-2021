from controllers.controllers import *
from aed_ds.open_hash_table import OpenHashTable
from aed_ds.singly_linked_list import SinglyLinkedList



class menu():
    controller = Controller() 
    while True:
        comando = input("\n")
        comando = comando.split(" ")    #Divide a string numa lista de strings a partir do elemento inserido no split
        if comando[0] == "DD" and len(comando) == 2:
            print(controller.definir_data(int(comando[1])))    #---> Trocar uma variavel para tipo int/str/float/etc. chama-se fazer "cast"
           


        elif comando[0] == "RC":
            print(controller.registar_cliente(comando[1], ' '.join(comando[2:])))
            ### Falta verificar se existem clientes iguais(Resto das condições)
            ### Para isto acontecer a minha função registar_cliente precisa de ter acesso a openhashtable
                
        elif comando[0] == "RP":
            print(controller.registar_familia(' '.join(comando[1:])))

        elif comando [0] == "RS":
            print(controller.registar_serie(' '.join(comando[1:])))

        elif comando [0] == "RE":
            print(controller.registar_episodio(int(comando[1]), int(comando[2]), int(comando[3]), ' '.join(comando[4:])))

        elif comando [0] == "AP" and len(comando) == 3:
            print(controller.alterar_plano(int(comando[1]),comando[2]))

        elif comando [0] == "CP" and len(comando) == 2:
            print(controller.cancelar_plano(int(comando[1])))

        elif comando[0] == "AF" and len(comando) == 3:
           print(controller.associar_cliente_familia(int(comando[1]), int(comando[2])))

        elif comando[0] == "DF" and len(comando) == 2:
            print(controller.desassociar_cliente_familia(int(comando[1])))

        elif comando[0] == "EC" and len(comando) == 2:
            print(controller.eliminar_cliente(int(comando[1])))

        elif comando[0] == "ES" and len(comando) >= 2: #ES
            if len(comando) == 2:
                print(controller.eliminar_serie(int(comando[1]), 0, 0))
            if len(comando) == 3:
                print(controller.eliminar_serie(int(comando[1]), int(comando[2]), 0))
            if len(comando) == 4:
                print(controller.eliminar_serie(int(comando[1]), int(comando[2]), int(comando[3])))

        elif comando[0] == "LP" and len(comando) == 1:
            print(controller.listar_clientes())

        elif comando[0] == "LF" and len(comando) == 1:
            print(controller.listar_familias())
            
        elif comando[0] == "LS" and len(comando) == 1:
            print(controller.listar_series())
            
        elif comando[0] == "LSA" and len(comando) == 2:
            print#listar series alugadas
        elif comando[0] == "LSAF" and len(comando) == 2:
            print#listar series alugadas por familia
        elif comando[0] == "AS" and len(comando) >= 4:
            if len(comando) == 4:
                print(controller.alugar_serie(int(comando[1]), int(comando[2]), int(comando[3]), 0))
            if len(comando) == 5:
                print(controller.alugar_serie(int(comando[1]), int(comando[2]), int(comando[3]), int(comando[4])))
        
        elif comando[0] == "CA" and len(comando) == 2:
            if len(comando) == 4:
                print(controller.alugar_serie(int(comando[1]), int(comando[2]), int(comando[3]), 0))
            if len(comando) == 5:
                print(controller.alugar_serie(int(comando[1]), int(comando[2]), int(comando[3]), int(comando[4])))
        else:
            print("Instrução inválida")