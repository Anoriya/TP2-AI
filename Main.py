from functions import *


class Resolver:
    def __init__(self, path, init, but, strat, res, chemin, parcours):

        self.base = BaseDeConnaissance(path)
        self.EtatInit = init
        self.but = but
        self.graphe = Graph(self.EtatInit)
        self.strat = strat
        self.res = res
        self.chemin = chemin
        self.parcours = parcours

    def graph_construction(self, log_file):
        closedStates = []
        possibleStates = [self.EtatInit]
        i = 0
        # Graph construction
        while possibleStates:

            state = possibleStates.pop(0)
            closedStates.append(state)
            self.base.faits = state
            possibleConclusions = genererConclusionUnifies(self.base.regles, state, log_file)

            for conclusion in possibleConclusions:
                self.graphe.addEdge(state, conclusion)
                if not exist(conclusion, closedStates) and not exist(conclusion, possibleStates):
                    possibleStates.append(conclusion)
            i += 1
        self.graphe.graph_dispaly(log_file)

    # IDDS
    def recherche_idds(self, log_file):
        chemin = []
        parcours = []
        if self.but.vals[0].isdigit() and self.but.vals[1].isdigit():
            res = self.graphe.rechercheProfendeurLimiteIteratif(self.graphe.V, self.but, 10, chemin, parcours, log_file )
            if res:
                self.res.setText(str(res))
                chemin = functions.prepareChemin(chemin,
                                                 self.graphe.V)  # Function that modifies the path in order to get it in a good format
                for chem in chemin:
                    self.chemin.append("numero regle:" + str(chem.regle) + ", conclusion:" + str(chem))
            else:
                self.res.setText(str(res))
                self.chemin.setText("")

        else:
            res = self.graphe.rechercheProfendeurLimiteIteratif(self.graphe.V, self.but, 10, chemin, parcours, log_file)
            if res:
                self.res.setText("True")
                result = set(res)
                for resu in result:
                    self.chemin.append(str(resu))
            else:
                self.res.setText("False")
                self.chemin.setText("")
        for parc in parcours:
            self.parcours.append(str(parc))

    # A star
    def recherche_a_start(self, log_file):
        result, parcours = self.graphe.a_star_search(self.graphe.V, self.but, log_file)
        for chem in parcours:
            self.parcours.append(str(chem))
        self.chemin.setText("")
        self.res.setText(str(result))


    def start(self, log_path):
        log_file = open(log_path, "w")
        self.graph_construction(log_file)
        if self.strat == "A*":
            self.recherche_a_start(log_file)
        else:
            self.recherche_idds(log_file)
