import java.util.ArrayList;
import java.util.LinkedList;
import java.util.Queue;

public class Grafos {
    private int qtdVertices;
    private ArrayList<Integer>[] listaAdj;

    //construtor
    @SuppressWarnings("unchecked")
    public Grafos(int n){
        qtdVertices = n;
        listaAdj = new ArrayList[n]; //cria lista adj com n vertices

        for(int i = 0; i < n; i++ ){
            listaAdj[i] = new ArrayList<>(); //lista vazia para cada indice da lista adj
        }
    }

    public void inserirAresta(int origem, int destino){
        listaAdj[origem].add(destino);
        listaAdj[destino].add(origem);
    }

    public void exibirGrafo(){
        
        for(int v=0; v<qtdVertices; v++){
            System.out.println("Vertice " + v + " -> " + listaAdj[v]);
        }
    }

    //Algoritmos
    public void dfs(int origem){
        boolean[] visitado = new boolean[qtdVertices]; //ja cria com tudo false

        System.out.print("Ordem DFS: ");
        dfsAuxiliar(origem, visitado);
        System.out.println();
    }

    private void dfsAuxiliar(int v, boolean[] visitado ){ 
        visitado[v] = true;
        System.out.print(v + " ");
        for(Integer vizinho : listaAdj[v]){ // vizinho é cada elemento da lista do vértice v
            if(!visitado[vizinho]){ //visitado[vizinho] == false
                dfsAuxiliar(vizinho, visitado);
            }
        }
    }

    public void bfs(int origem){
        boolean[] visitado = new boolean[qtdVertices];
        Queue<Integer> fila = new LinkedList<>();

        visitado[origem] = true; //marca visitado ao ENFILEIRAR
        fila.offer(origem);

        System.out.print("Ordem do BFS: ");
        while (!fila.isEmpty()) {
            int v = fila.poll();
            System.out.print(v + " ");

            for(Integer vizinho : listaAdj[v]){
                if(!visitado[vizinho]){
                    visitado[vizinho] = true; //marca visitado ao ENFILEIRAR
                    fila.offer(vizinho);
                }
            }
        }
        System.out.println();
    }

    public void componentesConexas(){
        boolean[] visitado = new boolean[qtdVertices];
        int contador = 0;

        for(int v = 0; v < qtdVertices; v++){
            if(!visitado[v]){
                contador ++;
                System.out.printf("Componente %d: ", contador);
                dfsAuxiliar(v, visitado);
                System.out.println();
            }
        }
        System.out.println("Total de componentes: " + contador);
    }
}
