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
        self.symbolType = "Var"

    def description(self):
        return "%s,%s,%s,%s,%s" % (self.symbolType, self.name, self.type, self.val, self.line)


class Function:
    arguments = []

    def description(self):
        return "%s,%s,%s,%s,%s" % (self.symbolType, self.name, self.retorn_val, self.line, self. scope)

    def __init__(self, name, retorn_val, line):
        self.name = name
        self.retorn_val = retorn_val
        self.line = line
        self.symbolType = "Function"

    def set_scope(self):
        self.scope = "L.1:{} - L.2: {}".format(self.l1, self.l2)


def initScan(text=None):
    # abre el archivo
    if text is not None:
        file_ = readTxt(text)
    else:
        text = "test.txt"
        text = os.path.dirname(os.path.abspath(__file__)) + '\\' + text
        file_ = readTxt(text)

    # guarda las lineas en un array lines
    lines = spliter(file_)

    # tokeniza
    contTokens = tokenizer(lines)

    # construye y verifica la tabla correspondiente al codigo
    table, errores = runCode(contTokens)

    result = (lines, errores, table)
    return result


def runCode(contentTokens):
    table_of_symbols = {}  # diccionario con las variables y las funciones
    errores = []  # errores presentes en el codigo
    temps_var = []  # variables para la funcion5
    llaves = []
    parentecis = []
    # fue necesario para que no tuviera errores
    for ln, line in enumerate(contentTokens, 1):
        for idx, token in enumerate(line):
            if token == '{':
                llaves.append(ln)
            if token == '}':
                llaves.pop()
            if token == '(':
                parentecis.append(ln)
            if token == ')':
                parentecis.pop()

    while llaves != []:
        errores.append((llaves[0], " llave sin cerrar."))
        llaves.pop()

    while parentecis != []:
        errores.append((parentecis[0], " parentecis sin cerra sin cerrar."))
        parentecis.pop()

    if errores != []:
        return ([], errores)

    for ln, line in enumerate(contentTokens, 1):
        for idx, token in enumerate(line):
            if line == []:
                break

            # colecta todas los argumentos
            try:
                if gettingVarsFunc:
                    if ')' == token:
                        una_funcion.arguments = temps_var
                        temps_var = []
                        gettingVarsFunc = False
                        continue

                    temps_var.append(token)
                    continue
            except:
                pass

            # carga las variables de la funcion. para que se usen
            try:
                if in_func:
                    if '{' == token:
                        una_funcion.l1 = ln
                        # aqui se cargan todos los argumentos
                        tmp_var_arg = []
                        for tokArg in una_funcion.arguments:
                            if tokArg == ',':
                                continue
                            elif isType(tokArg):
                                typeVar = tokArg
                            else:
                                varName = tokArg
                                un_var = Var(typeVar, varName, ln)
                                if typeVar != "":
                                    tmp_var_arg.append(un_var)
                                    typeVar = ""
                        una_funcion.arguments = tmp_var_arg
                        continue

                    if '}' == token:
                        # borrar todas las variables locales de la
                        in_func = False
                        una_funcion.l2 = ln
                        una_funcion.set_scope()
                        continue

                    if 'return' == token:
                        return_var = line[idx + 1]
                        if typeOf(return_var) != una_funcion.retorn_val:
                            errores.append(
                                (ln, "El tipo de la variable con coincide con el tipo de retorno en la funcon"))
            except:
                pass

            # se econtro una palabra reservada.
            if isReserveWord(token):
                break

            # inicia los argumentos
            if '(' == token:
                gettingVarsFunc = True
                continue

            # declaraciones o funciones.
            elif isType(token):

                # preguntar si tiene () para que sea una funcion.
                if '(' in line or ')' in line:
                    in_func = True
                    una_funcion = Function(line[idx + 1], token, ln)
                    table_of_symbols.update({una_funcion.name: una_funcion})

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
                elif isType(line[idx]):
                    un_var = Var(line[idx], line[idx + 1], ln)
                    table_of_symbols.update({un_var.name: un_var})
                    break

            # se ecncotro una asignacion
            elif '=' in line:
                # revisa errores.
                is_in_table, same_type = isUpgradeable(
                    token, table_of_symbols, line[idx+2])
                if is_in_table and same_type:
                    updateTable(table_of_symbols, token, line[idx + 2])
                    break
                else:
                    if is_in_table is False:
                        errores.append((ln, " Variable no esta declarada"))
                        break
                    if same_type is False:
                        errores.append(
                            (ln, " Las variables no son del mismo tipo."))
                        break

    return (table_of_symbols, errores)


def updateTable(tabla, key, valor):
    my_var = tabla[key]
    my_var.val = valor
    tabla[key] = my_var


def isUpgradeable(token, table_of_symbols, val1):
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
        line = line.replace("//", " // ")
        lines[idx] = line
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
    for idx, line in enumerate(tokenContent):
        if line[0] == "//":
            tokenContent[idx] = []

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


def symbolType(object):
    print(object, end=" +: ")
    if isinstance(object, Var):
        return "Var"
    else:
        return "Funtion"


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
