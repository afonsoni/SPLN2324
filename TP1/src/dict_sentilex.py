import codecs

def sentiLexFlexToDict():
    fileName = "SentiLex-PT02/SentiLex-flex-PT02.txt"
    inputFile = codecs.open(fileName,"rb","utf-8")
    expressions = {}
    for line in inputFile:
        splitted = line.split(";")
        DicionarioAux = {}
        if(len(splitted[1].split('=')) == 1):
            DicionarioAux [splitted[1].split('=')[0]] = ''
        else:
            DicionarioAux [splitted[1].split('=')[0]] = splitted[1].split('=')[1] 
    
        DicionarioAux [splitted[2].split('=')[0]] = splitted[2].split('=')[1]
        DicionarioAux [splitted[3].split(':')[0]] = splitted[3].split(':')[1].split('=')[1]

        if (splitted[4].split('=')[0] == 'ANOT'):
            DicionarioAux [splitted[4].split('=')[0]] = splitted[4].split('=')[1]
        else:
            DicionarioAux [splitted[4].split('=')[0].split(':')[0] ] = splitted[4].split('=')[1]
    
        expressions[splitted[0].split(",")[0]] = DicionarioAux 
        expressions[splitted[0].split(",")[1]] = DicionarioAux
    
    return expressions #SentiLex-Flex em Dict