# Antony Oviedo Alfaro
# November 1,2019
# test 2
import os


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
        text = "test.txt"
        text = os.path.dirname(os.path.abspath(__file__)) + '\\' + text
        file_ = readTxt(text)
    lines = spliter(file_)

    # tokeniza
    contTokens = tokenizer(lines)

    # construye y verifica la tabla correspondiente al codigo
    table, errores = runCode(contTokens)

    result = (lines, errores, table)
    return result


def runCode(contentTokens):
    table_of_symbols = {}
    errores = []
    for ln, line in enumerate(contentTokens, 1):
        for idx, token in enumerate(line):

            # se econtro una palabra reservada.
            if isReserveWord(token):
                break

            # se econtro una declaracion.
            elif isType(token):

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
                # actualizar el caso en el que lo que se asigna no corresponde a var
                is_in_table, same_type = updateVar(
                    token, table_of_symbols, line[idx+2])

                if is_in_table and same_type:
                    updateTable(table_of_symbols, token, line[idx + 2])

                else:
                    if is_in_table is False:
                        errores.append((ln, "Variable no Existe"))
                        break
                    if same_type is False:
                        errores.append(
                            (ln, "Las variables no son del mismo tipo."))
                        break

    return (table_of_symbols, errores)


def updateTable(tabla, key, valor):
    my_var = tabla[key]
    my_var.val = valor
    tabla[key] = my_var


def updateVar(token, table_of_symbols, val1):
    # se fija que la variable exista y el val1 sea el mismo tipo de la variabble
    if token in table_of_symbols:
        is_in_table = True
        same_type = typeOf(val1) == table_of_symbols[token].type

    else:
        is_in_table = False
        same_type = True

    return (is_in_table, same_type)


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
            # obtener el elemento y insertar dos " "{" " para separar el texto
            line = line.replace("{", " { ")
            line = line.replace("}", " } ")
            lines[idx] = line

        if line.find(";") > -1:
            # obtener el elemento y insertar dos " "=" " para separar el texto
            line = line.replace(";", " ; ")
            lines[idx] = line

        if line.find("=") > -1:
            # obtener el elemento y insertar dos " "(" " para separar el texto
            line = line.replace("=", " = ")
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
    return token == 'if' or token == 'while' or token == 'for'


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


def sameType(val1, val2):
    return typeOf(val1) == typeOf(val2)


Result = initScan()
print(Result)
