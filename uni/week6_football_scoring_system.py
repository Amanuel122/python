team_name = input('Enter team name: ')
goal_scored1 = int(input('Goals scored in match #1: '))
goal_lost1 = int(input('Goals Against in match #1: '))
goal_scored2 = int(input('Goals scored in match #2: '))
goal_lost2 = int(input('Goals Against in match #2: '))
goal_scored3 = int(input('Goals scored in match #3: '))
goal_lost3 = int(input('Goals Against in match #3: '))
goal_scored4 = int(input('Goals scored in match #4: '))
goal_lost4 = int(input('Goals Against in match #4: '))
goal_scored5 = int(input('Goals scored in match #5: '))
goal_lost5 = int(input('Goals Against in match #5: '))

win_count = int()
point_count = int()
draw_count = int()
loss_count = int()

if goal_scored1 > goal_lost1:
    win_count +=1
    point_count+=3
elif goal_scored1 == goal_lost1:
    draw_count += 1
    point_count+=1
else:
    loss_count +=1

if goal_scored2 > goal_lost2:
    win_count +=1
    point_count+=3
elif goal_scored2 == goal_lost2:
    draw_count += 1
    point_count+=1
else:
    loss_count +=1

if goal_scored3 > goal_lost3:
    win_count +=1
    point_count+=3
elif goal_scored3 == goal_lost3:
    draw_count += 1
    point_count+=1
else:
    loss_count +=1

if goal_scored4 > goal_lost4:
    win_count +=1
    point_count+=3
elif goal_scored4 == goal_lost4:
    draw_count += 1
    point_count+=1
else:
    loss_count +=1

if goal_scored5 > goal_lost5:
    win_count +=1
    point_count+=3
elif goal_scored5 == goal_lost5:
    draw_count += 1
    point_count+=1
else:
    loss_count +=1

print(team_name)
print(('Wins: ')+ str(win_count))
print(('Draws: ')+ str(draw_count))
print(('Losses: ') +str(loss_count))
print(('Points: ') + str(point_count))
