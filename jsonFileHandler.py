#Importamos el archivo json dentro de files
import json

#Creamos la función para leer el archivo
def readJsonFile(fileName):
    data = ""
    try:
        with open(fileName) as json_file:
            data = json.load(json_file)
    except IOError:
        print("Could not read file")
    return data
    
    