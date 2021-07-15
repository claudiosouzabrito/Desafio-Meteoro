from PIL import Image
from matplotlib import image, pyplot
import copy
from dot import Dot, plotLine
import numpy as np

imageOriginal = Image.open("meteor_challenge_01.png")

data = image.imread("meteor_challenge_01.png")

numLines = data.shape[0]
numColums = data.shape[1]

numStars = 0
numMeteor = 0
water = []
meteorInWater = 0

dots = []

for l in reversed(range(numLines)):     #Percorrendo a imagem de trás para frente
    for c in reversed(range(numColums)):#do último pixel ao primeiro
        pixel = data[l][c]
        if pixel[0] == 0.0 and pixel[1] == 0.0 and pixel[2] == 1.0:#Se for um pixel azul puro, então é água
            water.append(c)                                        #Adicionar a coluna desse pixel na lista de colunas com água
            
        elif pixel[0] == 1.0 and pixel[1] == 0.0 and pixel[2] == 0.0:#Se for um pixel vermelho puro
            numMeteor += 1                                           #Aumenta a contagem de meteoros em 1
            if c in water:                                              #Se a coluna do meteoro está na lista de colunas com água   
                meteorInWater += 1                                      #Aumenta a contagem de mateoros caindo na água em 1
            dots.append(Dot(l,c))                                    #Adiciona ponto na lista de pontos para desenhar linhas
                
        elif pixel[0] == 1.0 and pixel[1] == 1.0 and pixel[2] == 1.0:#Se for um pixel branco puro
            numStars += 1                                            #Aumenta a contagem de estrelas em 1
            dots.append(Dot(l,c))                                    #Adiciona ponto na lista de pontos para desenhar linhas
        
print("Número de estrelas: " + str(numStars))
print("Número de meteoros: " + str(numMeteor))
print("Número de meteoros que caem na água perpendicularmente: " + str(meteorInWater))

data2 = copy.deepcopy(data)                                                          #Copiando o array da imagem original

for pixel1 in dots:                                                                  #Para cada pixel na lista de pontos
    coord1 = np.array((pixel1.x, pixel1.y))                                          #Pego suas coordenadas

    vizinhoProx = np.array((0,0))                                                    #Crio um vizinho com coordenadas zeradas
    menorDistancia = 9999999999                                                      #A menor distância é um número grande que será substituído logo na primeira iteração

    for pixel2 in dots:                                                              #Para cada pixel na lista de pontos  
        if pixel1 != pixel2 and (pixel2.duplaX != pixel1.x or pixel2.duplaY != pixel1.y):#Se os pixels são diferentes e se pixel2 não tem pixel1 como seu vizinho mais próximo
            coord2 = np.array((pixel2.x, pixel2.y))                                         #Pego as coordenadas dele
            dist = np.linalg.norm(coord1 - coord2)                                          #Calculo a distância euclidiana entre ambos

            if dist < menorDistancia:                                                       #Se a distância for menor que a menor distância até agora
                menorDistancia = dist                                                           #Atualiza a menor distância
                vizinhoProx[0] = coord2[0]                                                      #Atualiza as coordenadas do vizinho mais próximo
                vizinhoProx[1] = coord2[1]

    plotLine(data2, coord1[0], coord1[1], vizinhoProx[0], vizinhoProx[1])            #Pinta o caminho entre os pixels
    pixel1.duplaX = vizinhoProx[0]                                                   #Armazenando as informações do vizinho mais próximo no pixel1 
    pixel1.duplaY = vizinhoProx[1]

pyplot.imshow(data2)
pyplot.show()
