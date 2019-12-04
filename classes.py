from collections import defaultdict


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
        regle.conclusion = Predicat.extractConclusion(conclusion)
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
    def __init__(self, nom, vals):
        self.nom = nom
        self.vals = vals

    def __str__(self):
        return '\tpredicat: {},   vals:{}'.format(self.nom, self.vals)

    @staticmethod
    def extractPredicat(text):
        predicat = Predicat('', [])
        predicat.nom = text.split('(')[0].strip()
        vals = text.split('(')[1].split(')')[0].split(',')
        for val in vals:
            predicat.vals.append(val.strip())
        return predicat

    @staticmethod
    def extractConclusion(conclusion):
        predicat = Predicat('', [])
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


# This class represents a directed graph using adjacency
# list representation
class Graph:

    def __init__(self, vertices):
        # No. of vertices
        self.V = vertices

        # default dictionary to store graph
        self.graph = defaultdict(list)

        # function to add an edge to graph

    def addEdge(self, u, v):
        self.graph[u].append(v)

    # A function to perform a Depth-Limited search
    # from given source 'src'
    def rechercheProfendeurLimite(self, src, target, maxDepth):

        if src.vals[0] == target.vals[0] and src.vals[1] == target.vals[1]:
            return True

        # If reached the maximum depth, stop recursing.
        if maxDepth <= 0: return False

        # Recur for all the vertices adjacent to this vertex
        for i in self.graph[src]:
            if self.rechercheProfendeurLimite(i, target, maxDepth - 1):
                return True
        return False

    def rechercheProfendeurLimiteIteratif(self, src, target, maxDepth):

        # Repeatedly depth-limit search till the
        # maximum depth
        for i in range(maxDepth):
            if self.rechercheProfendeurLimite(src, target, i):
                return True
        return False
