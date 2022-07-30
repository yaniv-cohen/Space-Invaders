# #space invaders 
# import curses
import time
import curses
from curses import wrapper
import math
import requests
import webbrowser
import random
from classes import *
# from levels import *
window_width  = 80
window_height = 40
message_pad_height =3
message_pad_width = window_width

  
            #add delete me
#contains all the enemy methods and objects.
aliens = Aliens

items = Items()

def  level_0():
    alien_count =1
    missile_upgrade_count =3
    ammo_upgrade_count =1
    for index in range(alien_count):
        yPos = 6*index
        xPos = 5
        yV = 0.3
        xV = 0
        hp = 2
        type = 8
        aliens.array.append(Enemy(int(yPos), int(xPos), yV, xV, hp, type))
    for index in range(missile_upgrade_count):
        yPos =10+ 6*index
        xPos = 10
        yV =0.7
        xV = 1
        type = "missile_upgrade"
        size= items.size_dictionary[type]["size"]
        items.array.append(Item(int(yPos), int(xPos), yV, xV, type, size))
    for index in range(ammo_upgrade_count):
        yPos =0 -index*5
        xPos = 10+ index*8
        yV = 0.5
        xV = 0.8
        type = "ammo_up"
        size= items.size_dictionary[type]["size"]
        items.array.append(Item(int(yPos), int(xPos), yV, xV, type, size))

def  level_1():
    alien_count =4
    missile_upgrade_count = 1
    ammo_upgrade_count =2
    for index in range(alien_count):
        yPos = 6*index
        xPos = 5 *index
        yV = 0.2
        xV = 1
        hp = 2
        type = 5
        aliens.array.append(Enemy(int(yPos), int(xPos), yV, xV, hp, type))

    for index in range(missile_upgrade_count):
        yPos = 2*index +4
        xPos = 5 *index -2
        yV = 0.2
        xV = 2
        type = "missile_upgrade"
        size= items.size_dictionary[type]["size"]
        items.array.append(Item(int(yPos), int(xPos), yV, xV, type, size))
    for index in range(ammo_upgrade_count):
        yPos =0 -index*5
        xPos = 10+ index*8
        yV = 0.5
        xV = 0.8
        type = "ammo_up"
        size= items.size_dictionary[type]["size"]
        items.array.append(Item(int(yPos), int(xPos), yV, xV, type, size))
def  level_2():
    alien_count =4
    missile_upgrade_count =2

    for index in range(alien_count):
        yPos = 6 - 2*index
        xPos = 7*index
        yV = 0.3
        xV = 0.3
        hp = 2
        type = 4
        aliens.array.append(Enemy(int(yPos), int(xPos), yV, xV, hp, type))
    for index in range(missile_upgrade_count):
        yPos = 2*index +4
        xPos = 5 *index -2
        yV = 0.2
        xV = 2
        type = "missile_upgrade"
        size= items.size_dictionary[type]["size"]
        items.array.append(Item(int(yPos), int(xPos), yV, xV, type, size))
def  level_3():
    alien_count =2
    missile_upgrade_count =2

    ammo_upgrade_count =2

    for index in range(alien_count):
        yPos = 0
        xPos = 14 *index
        yV = 0.2
        xV = 0.5
        hp = 3
        type = 7
        aliens.array.append(Enemy(int(yPos), int(xPos), yV, xV, hp, type))
    missile_upgrade_count = 3
    for index in range(missile_upgrade_count):
        yPos = 2*index +4
        xPos = 5 *index -2
        yV = 0.2
        xV = 2
        type = "missile_upgrade"
        size= items.size_dictionary[type]["size"]
        items.array.append(Item(int(yPos), int(xPos), yV, xV, type, size))
    for index in range(ammo_upgrade_count):
        yPos =0 -index*5
        xPos = 10+ index*8
        yV = 0.5
        xV = 0.8
        type = "ammo_up"
        size= items.size_dictionary[type]["size"]
        items.array.append(Item(int(yPos), int(xPos), yV, xV, type, size))
def  end_screen():
    # todo: enter your own name
    names= ["Marie", "Lewis",
"Kiara" ,"Small",
"William" ,"Watkins",
"Lisa", "Brown",
"Jeffrey", "Pace",
"Lauren", "Hamilton",
"Michael" ,"Rowe",
"Brianna" ,"Valdez",
"Kimberly" ,"Ramirez",
"Stacy", "Robinson",
"Christopher" ,"Mitchell",
"Mindy" ,"Cohen"]
    name=str(names[round(random.randrange(12))] )
    end_score = player.score
    # end_score = 2001
    
    
    # resp = requests.post("https://invaders-page.herokuapp.com/")
    url = 'https://invaders-page.herokuapp.com/scores'
    payload = {
            'name': name,
            'score': end_score
    }
    
    # response = requests.post(url, json = payload)
    res = requests.post(url, json = payload)
    
    webbrowser.open('https://invaders-page.herokuapp.com/')

    
    # url = 'https://'
    # response = requests.post(url, data=payload, verify=False)
player = Player()
levels_array = []
levels_array.append(level_0)
levels_array.append(level_1)
levels_array.append(level_2)
levels_array.append(level_3)
levels_array.append(end_screen)
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
    stdscr.bkgd(' ', curses.color_pair(2))
    levels_array.pop(0)()

    #the game loop
    while 1:
        if(not game_running):
            time.sleep(3)
            break
        time.sleep(0.1)
        game_win.clear()
        message_pad.clear()
        game_win.bkgd(' ', curses.color_pair(2))
        message_pad.bkgd(' ', curses.color_pair(2))
        message_pad.addstr(0, 40, f"SCORE:{player.score}  " )

        if(len(aliens.array)==0):
            message_pad.clear()
            
            message_pad.addstr(0, 0, "LEVEL CLEARED!  ", curses.color_pair(1) )
            message_pad.addstr(0, 40, f"SCORE:{player.score}  " )

            message_pad.refresh( 0,0, 0, 0, 4, window_width)
            time.sleep(1)
            if(len(levels_array)>0):
                message_pad.clear()
                message_pad.addstr(0, 0, "STARTING NEXT LEVEL   ", curses.color_pair(3) )
                message_pad.addstr(0, 40, f"SCORE:{player.score}  " )

                levels_array.pop(0)()
            else:
                message_pad.clear()

                message_pad.addstr(0, 0, f"you WON!, Your SCORE is  : {player.score}  " , curses.color_pair(3))

                game_running = False
            message_pad.refresh( 0,0, 0, 0, 4, window_width)

            time.sleep(1)
        elif():
            #execute command for next level
            levels_array.pop()()
            message_pad.clear()

        # game_win.addstr(0, 0,"?>"*999 )

        if(player.yVelocity<0 and player.yPos + int(math.floor(player.yVelocity)) > 0):
            player.yPos += int(math.floor(player.yVelocity))
        elif(player.yVelocity >0 and player.xPos + math.floor(player.yVelocity) < window_height):
            player.yPos += int(math.floor(player.yVelocity))
        if(player.xVelocity<0 and player.xPos + player.xVelocity > 0):
            player.xPos += player.xVelocity
        elif(player.xVelocity > 0 and  player.xPos + math.floor(player.xVelocity) < window_width - len(ship[0])):
            player.xPos += player.xVelocity

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
                end_screen()
                game_running = False

            # stdscr.addstr(8+index, enemy.xPos,"alien "+"yPos " +str(enemy.yPos))


        #print all the missiles
        for missile in player.missile_array:
            missile.print_missile(game_win)
            target = missile.collision_detection(aliens)
            if target:
                # game_win.addstr(0, 40, "hit!" )
                kil_enemy = target.hit(missile.missile_char)
                if kil_enemy:
                    player.score += max((10-target.type)*100, 100  )
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
        #print all items
        for index,item in enumerate(items.array):
            item.print_item(game_win , items.size_dictionary)

            if(item.vY<0 and item.yPos + item.vY >= 0):
                item.yPos += item.vY
            elif(item.vY >0 and item.yPos + item.vY < window_height):
                item.yPos += item.vY
            else:
                items.array.remove(item)

            if(item.vX<0):
                if(item.xPos + item.vX >= 0):
                    item.xPos += item.vX
                else:
                    item.vX *= -1
            elif(item.vX > 0):
                if( item.xPos + item.vX < window_width - item.item_size-1):
                    item.xPos += item.vX
                else:
                    item.vX *= -1
            if( item.yPos - player.yPos <= item.item_size and item.yPos -player.yPos >0 
            and  item.xPos - player.xPos  <= item.item_size + len(ship[0]) ):
                game_win.addstr(0, 20, "item collected!")
                if(item.type=="ammo_up"):
                    player.max_ammo+=1
                    player.score+= 200
                elif(item.type=="missile_upgrade"):
                    if(len(player.upgrade_array)>0):
                        player.missile_char = player.upgrade_array.pop(0)
                items.array.remove(item)


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
                new_missile = Player_missile(player.yPos   ,player.xPos + math.floor(len(ship[0])/2) ,-1,0 , player.missile_char)
                player.add_missile(new_missile)
                player.ammo-=1


        elif key == curses.KEY_HOME:
            game_win.addstr(0, 0, "You pressed home key!  ")
            break
        message_pad.refresh( 0,0, 0, 0, 4, window_width)

wrapper(main)