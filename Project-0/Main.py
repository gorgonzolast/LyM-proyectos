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
    pos = 0

    if not (tokens[0] == "PROG" and tokens[-1] == "PROG"):
        isOK = False

    while n < len(tokens) and isOK and not stop:
        if newCommand:
            isOK, finishesAt = isCommand(tokens[pos], pos, tokens, variables, keywords, procedures)
        n += 1

    return isOK, pos 


def isCommand(commandName, i, lista, variables, keywords, funciones):
    "Verifica si el comando es correcto y regresa en qué parte de la lista termina este comando"

    flag = False
    finishesAt = i

    commonKW = ["jump", "drop", "grab", "get", "free", "pop"]
    if commandName in commonKW:
        #print("T1. lista[i="+str(i)+"] " +lista[i])
        if isType(variables, lista[i+1], "integer"):
            finishesAt = i+1
            flag = True

#Hola

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

    resultado, _ = iterateThruList(tokens, keywords, funciones)
    if resultado:
        print("The syntax is CORRECT.")
    else:
        print("The syntax is INCORRECT.")

startProgram()