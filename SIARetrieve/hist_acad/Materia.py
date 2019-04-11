class Materia:

    def __init__(self, codigo, nombre, tipologia, creditos, nota):
        aux = codigo.split("-")
        if len(aux) > 2:
            self.codigo = aux[0] + "-" + aux[1]
            self.grupo = aux[2]
        else:
            self.codigo = aux[0]
            self.grupo = aux[1]
        self.nombre = nombre
        self.tipologia = tipologia
        self.creditos = creditos
        self.nota = nota

    def __str__(self):
        return self.codigo + "\t" + self.grupo + "\t" + self.tipologia + "\t" + self.creditos + "\t" + self.nota
