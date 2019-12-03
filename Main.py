from functions import *

base = BaseDeConnaissance('C:/Users/Kalelt\'has/Desktop/My GL4/AI/Tp 2/cruches.txt')

# for regle in (genererConclusionUnifies(base, Predicat.extractPredicat('cruchesAetB(4,0)'))):
#     pass

EtatInit = base.faits[0].predicat
graphe = Graph(EtatInit)
closedStates = []
possibleStates = [EtatInit]

# for conc in genererConclusionUnifies(base, EtatInit):
#     possibleStates.append(conc)

while possibleStates:
    state = possibleStates.pop(0)
    closedStates.append(state)
    base.faits.append(state)
    possibleConclusions = genererConclusionUnifies(base, state)
    print("AAAAAA", state)
    for possible in possibleConclusions:
        print("HHHHH", possible)
    for conclusion in possibleConclusions:
        graphe.addEdge(state, conclusion)
        if not conclusion in closedStates and not conclusion in possibleStates:
            possibleStates.append(conclusion)

for key in graphe.graph:
    print("*********")
    print("Sommet: ", key.nom, '(', key.vals, ')')
    print("Values")
    for val in graphe.graph[key]:
        print("fils: ", val.nom, '(', val.vals, ')')
