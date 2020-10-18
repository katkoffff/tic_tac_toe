import numpy as np
game_elem=[' ',0,1,2,'-','o','x']
game_matrix=np.array([[game_elem[0],game_elem[1],game_elem[2],game_elem[3]],
                     [game_elem[1],game_elem[4],game_elem[4],game_elem[4]],
                     [game_elem[2],game_elem[4],game_elem[4],game_elem[4]],
                     [game_elem[3],game_elem[4],game_elem[4],game_elem[4]]
                     ])
def game_table(fplayer,x=None,y=None):
    if (x is not None) and (y is not None):        
        if fplayer==0:            
            if game_matrix[x+1,y+1] == game_elem[4]:                
                game_matrix[x+1,y+1]=game_elem[5]
        else: 
            if game_matrix[x+1,y+1] == game_elem[4]:
                game_matrix[x+1,y+1]=game_elem[6]    
    for i in game_matrix:
        print(f"{i[0]}  {i[1]}  {i[2]}  {i[3]}")
    bonus=[all([i == game_elem[5] for i in game_matrix[1,1:]]), all([i == game_elem[6] for i in game_matrix[1,1:]]),
           all([i == game_elem[5] for i in game_matrix[2,1:]]), all([i == game_elem[6] for i in game_matrix[2,1:]]),
           all([i == game_elem[5] for i in game_matrix[3,1:]]), all([i == game_elem[6] for i in game_matrix[3,1:]]),
           all([i == game_elem[5] for i in game_matrix[1:,1]]), all([i == game_elem[6] for i in game_matrix[1:,1]]),
           all([i == game_elem[5] for i in game_matrix[1:,2]]), all([i == game_elem[6] for i in game_matrix[1:,2]]),
           all([i == game_elem[5] for i in game_matrix[1:,3]]), all([i == game_elem[6] for i in game_matrix[1:,3]]),
           all([i == game_elem[5] for i in (game_matrix[1,1],game_matrix[2,2],game_matrix[3,3])]),all([i == game_elem[6] for i in (game_matrix[1,1],game_matrix[2,2],game_matrix[3,3])]),
           all([i == game_elem[5] for i in (game_matrix[1,3],game_matrix[2,2],game_matrix[3,1])]),all([i == game_elem[6] for i in (game_matrix[1,3],game_matrix[2,2],game_matrix[3,1])]),
           ]      
    over=all([all([j in (game_elem[5],game_elem[6]) for j in i[1:]]) for i in game_matrix[1:]])       
    return any(bonus),over    
x,y=game_table(0)
in_game=True
player=[[],[]]
while True:
    while True:
        player[0]=list(map(int,input("1-игрок введите координаты через пробел: ").split(' ')))
        x,y=game_table(0,player[0][0],player[0][1])
        if x:
            print('1-ый игрок победил')
            break
        elif y:
            print('Ничья')
            break
        player[1]=list(map(int,input("2-игрок введите координаты через пробел: ").split(' ')))
        x,y=game_table(1,player[1][0],player[1][1])
        if x:
            print('2-ой игрок победил')
            break
        elif y:
            print('Ничья')
            break
    ig=input("Играем дальше (y/n): ")
    if ig=='y':
        game_matrix=np.array([[game_elem[0],game_elem[1],game_elem[2],game_elem[3]],
                     [game_elem[1],game_elem[4],game_elem[4],game_elem[4]],
                     [game_elem[2],game_elem[4],game_elem[4],game_elem[4]],
                     [game_elem[3],game_elem[4],game_elem[4],game_elem[4]]
                     ])
        x,y=game_table(0)
    elif ig=='n':
        break
    
    
