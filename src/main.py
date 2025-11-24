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