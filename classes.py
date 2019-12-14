import collections
import heapq

import functions


class Fait:
    def __init__(self, predicat):
        self.predicat = predicat

    def __str__(self):
        return "\nfait : \n\t{}".format(self.predicat)


class Regle:
    def __init__(self, rang, conclusion, predicats, operations):
        self.rang = rang
        self.conclusion = conclusion
        self.predicats = predicats
        self.operations = operations

    def __str__(self):
        premisses = ''
        predicats = ''
        for predicat in self.predicats:
            predicats = '\t\t' + predicats + str(predicat) + '\n'
        operations = ''
        for operation in self.operations:
            operations = '\t\t' + operations + str(operation) + '\n'

        return '\nregle\n' + '\tpredicats\n' + predicats + '\topeartions \n' + str(
            operations) + '\tconclusion\n' + '\t\t' + str(
            self.conclusion) + '\n\trang ' + str(self.rang)

    @staticmethod
    def extractRegle(text):
        regle = Regle(0, '', [], [])
        regle.rang = text.split(':')[0]
        premisses = text.split(':')[1].split(' alors ')[0]
        conclusion = text.split(':')[1].split(' alors ')[1]
        regle.conclusion = Predicat.extractConclusion(conclusion,regle.rang)
        for premisse in premisses.split(' et '):
            if not (
                    '<=' in premisse or '>=' in premisse or '<' in premisse or '>' in premisse or '==' in premisse or '=' in premisse):
                regle.predicats.append(Predicat.extractPredicat(premisse.replace('Si ', '')))
            else:
                regle.operations.append(Operation.extractOperation(premisse))

        return regle


class Premisse:
    def __init__(self, attribut, valeur, operateur):
        self.attribut = attribut
        self.valeur = valeur
        self.operateur = operateur

    def __str__(self):
        return "\t\tattribut:{}, valeur:{}, operateur:{}".format(self.attribut, self.valeur, self.operateur)


class Operation:
    def __init__(self, att1, att2, op):
        self.att1 = att1
        self.att2 = att2
        self.op = op

    def __str__(self):
        return 'operation : {} {} {}'.format(self.att1, self.op, self.att2)

    def verifOperation(self):
        if self.op == '>=':
            return self.att1 >= self.att2
        if self.op == '<=':
            return self.att1 <= self.att2
        if self.op == '==':
            return self.att1 == self.att2
        if self.op == '=':
            return self.att1 == self.att2
        if self.op == '>':
            return self.att1 > self.att2
        if self.op == '<':
            return self.att1 < self.att2

    @staticmethod
    def extractOperation(text):
        operation = Operation(0, 0, '')
        elems = text.strip()
        elems = elems.split(' ')
        operation.att1 = elems[0].strip()
        operation.att2 = elems[2].strip()
        operation.op = elems[1].strip()
        return operation


class Predicat:
    def __init__(self, nom, vals , regle):
        self.nom = nom
        self.vals = vals
        self.regle = regle

    def __str__(self):
        return '\tpredicat: {},   vals:{}'.format(self.nom, self.vals)

    @staticmethod
    def extractPredicat(text):
        predicat = Predicat('', [], 'fait')
        predicat.nom = text.split('(')[0].strip()
        vals = text.split('(')[1].split(')')[0].split(',')
        for val in vals:
            predicat.vals.append(val.strip())
        return predicat

    @staticmethod
    def extractConclusion(conclusion,rang_regle):
        predicat = Predicat('', [], rang_regle)
        predicat.nom = conclusion.split('( ')[0].strip()
        vals = conclusion.split('( ')[1].strip()
        vals = list(vals)
        vals[len(vals) - 1] = ''
        vals = ''.join(vals).strip().split(', ')
        for val in vals:
            predicat.vals.append(val.strip())
        return predicat


class BaseDeConnaissance:
    def __init__(self, base):
        self.base = base
        self.regles = []
        self.faits = []
        f = open(self.base)
        line = f.readline()
        while line:
            if line != '\n':
                if ':' in line:
                    self.regles.append(Regle.extractRegle(line))
                else:
                    self.faits.append(Fait(Predicat.extractPredicat(line)))
            line = f.readline()

    def __str__(self):
        string = 'base\n\tfaits\n'
        for fait in self.faits:
            string += str(fait)
            string += '\n'
        string += '\n'
        for regle in self.regles:
            string += str(regle)
            string += '\n'
        return string


class PriorityQueue:
    def __init__(self):
        self.elements = []

    def empty(self):
        return len(self.elements) == 0

    def put(self, item, priority):
        heapq.heappush(self.elements, (priority, item))

    def get(self):
        return heapq.heappop(self.elements)[1]


# This class represents a directed graph using adjacency
# list representation
class Graph:

    def __init__(self, vertices):
        # No. of vertices
        self.V = vertices

        # default dictionary to store graph
        self.graph = collections.defaultdict(list)

        def neighbors(self, id):
            return self.graph[id]

        # function to add an edge to graph

    def addEdge(self, u, v):
        self.graph[u].append(v)

    #Display graph
    def graph_dispaly(self,log_file):
        # Graph display
        for key in self.graph:
            print("*********")
            print("Sommet: ", key.nom, '(', key.vals, ')')
            print("Values")
            for val in self.graph[key]:
                print("fils: ", val.nom, '(', val.vals, ')')

    # A function to perform a Depth-Limited search
    # from given source 'src'
    def rechercheProfendeurLimite(self, src, target, maxDepth, chemin, parcours, log_file):

        if src.vals[0] == target.vals[0] and src.vals[1] == target.vals[1]:
            chemin.append(src)
            return True

        # If reached the maximum depth, stop recursing.
        if maxDepth <= 0: return False

        # Recur for all the vertices adjacent to this vertex
        for i in self.graph[src]:
            parcours.append(i)
            if self.rechercheProfendeurLimite(i, target, maxDepth - 1, chemin, parcours, log_file):
                chemin.append(i)
                return True
        return False

    def rechercheProfendeurLimiteseulinconnu(self, src, target, maxDepth, chemin, parcours, log_file):
        if src.vals[0] == target.vals[0]:
            chemin.append(src.vals[1])
        if src.vals[1] == target.vals[1]:
            chemin.append(src.vals[0])
        if maxDepth <= 0:
            for i in self.graph[src]:
                parcours.append(i)
                self.rechercheProfendeurLimiteseulinconnu(i, target, maxDepth - 1, chemin, parcours, log_file)
        return chemin

    def rechercheProfendeurLimiteIteratif(self, src, target, maxDepth, chemin, parcours, log_file):

        # Repeatedly depth-limit search till the
        # maximum depth
        if not target.vals[0].isdigit() or not target.vals[1].isdigit():
            for i in range(maxDepth):
                return self.rechercheProfendeurLimiteseulinconnu(src, target, i, chemin, parcours, log_file)
        else:
            for i in range(maxDepth):
                if self.rechercheProfendeurLimite(src, target, i, chemin, parcours, log_file):
                    return True
            return False



    def a_star_search(self, start, goal, log_file):
        openstates = [start]
        cost_so_far = {start: 0}
        came_from = {start: None}
        closed = []
        parcours = []
        while openstates:
            selected, index = functions.getNodewithLowestCost(openstates, cost_so_far)
            openstates.pop(index)
            closed.append(selected)
            parcours.append(selected)
            if selected.vals[0] == goal.vals[0] and selected.vals[1] == goal.vals[1]:
                parcours.append(selected)
                return True, parcours
            for child in self.graph[selected]:
                if child not in openstates and child not in closed:
                    openstates.append(child)
                    # came_from[child] = selected
                    functions.addPredicatToDict(child, came_from, selected)
                    new_cost = functions.getCostFromList(cost_so_far, selected) + 1 + functions.heuristic(child)
                    functions.addPredicatToDict(child, cost_so_far, new_cost)
                    # cost_so_far[child] = new_cost
                elif child in openstates or child in closed and functions.getCostFromList(cost_so_far,
                                                                                          selected) + 1 < functions.getCostFromList(
                        cost_so_far, child):
                    # cost_so_far[child] = cost_so_far[selected] + 1
                    functions.addPredicatToDict(child, cost_so_far,
                                                functions.getCostFromList(cost_so_far, selected) + 1)
                    openstates.append(child)
                    # came_from[child] = selected
                    functions.addPredicatToDict(child, came_from, selected)

        return False, parcours
