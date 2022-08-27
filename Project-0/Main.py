from mimetypes import init
from operator import truediv
from re import I


def initilizeKeyWords()->list:
    keywords = ["walk", "jump", "jumpTo", "veer", "look", "drop", "grab", "get", "free", "pop", "if", "else", "while", "do", "(", ")", "{", "}", "isfacing", "isValid", "canWalk", "not"]
    return keywords

def initializeVariables()->dict:
    variables = {}
    return variables

def initializeProcedures()->dict:
    procedures = {}
    return procedures
def initializeSemicolon():
    semicolon = 0
    return semicolon
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
    elif type == "ins":
        instructions = ["walk","jump","grab","pop","pick","free","drop"]
        if text in instructions:
            confirmation = True
            
    return confirmation

def iterateThruList(tokens, variables, keywords, procedures,block=False,proc=False):
    isOK = True
    newCommand = True
    stop = False
    pos = 1

    if not (tokens[0] == "PROG" and tokens[-1] == "GORP") and not block and not proc:
        isOK = False
    
    while pos < len(tokens) - 1 and isOK and not stop:
        if tokens[pos] == "newline":
            newCommand = True

        elif block and tokens[pos] == "}":
            stop = True
            pos -= 1

        elif proc and tokens[pos] == "CORP":
            stop = True

        elif newCommand:
            isOK, finishesAt = isCommand(tokens[pos], pos, tokens, variables, keywords, procedures)
            pos = finishesAt
        else:
            isOK = False
        pos += 1

    return isOK, pos 

def isCommand(commandName, i, lista, variables, keywords, funciones):
    "Verifica si el comando es correcto y regresa en qué parte de la lista termina este comando"

    flag = False
    finishesAt = i
    m = 1
    commonKW = ["jump", "drop", "grab", "get", "free", "pop"]
    semicolon = initializeSemicolon()

    chars = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","o","p","q","r","s","t","v","w","x","y","z"]
    print(commandName)
    if commandName in commonKW or (commandName == "walk" and isType(variables, lista[i+2], "integer") and lista[i+1] == "(" and lista[i+3] == ")"):
        if isType(variables, lista[i+2], "integer") and lista[i+1] == "(" and lista[i+3] == ")":
            finishesAt = i+3
            print(lista[i+3])
            flag = True
            semicolon += 1
    
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

    elif commandName == "VAR" and lista[i-2] == "PROG":
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

    elif commandName == "if":
        cond,j = isCondition(lista[i+2],i+2,lista,variables)
        com1,k = isCommand(lista[j+2],j+2,lista,variables,keywords,funciones)
        com2,l = isCommand(lista[k+2],k+2,lista,variables,keywords,funciones)
        if lista[k+1] == "else":
            if cond and com1 and com2 and lista[j+2] == "{" and lista[k] == "}" and lista[l+1] == "fi":
                finishesAt = l + 1
                flag = True
        else:
            if cond and com1:
                finishesAt = i + 17
                print(lista[i+17])
                flag = True
    
    elif commandName == "while":
        cond,j = isCondition(lista[i+2],i+2,lista,variables)
        com,k = isCommand(lista[j+3],j+3,lista,variables,keywords,funciones)
        if cond and com and lista[j+3] == "{" and lista[k] == "}" and lista[k+1] == "od":
            finishesAt = k + 1
            flag = True
        
    elif commandName == "PROC":
        print(lista[i])
        if lista[i+1] != "(" and lista[i+2] == "(":
            s = True
            pos = i + 3
            while s and lista[pos] != ")":
                if lista[pos] == ",":
                    pos += 1
                elif lista[pos] == "{":
                    s = False
                else:
                    variables[lista[pos]] = 0
                    pos += 1
            flag,j = iterateThruList(lista[(pos+1):],variables,keywords,funciones,proc=True)
            finishesAt = j

    elif commandName == "{":
        flag, j = iterateThruList(lista[i:],variables,keywords,funciones,block=True)
        finishesAt = i+j
    
    elif commandName == ";":
        flag = True
        semicolon -= 1

    elif commandName in variables.keys() and lista[i+1] == ":" and lista[i+2] == "=" and lista[i+4] == ";":
        variables[commandName] = lista[i+3]
        finishesAt = i+4
        flag = True

    if semicolon == 1:
        flag = True
    else:
        flag = False
    return flag, finishesAt

def isCondition(cName,i,tokens,variables):
    flag = False
    finishesAt = i
    conditions = initializeConditions()
    print(cName)
    if cName in conditions:
        if cName == "isValid":  
            if isType(variables,tokens[i+2],"ins") and isType(variables,tokens[i+4],"integer") and tokens[i+1] == "(" and tokens[i+3] == "," and tokens[i+5] ==")":
                finishesAt = i + 5
                print(tokens[i+5])
                flag = True
        elif cName == "isfacing":
            if isType(variables,tokens[i+2],"direction") and tokens[i+1] == "(" and tokens[i+3] == ")":
                finishesAt = i + 3
                print(tokens[i+3])
                flag = True
        elif cName == "canWalk":
            if (isType(variables,tokens[i+2],"direction") or isType(variables,tokens[i+2],"position")) and isType(variables,tokens[i+4],"integer") and tokens[i+1] == "(" and tokens[i+3] == "," and tokens[i+5] ==")":
                finishesAt = i + 5
                print(tokens[i+5])
                flag = True
        elif cName == "not":
            cond, _ = isCondition("not",tokens[i+2],tokens,variables)
            if tokens[i+1] == "(" and tokens[i+3] == ")" and cond:
                finishesAt = i + 3
                print(tokens[i+3])
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
            
            elif char == ":":
                addWord(word,words)
                words.append(":")
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