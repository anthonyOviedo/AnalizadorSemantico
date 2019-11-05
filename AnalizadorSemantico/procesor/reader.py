# Antony Oviedo Alfaro
# November 1,2019
# test 2


class Var:
    def __init__(self, _type, name, line, val=None):
        self.name = name
        self.type = _type
        self.val = val
        self.line = line


class Function:
    def __init__(self, name, retorn_val, line):
        self.name = name
        self.retorn_val = retorn_val
        self.line = line


def builderTable(contentTokens):
    # buscar asignaciones, el elemento '='
    table_of_symbols = {}
    for ln, line in enumerate(contentTokens, 1):
        for idx, token in enumerate(line):

            # se econtro una declaracion.
            if isType(token):

                # preguntar si tiene () para que sea una funcion.
                if '(' in line and ')' in line:
                    una_funcion = Function(line[idx + 1], token, ln)
                    table_of_symbols.update({una_funcion.name: una_funcion})

                # variable y asignacion
                elif '=' in line:
                    un_var = Var(line[idx], line[idx + 1], ln, line[idx + 3])
                    table_of_symbols.update({un_var.name: un_var})
                    break

                # declaracion solamante
                else:
                    un_var = Var(line[idx], line[idx + 1], ln)
                    table_of_symbols.update({un_var.name: un_var})
                    break

    return table_of_symbols


def readTxt(text):
    fle = open(text, "r")
    # retorna la tupla del doc, cada elemento de la tupla es una line de codigo
    return fle


def tokenizer(lines):
    tokenContent = []
    # meter  " " para separar simbolos () {} ;
    for idx, line in enumerate(lines):
        if line.find("(") > -1 or line.find(")") > -1:
            # obtener el elemento y insertar dos " "(" " para separar el texto
            line = line.replace("(", " ( ")
            line = line.replace(")", " ) ")
            lines[idx] = line

        if line.find("{") > -1 or line.find("}") > -1:
            # obtener el elemento y insertar dos " "(" " para separar el texto
            line = line.replace("{", " { ")
            line = line.replace("}", " } ")
            lines[idx] = line

        if line.find(";") > -1:
            # obtener el elemento y insertar dos " "(" " para separar el texto
            line = line.replace(";", " ; ")
            lines[idx] = line

    # tokenizar
    for line in lines:
        tokenContent.append(line.split())
    return tokenContent


def spliter(file_):
    lines = []
    for x in file_.readlines():
        lines.append(x)

    return lines


def initScan():
    file_ = readTxt("test.txt")
    lines = spliter(file_)
    contTokens = tokenizer(lines)
    return builderTable(contTokens)


def checkCode(table_of_simbols):
    pass
    # En esta funcion busco los errores del codigo


def isType(token):
    return token == 'int' or token == 'string' or token == 'void' or token == 'float'


table_of_simbols = initScan()
Result = checkCode(table_of_simbols)
