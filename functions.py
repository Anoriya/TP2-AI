import copy

from classes import *

log_file = None


def listSubitute(list, dict):
    i = 0
    while i < len(list):
        for d in dict:
            if list[i] == d:
                log_file.write(str(list[i]) + str(dict[d]))
                list[i] = dict[d]
                break
        i += 1
    return list


def opeartionSubtitue(operation: Operation, dict):
    for d in dict:

        if d in operation.att1:
            operation.att1 = operation.att1.replace(d, dict[d])
            log_file.write("Attribut 1" + operation.att1)
        if d in operation.att2:
            operation.att2 = operation.att2.replace(d, dict[d])
            log_file.write("Attribut 2" + operation.att2)

    # Calculating operations case att 1 or att 2 is an operation
    if '?x' not in operation.att1 and '?y' not in operation.att1:
        operation.att1 = str(eval(operation.att1))

    if '?x' not in operation.att2 and '?y' not in operation.att2:
        operation.att2 = str(eval(operation.att2))

    return operation


def is_atom(expr):
    return len(expr) == 1


def is_variable(expr):
    return '?' in expr


def unifier_atom(expr1, expr2):
    log_file.write('unifier atome')

    if is_atom(expr1):
        expr1 = expr1[0]
    if is_atom(expr2):
        expr1, expr2 = expr2[0], expr1
    log_file.write(str(expr1) + str(expr2))
    if expr1 == expr2:
        return {}
    if is_variable(expr2):
        expr1, expr2 = expr2, expr1
    if is_variable(expr1):
        if expr1 in expr2:
            return None
        if is_atom(expr2):
            return {expr1: expr2[0]}
        return {expr1: expr2}
    return None


def unifier(terms1, terms2):
    log_file.write('\n')
    log_file.write('unifier' + str(terms1) + str(terms2))
    if is_atom(terms1) or is_atom(terms2):
        return unifier_atom(terms1, terms2)
    F1, F2 = [], []
    log_file.write(str(F1))
    F1.append(terms1.pop(0))
    T1 = terms1
    F2.append(terms2.pop(0))
    T2 = terms2
    log_file.write('F1=' + str(F1))
    log_file.write('T1=' + str(T1))
    log_file.write('F2=' + str(F2))
    log_file.write('T2=' + str(T2))
    Z1 = unifier(F1, F2)
    if Z1 is None:
        return None
    log_file.write("FF" + str(Z1))

    log_file.write('T1=' + str(T1))

    log_file.write('T2=' + str(T2))

    T1 = listSubitute(T1, Z1)
    T2 = listSubitute(T2, Z1)
    log_file.write('T1=' + str(T1))

    log_file.write('T2=' + str(T2))

    Z2 = unifier(T1, T2)
    if Z2 is None:
        return None
    Z2.update(Z1)
    return Z2


def genererConclusionUnifies(reglos, pred: Predicat, log_filez):
    global log_file
    log_file = log_filez
    reglesExecutable = []
    # Deep copy copy the variable and change the adress (recursively)
    regles = copy.deepcopy(reglos)

    for regle in regles:
        log_file.write('rang : ' + regle.rang)
        log_file.write(str(pred))
        predicatvals1 = regle.predicats[0].vals.copy()
        predicatvals2 = pred.vals.copy()
        unificateur = unifier(predicatvals1, predicatvals2)

        if unificateur != None:
            i = 0
            test = True
            while i < len(regle.operations) and test:
                operation = opeartionSubtitue(regle.operations[i], unificateur)
                log_file.write("OPERATION " + str(i) + " " + str(operation))
                i += 1
                if not operation.verifOperation():
                    test = False
            if test:
                log_file.write("REGLE A EXECUTER " + regle.rang)
                reglesExecutable.append({regle.rang: unificateur})

    conclusionUnifies = unifierConclusion(reglesExecutable, regles)
    for conc in conclusionUnifies:
        log_file.write("Conclusion unifiées : " + str(conc))
    log_file.write("\n" + '-----------------' + "\n")
    for conclusion in conclusionUnifies:
        log_file.write(str(conclusion))
    log_file.write("\n" + '-----------------' + "\n")
    return conclusionUnifies


def unifierConclusion(reglesDeclenchables, regles):
    # Contient les conclusion unifiées
    x = '?x'
    y = '?y'
    conclusionsUnifies = []

    for regleDeclenchable in reglesDeclenchables:

        key = list(regleDeclenchable.keys())[0]
        value = list(regleDeclenchable.values())[0]

        for regle in regles:
            if regle.rang == key:
                conclusion = regle.conclusion

                # Extracting variables from unification result
                if '?y' in value.keys():
                    y = value['?y']
                if '?x' in value.keys():
                    x = value['?x']

                # Remplacer les variables de la conclusion selon l'unification
                substitutionX = [variable.replace('?x', x) if '?x' in variable else variable for variable in
                                 conclusion.vals]
                substitutionY = [variable.replace('?y', y) if '?y' in variable else variable for variable in
                                 substitutionX]

                # Calculating with eval
                vals = [eval(operation) for operation in substitutionY]
                # Converting int to string as eval return int
                valsString = [str(string) for string in vals]

                conclusion.vals = valsString

                conclusionsUnifies.append(conclusion)
                break
    return conclusionsUnifies


def heuristic(predicat):
    if eval(predicat.vals[0]) == 2:
        return 0
    if (eval(predicat.vals[0]) + eval(predicat.vals[1])) < 2:
        return 7
    if eval(predicat.vals[1]) > 2:
        return 3
    return 1


def getNodewithLowestCost(list, cost_so_far):
    minNode = list[0]
    for node in list:
        if (heuristic(node) + getCostFromList(cost_so_far, node)) < (
                heuristic(minNode) + getCostFromList(cost_so_far, minNode)):
            minNode = node
    return minNode, list.index(minNode)


def addPredicatToDict(predicat, dictionnaire, new_val):
    for key in dictionnaire:
        if key.vals[0] == predicat.vals[0] and key.vals[1] == predicat.vals[1]:
            dictionnaire[key] = new_val
            return True
    dictionnaire[predicat] = new_val
    return True


def getCostFromList(dictionnaire, predicat):
    for key in dictionnaire:
        if key.vals[0] == predicat.vals[0] and key.vals[1] == predicat.vals[1]:
            return dictionnaire[key]
    return None


def prepareChemin(chemin, V):
    chemin.append(V)
    chemin.pop(0)
    chemin.reverse()
    return chemin


# Function to check the existence of un predicat dans un tableaux de predicats
def exist(conclusion, predicats):
    if not predicats:
        return False
    verif = False
    for predicat in predicats:
        if predicat.vals[0] == conclusion.vals[0] and predicat.vals[1] == conclusion.vals[1]:
            return True

    return verif
