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