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
            # print(premisse)
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

    def verifirOperation(self):
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
                # print(line)
                if ':' in line:
                    # print('contains')
                    self.regles.append(Regle.extractRegle(line))
                else:
                    # print('not contains')
                    self.faits.append(Fait(Predicat.extractPredicat(line)))
                    # print('got fait')
            line = f.readline()
            # print('got new line')

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


def listSubitute(list, dict):
    i = 0
    while i < len(list):
        for d in dict:
            if list[i] == d:
                print(list[i], dict[d])
                list[i] = dict[d]
                break
        i += 1
    return list


def opeartionSubtitue(operation: Operation, dict):
    i = 0
    for d in dict:
        if operation.att1 == d:
            operation.att1 = dict[d]
            i += 1
        if operation.att2 == d:
            operation.att2 = dict[d]
            i += 1
        if (i == 2):
            break
    return operation


def is_atom(expr):
    return len(expr) == 1


def is_variable(expr):
    return '?' in expr


def unifier_atom(expr1, expr2):
    print('unifier atome')
    # print(expr1, expr2)
    # print(len(expr1))
    if is_atom(expr1):
        expr1 = expr1[0]
    if is_atom(expr2):
        expr1, expr2 = expr2[0], expr1
    print(expr1, expr2)
    if expr1 == expr2:
        return {}
    if is_variable(expr2):
        expr1, expr2 = expr2, expr1
    # print(expr1, expr2)
    if is_variable(expr1):
        if expr1 in expr2:
            return None
        if is_atom(expr2):
            # print(expr1, expr2)
            return {expr1: expr2[0]}
        return {expr1: expr2}
    return None


def unifier(terms1, terms2):
    print('\n')
    print('unifier', terms1, terms2)
    print(isinstance(terms1, list))
    print(len(terms1))
    if is_atom(terms1) or is_atom(terms2):
        return unifier_atom(terms1, terms2)
    F1, F2 = [], []
    print(F1)
    F1.append(terms1.pop(0))
    T1 = terms1  # return 2 lists : [first elt] [..rest..]
    F2.append(terms2.pop(0))
    T2 = terms2
    print('F1=', F1)
    print('T1=', T1)
    print('F2=', F2)
    print('T2=', T2)
    Z1 = unifier(F1, F2)
    if Z1 is None:
        return None
    print(Z1)
    # print(type(Z1))

    print('T1=', T1)

    print('T2=', T2)

    T1 = listSubitute(T1, Z1)
    T2 = listSubitute(T2, Z1)
    print('T1=', T1)

    print('T2=', T2)

    Z2 = unifier(T1, T2)
    if Z2 is None:
        return None
    Z2.update(Z1)
    return Z2


def genereOperateursApplicables(base: BaseDeConnaissance, pred: Predicat):
    regles = base.regles
    resultat = ''

    reglesExecutable = []

    for regle in regles:
        print('rang : ', regle.rang)
        print(pred)
        predicatvals1 = regle.predicats[0].vals.copy()
        predicatvals2 = pred.vals.copy()
        unificateur = unifier(predicatvals1, predicatvals2)
        if (unificateur != None):
            print('not none')
            i = 0
            test = True
            print(len(regle.operations))
            while i < len(regle.operations) and test:
                operation = opeartionSubtitue(regle.operations[i], unificateur)
                print(operation)
                i += 1
                if not operation.verifirOperation():
                    test = False
            if (test):
                reglesExecutable.append({regle.rang: unificateur})

    print('-----------------')
    for regle in reglesExecutable:
        print(regle)
    print('-----------------')
    return reglesExecutable


def rechercheProfendeurLimiteIteratif():
    for x in range(10):
        rechercheProfendeurLimite(3)

def rechercheProfendeurLimite(depth):
    pass

base = BaseDeConnaissance('C:/Users/Kalelt\'has/Desktop/My GL4/AI/Tp 2/cruches.txt')
print(base)

for regle in (genereOperateursApplicables(base, Predicat.extractPredicat('cruchesAetB(0,0)'))):
    for attribut in regle:
        print(attribut)
        print(regle[attribut])
        print('\n')
