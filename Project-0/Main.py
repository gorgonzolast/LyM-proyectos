def init_Keywords()->list:
    keywords = ["walk","jump","jumpTo","veer","look","drop","grab","get","free","pop","if","else","while","do","(",")","{","}","isfacing","isValid","canWalk","not"]
    return keywords

def isCommand(CommandName, i, lista, variables, keywords, funciones):
    "Verifica si el comando es correcto y regresa en qué parte de la lista termina este comando"

    correcto = False
    termina_en = i

    commonKw = ["jump","drop","grab","get","free","pop"]
    if CommandName in commonKw:
        #print("T1. lista[i="+str(i)+"] " +lista[i])
        if is_Type(variables, lista[i+1], "numero"):
            termina_en = i+1
            correcto = True

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

    #variables = init_Variables()
    keywords = init_Keywords()
    #funciones = init_Funciones()

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