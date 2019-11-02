# Antony Oviedo Alfaro
# November 1,2019


def buiderTable(contentTokens):
    # buscar asignaciones, el elemento '='
    for line in contentTokens:
        for token in line:
            if token is '=':
                # armar la tabla aqui...


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


class var:
    def __init__(self, nombre, val):
        self.nombre = nombre
        self.val = val
