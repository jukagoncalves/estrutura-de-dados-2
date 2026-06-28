from Bts import ArvoreBinariaBusca

arvore = ArvoreBinariaBusca()


def exibir_menu():
    print("""
╔══════════════════════════════════════╗
║     ÁRVORE BINÁRIA DE BUSCA (BST)    ║
╠══════════════════════════════════════╣
║  1. Inserir valor                    ║
║  2. Buscar valor                     ║
║  3. Remover valor                    ║
║  4. Menor valor                      ║
║  5. Maior valor                      ║
║  6. Percurso pré-ordem               ║
║  7. Percurso em-ordem                ║
║  8. Percurso pós-ordem               ║
║  9. Contar nós                       ║
║ 10. Contar folhas                    ║
║ 11. Altura da árvore                 ║
║ 12. Verificar se está vazia          ║
║ 13. Visualizar árvore                ║
║  0. Sair                             ║
╚══════════════════════════════════════╝""")


def ler_inteiro(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Digite um número inteiro válido")


def main():

    while True:
        exibir_menu()
        opcao = ler_inteiro("  Escolha uma opção: ")

        if opcao == 0:
            print("\n  Encerrando. Até logo!\n")
            break

        elif opcao == 1:
            entrada = input("  Valores para inserir (separados por espaço): ")
            valores = [int(v) for v in entrada.split() if v.lstrip('-').isdigit()]
            for v in valores:
                arvore.inserir(v)
            print(f"   Inserido(s): {valores}")
            print("  Árvore atual:")
            arvore.visualizar_arvore(arvore.raiz)

        elif opcao == 2:
            v = ler_inteiro("  Valor a buscar: ")
            if arvore.buscar(v):
                print(f"   {v} encontrado na árvore.")
            else:
                print(f"   {v} não encontrado na árvore.")

        elif opcao == 3:
            v = ler_inteiro("  Valor a remover: ")
            if arvore.buscar(v):
                arvore.remover(arvore.raiz, v)
                print(f"   {v} removido.")
                print("  Árvore atual:")
                arvore.visualizar_arvore(arvore.raiz)
            else:
                print(f"   Valor {v} não existe na árvore.")

        elif opcao == 4:
            m = arvore.minimo()
            if m is None:
                print("   Árvore vazia.")
            else:
                print(f"   Menor valor: {m}")

        elif opcao == 5:
            m = arvore.maximo()
            if m is None:
                print("   Árvore vazia.")
            else:
                print(f"   Maior valor: {m}")

        elif opcao == 6:
            print(f"   Pré-ordem:  {arvore.pre_ordem()}")

        elif opcao == 7:
            print(f"  Em-ordem:   {arvore.em_ordem()}")

        elif opcao == 8:
            print(f"  Pós-ordem:  {arvore.pos_ordem()}")

        elif opcao == 9:
            print(f"  Quantidade de nós: {arvore.contar_nos(arvore.raiz)}")

        elif opcao == 10:
            print(f"  Quantidade de folhas: {arvore.contar_folhas(arvore.raiz)}")

        elif opcao == 11:
            print(f"  Altura da árvore: {arvore.altura()}")

        elif opcao == 12:
            if arvore.vazia():
                print("  A árvore está vazia.")
            else:
                print("  A árvore não está vazia.")

        elif opcao == 13:
            print("   Estrutura da árvore:")
            arvore.visualizar_arvore(arvore.raiz)

        else:
            print("Opção inválida. Tente novamente.")

        input("  [Enter para continuar]")


if __name__ == "__main__":
    main()
