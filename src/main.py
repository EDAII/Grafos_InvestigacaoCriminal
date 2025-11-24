from collections import deque
import os
import time


# estrutura do grafo
class Grafo:
    def __init__(self):
        self.adjacencias = {}
        self.suspeitos = {}

    def adicionar_suspeito(self, id_suspeito, nome, ocupacao, periculosidade):
        self.suspeitos[id_suspeito] = {
            'nome': nome,
            'ocupacao': ocupacao,
            'periculosidade': periculosidade,
            'investigado': False
        }
        if id_suspeito not in self.adjacencias:
            self.adjacencias[id_suspeito] = []

    def adicionar_conexao(self, suspeito1, suspeito2, tipo_relacao):
        # grafo nao direcionado
        if suspeito1 not in self.adjacencias:
            self.adjacencias[suspeito1] = []
        if suspeito2 not in self.adjacencias:
            self.adjacencias[suspeito2] = []

        self.adjacencias[suspeito1].append({'id': suspeito2, 'relacao': tipo_relacao})
        self.adjacencias[suspeito2].append({'id': suspeito1, 'relacao': tipo_relacao})

    def obter_vizinhos(self, suspeito_id):
        return self.adjacencias.get(suspeito_id, [])

    def marcar_investigado(self, suspeito_id):
        if suspeito_id in self.suspeitos:
            self.suspeitos[suspeito_id]['investigado'] = True


#bfs e dfs

#busca em largura, para encontrar o caminho mais curto
def bfs(grafo, inicio, objetivo=None):   
    visitados = set()
    fila = deque([(inicio, [inicio])])
    ordem_visita = []

    while fila:
        atual, caminho = fila.popleft()

        if atual in visitados:
            continue

        visitados.add(atual)
        ordem_visita.append(atual)
        grafo.marcar_investigado(atual)

        if objetivo and atual == objetivo:
            return caminho, ordem_visita

        for vizinho in grafo.obter_vizinhos(atual):
            if vizinho['id'] not in visitados:
                fila.append((vizinho['id'], caminho + [vizinho['id']]))

    return None, ordem_visita

#busca em profundidade, para explorar todo o grafo(rede)
def dfs(grafo, inicio, objetivo=None, visitados=None, caminho=None, ordem_visita=None):
    if visitados is None:
        visitados = set()
    if caminho is None:
        caminho = [inicio]
    if ordem_visita is None:
        ordem_visita = []


    visitados.add(inicio)
    ordem_visita.append(inicio)
    grafo.marcar_investigado(inicio)

    if objetivo and inicio == objetivo:
        return caminho, ordem_visita

    for vizinho in grafo.obter_vizinhos(inicio):
        if vizinho['id'] not in visitados:
            resultado = dfs(grafo, vizinho['id'], objetivo, visitados,
                          caminho + [vizinho['id']], ordem_visita)
            if objetivo and resultado[0]:
                return resultado

    if objetivo:
        return None, ordem_visita
    return caminho, ordem_visita


# missoes

class SistemaMissoes:
    def __init__(self):
        self.pontos = 0
        self.missoes_completadas = 0
        self.casos_resolvidos = []

    def adicionar_pontos(self, pontos):
        self.pontos += pontos

    def completar_missao(self, nome_missao):
        self.missoes_completadas += 1
        self.casos_resolvidos.append(nome_missao)

# casos e cenarios

#caso 1 para resolver: rede de trafico de drogas
def criar_caso_rede_trafico():
    grafo = Grafo()
    # adicionar suspeitos
    grafo.adicionar_suspeito('s1', 'marcos silva', 'empresario', 'alto')
    grafo.adicionar_suspeito('s2', 'ana costa', 'advogada', 'medio')
    grafo.adicionar_suspeito('s3', 'carlos mendes', 'motorista', 'baixo')
    grafo.adicionar_suspeito('s4', 'julia santos', 'contadora', 'medio')
    grafo.adicionar_suspeito('s5', 'roberto alves', 'dono de bar', 'alto')
    grafo.adicionar_suspeito('s6', 'patricia lima', 'estudante', 'baixo')
    grafo.adicionar_suspeito('s7', 'fernando cruz', 'gerente de banco', 'alto')
    grafo.adicionar_suspeito('s8', 'lucia rocha', 'enfermeira', 'medio')
    # adicionar conexoes
    grafo.adicionar_conexao('s1', 's2', 'cliente-advogado')
    grafo.adicionar_conexao('s1', 's4', 'socio comercial')
    grafo.adicionar_conexao('s1', 's7', 'amigo proximo')
    grafo.adicionar_conexao('s2', 's3', 'conhecido')
    grafo.adicionar_conexao('s3', 's5', 'empregado')
    grafo.adicionar_conexao('s4', 's7', 'cliente')
    grafo.adicionar_conexao('s5', 's6', 'vizinho')
    grafo.adicionar_conexao('s5', 's8', 'frequentador')
    grafo.adicionar_conexao('s6', 's8', 'amiga')
    grafo.adicionar_conexao('s7', 's8', 'primo')

    return grafo, {
        'nome': 'operacao serpente negra',
        'descricao': 'rede de trafico de drogas na cidade',
        'suspeito_principal': 's1',
        'alvo_final': 's5'
    }

#caso 2 p/resolver: esquema de lavagem de dinheiro
def criar_caso_lavagem_dinheiro():
    grafo = Grafo()

    grafo.adicionar_suspeito('l1', 'dr. eduardo souza', 'medico', 'alto')
    grafo.adicionar_suspeito('l2', 'mario tavares', 'dono de lavanderia', 'medio')
    grafo.adicionar_suspeito('l3', 'vanessa gomes', 'caixa de banco', 'baixo')
    grafo.adicionar_suspeito('l4', 'thiago barros', 'corretor de imoveis', 'alto')
    grafo.adicionar_suspeito('l5', 'sandra reis', 'secretaria', 'baixo')
    grafo.adicionar_suspeito('l6', 'paulo monteiro', 'dono de restaurante', 'medio')

    grafo.adicionar_conexao('l1', 'l2', 'socio oculto')
    grafo.adicionar_conexao('l1', 'l4', 'investidor')
    grafo.adicionar_conexao('l2', 'l3', 'cliente frequente')
    grafo.adicionar_conexao('l2', 'l6', 'fornecedor')
    grafo.adicionar_conexao('l3', 'l5', 'colega de trabalho')
    grafo.adicionar_conexao('l4', 'l6', 'parceiro comercial')
    grafo.adicionar_conexao('l5', 'l1', 'funcionaria')

    return grafo, {
        'nome': 'operacao lava jato local',
        'descricao': 'esquema de lavagem de dinheiro',
        'suspeito_principal': 'l1',
        'alvo_final': 'l6'
    }

#caso 3 p/resolver: rede de corrupcao
def criar_caso_corrupcao():
    grafo = Grafo()

    grafo.adicionar_suspeito('c1', 'deputado joao neves', 'politico', 'alto')
    grafo.adicionar_suspeito('c2', 'ricardo farias', 'empresario', 'alto')
    grafo.adicionar_suspeito('c3', 'marcia oliveira', 'assessora', 'medio')
    grafo.adicionar_suspeito('c4', 'alberto cunha', 'fiscal', 'medio')
    grafo.adicionar_suspeito('c5', 'beatriz moura', 'lobista', 'alto')
    grafo.adicionar_suspeito('c6', 'sergio pinto', 'jornalista', 'baixo')
    grafo.adicionar_suspeito('c7', 'camila assis', 'secretaria municipal', 'medio')

    grafo.adicionar_conexao('c1', 'c2', 'financiador de campanha')
    grafo.adicionar_conexao('c1', 'c3', 'assessor direto')
    grafo.adicionar_conexao('c1', 'c5', 'contato politico')
    grafo.adicionar_conexao('c2', 'c4', 'pagador de propina')
    grafo.adicionar_conexao('c2', 'c5', 'parceiro')
    grafo.adicionar_conexao('c3', 'c7', 'amiga pessoal')
    grafo.adicionar_conexao('c4', 'c7', 'subordinado')
    grafo.adicionar_conexao('c5', 'c6', 'fonte anonima')

    return grafo, {
        'nome': 'operacao mao limpa',
        'descricao': 'rede de corrupcao politica',
        'suspeito_principal': 'c1',
        'alvo_final': 'c2'
    }


# interface do jogo
def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def exibir_banner():
    print("=" * 60)
    print(" " * 15 + "DIVISAO DE INVESTIGACAO CRIMINAL")
    print("=" * 60)
    print()

def exibir_status(sistema):
    print(f"\n[STATUS] Pontos: {sistema.pontos} | Casos Resolvidos: {sistema.missoes_completadas}/3")
    print("-" * 60)

def exibir_suspeito(grafo, suspeito_id, marcador_especial=None):
    info = grafo.suspeitos[suspeito_id]
    status = "[INVESTIGADO]" if info['investigado'] else "[NAO INVESTIGADO]"

    # marcador visual para suspeito principal ou alvo
    if marcador_especial:
        print(f"\n  {marcador_especial}")
        print(f"  {'=' * 50}")

    print(f"\n  ID: {suspeito_id}")
    print(f"  Nome: {info['nome'].upper()}" if marcador_especial else f"  Nome: {info['nome']}")
    print(f"  Ocupacao: {info['ocupacao']}")
    print(f"  Periculosidade: {info['periculosidade']}")
    print(f"  Status: {status}")

    if marcador_especial:
        print(f"  {'=' * 50}")

def exibir_conexoes(grafo, suspeito_id):
    print(f"\n  Conexoes de {grafo.suspeitos[suspeito_id]['nome']}:")
    vizinhos = grafo.obter_vizinhos(suspeito_id)
    if not vizinhos:
        print("    - nenhuma conexao conhecida")
    for vizinho in vizinhos:
        nome_vizinho = grafo.suspeitos[vizinho['id']]['nome']
        print(f"    - {nome_vizinho} ({vizinho['id']}) [{vizinho['relacao']}]")

def executar_investigacao_bfs(grafo, inicio, fim, sistema):
    limpar_tela()
    exibir_banner()
    print("\n>>> INICIANDO BUSCA EM LARGURA (BFS) <<<")
    print("Objetivo: encontrar caminho mais curto entre suspeitos\n")

    print(f"Ponto de partida: {grafo.suspeitos[inicio]['nome'].upper()} ({inicio})")
    print(f"Alvo da investigacao: {grafo.suspeitos[fim]['nome'].upper()} ({fim})")
    print()
    time.sleep(1)

    caminho, ordem = bfs(grafo, inicio, fim)

    print(f"ordem de investigacao (nivel por nivel):")
    for i, suspeito_id in enumerate(ordem, 1):
        print(f"  {i}. {grafo.suspeitos[suspeito_id]['nome']} ({suspeito_id})")
        time.sleep(0.3)

    if caminho:
        print(f"\n[SUCESSO] caminho mais curto encontrado ({len(caminho)-1} conexoes):")
        print(f"\nCadeia de conexoes ate o alvo:")
        for i, suspeito_id in enumerate(caminho):
            nome = grafo.suspeitos[suspeito_id]['nome']
            if i == 0:
                print(f"  {i+1}. {nome.upper()} ({suspeito_id}) [PONTO DE PARTIDA]")
            elif i == len(caminho) - 1:
                print(f"  {i+1}. {nome.upper()} ({suspeito_id}) [ALVO ENCONTRADO]")
            else:
                print(f"  {i+1}. {nome} ({suspeito_id})")
        sistema.adicionar_pontos(50)
        print(f"\n+50 pontos! total: {sistema.pontos}")
    else:
        print(f"\n[FALHA] nenhum caminho encontrado entre os suspeitos")

    input("\npressione ENTER para continuar...")

def executar_investigacao_dfs(grafo, inicio, sistema):
    limpar_tela()
    exibir_banner()
    print("\n>>> INICIANDO BUSCA EM PROFUNDIDADE (DFS) <<<")
    print("Objetivo: explorar toda a rede criminosa\n")

    print(f"Ponto de partida: {grafo.suspeitos[inicio]['nome'].upper()} ({inicio})")
    print()
    time.sleep(1)

    _, ordem = dfs(grafo, inicio)

    print(f"ordem de investigacao (profundidade primeiro):")
    for i, suspeito_id in enumerate(ordem, 1):
        perigo = grafo.suspeitos[suspeito_id]['periculosidade']
        print(f"  {i}. {grafo.suspeitos[suspeito_id]['nome']} ({suspeito_id}) - perigo: {perigo}")
        time.sleep(0.3)

    print(f"\n[SUCESSO] rede completa mapeada: {len(ordem)} suspeitos identificados")
    sistema.adicionar_pontos(75)
    print(f"\n+75 pontos! total: {sistema.pontos}")

    input("\npressione ENTER para continuar...")

def menu_caso(grafo, info_caso, sistema):
    while True:
        limpar_tela()
        exibir_banner()
        print(f"CASO: {info_caso['nome'].upper()}")
        print(f"Descricao: {info_caso['descricao']}")
        print()
        print(f"[SUSPEITO PRINCIPAL] {grafo.suspeitos[info_caso['suspeito_principal']]['nome'].upper()}")
        print(f"                     ({grafo.suspeitos[info_caso['suspeito_principal']]['ocupacao']})")
        print()
        print(f"[ALVO DA INVESTIGACAO] {grafo.suspeitos[info_caso['alvo_final']]['nome'].upper()}")
        print(f"                       ({grafo.suspeitos[info_caso['alvo_final']]['ocupacao']})")
        exibir_status(sistema)

        print("\n=== OPCOES DE INVESTIGACAO ===")
        print("\n1. visualizar todos os suspeitos")
        print("2. visualizar conexoes de um suspeito")
        print("3. executar BFS (busca em largura - caminho mais curto)")
        print("4. executar DFS (busca em profundidade - rede completa)")
        print("5. resolver caso automaticamente")
        print("0. voltar ao menu principal")

        escolha = input("\nescolha uma opcao: ").strip()

        if escolha == '1':
            limpar_tela()
            exibir_banner()
            print(f"CASO: {info_caso['nome'].upper()}\n")
            print("=== LISTA DE SUSPEITOS ===\n")

            #exibe suspeito principal primeiro
            exibir_suspeito(grafo, info_caso['suspeito_principal'],
                          ">>> SUSPEITO PRINCIPAL (PONTO DE PARTIDA) <<<")

            #exibe alvo
            exibir_suspeito(grafo, info_caso['alvo_final'],
                          ">>> ALVO DA INVESTIGACAO <<<")

            #exibir demais suspeitos
            print("\n=== OUTROS SUSPEITOS NA REDE ===")
            for suspeito_id in sorted(grafo.suspeitos.keys()):
                if suspeito_id not in [info_caso['suspeito_principal'], info_caso['alvo_final']]:
                    exibir_suspeito(grafo, suspeito_id)

            print(f"\n  Total de suspeitos na rede: {len(grafo.suspeitos)}")
            input("\npressione ENTER para continuar...")

        elif escolha == '2':
            limpar_tela()
            exibir_banner()
            print(f"CASO: {info_caso['nome'].upper()}\n")
            print("=== SUSPEITOS DISPONIVEIS ===\n")

            #destacar suspeito principal e alvo
            print(f"  {info_caso['suspeito_principal']}: {grafo.suspeitos[info_caso['suspeito_principal']]['nome'].upper()} [SUSPEITO PRINCIPAL]")
            print(f"  {info_caso['alvo_final']}: {grafo.suspeitos[info_caso['alvo_final']]['nome'].upper()} [ALVO]")
            print()

            for sid in sorted(grafo.suspeitos.keys()):
                if sid not in [info_caso['suspeito_principal'], info_caso['alvo_final']]:
                    print(f"  {sid}: {grafo.suspeitos[sid]['nome']}")

            suspeito = input("\nDigite o ID do suspeito: ").strip()
            if suspeito in grafo.suspeitos:
                marcador = None
                if suspeito == info_caso['suspeito_principal']:
                    marcador = ">>> SUSPEITO PRINCIPAL (PONTO DE PARTIDA) <<<"
                elif suspeito == info_caso['alvo_final']:
                    marcador = ">>> ALVO DA INVESTIGACAO <<<"

                exibir_suspeito(grafo, suspeito, marcador)
                exibir_conexoes(grafo, suspeito)
            else:
                print("\nSuspeito nao encontrado!")
            input("\npressione ENTER para continuar...")

        elif escolha == '3':
            inicio = info_caso['suspeito_principal']
            fim = info_caso['alvo_final']
            executar_investigacao_bfs(grafo, inicio, fim, sistema)

        elif escolha == '4':
            inicio = info_caso['suspeito_principal']
            executar_investigacao_dfs(grafo, inicio, sistema)

        elif escolha == '5':
            limpar_tela()
            exibir_banner()
            print("\n>>> RESOLVENDO CASO COMPLETO <<<")
            print(f"\nCaso: {info_caso['nome'].upper()}")
            print(f"Suspeito Principal: {grafo.suspeitos[info_caso['suspeito_principal']]['nome'].upper()}")
            print(f"Alvo: {grafo.suspeitos[info_caso['alvo_final']]['nome'].upper()}\n")
            time.sleep(1)

            print("[FASE 1] Executando BFS para encontrar caminho mais curto...")
            time.sleep(1)
            caminho_bfs, _ = bfs(grafo, info_caso['suspeito_principal'],
                                  info_caso['alvo_final'])

            print("[FASE 2] Executando DFS para mapear rede completa...")
            time.sleep(1)
            _, ordem_dfs = dfs(grafo, info_caso['suspeito_principal'])

            print(f"\n{'=' * 60}")
            print(f"{'RELATORIO FINAL DA INVESTIGACAO':^60}")
            print(f"{'=' * 60}")
            print(f"\nCaso: {info_caso['nome']}")
            print(f"Suspeitos identificados na rede: {len(ordem_dfs)}")
            print(f"Caminho mais curto ate o alvo: {len(caminho_bfs)-1} conexoes")
            print(f"\nStatus: CASO RESOLVIDO")
            print(f"{'=' * 60}")

            sistema.adicionar_pontos(150)
            sistema.completar_missao(info_caso['nome'])

            print(f"\n[RECOMPENSA] +150 pontos!")
            print(f"Pontos totais: {sistema.pontos}")
            print(f"Casos resolvidos: {sistema.missoes_completadas}")

            input("\npressione ENTER para continuar...")

        elif escolha == '0':
            break


def menu_principal():
    sistema = SistemaMissoes()

    while True:
        limpar_tela()
        exibir_banner()
        print("Bem-vindo, detetive!")
        print("Sua missao: investigar redes criminosas usando algoritmos de busca em grafos.")
        exibir_status(sistema)

        print("\n=== CASOS DISPONIVEIS ===\n")
        print("1. Operacao Serpente Negra")
        print("   [Rede de Trafico de Drogas | 8 suspeitos]")
        print()
        print("2. Operacao Lava Jato Local")
        print("   [Esquema de Lavagem de Dinheiro | 6 suspeitos]")
        print()
        print("3. Operacao Mao Limpa")
        print("   [Rede de Corrupcao Politica | 7 suspeitos]")
        print()
        print("4. Ver Estatisticas")
        print("0. Sair")

        escolha = input("\nescolha um caso para investigar: ").strip()

        if escolha == '1':
            grafo, info = criar_caso_rede_trafico()
            menu_caso(grafo, info, sistema)

        elif escolha == '2':
            grafo, info = criar_caso_lavagem_dinheiro()
            menu_caso(grafo, info, sistema)

        elif escolha == '3':
            grafo, info = criar_caso_corrupcao()
            menu_caso(grafo, info, sistema)

        elif escolha == '4':
            limpar_tela()
            exibir_banner()
            print("\n=== ESTATISTICAS DO DETETIVE ===\n")
            print(f"pontos totais: {sistema.pontos}")
            print(f"casos resolvidos: {sistema.missoes_completadas}")
            if sistema.casos_resolvidos:
                print(f"\ncasos completados:")
                for caso in sistema.casos_resolvidos:
                    print(f"  - {caso}")
            else:
                print("\nnenhum caso resolvido ainda")
            input("\npressione ENTER para continuar...")

        elif escolha == '0':
            limpar_tela()
            exibir_banner()
            print("\nobrigado por jogar!")
            print("ate a proxima, detetive!\n")
            break

# inicio do jogo
if __name__ == "__main__":
    menu_principal()
