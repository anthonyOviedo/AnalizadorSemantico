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


def initScan(text=None):
        # guarda las lineas en un array lines
    if text is not None:
        file_ = readTxt(text)
    else:
        file_ = readTxt("test.txt")
    lines = spliter(file_)

    # tokeniza
    contTokens = tokenizer(lines)

    # construye y verifica la tabla correspondiente al codigo
    table, errores = runCode(contTokens)

    result = (lines, errores, table)
    return result


def runCode(contentTokens):
    # buscar asignaciones, el elemento '='
    errores = []
    table_of_symbols = {}
    errores = []
    for ln, line in enumerate(contentTokens, 1):
        for idx, token in enumerate(line):

            if isReserveWord(token):
                # casos de if y whiles.
                # hacer una funcion para obtener las varibles locales.
                break

            # se econtro una declaracion.
            if isType(token):

                # preguntar si tiene () para que sea una funcion.
                if '(' in line and ')' in line:
                    una_funcion = Function(line[idx + 1], token, ln)
                    table_of_symbols.update({una_funcion.name: una_funcion})
                    break

                # asignacion automatica
                elif '=' in line and 'auto' in line:
                    typ = typeOf(line[idx + 3])
                    un_var = Var(typ, line[idx + 1], ln, line[idx + 3])
                    table_of_symbols.update({un_var.name: un_var})
                    break

                # declaracion de variable y asignacion
                elif '=' in line and isType(token):
                    un_var = Var(line[idx], line[idx + 1], ln, line[idx + 3])
                    table_of_symbols.update({un_var.name: un_var})
                    break

                # declaracion solamante
                else:
                    un_var = Var(line[idx], line[idx + 1], ln)
                    table_of_symbols.update({un_var.name: un_var})
                    break

            # se ecncotro una asignacion
            else:
                if updateVar(token, table_of_symbols):
                    table_of_symbols.update({token: line[idx + 2]})
                else:
                    errores.append((ln, "Variable no Existe"))

    return table_of_symbols


def updateVar(token, table_of_symbols):
    if token in table_of_symbols:
        return True
    else:
        return False


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

        if line.find("=") > -1:
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


def isReserveWord(token):
    pass


def isType(token):
    return token == 'int' or token == 'string' or token == 'void' or token == 'float' or token == 'auto'


def typeOf(val):
    try:
        int(val)
        return 'int'
    except ValueError:
        pass
    try:
        float(val)
        return 'float'
    except ValueError:
        pass

    if val[0] == '"' and val[len(val) - 1] == '"':
        return 'string'

    elif val == "true" or val == "false":
        return "bool"


table_of_simbols = initScan()
Result = checkCode(table_of_simbols)
