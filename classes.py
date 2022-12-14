import time
import curses
from curses import wrapper
import math
import requests
import webbrowser
import random
window_width  = 300
window_height = 40
message_pad_height =3
message_pad_width = window_width
ship  = ['@@@@@@@', 'l     l']
delta_time =0.02

class Aliens:
    alien_spawn_count = 4
    enemy_missiles= [] # contains an array of Enemy_missile objects
    array = []
    missile_speeds = [0.2, 0.25,0.3, 0.35, 0.4]
    def print_all(self, window):
        for enemy in self.array:
            enemy.printEnemy(window)
        
class Enemy:
    def __init__(self , yPos=0, xPos=0,yV=0,xV=0,hp=0,type=1,shoot_timer=4,timer_counter=0):
        self.type = type
        self.yPos = yPos
        self.xPos = xPos
        self.vY = yV
        self.vX = xV
        self.hp = hp
        self.color_id = 2
        self.shoot_timer = shoot_timer
        self.timer_counter = timer_counter
    def printEnemy(self, window):
        for count in range(self.type):
            if(window_height>=self.yPos-count>=0 and window_width-1>self.xPos >=0):
                window.addstr(math.floor(self.yPos)-count, math.floor(self.xPos), "#"*self.type ,curses.color_pair(self.color_id)  )
    


        
        # window.addstr(math.floor(self.yPos), math.floor(self.xPos), "#"*self.type )
        # if(self.yPos-1>=0):
        #     window.addstr(math.floor(self.yPos)-1, math.floor(self.xPos),"#"*self.type +str(vars(self)))
        #     if(self.yPos-2>=0):
        #         window.addstr(math.floor(self.yPos)-2, math.floor(self.xPos),"#"*self.type +str(vars(self)))
    def hit(self,char):
        damage=(["'",'*','!',"^", "|", "O", "@", "A"].index(char)+1)*1.3
        
        self.hp -= damage
        self.color_id =3
        if(self.hp <= 0):
            return True
        else:
            return False
        
class Player_missile:
    def __init__(self, yPos ,xPos, vY,vX, missile_char,color_id =2):
        self.yPos =yPos
        self.xPos =xPos
        self.vY   =vY
        self.vX   =vX
        self.missile_char = missile_char
        self.color_id = color_id  
    def print_missile(self, window):
        if(math.floor(self.yPos)>=0 and
         math.floor(self.xPos)>=0 and
         math.floor(self.xPos)< window_width):
            window.addstr(math.floor(self.yPos), math.floor(self.xPos), self.missile_char, curses.color_pair(self.color_id))
    def load_movement_return_kill(self):
        self.xPos +=self.vX
        if(self.yPos>0):
            self.yPos +=self.vY
            return False
        else:
            return True
    def collision_detection(self, aliens):
        for enemy in aliens.array:
            if( enemy.yPos - self.yPos - 2 < enemy.type 
            and enemy.yPos - self.yPos >=0   
            and self.xPos - enemy.xPos < enemy.type -1
            and self.xPos - enemy.xPos >=0 ):
                return enemy

class Enemy_missile:
    def __init__(self, yPos ,xPos, vY,vX, missile_char, color_id=5):
        self.yPos =yPos
        self.xPos =xPos
        self.vY   =vY
        self.vX   =vX
        self.color_id = color_id
        self.missile_char = missile_char
    def print_missile(self, window):
        if(math.floor(self.yPos)>=0 and
         math.floor(self.xPos)>=0 and
         math.floor(self.xPos)< window_width):
            window.addstr(math.floor(self.yPos), math.floor(self.xPos), self.missile_char,curses.color_pair(self.color_id))
    def load_movement_return_kill(self):
        self.xPos +=self.vX
        if(self.yPos>0 and self.yPos<window_height-1):
            self.yPos +=self.vY
            return False
        else:
            return True
    def collision_detection(self, player):
        if(len(ship[0]) > player.xPos- self.xPos >=0 
        and -1<=self.yPos - player.xPos <=0 ):
            return True
        return False


class Items:
    array = []
    size_dictionary = {"missile_upgrade": {'size':2, 'char': "+"},
     "ammo_up" : {'size':3, 'char': "!"} ,
      "coin" : {'size':1, 'char':'$'},
      "extra_missiles":{'size':1, 'char': '??'}}
    def __init__(self):
        self.array = []
    def print_all(self, window):
        for item in self.array:
            item.print_item(window, self.size_dictionary)
items = Items()

class Item:
    def __init__(self, yPos, xPos, vY, vX, type, size):
        self.yPos =yPos
        self.xPos =xPos
        self.vY   =vY
        self.vX   =vX
        self.type =type
        if(type=="missile_upgrade"):
            self.color_id =1
        else:
            self.color_id =4
        self.item_size = size

    def print_item(self, window, dictionary):
        for count in range(self.item_size):
            if(self.yPos-count >= 0 and self.yPos < window_height 
            and self.xPos < window_width and self.xPos > 0):
                window.addstr(math.floor(self.yPos)-count, math.floor(self.xPos), items.size_dictionary[self.type]["char"]*self.item_size ,curses.color_pair(self.color_id)  )
            # if(self.yPos-self.item_size>=0 and self.yPos < window_height 
            # and self.xPos>=0 and self.xPos < window_height):
            #     window.addstr(math.floor(self.yPos)-count, math.floor(self.xPos), "?"*self.item_size ,curses.color_pair(self.color_id)  )

class Player:
    def __init__(self):
        self.missile_vY=-1
        self.missile_vX=0
    xPos = 35
    yPos = 35
    xVelocity = 0
    yVelocity = 0
    missile_array = []
    max_ammo = 4
    ammo =max_ammo
    score=0
    missile_count =1
    missle_vX_array_odd_number =[0,-0.2,0.2, -0.35 , 0.35, -0.5,0.5]
    missle_vX_array_even_number =[-0.15 , 0.15, -0.3 , 0.3, -0.42, 0.42]
    missile_char ="'"
    upgrade_array = ['*','!',"^", "|", "O", "@", "A"]
    def printShip(self, game_win):
        game_win.addstr(round(self.yPos)    , round(self.xPos), ship[0])
        game_win.addstr(self.yPos + 1, self.xPos, ship[1])
    def add_missile(self, playerMissile):
        self.missile_array.append(playerMissile)
