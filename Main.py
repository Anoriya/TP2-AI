from functions import *


class resolver:
    def __init__(self, path, init, but):

        self.base = BaseDeConnaissance(path)
        self.EtatInit = init
        self.but = but
        self.graphe = Graph(self.EtatInit)

    def graph_construction(self):
        closedStates = []
        possibleStates = [self.EtatInit]
        i = 0
        # Graph construction
        while possibleStates:

            state = possibleStates.pop(0)
            closedStates.append(state)
            self.base.faits = state
            possibleConclusions = genererConclusionUnifies(self.base.regles, state)

            for conclusion in possibleConclusions:
                self.graphe.addEdge(state, conclusion)
                if not exist(conclusion, closedStates) and not exist(conclusion, possibleStates):
                    possibleStates.append(conclusion)
            i += 1

    # IDDS
    def recherche_idds(self):
        test = Predicat("cruchesAetB", ['2', '0'], -1)
        chemin = []
        if test.vals[0].isdigit() and test.vals[1].isdigit():
            print(self.graphe.rechercheProfendeurLimiteIteratif(self.graphe.V, test, 10, chemin))
            chemin = functions.prepareChemin(chemin,
                                             self.graphe.V)  # Function that modifies the path in order to get it in a good format
            for chem in chemin:
                print("numero regle:", chem.regle, ", conclusion:", chem)
        else:
            print(set(self.graphe.rechercheProfendeurLimiteIteratif(self.graphe.V, test, 10, chemin)))

    # A star
    def recherche_a_start(self):
        result, parcours = self.graphe.a_star_search(self.graphe.V, self.but)
        for chem in parcours:
            print(chem)

