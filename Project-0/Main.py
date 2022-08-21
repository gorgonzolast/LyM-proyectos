def initilizeKeyWords()->list:
    keywords = ["walk", "jump", "jumpTo", "veer", "look", "drop", "grab", "get", "free", "pop", "if", "else", "while", "do", "(", ")", "{", "}", "isfacing", "isValid", "canWalk", "not"]
    return keywords

def initializeVariables()->dict:
    variables = {}
    return variables

def initializeProcedures()->dict:
    procedures = {}
    return procedures

def getValue(variables, name):
    return variables[name]

def existVariable(variables, name):
    return name in variables

def isType(variables, text, type):
    confirmation = False
    if type == "integer":
        if text.isdigit() or (existVariable(variables, text) and (getValue(variables, text).isdigit() or getValue(variables, text) == None)):
            confirmation = True
    elif type == "direction":
        directions = ["N","S","W","E"]
        if text in directions or (existVariable(variables, text) and (getValue(variables, text).isdigit() or getValue(variables, text) == None)):
            confirmation = True
    elif type == "turn":
        turnInto = ["left","right","around"]
        if text in turnInto:
            confirmation = True
    elif type == "position":
        positions = ["front","back","left","right"]
        if text in positions:
            confirmation = True
            
    return confirmation

def iterateThruList(tokens, variables, keywords, procedures):
    isOK = True
    newCommand = True
    stop = False
    pos = 1

    if not (tokens[0] == "PROG" and tokens[-1] == "GORP"):
        isOK = False

    while pos < len(tokens) - 1 and isOK and not stop:
        if tokens[pos] == "newline":
            newCommand = True

        elif newCommand:
            isOK, finishesAt = isCommand(tokens[pos], pos, tokens, variables, keywords, procedures)
            pos = finishesAt
        pos += 1

    return isOK, pos 


def isCommand(commandName, i, lista, variables, keywords, funciones):
    "Verifica si el comando es correcto y regresa en qué parte de la lista termina este comando"

    flag = False
    finishesAt = i

    commonKW = ["jump", "drop", "grab", "get", "free", "pop"]
    print(commandName)
    if commandName in commonKW:
        if isType(variables, lista[i+2], "integer") and lista[i+1] == "(" and lista[i+3] == ")":
            finishesAt = i+3
            print(lista[i+3])
            flag = True
    elif commandName == "var":
        if type(lista[i+1][0]) is float:
            
            addVariables(variables,lista[i+1],lista[i+2],funciones)

    
    return flag, finishesAt

def tokenizer(filename):
    """
    Splits the file into tokens for it to be stored on a list
    """
    
    file = open(filename, "r")
    line = file.readline()

    words = []
    word = ""

    while len(line)>0:
        for char in line:

            if char == " " or char == "\t":
                addWord(word, words)
                word = ""
            
            elif char == "(":                 
                addWord(word, words)
                words.append("(")
                word = ""

            elif char == ")":                 
                addWord(word, words)
                words.append(")")
                word = ""

            elif char == "{":                 
                addWord(word, words)
                words.append("{")
                word = ""

            elif char == "}":                 
                addWord(word, words)
                words.append("}")
                word = ""

            elif char == "\n":                 
                addWord(word, words)
                words.append("newline")
                word = ""

            else:
                word += char

        line = file.readline()

    addWord(word, words)

    file.close()

    return words

def addWord(word, words):
    if word != "":
        words.append(word)

def startProgram():

    variables = initializeVariables()
    keywords = initilizeKeyWords()
    procedures = initializeProcedures()

    filename = input("Introduce the name of the textfile ")
    if ".txt" != filename[-4:]:
        filename += ".txt"
    tokens = tokenizer(filename)

    resultado, _ = iterateThruList(tokens, variables, keywords, procedures)
    if resultado:
        print("The syntax is CORRECT.")
    else:
        print("The syntax is INCORRECT.")

startProgram()