'''
-----------------------------------------------------------------------------
Program Name: (never put your personal name or information on the Internet)
Program Description:

-----------------------------------------------------------------------------
References:

(put a link to your reference here but also add a comment in the code below where you used the reference)

-----------------------------------------------------------------------------

Additional Libraries/Extensions:

(put a list of required extensions so that the user knows that they need to download extra features)

-----------------------------------------------------------------------------

Known bugs:

(put a list of known bugs here, if you have any)

----------------------------------------------------------------------------


Program Reflection:
I think this project deserves a level XXXXXX because ...

 Level 3 Requirements Met:
• 
•  
•  
•  
•  
• 

Features Added Beyond Level 3 Requirements:
• 
•  
•  
•  
•  
• 
-----------------------------------------------------------------------------
'''

import pygame 
import random
pygame.init()

WindowWidth = 600
WindowHeight = 400

window = pygame.display.set_mode((WindowWidth,WindowHeight))
clock = pygame.time.Clock()

GameBg = pygame.image.load("images/bg.png")
GameOver = pygame.image.load("images/gameover.png")
Title = pygame.image.load("images/title.png")

state = "HOME"

BeginButton = pygame.Rect(0,0,600,400)

Bugs = [

    pygame.image.load("images/bug0.png"),
    pygame.image.load("images/bug1.png"),
    pygame.image.load("images/bug3.png"),
    pygame.image.load("images/bug4.png"),
    pygame.image.load("images/bug5.png"),
    pygame.image.load("images/bug6.png"),
    pygame.image.load("images/bug7.png")
]

font = pygame.font.Font("fonts/fontminecraft.ttf", 26)
BLACK = (0,0,0)
CurrentBug = None
BugRect = None
BugsClicked = 0

Running = True
while Running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Running = False
        
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            click_pos = event.pos

            if state == "HOME":
                if BeginButton.collidepoint(click_pos):
                    state = "PLAY"

    if state == "HOME":
        window.blit(GameBg, (0,0,))
        GameInstructions1 = "Click the screen to start the game"
        GameInstructions2 = "Click the bugs to win, smash 15 bugs!"
        renderText1 = font.render(GameInstructions1, 1, pygame.Color(BLACK))
        renderText2 = font.render(GameInstructions2, 1, pygame.Color(BLACK))
        window.blit(renderText1, (70,300))
        window.blit(renderText2, (60,200))
        window.blit(Title, (40,40))

    if state == "PLAY":
        window.blit(GameBg, (0,0,))

        if CurrentBug is None:
            CurrentBug = random.choice(Bugs)
            BugSize = random.randint(75,100)
            CurrentBug = pygame.transform.scale(CurrentBug, (BugSize, BugSize))
            BugX = random.randint(0, WindowWidth - BugSize)
            BugY = random.randint(0, WindowHeight - BugSize)
            BugRect = CurrentBug.get_rect(topleft = (BugX,BugY))

        
        if CurrentBug is not None:
            window.blit(CurrentBug, BugRect)

        renderText3 = font.render("Current Score: " + str(BugsClicked), 1, pygame.Color(BLACK))
        window.blit(renderText3, (200,350))
        
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            click_pos = event.pos
            if CurrentBug is not None:
                if BugRect.collidepoint(click_pos):
                    print("bug clicked")

                    
                    CurrentBug = None
                    BugRect = None
                    BugsClicked += 1

                    if BugsClicked == 15:
                        state = "WIN"

    if state == "WIN":
        window.blit(GameBg, (0,0,))
        window.blit(GameOver, (0, 80))


    pygame.display.flip()
    clock.tick(60)

pygame.quit()
