import random
import pygame
import math
import time 
from copy import deepcopy
class BoxesandGridsGame():
    def __init__(self):
        pass
        #1
        pygame.init()
        pygame.font.init()
        width, height = 389, 489
        #2
        self.hColor=[[0 for x in range(6)] for y in range(7)]
        self.vColor=[[0 for x in range(7)] for y in range(6)]
        #initialize the screen
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Boxes")
        #3
        #initialize pygame clock
        self.clock=pygame.time.Clock()
        self.boardh = [[False for x in range(6)] for y in range(7)]
        self.boardv = [[False for x in range(7)] for y in range(6)]
        self.boardh_temp = self.boardh
        self.boardv_temp = self.boardv
        self.initGraphics();
        self.drawBoard();
        self.hColor=[[0 for x in range(6)] for y in range(7)]
        self.vColor=[[0 for x in range(7)] for y in range(6)]
        
        self.goal_x=6;
        self.goal_y=5;
        self.initial_move=[0,0,0];
        
        
        self.score_player1=0;
        self.score_player2=0;
        
    def update(self):
    #sleep to make the game 60 fps
        self.clock.tick(60)

    #clear the screen
        self.screen.fill(0)
        self.drawBoard()
        self.drawHUD()

        for event in pygame.event.get():
        #quit if the quit button was pressed
            if event.type == pygame.QUIT:
                exit()
        print ('before making a move')
        self.player2();
        print ('move made by player 2')
        self.player1();
        print ('move made by player 1')
        print('\n')
        self.print(self.boardh, self.boardv);
        print('\n')
        
    #update the screen
    
        pygame.display.flip()
    def initGraphics(self):
        self.normallinev=pygame.image.load("normalline.png")
        self.normallineh=pygame.transform.rotate(pygame.image.load("normalline.png"), -90)
        self.bar_donev=pygame.image.load("bar_done.png")
        self.bar_doneh=pygame.transform.rotate(pygame.image.load("bar_done.png"), -90)
        self.bar_donev_r=pygame.image.load("bar_done_red.png")
        self.bar_doneh_r=pygame.transform.rotate(pygame.image.load("bar_done_red.png"), -90)
        self.bar_donev_g=pygame.image.load("bar_done_green.png")
        self.bar_doneh_g=pygame.transform.rotate(pygame.image.load("bar_done_green.png"), -90)
        self.bar_donev_r_l=pygame.image.load("bar_done_light_red.png")
        self.bar_doneh_r_l=pygame.transform.rotate(pygame.image.load("bar_done_light_red.png"), -90)
        self.bar_donev_g_l=pygame.image.load("bar_done_light_green.png")
        self.bar_doneh_g_l=pygame.transform.rotate(pygame.image.load("bar_done_light_green.png"), -90)
        self.hoverlinev=pygame.image.load("hoverline.png")
        self.hoverlineh=pygame.transform.rotate(pygame.image.load("hoverline.png"), -90)
        self.separators=pygame.image.load("separators.png")
        self.redindicator=pygame.image.load("redindicator.png")
        self.greenindicator=pygame.image.load("greenindicator.png")
        self.greenplayer=pygame.image.load("greenplayer.png")
        self.blueplayer=pygame.image.load("blueplayer.png")
        self.winningscreen=pygame.image.load("youwin.png")
        self.gameover=pygame.image.load("gameover.png")
        self.score_panel=pygame.image.load("score_panel.png")
    def drawBoard(self):
        for x in range(6):
            for y in range(7):
                
                if  (self.hColor[y][x]==-1):
                    self.screen.blit(self.bar_doneh_r, [(x)*64+5, (y)*64])
                elif  self.hColor[y][x]==1:
                    self.screen.blit(self.bar_doneh_g, [(x)*64+5, (y)*64])
                else:
                    self.screen.blit(self.bar_doneh, [(x)*64+5, (y)*64])
                    
        for x in range(7):
            for y in range(6):
                
                if  (self.vColor[y][x]==-1):
                    self.screen.blit(self.bar_donev_r, [(x)*64, (y)*64+5])
                elif  self.vColor[y][x]==1:
                    self.screen.blit(self.bar_donev_g, [(x)*64, (y)*64+5])
                else:
                    self.screen.blit(self.bar_donev, [(x)*64, (y)*64+5])
          
                  
        for x in range(7):
            for y in range(7):
                self.screen.blit(self.separators, [x*64, y*64])
                
    def drawHUD(self):
    #draw the background for the bottom:
        self.screen.blit(self.score_panel, [0, 389])
        #create font
        myfont = pygame.font.SysFont(None, 32)

        #create text surface
        label = myfont.render("Player 1:", 1, (255,255,255))

        #draw surface
        self.screen.blit(label, (10, 400))
        #same thing here
        myfont64 = pygame.font.SysFont(None, 64)
        myfont20 = pygame.font.SysFont(None, 20)

        scoreme = myfont64.render(str(self.score_player1), 1, (255,255,255))
        scoreother = myfont64.render(str(self.score_player2), 1, (255,255,255))
        scoretextme = myfont20.render("Player1", 1, (255,255,255))
        scoretextother = myfont20.render("Player2", 1, (255,255,255))
        
        self.screen.blit(scoretextme, (10, 425))
        self.screen.blit(scoreme, (10, 435))
        self.screen.blit(scoretextother, (280, 425))
        self.screen.blit(scoreother, (340, 435))
    def finished(self):
        self.screen.blit(self.winningscreen, (0,0))
        while 1:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
            pygame.display.flip()   
          

    def next_possible_moves(self,move):
        #make the move true if the last move is not true to be true in the psuedo list
        if(move[2]==1):
            self.boardh_temp[move[0]][move[1]]=True;
        elif(move[2]==0):
            self.boardv_temp[move[0]][move[1]]=True;
        else: 
            print ("Invalid move");
        next_moves=[];
        
        for x in range (7):
            for y in range(6):
                if(self.boardh_temp[x][y]==False):
                    next_moves.append([x,y,1]); # append all horizontal moves
                
        for x in range (6):
            for y in range(7):
                if(self.boardv_temp[x][y]==False):
                    next_moves.append([x,y,0]); # append all horizontal moves
        
                
        return next_moves 
    def list_possible_moves(self,state_h,state_v):
        #make the move true if the last move is not true to be true in the psuedo list
        
        next_moves=[];
        for x in range (7):
            for y in range(6):
                if(state_h[x][y]==False):
                    next_moves.append([x,y,1]); # append all horizontal moves
                
                
                
        for x in range (6):
            for y in range(7):
                if(state_v[x][y]==False):
                    next_moves.append([x,y,0]); # append all horizontal moves
                
        
                
        return next_moves
    def current_state(self):
        return self.boardh,self.boardv
    
    def increment_score(self,move,h_matrix,v_matrix):
        temp_score=0;
        xpos=move[0];
        ypos=move[1];
        if(move[2]==0): # vertical matrices
            if(ypos==0):# left most edge
                if(h_matrix[xpos][ypos]==True and h_matrix[xpos+1][ypos]==True and v_matrix[xpos][ypos+1]==True):
                    temp_score=1;
            elif(ypos==6):# left most edge   
                if(h_matrix[xpos][ypos-1]==True and h_matrix[xpos+1][ypos-1]==True and v_matrix[xpos][ypos-1]==True):
                    temp_score=1;     
            else:
                if(h_matrix[xpos][ypos]==True and h_matrix[xpos+1][ypos]==True and v_matrix[xpos][ypos+1]==True):
                    temp_score=temp_score+1;
                if(h_matrix[xpos][ypos-1]==True and h_matrix[xpos+1][ypos-1]==True and v_matrix[xpos][ypos-1]==True):
                    temp_score=temp_score+1;
                    
        if(move[2]==1): # horizontal matrices
            if(xpos==0):
                if(v_matrix[xpos][ypos]==True and v_matrix[xpos][ypos+1]==True and h_matrix[xpos+1][ypos]==True):
                    temp_score=1;
            elif(xpos==6):
                if(v_matrix[xpos-1][ypos]==True and v_matrix[xpos-1][ypos+1]==True and h_matrix[xpos-1][ypos]==True):
                    temp_score=1;
                
            else:
                if(v_matrix[xpos][ypos]==True and v_matrix[xpos][ypos+1]==True and h_matrix[xpos+1][ypos]==True):
                    temp_score=temp_score+1;
                if(v_matrix[xpos-1][ypos]==True and v_matrix[xpos-1][ypos+1]==True and h_matrix[xpos-1][ypos]==True):
                    temp_score=temp_score+1;
                
                
            
        return temp_score;
    def make_move(self,move,player_id):
        #print ('value before coming',self.boardh)
        xpos=move[0];
        ypos=move[1];
        #print xpos,ypos
        if(move[2]==1):# Vertical Matrices
            
            self.boardh[xpos][ypos]=True;
            
        if(move[2]==0):
            self.boardv[xpos][ypos]=True;
        self.boardh_temp = self.boardh
        self.boardv_temp = self.boardv
        #score=self.increment_score(move,self.boardh,self.boardv);
        #print self.boardh,self.boardv
        ### Leave space here for player color change 
        
        
        if(player_id==0):
            self.score_player1=self.score_player1+self.increment_score(move,self.boardh,self.boardv);
            if(move[2]==1):
                self.hColor[xpos][ypos]=-1;
            if(move[2]==0):
                print (xpos,ypos)
                self.vColor[xpos][ypos]=-1;
            
        if(player_id==1):
            self.score_player2=self.score_player2+self.increment_score(move,self.boardh,self.boardv);
            if(move[2]==1):
                self.hColor[xpos][ypos]=1;
            if(move[2]==0):
                self.vColor[xpos][ypos]=1;
    def next_state(self,move,h1,v1):
        xpos=move[0];
        ypos=move[1];
        h_matrix1=deepcopy(list(h1))
        v_matrix1=deepcopy(list(v1))
        
        
        score=self.increment_score(move,h_matrix1,v_matrix1);
        #print move[2];
        if(move[2]==0):#vetical matrices
            
            v_matrix1[xpos][ypos]=True;
            
            #self.boardv[xpos][ypos]=False
        if(move[2]==1):#horizontal matrices
            
            h_matrix1[xpos][ypos]=True;
            
            #self.boardh[xpos][ypos]=False
        #print move ,h_matrix,v_matrix
        return h_matrix1,v_matrix1,score;
    def game_ends(self,temp_h,temp_v):
        count=True;
        for x in range(6):
            for y in range(7):
                if not temp_h[y][x]:
                    count=False;
        for x in range(7):
            for y in range(6):
                if not temp_v[y][x]:
                    count=False;
        return count;
    
    def player1(self):
        temp_h=self.boardh
        temp_v=self.boardv

        depth = 3
        '''
        possible_moves = self.list_possible_moves(self.boardh, self.boardv)
        if len(possible_moves) <= 45:
            depth = depth + 1

        if len(possible_moves)  <= 36:
            depth = depth + 1
        
        if len(possible_moves) <= 22:
            depth = depth + 1


        if len(possible_moves) <= 12:
            depth = depth + 1

        if len(possible_moves) <= 10:
            depth = 10
        '''
        '''
        next_move=self.list_possible_moves(temp_h,temp_v);
        best_move=next_move[0];
        best_score=0;
        
        for move in next_move:
            
            temp_h,temp_v,score=self.next_state(move,temp_h,temp_v);
            
            if(score>best_score):
                best_score=score;
                best_move=move;
        '''        

        best_move = self.minimax(self.boardh,self.boardv,depth)
        
        self.make_move(best_move,0);
        
    '''
    You will make changes to the code from this part onwards
    '''
    def player2(self):
        time1 = time.time()
        temp_h=self.boardh
        temp_v=self.boardv
        '''
        Call the minimax/alpha-beta pruning  function to return the optimal move
        '''
        
        ## change the next line of minimax/ aplpha-beta pruning according to your input and output requirments
        possible_moves = self.list_possible_moves(self.boardh, self.boardv)
        depth = 3

        
        if len(possible_moves) <= 45:
            depth = depth + 1

        if len(possible_moves)  <= 36:
            depth = depth + 1
        
        if len(possible_moves) <= 22:
            depth = depth + 1

        if len(possible_moves) <= 12:
            depth = depth + 1

        if len(possible_moves) <= 10:
            depth = 10
        
             
        next_move=self.minimax(self.boardh,self.boardv,depth)
        self.make_move(next_move,1);
        time2 = time.time()
        print('%s function took %0.3f secs' % ("Minimax", (time2-time1)))
        print("Depth           ", depth)
        print("Lenght of possible moves      ", len(possible_moves))
        #next_move_alpha=self.alphabetapruning();
        
        
        
        
        print ('move_made by player 2',next_move)
        
    '''
    Write down the code for minimax to a certain depth do no implement minimax all the way to the final state. 
    '''

     # You will implement the minimax algorithm in this function. You can change the 
     # number of input parameters of the function and the output of the function must 
     # be the optimal move made by the function.

    def minimax(self,horizontal,vertical,depth):
        alpha = -math.inf
        beta = math.inf
        next_score = 0
        v, best_move = self.max_value(horizontal, vertical,alpha,beta,depth, next_score)
        #print("V ", v)
        print("Best move ", best_move)
        return best_move

    def min_value(self, horizontal, vertical,alpha, beta,depth, score):
        if depth == 0 or self.game_ends(horizontal,vertical):
            return  self.evaluate(horizontal,vertical,score,False), [0,0,0]
        v = math.inf
        #best_horizontal = []
        #best_vertical = []
        best_move = []
        
        possible_moves = self.list_possible_moves(horizontal, vertical)

        #sort the values based on score 
        temp_list = []
        score_list = []
        for move in possible_moves:
            h_matrix, v_matrix, next_score = self.next_state(move,horizontal,vertical)
            temp_tuple = [h_matrix, v_matrix, next_score,move]
            temp_list.append(temp_tuple)
            score_list.append((next_score,move))
            

        sorted_possible_moves = sorted(temp_list, key=lambda s : s[2], reverse = True)
        sorted_scores = sorted(score_list,key=lambda s:s[0], reverse = True)
        #print("Min Sorted Scores ",sorted_scores )


        for move_tuple in sorted_possible_moves:
            move = move_tuple[3]
            next_score = move_tuple[2]
            h_matrix = move_tuple[0]
            v_matrix = move_tuple[1]
            

            #h_matrix, v_matrix, next_score = self.next_state(move,horizontal,vertical)
            v_prime, previous_move = self.max_value(h_matrix, v_matrix, alpha, beta, depth-1, score - next_score)
            if v_prime < v:
                v = v_prime
                #best_horizontal = horizontal_prime
                #best_vertical = vertical_prime
                best_move = move
            if v_prime <= alpha:
                #print("Min : Alpha pruning")
                #print("Alpha ", alpha , "   Beta ", beta , "   Value Prime ", v_prime, "   Depth ", depth)
                
                return v, best_move
            if v_prime < beta:
                beta = v_prime
        
        return  v, best_move

    def max_value(self, horizontal,vertical,alpha,beta,depth, score):
        if depth == 0 or self.game_ends(horizontal,vertical):
            return self.evaluate(horizontal,vertical, score,True), [0,0,0]
        
        v = -math.inf
        possible_moves = self.list_possible_moves(horizontal,vertical)
        #best_horizontal = []
        #best_vertical = []

        
        temp_list = []
        for move in possible_moves:
            h_matrix, v_matrix, next_score = self.next_state(move,horizontal,vertical)
            temp_tuple = [h_matrix, v_matrix, next_score,move]
            temp_list.append(temp_tuple)

        sorted_possible_moves = sorted(temp_list, key=lambda s : s[2], reverse = True)


        for move_tuple in sorted_possible_moves:
            move = move_tuple[3]
            next_score = move_tuple[2]
            h_matrix = move_tuple[0]
            v_matrix = move_tuple[1]

            v_prime ,previous_move = self.min_value(h_matrix,v_matrix,alpha,beta,depth-1, next_score + score)
            if v_prime > v:
                v = v_prime
                #best_horizontal = horizontal_prime
                #best_vertical = vertical_prime
                best_move = move
            if v_prime >= beta:
                #print("Max : Beta pruning")
                #print("Alpha ", alpha , "   Beta ", beta , "   Value Prime", v_prime, "   Depth ", depth)
                
                return  v, best_move
            if v_prime > alpha:
                alpha = v_prime
            
        return  v, best_move


    


       
    '''
    Write down you own evaluation strategy in the evaluation function 
    '''
    def evaluate(self,horizontal,vertical, score,isMax):
        possible_moves = self.list_possible_moves(horizontal,vertical)
        #constant 3 is added so that we dont multiply by zero
        total_moves = len(possible_moves) + 10
        total_score = 0
        

        
        next_score = 0
        for move in possible_moves:
            temp_score = self.increment_score(move, horizontal,vertical)
            if temp_score > next_score:
                next_score = temp_score
           
        if isMax:
            score = score + next_score
        else:
            score = score - next_score
              

        if score == 0:
            total_score = random.randint(-total_moves//2 , total_moves//2)
        else:
            total_score =  (total_moves * score) + random.randint(-total_moves//10 , total_moves//10 )

        
        #print("Evaluate Score ", total_score)
        return total_score

    def print(self, horizontal,vertical):

        for row in range(len(horizontal)):
            line = "     *"
            #print(h_row)
            for seg in horizontal[row]:
                if seg:
                    line = line + "--"
                else:
                    line = line + "  "
                line = line + "*"

            line = line + "\n"
            
            line = line + "     "
            if(row <= len(vertical) - 1):
                
                for seg in range(len(vertical[row])):
                    
                    if vertical[row][seg]:
                        line = line + "|"
                    else:
                        line = line + " "
                    line = line + "  "
            print(line)
    

 
bg=BoxesandGridsGame();
while (bg.game_ends(bg.boardh,bg.boardv)==False):
    bg.update();
    print ('Player1 :score',bg.score_player1)
    print ('Player2 :score',bg.score_player2)
    time.sleep(2)
time.sleep(10)
pygame.quit()
