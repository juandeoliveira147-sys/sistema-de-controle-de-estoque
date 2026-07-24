'''
este projeto representa um fluxo de controle de estoque para estudos e evolução dos meus conhecimentos em Python

'''
import sys
import time

estoque = {}

def cadastrar_produto():
    while True:
        nome = input("\nDigite o nome do produto: ").strip().capitalize()
        if len(nome) <2:
            print("\nDigite um nome valido!")
            continue
        if nome in estoque:
            escolha = input("\nVocê já cadastrou este produto, desejá dar entrada de mais estoque s/n? :").strip().lower()
            if escolha in ("s","sim"):
                return entrada_estoque(nome)
            elif escolha in ("n","não","nao"):
                continue
            else:
                print("\nDigite uma opção valida!")
                continue
        categoria = input("\nDigite a categoria do produto: ").strip().capitalize()
        if len(categoria) <2:
            print("\nDigite uma categoria valida!")
            continue
        try:
            preco = float(input("\n Digite o preço do produto: "))
        except ValueError:
            print("\nPor favor!Digite um numero valido!")
            continue
        if preco < 0:
            print("\nSelecione um preço valido!")
            continue
        try:
            quantidade = int(input("\nDigite a quantidade que tem no estoque: "))
        except ValueError:
            print("\nDIgite um numero valido para quantia do estoque: ")
            continue
        if quantidade <0:
            print("\nDIgite um numero valido para quantia do estoque: ")
            continue
        novo_produto = {

            "nome": nome,
            "categoria": categoria,
            "preço": preco,
            "quantidade": quantidade,

        }
        estoque[nome] = novo_produto
        print("\nNovo produto cadastrado com sucesso!")
        time.sleep(3)
        return menu()

        

def listar_produtos():
    print("\n===Produtos===")
    if not estoque:
        print("\nSeu estoque de produtos está vazio!")
        print("==============")
        time.sleep(3)
        return menu()
    for produtos in estoque:
        print(f"\n{estoque[produtos]["nome"]}: {estoque[produtos]["quantidade"]} no estoque")
    print("==============")
    time.sleep(5)
    return menu()

def procurar_produto():
    if not estoque:
        print("\nSeu estoque está vazio")
        time.sleep(2)
        return menu()
    while True:
        produto = input("\nDigite o produto que você gostaria de procurar: ").strip().capitalize()
        if produto in estoque:
            print("\nAchei o seu produto! aqui está")
            escolha = input("\nGostaria de visualizar as informações do seu produto? s/n: ").strip().lower()
            if escolha in ("s","sim"):
                return ver_produtos(produto)
        else:
            print("\nNão encontrei o seu produto")
            while True:
                print("1 - voltar para o menu")
                sair = input("2 - continuar: ").strip().lower()
                if sair in ("1","voltar"):
                    print("\nVoltando para o menu....")
                    time.sleep(3)
                    return menu()
                elif sair in ("2","continuar"):
                    print("\nVamos continuar")
                    break
                else:
                    print("\nOpção invalida!, tente novamente")
                    continue
                

def ver_produtos(produto):
    print(f"produto : {estoque[produto]["nome"]}")
    print(f"categoria : {estoque[produto]["categoria"]}")
    print(f"preço : {estoque[produto]["preço"]}")
    print(f"quantidade restante : {estoque[produto]["quantidade"]}\n")
    escolha = input("Gostaria de atualizar alguma informação? s/n: ").strip().lower()
    if escolha in ("não","n","nao"):
        return menu()
    elif escolha in ("s","sim"):
        return editar_produto(produto)
    
    
        
def editar_produto(produto = None):
    while True:
        if not estoque:
            print("\nO seu estoque está vazio!!")
            time.sleep(3)
            return menu()
        if produto is None:
            produto = input("Digite o nome do produto que deseja editar: ").strip().capitalize()
            if produto in estoque:
                print("\nAcabei de achar o seu produto!")
                break
            
            else:
                print("\nEste produto não está no estoque, tente novamente!")
                continue
        else:
            break
    while True:
        print(f"produto : {estoque[produto]["nome"]}")
        print(f"categoria : {estoque[produto]["categoria"]}")
        print(f"preço : {estoque[produto]["preço"]}")
        print(f"quantidade restante : {estoque[produto]["quantidade"]}\n")
        escolha = input("\nQual informação você deseja alterar?").strip().lower()
        if escolha in ("nome","produto"):
            novo_nome = input("\nQual será o novo nome do produto?: ").strip().capitalize()
            if len(novo_nome) <2:
                print("\nDigite um nome valido!")
                continue
            elif novo_nome in estoque:
                print("\nJá tem um produto com esse nome no estoque")
                adicionar = input(f"\nDeseja adicionar mais {novo_nome} ao estoque? s/n: ").strip().lower()
                if adicionar in ("s","sim"):
                    return entrada_estoque(novo_nome)
                elif adicionar in ("n","nao","não"):
                    continue

            else:
                dados = estoque.pop(produto)
                dados["nome"] = novo_nome
                estoque[novo_nome] = dados
                produto = novo_nome
                print(f"\nO nome do produto foi atualizado para {novo_nome}")
                time.sleep(5)
                return menu()
        elif escolha in ("categoria"):
            nova_categoria = input("\nQual será o novo nome da categoria?: ").strip().capitalize()
            if len(nova_categoria) <2:
                print("\nDigite um nome valido para a categoria!")
                continue
            else:
                estoque[produto]["categoria"] = nova_categoria
                print(f"\nA categoria foi atualizada para {nova_categoria}")
                time.sleep(5)
                return menu()
        elif escolha in ("preço","preco"):
            try:
                novo_preco = float(input("\nQual será o novo preço?: "))
                if novo_preco <0:
                    print("\nDigite um numero valido para o novo preço!")
                    continue
            except ValueError:
                print("\nDigite um valor valido!")
                continue
            estoque[produto]["preço"] = novo_preco
            print(f"\nSeu preço foi atualizado para {novo_preco}")
            time.sleep(5)
            return menu()
        elif escolha in ("estoque","quantidade"):
            while True:
                escolha_do_estoque = input("\nDeseja voltar, retirar do estoque, adicionar ao estoque ou remover um produto do estoque: ").strip().lower()
                if escolha_do_estoque in ("adicionar","colocar"):
                    return entrada_estoque(produto)
                elif escolha_do_estoque in ("retirar","tirar"):
                    return saida_estoque(produto)
                elif escolha_do_estoque in ("voltar"):
                    break
                elif escolha_do_estoque in ("remover"):
                    return remover_produto(produto)
                else:
                    print("\nDigite uma opção valida!")
                    continue
        
        


                
                



def remover_produto(produto = None):
    while True:
        if not estoque:
            print("\nEstoque vazio!")
            time.sleep(3)
            return menu()
        if produto is None:
            produto = input("\nQual produto você gostaria de remover? : ").strip().capitalize()
            if produto not in estoque:
                print("\nEste produto não está no estoque")
                produto = None
                print("\n1 - sair")
                decisao = input("2 - tentar novamente: ").strip().lower()
                if decisao in ("1","sair"):
                    print("\nVoltando para o menu!")
                    time.sleep(3)
                    return menu()
                elif decisao in ("2","tentar novamente"):
                    print("\nVamos tentar denovo!")
                    return remover_produto()
                else:
                    print("\nOpção invalida")
                    continue
            else:
                break
        else:
            break
    while True:
        escolha = input("\nDeseja mesmo remover o produto? s/n :").strip().lower()
        if escolha in ("s","sim"):
            del estoque[produto]
            print("\nRemovendo produto...")
            time.sleep(5)
            print("\nProduto removido")
            time.sleep(3)
            return menu()
        elif escolha in ("n","nao","não"):
            print("\n1 - escolher outro item para remover")
            escolha2 = input("2 - voltar para o menu:  ")
            if escolha2 in ("1"):
                return remover_produto()
            elif escolha2 in ("2","menu"):
                print("\nVoltando para o menu")
                time.sleep(3)
                return menu()

    

def entrada_estoque(produto = None):
    while True:
        if produto is None:
            produto = input("\nDigite o nome do produto: ").strip().capitalize()
            if produto in estoque:
                break
            else:
                print("\nNão encotrei o seu produto!")
                time.sleep(3)
                return menu()
    if produto in estoque:
        while True:
            try:
                entrando_no_estoque = int(input(f"\nQuanto gostaria de adicionar ao estoque do produto?({produto})"))
                if entrando_no_estoque <= 0:
                    print("Digite um número maior que zero.")
                    continue
                else:
                    estoque[produto]["quantidade"] += entrando_no_estoque
                    break
            except ValueError:
                print("\nPor favor, digite um numero valido!")


        print("\nNovo estoque atualizado com sucesso!")
        escolha = input("\nDeseja visualizar as informações atualizadas? s/n: ").strip().lower()
        if escolha in ("s","sim"):
            print(f"produto : {estoque[produto]["nome"]}")
            print(f"categoria : {estoque[produto]["categoria"]}")
            print(f"preço : {estoque[produto]["preço"]}")
            print(f"quantidade restante : {estoque[produto]["quantidade"]}\n")
            print("\nVoltando para o menu em 5 segundos...")
            time.sleep(5)
            return menu()

        elif escolha in ("n","não","nao"):
            return menu()


def saida_estoque(produto = None):
    while True:
        if not estoque:
            print("\nEstoque vazio!")
            time.sleep(3)
            return menu()
        if produto is None:
            produto = input("\nDigite o nome do produto: ").strip().capitalize()
            if produto in estoque:
                break
            
            else:
                print("\nNão encotrei o seu produto!")
                print("\n1 - Sair")
                tentar_novamente = input("2 - Tentar novamente: ").strip().lower()
                if tentar_novamente in ("1","sair"):
                    print("\nVoltando para o menu...")
                    time.sleep(2)
                    return menu()
                elif tentar_novamente in ("2","tentar novamente"):
                    print("\nVamos tentar novamente!")
                    return saida_estoque()
                else:
                    print("\nDigite uma opção valida!")
                    continue
        else:   
            break
    if produto in estoque:
        while True:
            try:
                saindo_do_estoque = int(input(f"\nQuanto gostaria de retirar do estoque do produto?({produto})"))
                if saindo_do_estoque > estoque[produto]["quantidade"]:
                    print("\nNão há quantidade suficiente em estoque!")
                    continue
                else:
                    estoque[produto]["quantidade"] -= saindo_do_estoque
                    break
            except ValueError:
                print("\nPor favor, digite um numero valido!")
        print("\nNovo estoque atualizado com sucesso!")
        escolha = input("\nDeseja visualizar as informações atualizadas? s/n: ").strip().lower()
        if escolha in ("s","sim"):
            print(f"produto : {estoque[produto]["nome"]}")
            print(f"categoria : {estoque[produto]["categoria"]}")
            print(f"preço : {estoque[produto]["preço"]}")
            print(f"quantidade restante : {estoque[produto]["quantidade"]}\n")
            print("\nVoltando para o menu em 5 segundos...")
            time.sleep(5)
            return menu()
    
        elif escolha in ("n","não","nao"):
            return menu()
    else:
        print("Seu produto não está no estoque")
        time.sleep(5)
        return menu()

def menu():
    while True:
        print("\n===Controle de estoque===")
        print("\n1 - Cadastrar produto")
        print("\n2 - Visualizar todos os produtos")
        print("\n3 - Procurar produto")
        print("\n4 - Editar produto")
        print("\n5 - Entrada de estoque")
        print("\n6 - Saída de estoque")
        print("\n7 - Remover produto")
        escolha = input("\n8 - Encerrar programa: ").strip().capitalize()
        if escolha in ("1","Cadastrar","Cadastrar produto"):
            cadastrar_produto()
        elif escolha in ("2","Visualizar todos os produtos"):
            listar_produtos()
        elif escolha in ("3","Procurar produto"):
            procurar_produto()
        elif escolha in ("4",'Editar produto'):
            editar_produto()
        elif escolha in ("5","Entrada de estoque"):
            entrada_estoque()
        elif escolha in ("6","Saída de estoque"):
            saida_estoque()
        elif escolha in ("7","Remover produto"):
            remover_produto()
        elif escolha in ("8","Encerrar Programa"):
            sys.exit()





if __name__ == "__main__":
    menu()