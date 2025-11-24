# Grafo_InvestigacaoCriminal

Jogo simples de investigação criminal usando algoritmos de busca em grafos (BFS e DFS).

## Alunos
| Matrícula | Nome |
|-----------|------|
| 21/1031593 | Andre Lopes de Sousa |
| 23/1012129 | Gabriel Lopes de Amorim |

## Descrição do projeto

Jogo de investigação criminal desenvolvido em Python para terminal que utiliza algoritmos de busca em grafos (BFS e DFS) para rastrear redes criminosas. O jogador assume o papel de um detetive que deve identificar conexões entre suspeitos e resolver casos criminais.

### Algoritmos implementados

BFS (Busca em Largura)
- Encontra o caminho mais curto entre dois suspeitos na rede
- Explora nível por nível (todos os vizinhos antes de aprofundar)
- Útil para identificar conexões diretas e rotas mais rápidas
- Implementação com fila

DFS (Busca em Profundidade)
- Mapeia toda a rede criminosa conectada a um suspeito
- Explora o máximo possível antes de retroceder
- Útil para descobrir toda a organização criminal
- Implementação recursiva

### Funcionalidades

- 3 casos criminais diferentes.
- Sistema de pontuação e missões.
- Visualização de suspeitos e suas conexões.
- Execução dos algoritmos.

## Guia de instalação

### Dependências do projeto

- Python 3.6 ou superior
- Bibliotecas padrão: `collections`, `os`, `time`

### Como executar o projeto

1. Clone ou baixe o repositório:
```bash
https://github.com/EDAII/Grafos_InvestigacaoCriminal
```

2. Entre na pasta do projeto:
```bash
cd src/
```

3. Execute o arquivo python
```bash
python3 main.py
```

Navegue pelos menus usando os números e pressione Enter.

### Como jogar

1. Escolha um dos 3 casos disponíveis no menu principal
2. Dentro do caso, você pode:
   - Visualizar todos os suspeitos
   - Ver conexões específicas entre pessoas
   - Executar BFS para encontrar caminho mais curto
   - Executar DFS para mapear rede completa
   - Resolver o caso automaticamente (executa ambos algoritmos)
3. Acumule pontos resolvendo casos

### Sistema de pontuação

- BFS (caminho mais curto): 50 pontos
- DFS (rede completa): 75 pontos
- Resolver caso completo: 150 pontos

### Casos disponíveis

1. Operação Serpente Negra: rede de trafico de drogas (8 suspeitos)
2. Operação Lava Jato Local: esquema de lavagem de dinheiro (6 suspeitos)
3. Operação Mão Limpa: rede de corrupção política (7 suspeitos)

## Capturas de tela

### Menu Principal
![Menu Principal](/assets/img/menu.png)

O menu principal apresenta todas as funcionalidades do game.

### Casos - Informações sobre os casos e Opções de Investigação
![opções de investigação](/assets/img/opcoes_invest.png)

### Casos - Visualizar todos os suspeitos
![opções de investigação](/assets/img/c1_opção1.png)

### Casos - Visualizar conexões de um suspeitos
![opções de investigação](/assets/img/c1_opção2.png)

Mostra todas as conexões de um suspeito.

### Casos - Executar BFS
![opções de investigação](/assets/img/c1_opção3.png)

Executa BFS para encontrar caminho mais curto entre os suspeitos.

### Casos - Executar DFS
![opções de investigação](/assets/img/c1_opção4.png)

Executa DFS para mapear toda a rede criminosa.

### Casos - Resolver casos
![opções de investigação](/assets/img/c1_opção5.png)

Executa ambas as buscas para resolver o caso.

### Casos - Visualizar estatísticas
![opções de investigação](/assets/img/estatisticas.png)

## Conclusões
Os algoritmos BFS e DFS foram extremamente úteis para a identificação de conexões. BFS é ideal quando precisamos do caminho mais curto, enquanto DFS é melhor para mapear toda a estrutura da rede.

No contexto do jogo, a combinação de ambos algoritmos permitiu tanto encontrar rotas diretas entre suspeitos quanto mapear toda a organização criminosa.
## Vídeo de Apresentação

Aqui está o vídeo de apresentação do projeto:

[Link para o vídeo](https://youtu.be/)

## Referências
- Algoritmos de grafos: material da disciplina disponibilizado pelo professor.
- Python collections.deque: https://docs.python.org/3/library/collections.html#collections.deque