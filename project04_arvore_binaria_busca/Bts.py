class No:
    def __init__(self, valor):
        self.valor = valor
        self.esq = None
        self.dir = None

 
class ArvoreBinariaBusca:
    def __init__(self):
        self.raiz = None
    
    #verificar se a arvore esta vazia
    def vazia(self):
        return self.raiz is None

    # Inserção de nó
    def inserir(self, valor):
        self.raiz = self._inserir(self.raiz, valor)
 
    def _inserir(self, no, valor):
        if no is None:
            return No(valor)
        if valor < no.valor:
            no.esq = self._inserir(no.esq, valor)
        elif valor > no.valor:
            no.dir = self._inserir(no.dir, valor)
        # valor repetido: ignorado
        return no
 
    # busca de nó
    def buscar(self, valor):
        return self._buscar(self.raiz, valor)
 
    def _buscar(self, no, valor):
        if no is None:
            return False
        if valor == no.valor:
            return True
        if valor < no.valor:
            return self._buscar(no.esq, valor)
        return self._buscar(no.dir, valor)
 
    # acha valor minimo da árvore (menor valor)
    def minimo(self):
        if self.raiz is None:
            return None
        atual = self.raiz
        while atual.esq is not None:
            atual = atual.esq
        return atual.valor
 
    # acha valor máximo da árvore (maior valor)
    def maximo(self):
        if self.raiz is None:
            return None
        atual = self.raiz
        while atual.dir is not None:
            atual = atual.dir
        return atual.valor

    def menor_sucessor(self, no):
        atual = no                  
        while atual.esq is not None:   
            atual = atual.esq            
        return atual   

    #Remover um valor
    def remover(self, no, valor):
        if no is None:
            return None
        if valor < no.valor:
            no.esq = self.remover(no.esq, valor)  
        elif valor > no.valor:
            no.dir = self.remover(no.dir, valor)
        else:
            if no.esq == None:
                return no.dir
            if no.dir == None:
                return no.esq  
            sucessor = self.menor_sucessor(no.dir)
            no.valor = sucessor.valor
            no.dir = self.remover(no.dir, sucessor.valor)
        return no
    
    # Percursos
    def pre_ordem(self):
        resultado = []
        self._pre_ordem(self.raiz, resultado)
        return resultado
    
    def _pre_ordem(self, no, resultado):
        if no is not None:
            resultado.append(no.valor)
            self._pre_ordem(no.esq, resultado)
            self._pre_ordem(no.dir, resultado)

    def em_ordem(self):
        resultado = []
        self._em_ordem(self.raiz, resultado)
        return resultado
    
    def _em_ordem(self, no, resultado):
        if no is not None:
            self._em_ordem(no.esq, resultado)
            resultado.append(no.valor)
            self._em_ordem(no.dir, resultado)
    
    def pos_ordem(self):
        resultado = []
        self._pos_ordem(self.raiz, resultado)
        return resultado
    
    def _pos_ordem(self, no, resultado):
        if no is not None:
            self._pos_ordem(no.esq, resultado)
            self._pos_ordem(no.dir, resultado)
            resultado.append(no.valor)

    def altura(self):
        return self._altura(self.raiz)
 
    def _altura(self, no):
        if no is None:
            return -1
        h_esq = self._altura(no.esq)
        h_dir = self._altura(no.dir)
        return 1 + max(h_esq, h_dir)

    def contar_nos(self, no):
        if no == None:
            return 0
        return 1 + self.contar_nos(no.esq) + self.contar_nos(no.dir)

    def contar_folhas(self, no):
        if no == None:
            return 0
        if no.esq == None and no.dir ==None:
            return 1
        return self.contar_folhas(no.esq) + self.contar_folhas(no.dir)
    
    def visualizar_arvore(self, raiz):
        if raiz is None:
            print("\n  (árvore vazia)\n")
            return

        linhas = []
    
        def _build(no, prefixo, is_esq, is_raiz):
            if no is None:
                return
            if is_raiz:
                conector    = ""
                novo_prefixo = ""
            elif is_esq:
                conector     = "├── "
                novo_prefixo = prefixo + "│   "
            else:
                conector     = "└── "
                novo_prefixo = prefixo + "    "
    
            linhas.append(f"{prefixo}{conector}[{no.valor}]")
    
            if no.esq or no.dir:
                if no.esq:
                    _build(no.esq, novo_prefixo, True, False)
                else:
                    linhas.append(f"{novo_prefixo}├── (vazio)")
                if no.dir:
                    _build(no.dir, novo_prefixo, False, False)
                else:
                    linhas.append(f"{novo_prefixo}└── (vazio)")
    
        _build(raiz, "", False, True)
        print()
        for linha in linhas:
            print("  " + linha)
        print()
