# #space invaders 
# import curses
import time
import curses
from curses import wrapper
import math
window_width  = 80
window_height = 40
message_pad_height =3
message_pad_width = window_width

ship  = ['@@@@@', 'l   l']
class Aliens:
    alien_spawn_count = 4

    array = []
    def print_all(self, window):
        for enemy in self.array:
            enemy.printEnemy(window)
            
class Enemy:
    def __init__(self , yPos=0, xPos=0,yV=0,xV=0,hp=0,type=1):
        self.type = type
        self.yPos = yPos
        self.xPos = xPos
        self.vY = yV
        self.vX = xV
        self.hp = hp
        self.color_id = 2

    def printEnemy(self, window):
        for count in range(self.type):
            if(self.yPos-count>=0):
                window.addstr(math.floor(self.yPos)-count, math.floor(self.xPos), "#"*self.type ,curses.color_pair(self.color_id)  )

        
        # window.addstr(math.floor(self.yPos), math.floor(self.xPos), "#"*self.type )
        # if(self.yPos-1>=0):
        #     window.addstr(math.floor(self.yPos)-1, math.floor(self.xPos),"#"*self.type +str(vars(self)))
        #     if(self.yPos-2>=0):
        #         window.addstr(math.floor(self.yPos)-2, math.floor(self.xPos),"#"*self.type +str(vars(self)))
    def hit(self,damage):
        self.hp -= damage
        self.color_id =3
        if(self.hp <= 0):
            return True
        else:
            return False
            #add delete me
class player_missile:
    def __init__(self, yPos ,xPos, vY,vX, missile_tier):
        self.yPos =yPos
        self.xPos =xPos
        self.vY   =vY
        self.vX   =vX
        self.missile_tier = missile_tier
        self.missile_char = "|"
    def print_missile(self, window):
        window.addstr(math.floor(self.yPos), math.floor(self.xPos), self.missile_char)
    def load_movement_return_kill(self):
        self.xPos +=self.vX
        if(self.yPos>0):
            self.yPos +=self.vY
            return False
        else:
            return True
    def collision_detection(self, aliens):
        for enemy in aliens.array:
            if( enemy.yPos - self.yPos - 2 < enemy.type and enemy.yPos - self.yPos >=0   and   self.xPos - enemy.xPos - 2 < enemy.type and self.xPos - enemy.xPos >=0 ):
                return enemy
#contains all the enemy methods and objects.
aliens = Aliens



    

class Player:
    xPos = 35
    yPos = 35
    xVelocity = 0
    yVelocity = 0
    missile_array = []
    missile_tier=1
    max_ammo = 8
    ammo =max_ammo
    score=0
    def printShip(self, game_win):
        game_win.addstr(self.yPos    , player.xPos, ship[0])
        game_win.addstr(self.yPos + 1, player.xPos, ship[1])
    def add_missile(self, playerMissile):
        self.missile_array.append(playerMissile)

def  zero_level():
    for index in range(1):
        yPos = 6*index
        xPos = 5
        yV = 0.2
        xV = 1
        hp = 2
        type = 8
        aliens.array.append(Enemy(int(yPos), int(xPos), yV, xV, hp, type))

def  first_level():
    for index in range(4):
        yPos = 6*index
        xPos = 5
        yV = 0.2
        xV = 1
        hp = 2
        type = 5
        aliens.array.append(Enemy(int(yPos), int(xPos), yV, xV, hp, type))
def  second_level():
    for index in range(6):
        yPos = 6
        xPos = 5*index
        yV = 0.2
        xV = 0.4
        hp = 1
        type = 5
        aliens.array.append(Enemy(int(yPos), int(xPos), yV, xV, hp, type))
def  end_screen(message_pad):
    import requests
    import webbrowser
    message_pad.addstr(0, 0, "LEVEL CLEARED!  " )
    name="python"
    end_score = player.score
    # end_score = 2001
    
    
    # resp = requests.post("https://invaders-page.herokuapp.com/")
    url = 'https://invaders-page.herokuapp.com/scores'
    payload = {
            'name': name,
            'score': end_score
    }
    
    # response = requests.post(url, json = payload)
    requests.post(url, json = payload)
    webbrowser.open('https://invaders-page.herokuapp.com/')

    
    # url = 'https://'
    # response = requests.post(url, data=payload, verify=False)
player = Player()
levels_array = []
levels_array.append(zero_level)
levels_array.append(first_level)
levels_array.append(second_level)
levels_array.append(end_screen)
print(len(levels_array))
time.sleep(1)
def main(stdscr):
    stdscr.clear()


    
    game_win = curses.newwin(window_height, window_width, 3, 0)
    message_pad = curses.newpad(message_pad_height, message_pad_width)
    curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLUE)
    curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(4, curses.COLOR_RED, curses.COLOR_WHITE)
    game_running= True
    stdscr.bkgd(' ', curses.color_pair(1))
    levels_array.pop(0)()

    while 1:
        if(not game_running):
            time.sleep(4)
            break
        time.sleep(0.1)
        game_win.clear()
        message_pad.clear()
        game_win.bkgd(' ', curses.color_pair(2))
        message_pad.bkgd(' ', curses.color_pair(2))
        message_pad.addstr(0, 40, f"SCORE:{player.score}  " )

        if(len(aliens.array)==0):
            message_pad.clear()
            
            message_pad.addstr(0, 0, "LEVEL CLEARED!  " )
            message_pad.addstr(0, 40, f"SCORE:{player.score}  " )

            message_pad.refresh( 0,0, 0, 0, 4, window_width)
            time.sleep(2)
            if(len(levels_array)>1):
                message_pad.clear()
                message_pad.addstr(0, 0, "STARTING NEXT LEVEL   " )
                message_pad.addstr(0, 40, f"SCORE:{player.score}  " )

                levels_array.pop(0)()
            else:
                message_pad.clear()

                message_pad.addstr(0, 0, f"you WON!, Your SCORE is  : {player.score}  " )

                game_running = False
            message_pad.refresh( 0,0, 0, 0, 4, window_width)

            time.sleep(2)
        elif():
            #execute command for next level
            levels_array.pop()()
            message_pad.clear()

        # game_win.addstr(0, 0,"?>"*999 )

        if(player.yVelocity<0 and player.yPos + int(math.floor(player.yVelocity)) > 0):
            player.yPos += int(math.floor(player.yVelocity))
        elif(player.yVelocity >0 and player.xPos + math.floor(player.yVelocity) < window_height):
            player.yPos += int(math.floor(player.yVelocity))
        if(player.xVelocity<0 and player.xPos + math.floor(player.xVelocity) > 0):
            player.xPos += int(math.floor(player.xVelocity))
        elif(player.xVelocity > 0 and  player.xPos + math.floor(player.xVelocity) < window_width - len(ship[0])):
            player.xPos += int(math.floor(player.xVelocity))

        if(player.xVelocity>0):
            player.xVelocity-=1
        elif(player.xVelocity<0):
            player.xVelocity+=1
        if(player.yVelocity>0):
            player.yVelocity-=1
        elif(player.yVelocity<0):
            player.yVelocity+=1
        #printPlayer
        player.printShip(game_win)
        #todo: print aliens 
        # aliens.print_all(game_win)
        for index,enemy in enumerate(aliens.array):
            enemy.printEnemy(game_win)
            # if(enemy.yPos-1>=0):
            #     game_win.addstr(math.floor(enemy.yPos)-1, math.floor(enemy.xPos),"##" +str(vars(enemy)))
            game_win.addstr(0,60, f"{enemy.vY} , {str(math.ceil(enemy.vY))}" )

            if(enemy.vY<0 and enemy.yPos + int(math.ceil(enemy.vY)) >= 0):
                enemy.yPos += enemy.vY

            elif(enemy.vY >0 and enemy.yPos + math.ceil(enemy.vY) < window_height):
                enemy.yPos += enemy.vY
            if(enemy.vX<0):
                if(enemy.xPos + math.ceil(enemy.vX) > 0):
                    enemy.xPos += enemy.vX
                else:
                    enemy.vX *= -1
            elif(enemy.vX > 0):
                if( enemy.xPos + math.ceil(enemy.vX) < window_width - enemy.type-1):
                    enemy.xPos += enemy.vX
                else:
                    enemy.vX *= -1
            # enemy.yPos += enemy.vY
            # enemy.xPos += enemy.vX
            if(enemy.yPos>= player.yPos):
                enemy.vY = 0
                game_win.addstr(0, 30, "you lost!" )
                game_running = False

            # stdscr.addstr(8+index, enemy.xPos,"alien "+"yPos " +str(enemy.yPos))

        #print all the missiles
        for missile in player.missile_array:
            missile.print_missile(game_win)
            target = missile.collision_detection(aliens)
            if target:
                # game_win.addstr(0, 40, "hit!" )
                kil_enemy = target.hit(missile.missile_tier)
                if kil_enemy:
                    player.score += (10-target.type)*100  
                    message_pad.addstr(0, 20, f"+{player.score}" )
                    # game_win.addstr(2, 40, "kill me!" )
                    aliens.array.remove(target)
                player.missile_array.remove(missile)
                player.ammo +=1

            else:
                 kill_missile = missile.load_movement_return_kill()
                 if kill_missile:
                    player.missile_array.remove(missile)
                    player.ammo +=1
        
        #display player ammo on screen
        game_win.addstr(0, 2, f"AMMO : {player.ammo}/{player.max_ammo}" )
        
        game_win.refresh()

        stdscr.nodelay(True)
        key = stdscr.getch()

        if key == curses.KEY_UP:
            game_win.addstr(0, 0, "You pressed Up key!  ")
            player.yVelocity = -3
        elif key == curses.KEY_DOWN:
            game_win.addstr(0, 0, "You pressed Down key!  ")
            player.yVelocity = 3

        elif key == curses.KEY_RIGHT:
            game_win.addstr(0, 0, "You pressed right key!    ")
            player.xVelocity = 3

        elif key == curses.KEY_LEFT:
            game_win.addstr(0, 0, "You pressed left key!     ")      
            player.xVelocity =-3

        elif key == 32 :
            game_win.addstr(0, 0, "You pressed space.     , shoot missile")  
            # check if I have ammo -
            if( player.ammo > 0):
                #create new missile object
                new_missile = player_missile(player.yPos   ,player.xPos + math.floor(len(ship[0])/2) ,-1,0 , player.missile_tier)
                player.add_missile(new_missile)
                player.ammo-=1


        elif key == curses.KEY_HOME:
            game_win.addstr(0, 0, "You pressed home key!  ")
            break
        message_pad.refresh( 0,0, 0, 0, 4, window_width)
        


wrapper(main)