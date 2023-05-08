##MICAEL CADETE

from random import randrange 
import os 

#Função do quadro de jogo
def quadro(board):
    print("+-------" * 3, sep="") #*3 = escrever tal string 3 vezes e separar com espaço em branco 
    for linha in range(3):
       print("|       " * 3, "|", sep="")
       for coluna in range(3):
           print("|    " + str(board[linha][coluna]) + "  ", end="")
       print("|")
       print("|       " * 3, "|", sep="")
       print("+-------" * 3, "+", sep="")

##Função de nova jogada 
def jogada(board):
    ok = False
    while not ok:
        movimento = input("Digite seu movimento: ")
        ok = len(movimento) == 1 and movimento >=  '1' and movimento <= '9' #Esta linha verifica se o número inserido pelo jogador tem apenas 1 caracter, e se ele é um num entre 1 e 9, se estiver tudo certo, ok recebe True 
        if not ok:
            print("O número inserido não é válido!!")
            print("Por favor, repita seu movimento: ")
            continue
        movimento = int(movimento) - 1 #Pq o usuario vai ver a posição de jogada de 1 a 9 // mas o vetor vai de 0 a 8 
        linha = movimento // 3 # identificar a linha do quadrado que o jogador deseja jogar 
        coluna = movimento % 3 # identifcar a coluna do quadrado que o jogador desja jogar 
        verificacao = board[linha][coluna] # parte da verificação se o quadrado selecionado pelo jogador está disponível 
        ok = verificacao not in ['O', 'X'] # se naõ tiver nem 'O' e nem ´X', então o quadrado está disponível e vai retornar True para o Ok 
        if not ok: 
            print("Quadrado já ocupado!")
            print("Por favor, repita seu movimento: ")
            continue
        board[linha][coluna] = 'O' # Só chega nessa linha se OK == "True", e issó só acontecerá se estiver tudo certo, caso contrário, vai repetir o loop
                                   # Esta linha faz a jogada do usuário e coloca a bolinha no quadrado desejado 

#Função para ver quais quadrados estão livres para novas jogadas
def quadrados_livres(board):
    quad_livre = [] ## Criação de lista/Vetor que vai guardar os quadrados livres
    for linha in range(3):
        for coluna in range(3):
            if board[linha][coluna] not in ['O', 'X']: # se no quadrado daquela linha e coluna não tiver nem 'O' e nem ´X', então ele ta livre
                quad_livre.append((linha, coluna)) # se ele ta livre, então esse quadrado vai pra lista de quadrados livres
    return quad_livre # retorna os quadrados livres

#Função para verificar vencedor do game
def vencendor(board, player):
    #If para verificar qual é o jogador, se é o usuário ou a máquina 
    if player == 'X':
        who = 'computador'
    elif player == 'O':
        who = 'usuário'
    else:
        who = None #erro    
    dg1 = True # diagonal 1 
    dg2 = True # diagonal 2 
    for i in range(3):
        if board[i][0] == player and board[i][1] == player and board[i][2] == player: #verfica se todos os quadrados daquela linha pertence ao mesmo jogador
            return who
        if board[0][i] == player and board[1][i] == player and board[2][i] == player: #verfica se todos os quadrados daquela coluna pertence ao mesmo jogador
            return who
        if board[i][i] != player: #verifica se os quadrados  estão preenchidos pelo mesmo jogador
            dg1 = False
        if board[2 - i][2 - i] != player: #verifica se os quadrados estão preenchidos pelo mesmo jogador
            dg2 = False
    if dg1 or dg2:
        return who
    return None ## so não vai retornar o vencedor se dg 1 e 2 forem False, e isso só acontecerá se não tiver quadrados da mesma linha/coluna preenchidos pelo mesmo jogador

#Função para fazer a jogada do computador
def comp_jogada(board):
    quad_livre = quadrados_livres(board) #saber quais os quadrados estão livres para jogar
    i = len(quad_livre) # meu contador vai ser do tamanho da lista de quadrados livres
    if i > 0: # se a lista não tiver vazia, continue... A lista só estará vazia se não tiver mais quadrados para jogar
        posicao = randrange(i) #variavel de aleatoriedade
        linha, coluna = quad_livre[posicao] #vai escolher aleatoriamente uma linha e uma coluna disponivel para jogar
        board[linha][coluna] = 'X' #vai jogar o 'X' no qadrante escolhido

#METODO MAIN 
jogar = int('1')
while jogar != '2':
    board = [[3 * j + i + 1 for i in range(3)]for j in range(3)] ## criar um quadro vazio
    board[1][1] = 'X' # faz a primeira jogada, o X no meio 
    quad_livre = quadrados_livres(board) #chama a função que vai ver os quadrados disponiveis
    vez_do_usuario = True #durante o loop vai verificar de quem é a vez de jogar

    while len(quad_livre): # enquanto tiver quadrados livres, tem jogo!
        quadro(board) # chama o quadro do jogo 
        if vez_do_usuario: # se for a vez do usuario, entra a jogada do usuario 
            jogada(board)
            vitoria = vencendor(board, 'O')
        else: # se não for a vez do usuario, o computador faz a sua jogada
            comp_jogada(board)
            vitoria = vencendor(board, 'X')
        if vitoria != None:
            break
        vez_do_usuario = not vez_do_usuario # Inverte a vez/jogador da proxima rodada
        quad_livre = quadrados_livres(board)#atualiza a lista dos quadrados livres 
        

    quadro(board)
    if vitoria == 'usuário':
        print("Parabéns!! você venceu o jogo...")
    elif vitoria == 'computador':
        print("Não foi dessa vez! Eu venci o jogo...")
    else:
        print("Deu velha!")

    print("Deseja jogar novamente? ")    
    print("[1] SIM")
    print("[2] NÃO")
    jogar = input((""))