# Antony Oviedo Alfaro
# November 1,2019
# test

table_of_symbols = {}


class Var:
    def __init__(self, nombre, val):
        self.nombre = nombre
        self.val = val


def buiderTable(contentTokens):
    # buscar asignaciones, el elemento '='
    table_of_symbols = {}
    for line in contentTokens:
        for idx, token in enumerate(line):
            # en busca de variables.
            if token is '=':
                # armar la tabla aqui...
                un_var = Var(line[idx - 1], line[idx + 1])
                table_of_symbols.update({un_var.nombre: un_var.val})

    return table_of_symbols


def readTxt(text):
    fle = open(text, "r")
    # retorna la tupla del doc, cada elemento de la tupla es una line de codigo
    return fle


def initScan():
    file_ = readTxt("test.txt")
    lines = spliter(file_)
    contetTokens = tokenizer(lines)
    buiderTable(contetTokens)


def tokenizer(lines):
    tokenContent = []
    for line in lines:
        tokenContent.append(line.split())
    return tokenContent


def spliter(file_):
    # guardar las instrucciones aqui
    # linea por linea y bloques de codigo {...}
    # donde termina con comas es una instruccion.
    # el inicio de {} implica recuperar xxxx antes.
    lines = []
    for x in file_.readlines():
        lines.append(x)

    return lines


initScan()
