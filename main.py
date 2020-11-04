import sys
import numpy as np
import pygame
import math

pygame.init()
ROW = 6
COLUM = 7

def create_board():
    board = np.zeros((ROW,COLUM))
    return board

def mutare_posibila(j,board):
    if(board[ROW-1][j]==0):
        return True

def mutare(player,i,j,board ):
    board[i][j]=player

def urm_poz(j,board):
    for i in range(ROW):
        if(board[i][j]==0):
            return i

def verificare_col(i,j,board):
    count = 0
    number1 = 0
    number2 = 0
    for x in range(4):
        if(i+x<ROW and board[i+x][j]!=0):
            if(board[i+x][j]==1):
                number1+=1
                count+=1
            else :
                number2+=1
                count+=1
    if(count!=4) :
        return 0
    if(number1==4) :
        return 1
    if(number2==4) :
        return 2
    return 0

def verificare_linie(i,j,board):
    count = 0
    number1 = 0
    number2 = 0
    for x in range(4):
        if(j+x<COLUM and board[i][j+x]!=0):
            if(board[x][j+x]==1):
                number1+=1
                count+=1
            else :
                number2+=1
                count+=1
    if(count!=4) :
        return 0
    if(number1==4) :
        return 1
    if(number2==4) :
        return 2
    return 0

def verificare_diag(i,j,board):
    count = 0
    number1 = 0
    number2 = 0
    for x in range(4):
        if(i+x<ROW and j+x<COLUM and board[i+x][j+x]!=0):
            if(board[i+x][j+x]==1):
                number1+=1
                count+=1
            else :
                number2+=1
                count+=1

    if(count!=4) :
        return 0
    if(number1==4) :
        return 1
    if(number2==4) :
        return 2
    return 0

def verificare(i,j,board):
    c=verificare_col(i,j,board)
    l=verificare_linie(i,j,board)
    d=verificare_diag(i,j,board)
    if(c) :
        return c

    if(l):
        return l
    if(d) :
        return d
    return 0

def verif_castig(board):
    for i in range(ROW):
        for j in range(COLUM):
            x = verificare(i,j,board)
            if(x):
                return x
    return 0

def draw_board(board) :
    pass

def game4():
    DIM=100
    lungime = COLUM * DIM
    inaltime= ROW* DIM
    size = (lungime,inaltime)
    #screen = pygame.display.set_mode(size)
    board = create_board()
    tura = 0
    joc_terminat = 0
    while not joc_terminat:
        """
        for event in pygame.event.get():
            if( event.type == pygame.QUIT ) :
                sys.exit()

            if(event.type == pygame.MOUSEBUTTONDOWN) :
                print("merge")
        """
        if (tura == 0):
            j = int(input("P1 : "))
            j -= 1
            if (mutare_posibila(j, board)):
                mutare(1, urm_poz(j, board), j, board)
        else:
            j = int(input("P2 : "))
            j -= 1
            if (mutare_posibila(j, board)):
                mutare(2, urm_poz(j, board), j, board)
        
        print(np.flip(board, 0))
        castigator = verif_castig(board)

        if (castigator):
            print("Castigatorul este " + str(castigator))
            joc_terminat = 1
        tura += 1
        tura = tura % 2



if __name__ == '__main__':
    pygame.init()
    game4()
    