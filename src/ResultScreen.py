import pygame,sys
import Utilities
import math
from pygame.locals import *
import Text

FONT = "fonts\\Aller_Lt.ttf"
WHITE = (255,255,255)

def Render(target,map_,diff,skin,mods,score,acc,rating_count,max_combo):
    Rank_texture={}
    Rank_texture["SS"]=pygame.image.load("skins\\"+skin+"\\SS.png").convert_alpha()
    Rank_texture["S"]=pygame.image.load("skins\\"+skin+"\\S.png").convert_alpha()
    Rank_texture["A"]=pygame.image.load("skins\\"+skin+"\\A.png").convert_alpha()
    Rank_texture["B"]=pygame.image.load("skins\\"+skin+"\\B.png").convert_alpha()
    Rank_texture["C"]=pygame.image.load("skins\\"+skin+"\\C.png").convert_alpha()
    Rank_texture["D"]=pygame.image.load("skins\\"+skin+"\\D.png").convert_alpha()
    Cursor=pygame.image.load("skins\\"+skin+"\\cursor.png").convert_alpha()
    GUI=pygame.image.load("skins\\"+skin+"\\result_screen.png").convert_alpha()
    FC=pygame.image.load("skins\\"+skin+"\\FC.png").convert_alpha()
    HR = pygame.image.load("skins\\"+skin+"\\hr.png").convert_alpha()
    EZ = pygame.image.load("skins\\"+skin+"\\ez.png").convert_alpha()
    DT = pygame.image.load("skins\\"+skin+"\\dt.png").convert_alpha()
    HT = pygame.image.load("skins\\"+skin+"\\ht.png").convert_alpha()
    try:
        Background=pygame.image.load("maps\\"+map_+"\\background.png").convert_alpha()
    except:
        Background=pygame.Surface((1080,720))
        Background.fill(WHITE)
    do_FC=False
    map_combo=rating_count["300"]+rating_count["100"]+rating_count["50"]+rating_count["0"]
    if max_combo == map_combo:
        do_FC=True
    if rating_count["300"] == map_combo:
        rank = "SS"
    elif rating_count["300"]>=0.9*map_combo and rating_count["0"]==0 and rating_count["50"]<=0.01*map_combo:
        rank = "S"
    elif (rating_count["300"]>=0.8*map_combo and rating_count["0"]==0 )or rating_count["300"]>=0.9*map_combo:
        rank = "A"
    elif (rating_count["300"]>=0.7*map_combo and rating_count["0"]==0 )or rating_count["300"]>=0.8*map_combo:
        rank = "B"
    elif rating_count["300"]>=0.6*map_combo:
        rank = "C"
    else:
        rank = "D"
    MaxCombo_text = Text.Text(FONT,30,WHITE)
    Acc_text = Text.Text(FONT,30,WHITE)
    Score_text = Text.Text(FONT,50,WHITE)
    Rating_text_300 = Text.Text(FONT,50,WHITE)
    Rating_text_100 = Text.Text(FONT,50,WHITE)
    Rating_text_50 = Text.Text(FONT,50,WHITE)
    Rating_text_0 = Text.Text(FONT,50,WHITE)
    Topic_text = Text.Text(FONT,35,WHITE)
    
    while True:
        for event in pygame.event.get():
            if (event.type == QUIT):
                pygame.quit()
                sys.exit()
            if (event.type == KEYDOWN):
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
        Curr_Objects = []
        Curr_Objects.append((Background,(0,0)))
        Curr_Objects.append((GUI,(0,0)))
        if do_FC:
            Curr_Objects.append((FC,(400,507)))
        Curr_Objects.append((Rank_texture[rank],(576,47)))

        Acc_text.render_tlcorner(Curr_Objects,"Accurracy:"+str(math.ceil(acc*10000)/100)+"%",100,433)
        MaxCombo_text.render_tlcorner(Curr_Objects,"Max combo:"+str(max_combo)+"x",100,527)
        Score_text.render_tlcorner(Curr_Objects,"Score:"+str(math.ceil(score)),100,329)
        Rating_text_300.render_center(Curr_Objects,str(rating_count["300"]),230,145)
        Rating_text_100.render_center(Curr_Objects,str(rating_count["100"]),456,145)
        Rating_text_50.render_center(Curr_Objects,str(rating_count["50"]),230,252)
        Rating_text_0.render_center(Curr_Objects,str(rating_count["0"]),456,252)
        Topic_text.render_tlcorner(Curr_Objects,map_+"["+diff+"]",10,10)

        mod_count = 0
        if mods[2] == -1:
            Curr_Objects.append((EZ,(576+80*mod_count,397)))
            mod_count+=1
        if mods[1] == -1:
            Curr_Objects.append((HT,(576+80*mod_count,397)))
            mod_count+=1
        if mods[1] == 1:
            Curr_Objects.append((DT,(576+80*mod_count,397)))
            mod_count+=1
        if mods[2]== 1:
            Curr_Objects.append((HR,(576+80*mod_count,397)))
            mod_count+=1


        Mouse_pos = pygame.mouse.get_pos()
        Curr_Objects.append((Cursor,Utilities.center(Mouse_pos[0],Mouse_pos[1],50,50)))
        Utilities.render(target,Curr_Objects)