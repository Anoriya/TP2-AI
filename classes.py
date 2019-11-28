class Fait:
    def __init__(self, valeurA, valeurB, flag=-1):
        self.A = valeurA
        self.B = valeurB
        self.flag = flag

    def __str__(self):
        return "fait : \n\tNb litres dans A:{}, \n\tNb litres dans B:{}, \n\tflag:{}\n ".format(self.A, self.B,
                                                                                                self.flag)


class Regle:
    def __init__(self, premisses, conclusions, rang):
        self.premisses = premisses
        self.conclusions = conclusions
        self.rang = rang
        self.executed = False

    def __str__(self):
        res = 'regle\n'
        res += 'premisses\n'
        for premisse in self.premisses:
            res += '\t' + premisse.__str__().rstrip()
        res += '\n\tconclusion\n'
        res += '\t' + self.conclusions + '\n'
        res += '\texecuted ' + str(self.executed) + '\n'
        return res


class Premisse:
    pass


class PremisseVar(Premisse):
    def __init__(self, attribut, valeur, operateur):
        self.attribut = attribut
        self.valeur = valeur
        self.operateur = operateur

    def __str__(self):
        return "\tattribut:{}, valeur:{}, operateur:{}".format(self.attribut, self.valeur, self.operateur)


class PremisseExp(Premisse):
    def __init__(self, valeurA, valeurB):
        self.A = valeurA
        self.B = valeurB

    def __str__(self):
        return "fait : \n\tNb litres dans A:{}, \n\tNb litres dans B:{}, \n\t ".format(self.A, self.B)
