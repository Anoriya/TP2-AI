from classes import *


class ChainageAvant:

    def __init__(self):
        self.faits = []
        self.regles = []
        self.operateurs = ['<=', '>=', '<', '>', '=']

    def extractFait(self, line):
        if (not (line == '\n')):
            faitAttributeA = line[line.index('(')+1]
            faitAttributeB = line[line.index(',')+1]

            self.faits.append(
                Fait(faitAttributeA, faitAttributeB, -1))


    def extractRegle(self, line):
        regle = line.replace('Si', '').rstrip()
        premisses = regle.split(' alors ')[0].split(' et ')
        conclusions = regle.split(' alors ')[1].strip()

        newPremisses = []
        faitAttributeA = line[line.index('(') + 1]
        faitAttributeB = line[line.index(',') + 1]

        for premisse in premisses:
            for operateur in self.operateurs:
                if operateur in premisse:
                    premisseAttributes = premisse.split(operateur)
                    newPremisses.append(PremisseVar(premisseAttributes[0].strip().rstrip(),
                                                 premisseAttributes[1].strip().rstrip(),
                                                 operateur))
                    break


        self.regles.append(Regle(newPremisses, conclusions, len(self.regles) + 1))

    def checkRegleExecutable(self, regle):
        i = 0
        if regle.executed == True:
            return False
        for premisse in regle.premisses:
            for fait in self.faits:
                if (premisse.operateur == '='):
                    if (premisse.attribut == fait.attribut and premisse.valeur == fait.valeur):
                        i = i + 1
                        break
                if (premisse.operateur == '<='):
                    if (premisse.attribut.strip() == fait.attribut.strip() and premisse.valeur >= fait.valeur):
                        i = i + 1
                        break
                if (premisse.operateur == '<'):
                    if (premisse.attribut == fait.attribut and premisse.valeur > fait.valeur):
                        if premisse.attribut == "Température":
                            print(premisse.operateur)
                            print("DEBUGGGGGGGG***************")
                            print(premisse.valeur)
                            print(fait.valeur)
                        i = i + 1
                        break
                if (premisse.operateur.replace == '>'):
                    if (premisse.attribut == fait.attribut and premisse.valeur < fait.valeur):
                        i = i + 1
                        break
                if (premisse.operateur == '>='):
                    if (premisse.attribut == fait.attribut and premisse.valeur <= fait.valeur):
                        i = i + 1
                        break

        if (i == len(regle.premisses)):
            return True
        else:
            return False

    def addToBf(self, fait, rang):
        fait = Fait(fait.split('=')[0], fait.split('=')[1], rang)
        if self.checkFaitInBf(fait):
            self.faits.append(fait)

    def checkFaitInBf(self, fait):
        for f in self.faits:
            if (f.attribut == fait.attribut and f.valeur == fait.valeur):
                return False;
        return True

    def checkButAtteint(self, but, conclusion):
        if ((but.attribut.strip().rstrip() == conclusion.split('=')[0].strip().rstrip()) and (
                but.valeur.strip().rstrip() == conclusion.split('=')[1].strip().rstrip())):
            return True
        return False

    def checkButDansBF(self, but):
        for fait in self.faits:
            if ((but.attribut.strip().rstrip() == fait.attribut) and (
                    but.valeur.strip().rstrip() == fait.valeur)):
                return True
        return False

    def read_and_parse_file(self, path):
        f = open(path, "r")
        line = f.readline()
        while (line):
            if not line.startswith('si'):
                self.extractFait(line)

            if line.startswith('si'):
                self.extractRegle(line)
            line = f.readline()
        f.close()

    def StartChainge(self, key, value, log, path, saturation):
        self.read_and_parse_file(path)
        log_file = open("C:/Users/Kalelt'has/Desktop/My GL4/AI/Tp AI/logs/log.txt", "w")
        bre = []
        if saturation:
            but = Fait("", "")
        else:
            but = Fait(key, value)

        if self.checkButDansBF(but):
            log.setText("But atteint, se trouvant déjà dans BF")
            log_file.write("But atteint, se trouvant déjà dans BF")
            return but
        else:
            resultat_log = 'Debut chainage avant\n'
            while True:
                for regle in self.regles:
                    if (self.checkRegleExecutable(regle)):
                        regle.executed = True
                        bre.append(regle)

                if (len(bre) == 0):
                    log.setText(resultat_log)
                    log_file.write(resultat_log)
                    return False

                regleToExecute = bre[0]
                resultat_log += "\nRegle executée :\n" + str(regleToExecute)
                self.addToBf(regleToExecute.conclusions, regleToExecute.rang)

                if (self.checkButAtteint(but, regleToExecute.conclusions)):
                    resultat_log += '*****************\n'
                    resultat_log += 'But atteint \n'
                    resultat_log += '*****************\n'
                    log.setText(resultat_log)
                    log_file.write(resultat_log)
                    return but

                for regle in bre:
                    resultat_log += regle.__str__()

                bre.pop(0)

                resultat_log += 'Nouvelle base des faits\n'
                for fait in self.faits:
                    resultat_log += fait.__str__()
