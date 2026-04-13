import re  # necessário para tokenizar palavras
import matplotlib.pyplot as plt
import os

def le_arquivo(nome_arquvio):
    with open(nome_arquvio, 'r', encoding='utf-8', errors='ignore') as arquivo:
        conteudo = arquivo.read()
    conteudo = conteudo.lower()  # Converte letras para minúsculo
    return conteudo

def hash_soma(palavra):  # H1: soma dos caracteres
    h = 0
    for c in palavra:  #  itera sobre palavra
        h += ord(c)
    return h

def hash_ponderada(palavra):  # H2: soma ponderada pela posição
    h = 0
    for i in range(len(palavra)):
        h += (i + 1) * ord(palavra[i])
    return h

def hash_polinomial(palavra):  # H3: polinomial (Horner) com R=31
    h = 0
    r = 31
    for c in palavra:
        h = h * r + ord(c)
    return h

def hash_xor(palavra):  # H4: mistura com XOR/shift
    h = 0
    for c in palavra:
        h ^= ord(c)
        h = ((h << 5) | (h >> 27)) & 0xFFFFFFFF  # limita a 32 bits para não crescer infinito
    return h

# funcoes de hash "ruins" propositais
def hash_prefixo(palavra):
    h = 0
    for c in palavra[:3]:
        h += ord(c)
    return h

def hash_sufixo(palavra):
    h = 0
    for c in palavra[-3:]:
        h += ord(c)
    return h

# busca na hash - equivale ao contains(word)
def busca_hash(palavra, tabela, tamanho_M, hash_atual):
    h = hash_atual(palavra)
    idx = h % tamanho_M
    bucket = tabela[idx]
    comparacoes = 0
    for w in bucket:
        comparacoes += 1
        if w == palavra:
            return w, comparacoes  # encontrou
    return None, comparacoes  # não encontrou

def put_hash(palavra, tabela, tamanho_M, hash_atual):
    resultado, comp = busca_hash(palavra, tabela, tamanho_M, hash_atual)
    if resultado is None:
        h = hash_atual(palavra)
        categoria = h % tamanho_M
        tabela[categoria].append(palavra)

def busca_sequencial(palavra, lista_unica):
    comparacoes = 0
    for w in lista_unica:
        comparacoes += 1
        if palavra == w:
            return w, comparacoes
    return None, comparacoes

def put_linear(palavra, lista):
    resultado, comp = busca_sequencial(palavra, lista)
    if resultado is None:
        lista.append(palavra)

def imprime_histograma(tabela, tamanho_M, hash_atual, arquivo):
    tamanhos = [len(tabela[i]) for i in range(tamanho_M)]

    plt.figure(figsize=(12, 4))
    plt.bar(range(tamanho_M), tamanhos, color='steelblue', width=1.0)
    plt.title(f"Histograma | texto={arquivo} | M={tamanho_M} | hash={hash_atual.__name__}")
    plt.xlabel("Bucket")
    plt.ylabel("Quantidade de palavras")
    plt.tight_layout()

    os.makedirs('histogramas', exist_ok=True)
    caminho = f"histogramas/{arquivo}_M{tamanho_M}_{hash_atual.__name__}.png"
    plt.savefig(caminho)
    plt.close()
    print(f"  Histograma salvo em: {caminho}")

if __name__ == "__main__":
    arquivos = ["quincas_borba.txt" , "tale.txt"]
    tamanhos = [97, 100, 997]        # tamanhos da tabela hash
    funcoes = [hash_soma, hash_ponderada, hash_polinomial, hash_xor, hash_prefixo, hash_sufixo]

    with open("resultados.csv", "w") as f:
        f.write("texto,M,hash_name,n,alpha,max_bucket,avg_bucket,total_comp_success,avg_comp_success,total_comp_fail,avg_comp_fail\n")

        for arquivo in arquivos:
            conteudo = le_arquivo(arquivo) #le o arquivo a cada iteraçao
            for hash_atual in funcoes:
                for tamanho_M in tamanhos:
                    lista_unica = []

                    # inicializando a tabela
                    tabela = [[] for _ in range(tamanho_M)]

                    # tokeniza o texto em palavras (antes iterava caractere por caractere)
                    palavras = re.findall(r"[a-záàâãéêíóôõúùüçñ]+", conteudo)

                    # percorrer as palavras do texto e armazenar na categoria correta
                    for palavra in palavras:  # agora itera sobre palavras, não sobre conteudo
                        # só insere se a palavra ainda não existe (palavras distintas)
                        put_hash(palavra, tabela, tamanho_M, hash_atual)
                        put_linear(palavra,lista_unica)


                    print(f"\n{'='*55}")
                    print(f"  Arquivo: {arquivo} | Hash: {hash_atual.__name__} | M: {tamanho_M}")
                    print(f"{'='*55}")
                    # Calculo de fator de carga
                    n = len(lista_unica)  # n é o número de palavras distintas
                    fator_carga = n / tamanho_M
                    print(f"Fator de carga: {round(fator_carga, 4)}")  
                    print(f"Numero de palavras distintas: {n}")
                    print(f"Tamanho da tabela: {tamanho_M}")
                    print(f"Funcao de hash utilizada: {hash_atual.__name__}")

                    # métricas do histograma
                    tamanhos_buckets = [len(bucket) for bucket in tabela]
                    max_bucket = max(tamanhos_buckets)
                    media_bucket = n / tamanho_M
                    variancia = sum((t - media_bucket) ** 2 for t in tamanhos_buckets) / tamanho_M
                    print(f"Maior bucket: {max_bucket}")
                    print(f"Media por bucket: {round(media_bucket, 4)}")
                    print(f"Variancia: {round(variancia, 4)}")

                    # calculo de comparacoes
                    total_comp_sucesso_hash = 0
                    for palavra in lista_unica:
                        resultado, comp = busca_hash(palavra, tabela, tamanho_M, hash_atual)
                        total_comp_sucesso_hash += comp 

                    palavras_ausentes = [p + "xyz" for p in lista_unica[:1000]]
                    total_comp_falha_hash = 0
                    for palavra in palavras_ausentes:
                        resultado, comp = busca_hash(palavra, tabela, tamanho_M, hash_atual)
                        total_comp_falha_hash += comp

                    total_comp_sucesso_linear = 0
                    for palavra in lista_unica:
                        resultado, comp = busca_sequencial(palavra, lista_unica)
                        total_comp_sucesso_linear += comp

                    total_comp_falha_linear = 0
                    for palavra in palavras_ausentes:
                        resultado, comp = busca_sequencial(palavra, lista_unica)
                        total_comp_falha_linear += comp

                    avg_comp_sucesso_hash = round(total_comp_sucesso_hash / n, 4)
                    avg_comp_falha_hash = round(total_comp_falha_hash / 1000, 4)
                    avg_comp_sucesso_linear = round(total_comp_sucesso_linear/n, 4)
                    avg_comp_falha_linear = round(total_comp_falha_linear/1000, 4)
                    
                    print(f"Comp. sucesso hash: {total_comp_sucesso_hash} | media: {avg_comp_sucesso_hash}")
                    print(f"Comp. falha hash: {total_comp_falha_hash} | media: {avg_comp_falha_hash}")
                    print(f"Comp. sucesso linear: {total_comp_sucesso_linear} | media: {avg_comp_sucesso_linear}")
                    print(f"Comp. falha linear: {total_comp_falha_linear} | media: {avg_comp_falha_linear}")
                    print(f"{'-'*55}")

                    imprime_histograma(tabela, tamanho_M, hash_atual, arquivo)

                    f.write(f"{arquivo},{tamanho_M},{hash_atual.__name__},{n},{round(fator_carga,4)},{max_bucket},{round(media_bucket,4)},{total_comp_sucesso_hash},{avg_comp_sucesso_hash},{total_comp_falha_hash},{avg_comp_falha_hash}\n")
