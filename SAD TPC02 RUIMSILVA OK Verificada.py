#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 29 22:12:01 2018

@author: Rui Guilherme Silva
            19901535 
            Informática de Gestão
"""

""" Criação da função que permite obter uma comparação de uma lista definida como baralho_completo
     em baixo discriminada com LISTA_A e LISTA_B para testar o algoritmo de comparação
     VERSÂO FINAL - OPERACIONAL verificada <<<<<
"""

def deckSolutions(lista_de_cartas):

    # Criação do dicionário que representa um baralho completo de 52 cartas
    # Atribuída as notações do enunciado como 1C = Ás de Copas, ...
    # é atribuido o valor 0 que será usado para a comparação no ciclo com incrementação 
    # que encontre carta igual
    baralho_completo = {"1C":0, "2C":0, "3C":0, "4C":0, "5C":0, "6C":0, 
                        "7C":0, "8C":0, "9C":0, "10C":0, "DC":0, "VC":0, 
                        "RC":0, "1P":0, "2P":0, "3P":0, "4P":0, "5P":0,
                        "6P":0, "7P":0, "8P":0, "9P":0, "10P":0, "DP":0,
                        "VP":0, "RP":0, "1O":0, "2O":0, "3O":0, "4O":0, 
                        "5O":0, "6O":0, "7O":0, "8O":0, "9O":0, "10O":0, 
                        "DO":0, "VO":0, "RO":0,"1E":0, "2E":0, "3E":0,
                        "4E":0, "5E":0, "6E":0, "7E":0, "8E":0, "9E":0,
                        "10E":0, "DE":0, "VE":0, "RE":0}
    
    # define cartas como baralho contendo todas as cartas 
    cartas = baralho_completo.keys()
    
    # ciclo for que irá ler cada carta na lista de cartas obtida 
    for carta in lista_de_cartas:
        
        # Se a carta lida estiver no baralho 
        if carta in cartas:
    
        # adiciona uma carta 
           baralho_completo[carta] += 1


    # Contem a lista de todos os valores que corresponde ao números de cartas de cada um
    Numeros_Lista_Cartas = baralho_completo.values()
    
    # define resultado com quantos baralhos completos estão contados
    resultado = min(Numeros_Lista_Cartas)
    
    # Imprime o resultado de cada lista apresentada 
    print("o nº de baralhos completos de 52 cartas é:")
    print(resultado)
    

  # exemplo de uma lista com algumas cartas correspondendo a zero baralhos completos
LISTA_A = ["1P", "1C", "1O", "2P"]  

 # exemplo de uma lista dada no enunciado com cartas suficientes
# para formar  2 baralhos completos...
LISTA_B = ["1P", "1C", "1O", "2P", "2C", "2O", "2E", "3P", "3C", "3O", 
           "3E", "4P", "4C", "4O", "4E", "5P", "5C", "5O", "5E", "6P",
           "6C", "6O", "6E", "7P", "7C", "7O", "7E", "8P", "8C", "8O",
           "8E", "9P",  "9C", "9O",  "9E", "DP","DC", "DO", "DE", "JP", 
           "JE", "VP", "VC", "VO","VE", "RP", "RC", "RO", "RE", "1P", 
           "1C", "1O", "1E", "2P", "2C", "2O", "2E", "3P", "3C", "3O", 
           "3E", "4P", "4C", "4O", "4E", "5P","5C", "5O", "5E", "6P", 
           "6C", "6O", "6E", "7P", "7C", "7O", "7E", "8P", "8C", "8O",
           "8E", "9P", "9C", "9O", "9E", "DP", "DC", "DO", "DE", "JP", 
           "JC", "JO","JE", "VP", "VC", "VO", "VE", "RP", "RC", "RO", 
           "RE", "1P", "1C", "1O", "1E", "2P", "2C", "2O", "2E", "3P",
           "3C", "3O", "3E", "4P", "4C", "4O", "4E",  "5P", "5C", "5O", 
           "5E", "6P", "6C", "6O", "6E", "7P", "7C", "7O", "7E", "8P", 
           "8C", "8O", "8E", "9P", "9C", "9O", "9E", "DP", "DC", "DO", 
           "DE", "JP", "JC", "JO", "JE", "VP", "VC", "VO", "VE", "RP",
           "RC", "RO", "RE", "10C", "10P", "10O", "10E", "10C", "10P",
           "10O", "10E", "10C", "10P", "10O", "10E", "1E" "JC", "JO"]

#esta lista contem zero baralhos completos
LISTA_C = ["3E", "4P", "4C", "4O", "4E", "5P", "5C", "5O", "5E", "6P", "6C", "6O", 
     "6E", "7P", "7C", "7O", "7E", "8P", "8C", "8O", "8E", "9P", "9C", "9O", "9E", "DP", 
     "DC", "DO", "DE", "JP", "JC", "JO", "JE", "VP", "VC", "VO", "VE", "RP", "RC", "RO", "RE", 
     "1P", "1C", "1O", "1E", "2P", "2C", "2O", "2E", "3P", "3C", "3O", "3E", 
     "4P", "4C", "4O", "4E", "5P", "5C", "5O", "5E", "6P", "6C", "6O", "6E", "7P", "7C", 
     "7O", "7E", "8P", "8C", "8O", "8E", "9P", "9C", "9O", "9E", "DP", "DC", "DO", "DE", 
     "JP", "JC", "JO", "JE", "VP", "VC", "VO", "VE", "RP", "RC", "RO", "RE", "1P", "1C", 
     "1O", "1E", "2P", "2C", "2O", "2E", "3P", "3C", "3O", "3E", "4P", "4C", "4O", "4E", 
     "5P", "5C", "5O", "5E", "6P", "6C", "6O", "6E", "7P", "7C", "7O", "7E", "8P", "8C", 
     "8O", "8E", "9P", "9C", "9O", "9E", "DP", "DC", "DO", "DE", "JP", "JC", "JO", "JE", 
     "VP", "VC", "VO", "VE", "RP", "RC", "RO", "RE"] 

#Esta lista contem 1 baralho completo
LISTA_D = ["3E", "4P", "4C", "4O", "4E", "5P", "5C", "5O", "5E", "6P", "6C", "6O", 
     "6E", "7P", "7C", "7O", "7E", "8P", "8C", "8O", "8E", "9P", "9C", "9O", "9E", "DP", 
     "DC", "DO", "DE", "JP", "JC", "JO", "JE", "VP", "VC", "VO", "VE", "RP", "RC", "RO", "RE", 
     "1P", "1C", "1O", "1E", "2P", "2C", "2O", "2E", "3P", "3C", "3O", "3E", 
     "4P", "4C", "4O", "4E", "5P", "5C", "5O", "5E", "6P", "6C", "6O", "6E", "7P", "7C", 
     "7O", "7E", "8P", "8C", "8O", "8E", "9P", "9C", "9O", "9E", "DP", "DC", "DO", "DE", 
     "JP", "JC", "JO", "JE", "VP", "VC", "VO", "VE", "RP", "RC", "RO", "RE", "1P", "1C", 
     "1O", "1E", "2P", "2C", "2O", "2E", "3P", "3C", "3O", "3E", "4P", "4C", "4O", "4E", 
     "5P", "5C", "5O", "5E", "6P", "6C", "6O", "6E", "7P", "7C", "7O", "7E", "8P", "8C", 
     "8O", "8E", "9P", "9C", "9O", "9E", "DP", "DC", "DO", "DE", "JP", "JC", "JO", "JE", 
     "VP", "VC", "VO", "VE", "RP", "RC", "RO", "RE","10P","10O","10C","10E"] 

# Esta lista contem 3 baralhos completos...
LISTA_E =["1P", "1C", "1O", "2P", "2C", "2O", "2E", "3P", "3C", "3O", 
     "3E", "4P", "4C", "4O", "4E", "5P", "5C", "5O", "5E", "6P", "6C", 
     "6O", "6E", "7P", "7C", "7O", "7E", "8P", "8C", "8O", "8E", "9P", "9C", "9O", 
     "9E", "DP", "DC", "DO", "DE", "JP", "JC", "JO", "JE", "VP", "VC", "VO", 
     "VE", "RP", "RC", "RO", "RE", "1P", "1C", "1O", "1E", "2P", "2C", "2O", 
     "2E", "3P", "3C", "3O", "3E", "4P", "4C", "4O", "4E", "5P", "5C", "5O", "5E",
     "6P", "6C", "6O", "6E", "7P", "7C", "7O", "7E", "8P", "8C", "8O", "8E", "9P", 
     "9C", "9O", "9E", "DP", "DC", "DO", "DE",  "JP", "JC", "JO", "JE", "VP", "VC",
     "VO", "VE", "RP", "RC", "RO", "RE", "1P", "1C",  "1O", "1E", "2P", "2C", "2O",
     "2E", "3P", "3C", "3O", "3E", "4P", "4C", "4O", "4E", 
     "5P", "5C", "5O", "5E", "6P", "6C", "6O", "6E", "7P", 
     "7C", "7O", "7E", "8P", "8C", 
     "8O", "8E", "9P", "9C", "9O", "9E", "DP", "DC",
     "DO", "DE", "JP", "JC", "JO", "JE", 
     "VP", "VC", "VO", "VE", "RP", "RC", "RO", "RE",
     "10C", "10P", "10O", "10E", "10C", "10P", "10O", 
     "10E", "10C", "10P", "10O", "10E", "1E"]


deckSolutions(LISTA_A)
print()

deckSolutions(LISTA_B)
print()

deckSolutions(LISTA_C)
print()

deckSolutions(LISTA_D)
print()

deckSolutions(LISTA_E)


