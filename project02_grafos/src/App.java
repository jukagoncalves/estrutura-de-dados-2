
public class App {
    public static void main(String[] args){
        Grafos g = new Grafos(10);
        
        g.inserirAresta(0, 1);
        g.inserirAresta(1, 2);
        g.inserirAresta(2, 3);
        g.inserirAresta(4, 5);
        g.inserirAresta(6, 7);
        g.inserirAresta(7, 8);
        g.inserirAresta(8, 6);
        System.out.println("GRAFO (lista de adjacencia):");
        g.exibirGrafo();
        
        System.out.println("\n-----ALGORITMO DFS-----");
        g.dfs(0);
        g.dfs(4);
        g.dfs(6);
        g.dfs(9);

        System.out.println("\n-----ALGORIRMO BFS-----");
        g.bfs(0);
        g.bfs(4);
        g.bfs(6);
        g.bfs(9);

        System.out.println("\n-----COMPONENTES CONEXAS-----");
        g.componentesConexas();
    }
}
