from entrada import perguntar_sim_ou_nao

def remover_item(lista,nome):

    for item in lista:

        if item['produto'].lower() == nome.lower():

           confirmar=perguntar_sim_ou_nao(f"Deseja realmente remover {item['produto']}(sim/não)?")

           if confirmar == 'sim':

               lista.remove(item)

               print('Item removido com sucesso.')

               return item

           print('Remoção cancelada.')

           return None

    print(f'O {nome} não consta no sistema')

    return None

