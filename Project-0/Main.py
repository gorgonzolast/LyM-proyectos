def initilizeKeyWords()->list:
    keywords = ["walk", "jump", "jumpTo", "veer", "look", "drop", "grab", "get", "free", "pop", "if", "else", "while", "do", "(", ")", "{", "}", "isfacing", "isValid", "canWalk", "not"]
    return keywords

def initializeVariables()->dict:
    variables = {}
    return variables

def initializeProcedures()->dict:
    procedures = {}
    return procedures

def initializeConditions()->list:
    conditions = ["isfacing","isValid","canWalk","not"]
    return conditions

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
        directions = ["north","south","west","east"]
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
    m = 1
    commonKW = ["jump", "drop", "grab", "get", "free", "pop"]

    chars = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","o","p","q","r","s","t","v","w","x","y","z"]
    print(commandName)
    if commandName in commonKW or (commandName == "walk" and isType(variables, lista[i+2], "integer") and lista[i+1] == "(" and lista[i+3] == ")"):
        if isType(variables, lista[i+2], "integer") and lista[i+1] == "(" and lista[i+3] == ")":
            finishesAt = i+3
            print(lista[i+3])
            flag = True
    
    elif commandName == "walk" and lista[i+1] == "(" and lista[i+5] == ")" and lista[i+3] == "," and isType(variables, lista[i+4], "integer"):
        if isType(variables, lista[i+2], "position"):
            finishesAt = i+5
            print(lista[i+5])
            flag = True

        elif isType(variables, lista[i+2], "direction"):
            finishesAt = i+5
            print(lista[i+5])
            flag = True

    elif commandName == "jumpTo":
        if isType(variables, lista[i+2], "integer") and lista[i+3] == "," and isType(variables, lista[i+4], "integer") and lista[i+1] == "(" and lista[i+5] == ")":
            finishesAt = i+5
            print(lista[i+5])
            flag = True

    elif commandName == "look":
        if isType(variables, lista[i+2], "direction") and lista[i+1] == "(" and lista[i+3] == ")":
            finishesAt = i+3
            print(lista[i+3])
            flag = True

    elif commandName == "var":
        while lista[i+m] != "newline":
            if ((lista[i+m])[0]) in chars:
                addVariable(lista[i+m],variables,0,funciones)
                m += 1
            elif lista[i+m] == ",":
                m += 1
            elif lista[i+m] == ";":
                m += 1
                flag = True
        finishesAt = i + m
    
    elif commandName in variables.keys() and lista[i+1] == "=" and lista[i+3] == ";":
        variables[commandName] = lista[i+2]
        finishesAt = i+3
        flag = True

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

            elif char == ",":
                addWord(word,words)
                words.append(",")
                word = ""

            elif char == ";":
                addWord(word,words)
                words.append(";")
                word = ""
            
            elif char == "=":
                addWord(word,words)
                words.append("=")
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

def addVariable(var,allVariables,value,procedures):
    procedures.pop(var,None)
    allVariables[var] = value
    

def startProgram():

    variables = initializeVariables()
    keywords = initilizeKeyWords()
    procedures = initializeProcedures()

    filename = input("Introduce the name of the textfile ")
    if ".txt" != filename[-4:]:
        filename += ".txt"
    tokens = tokenizer(filename)

    resultado, _ = iterateThruList(tokens, variables, keywords, procedures)
    print(tokens)
    print(variables)
    if resultado:
        print("The syntax is CORRECT.")
    else:
        print("The syntax is INCORRECT.")

startProgram()