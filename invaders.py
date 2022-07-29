# #space invaders 
# import curses
from contextlib import nullcontext
import time

# # curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
# # curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
# # GREEN =  curses.color_pair(1)
# # RED =  curses.color_pair(2)
# def main(stdscr):
#     while 1:
# 	    key = stdscr.getch()
#         stdscr.clear()
#         stdscr.addstr(player.yPos , player.xPos , "ship[0]")
#         stdscr.addstr(player.yPos , player.xPos , "ship[1]")
#         if key == curses.KEY_UP:
# 	        stdscr.addstr(0, 0, "You pressed Up key!")
# 	    elif key == curses.KEY_DOWN:
# 	        stdscr.addstr(0, 0, "You pressed Down key!")
# 	    elif key == curses.KEY_ENTER or key in [10, 13]:
# 	        stdscr.addstr(0, 0, "You pressed Enter.")
# 	    else:
# 	        break
# 	    stdscr.refresh()
# curses.wrapper(main)

import curses
import math
ship  = ['@@@', 'l l']
class Aliens:
    alien_spawn_count = 4

    array = []
    def print_all(self, stdscr):
        for alien in self.array:
            print(alien.type, alien.posX, alien.posY)
            stdscr.addstr(alien.yPos    , "ggg")
            
class Enemy:
    
    def __init__(self , type,yPos, xPos,vY,vX,hp):
        type = type
        yPos = yPos
        xPos = xPos
        vY = vY
        vX = vX
        hp = hp
    type = 0
    xPos = 0
    yPos = 0
    vY = 0
    vX = 0
    hp = 1


#contains all the enemy methods and objects.
aliens = Aliens


for index in range(aliens.alien_spawn_count):
    aliens.array.append(Enemy(1,5*index,5,0,1,2))
    

class Player:
    xPos = 20
    yPos = 10
    xVelocity = 0
    yVelocity = 0
    def printShip(self, stdscr):
        stdscr.addstr(self.yPos    , player.xPos, ship[0])
        stdscr.addstr(self.yPos + 1, player.xPos, ship[1])
player = Player()

def main(stdscr):
    
    while 1:
        if( player.yPos + int(math.floor(player.yVelocity)) > 0):
            player.yPos += int(math.floor(player.yVelocity))
        if( player.xPos + math.floor(player.xVelocity) > 0):
            player.xPos += int(math.floor(player.xVelocity))
        if(player.xVelocity>0):
            player.xVelocity-=1
        elif(player.xVelocity<0):
            player.xVelocity+=1
        if(player.yVelocity>0):
            player.yVelocity-=1
        elif(player.yVelocity<0):
            player.yVelocity+=1
        time.sleep(0.1)
        stdscr.clear()
        #printPlayer
        player.printShip(stdscr)
        #print aliens
        for index,enemy in enumerate(aliens.array):
            stdscr.addstr(enemy.yPos, enemy.xPos,"alien "+"index" +str(enemy.hp))
            stdscr.addstr(8+index, enemy.xPos,"alien "+"yPos " +str(enemy.yPos))

        stdscr.refresh()
        stdscr.nodelay(True)
        key = stdscr.getch()

        if key == curses.KEY_UP:
            stdscr.addstr(0, 0, "You pressed Up key!  ")
            player.yVelocity = -3
        elif key == curses.KEY_DOWN:
            stdscr.addstr(0, 0, "You pressed Down key!  ")
            player.yVelocity = 3

        elif key == curses.KEY_RIGHT:
            stdscr.addstr(0, 0, "You pressed right key!    ")
            player.xVelocity = 3

        elif key == curses.KEY_LEFT:
            stdscr.addstr(0, 0, "You pressed left key!     ")      
            player.xVelocity =-3

        elif key == 32 :
            stdscr.addstr(0, 0, "You pressed space.     ")  
        elif key == curses.KEY_HOME:
            stdscr.addstr(0, 0, "You pressed home key!  ")
            break
        


curses.wrapper(main)