import pygame, sys, random, math, time
from pygame.locals import *

#define colors:
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
LIGHT_GREEN = (0, 255, 0)
MID_GREEN = (0, 70, 0)
DARK_GREEN = (0, 20, 0)

small_window_offset = 20 #distance from top left corner to small window
small_window_size = 200 #size of small window
small_dot_size = 3 #size of points in small window and graph
large_window_offset = small_window_offset * 2 + small_window_size #distance from top left corner to large window
large_window_size = small_window_size * 2 #size of large window
large_dot_size = small_dot_size * 2 #size of points in large window
graph_window_size = small_window_size + large_window_size + small_window_offset #size of window for graph
app_size = ((small_window_size + small_window_offset) * 3,
            (small_window_size + small_window_offset) * 3) #size of overall application
button_corner = (35, 583) #corner of the progress button, used for drawing the outline

mouse_x, mouse_y = 0, 0 #initialize the mouse position

graph_origin = (int(small_window_offset + graph_window_size/10),
                int(small_window_offset + 9 * graph_window_size/10)) #set the 'origin' of the graph
axis_length = graph_origin[1] - graph_origin[0] #set the length of axis on the graph
tick_size = 4

pygame.init() #initialize pygame object - this is needed to run various methods
DISPLAYSURF = pygame.display.set_mode(app_size) # application size: 660 by 660 pixels
pygame.display.set_caption("Geomemory") # game title: Geomemory

#create fonts
title_font = pygame.font.Font('freesansbold.ttf', 60)
score_font = pygame.font.Font('freesansbold.ttf', 45)
score_num_font = pygame.font.Font('freesansbold.ttf', 10)
highscore_font = pygame.font.Font('freesansbold.ttf', 25)
highscore_num_font = pygame.font.Font('freesansbold.ttf', 25)
countdown_font = pygame.font.Font('freesansbold.ttf', 160)
idle_font = pygame.font.Font('freesansbold.ttf', 30)
progress_font = pygame.font.Font('freesansbold.ttf', 30)
return_font = pygame.font.Font('freesansbold.ttf', 20)
graph_title_font = pygame.font.Font('freesansbold.ttf', 40)
graph_tick_font = pygame.font.Font('freesansbold.ttf', 10)

#create text
title_obj = title_font.render('GEOMEMORY', True, LIGHT_GREEN, DARK_GREEN)
score_obj = score_font.render('SCORE', True, LIGHT_GREEN, MID_GREEN)
score_num_obj = score_font.render('0', True, LIGHT_GREEN, MID_GREEN)
highscore_obj = highscore_font.render('HIGH  SCORES', True, LIGHT_GREEN, MID_GREEN)
highscore_num_one_obj = highscore_num_font.render('1.', True, LIGHT_GREEN, MID_GREEN)
highscore_num_two_obj = highscore_num_font.render('2.', True, LIGHT_GREEN, MID_GREEN)
highscore_num_three_obj = highscore_num_font.render('3.', True, LIGHT_GREEN, MID_GREEN)
highscore_num_four_obj = highscore_num_font.render('4.', True, LIGHT_GREEN, MID_GREEN)
countdown_obj = countdown_font.render('3', True, RED, MID_GREEN)
idle_obj = idle_font.render('press any key to begin', True, RED, MID_GREEN)
progress_obj = progress_font.render('PROGRESS', True, LIGHT_GREEN, DARK_GREEN)
return_obj = return_font.render('press any key to return', True, RED, MID_GREEN)
graph_title_obj = graph_title_font.render('SCORES OVER TIME', True, RED, MID_GREEN)
graph_tick_obj_1M = graph_tick_font.render('1M', True, LIGHT_GREEN, MID_GREEN)
graph_tick_obj_750K = graph_tick_font.render('750K', True, LIGHT_GREEN, MID_GREEN)
graph_tick_obj_500K = graph_tick_font.render('500K', True, LIGHT_GREEN, MID_GREEN)
graph_tick_obj_250K = graph_tick_font.render('250K', True, LIGHT_GREEN, MID_GREEN)

#create text box
title_rect_obj = title_obj.get_rect()
score_rect_obj = score_obj.get_rect()
score_num_rect_obj = score_num_obj.get_rect()
highscore_rect_obj = highscore_obj.get_rect()
highscore_num_one_rect_obj = highscore_num_one_obj.get_rect()
highscore_num_two_rect_obj = highscore_num_two_obj.get_rect()
highscore_num_three_rect_obj = highscore_num_three_obj.get_rect()
highscore_num_four_rect_obj = highscore_num_four_obj.get_rect()
countdown_rect_obj = countdown_obj.get_rect()
idle_rect_obj = idle_obj.get_rect()
progress_rect_obj = progress_obj.get_rect()
return_rect_obj = return_obj.get_rect()
graph_title_rect_obj = graph_title_obj.get_rect()
graph_tick_rect_obj_1M = graph_tick_obj_1M.get_rect()
graph_tick_rect_obj_750K = graph_tick_obj_750K.get_rect()
graph_tick_rect_obj_500K = graph_tick_obj_500K.get_rect()
graph_tick_rect_obj_250K = graph_tick_obj_250K.get_rect()

#place text box on the screen
title_rect_obj.center = (large_window_offset + large_window_size/2, small_window_offset + small_window_size/2)
score_rect_obj.center = (small_window_offset + small_window_size/2, large_window_offset + small_window_offset * 2)
score_num_rect_obj.center = (small_window_offset + small_window_size/2, large_window_offset + small_window_offset * 5)
highscore_rect_obj.center = (small_window_offset + small_window_size/2, large_window_offset + large_window_size/2 - small_window_offset * 2)
highscore_num_one_rect_obj.centery = large_window_offset + large_window_size/2
highscore_num_one_rect_obj.left = small_window_offset * 3
highscore_num_two_rect_obj.centery = large_window_offset + large_window_size/2 + small_window_offset * 2
highscore_num_two_rect_obj.left = small_window_offset * 3
highscore_num_three_rect_obj.centery = large_window_offset + large_window_size/2 + small_window_offset * 4
highscore_num_three_rect_obj.left = small_window_offset * 3
highscore_num_four_rect_obj.centery = large_window_offset + large_window_size/2 + small_window_offset * 6
highscore_num_four_rect_obj.left = small_window_offset * 3
countdown_rect_obj.center = (large_window_offset + large_window_size/2, large_window_offset + large_window_size/2)
idle_rect_obj.center = (large_window_offset + large_window_size/2, large_window_offset + large_window_size/2)
progress_rect_obj.center = (small_window_offset + small_window_size/2, large_window_offset + large_window_size/2 + small_window_offset * 8)
return_rect_obj.center = (small_window_offset + graph_window_size/2, graph_window_size - small_window_offset/2)
graph_title_rect_obj.center = (small_window_offset + graph_window_size/2, small_window_offset * 3)
graph_tick_rect_obj_1M.center = (small_window_offset * 3, graph_origin[0])
graph_tick_rect_obj_750K.center = (small_window_offset * 3, graph_origin[0] + axis_length/4)
graph_tick_rect_obj_500K.center = (small_window_offset * 3, graph_origin[0] + axis_length/2)
graph_tick_rect_obj_250K.center = (small_window_offset * 3, graph_origin[0] + 3 * axis_length/4)

DISPLAYSURF.fill(DARK_GREEN) # white background
    
def draw_smaller_window():
    pygame.draw.rect(DISPLAYSURF, MID_GREEN, (small_window_offset, small_window_offset, small_window_size, small_window_size))
    pygame.draw.line(DISPLAYSURF, LIGHT_GREEN, (small_window_offset + small_window_size/2, small_window_offset), (small_window_offset + small_window_size/2, small_window_offset + small_window_size),3)
    pygame.draw.line(DISPLAYSURF, LIGHT_GREEN, (small_window_offset, small_window_offset + small_window_size/2), (small_window_offset + small_window_size, small_window_offset + small_window_size/2),3)
    pygame.draw.rect(DISPLAYSURF, LIGHT_GREEN, (small_window_offset, small_window_offset, small_window_size, small_window_size), 6)

def draw_larger_window():
    pygame.draw.rect(DISPLAYSURF, MID_GREEN, (large_window_offset, large_window_offset, large_window_size, large_window_size))
    pygame.draw.line(DISPLAYSURF, LIGHT_GREEN, (large_window_offset + large_window_size/2, large_window_offset), (large_window_offset + large_window_size/2, large_window_offset + large_window_size),3)
    pygame.draw.line(DISPLAYSURF, LIGHT_GREEN, (large_window_offset, large_window_offset + large_window_size/2), (large_window_offset + large_window_size, large_window_offset + large_window_size/2),3)
    pygame.draw.rect(DISPLAYSURF, LIGHT_GREEN, (large_window_offset, large_window_offset, large_window_size, large_window_size), 6)

def draw_side_window():
    pygame.draw.rect(DISPLAYSURF, MID_GREEN, (small_window_offset, large_window_offset, small_window_size, large_window_size))

def draw_top_window():
    pygame.draw.rect(DISPLAYSURF, MID_GREEN, (large_window_offset, small_window_offset, large_window_size, small_window_size))

def draw_graph_data():
    highscores_list = []
    try:
        with open("geomemory_highscores.txt", "r") as highscore_text:
            for line in highscore_text:
                highscores_list.append(int(line.split()[0]))
        if len(highscores_list) > axis_length - 1:
            start_index = (len(highscores_list) - axis_length) + 1
            highscores_list = highscores_list[start_index:]
        step_length = int(axis_length/(len(highscores_list) + 1))
        print("step length:", step_length)
        for i in range(len(highscores_list)):
            pos = ((i + 1) * step_length + graph_origin[0], int(graph_origin[1] - axis_length * highscores_list[i]/1000000))
            pygame.draw.circle(DISPLAYSURF, RED, pos, small_dot_size, 0)
    except:
        print("failing gracefully at drawing a graph of highscores")
    print("highscorelist length:", len(highscores_list))
    print("axis length:", axis_length)


def draw_graph_window():
    origSurf = DISPLAYSURF.copy()
    pygame.draw.rect(DISPLAYSURF, MID_GREEN, (small_window_offset, small_window_offset, graph_window_size, graph_window_size))
    pygame.draw.line(DISPLAYSURF, LIGHT_GREEN, (graph_origin[0], graph_origin[0]), (graph_origin[0], graph_origin[1]),3)
    pygame.draw.line(DISPLAYSURF, LIGHT_GREEN, (graph_origin[0], graph_origin[1]), (graph_origin[1], graph_origin[1]),3)
    pygame.draw.rect(DISPLAYSURF, LIGHT_GREEN, (small_window_offset, small_window_offset, graph_window_size, graph_window_size), 6)    

    pygame.draw.line(DISPLAYSURF, LIGHT_GREEN, (graph_origin[0] - tick_size, graph_origin[0]), (graph_origin[0] + tick_size, graph_origin[0]),2) 
    pygame.draw.line(DISPLAYSURF, LIGHT_GREEN, (graph_origin[0] - tick_size, graph_origin[0] + axis_length/4), (graph_origin[0] + tick_size, graph_origin[0] + axis_length/4),2) 
    pygame.draw.line(DISPLAYSURF, LIGHT_GREEN, (graph_origin[0] - tick_size, graph_origin[0] + axis_length/2), (graph_origin[0] + tick_size, graph_origin[0] + axis_length/2),2) 
    pygame.draw.line(DISPLAYSURF, LIGHT_GREEN, (graph_origin[0] - tick_size, graph_origin[0] + 3 * axis_length/4), (graph_origin[0] + tick_size, graph_origin[0] + 3 * axis_length/4),2) 
    
    DISPLAYSURF.blit(return_obj, return_rect_obj)
    DISPLAYSURF.blit(graph_title_obj, graph_title_rect_obj)
    DISPLAYSURF.blit(graph_tick_obj_1M, graph_tick_rect_obj_1M)
    DISPLAYSURF.blit(graph_tick_obj_750K, graph_tick_rect_obj_750K)
    DISPLAYSURF.blit(graph_tick_obj_500K, graph_tick_rect_obj_500K)
    DISPLAYSURF.blit(graph_tick_obj_250K, graph_tick_rect_obj_250K)
    draw_graph_data()
    pygame.display.update()
    while True:
        pygame.time.wait(200)
        if checkForKeyPress():
            DISPLAYSURF.blit(origSurf,(0,0))
            pygame.event.get()
            return
    
    
def draw_countdown(count):
    global countdown_obj
    countdown_obj = countdown_font.render(str(count), True, RED, MID_GREEN)
    DISPLAYSURF.blit(countdown_obj, countdown_rect_obj)
    pygame.display.update()
    pygame.time.wait(1200)
    
def draw_highscores():

    highscores_list = []
    try:
        with open("geomemory_highscores.txt", "r") as highscore_text:
            for line in highscore_text:
                highscores_list.append(int(line.split()[0]))
    except:
        print("failing gracefully at getting highscores")
    try:
        highscores_list.sort()
        highscores_list = highscores_list[::-1] # reverse the list
        highscores_list = highscores_list[:max(len(highscores_list),4)] # get the highest 4 values
        print(highscores_list)
        if(len(highscores_list) > 0):
            highscore_num_one_obj = highscore_num_font.render('1. ' + str(highscores_list[0]), True, LIGHT_GREEN, MID_GREEN)
            DISPLAYSURF.blit(highscore_num_one_obj, highscore_num_one_rect_obj)
            
        if(len(highscores_list) > 1):
            highscore_num_two_obj = highscore_num_font.render('2. ' + str(highscores_list[1]), True, LIGHT_GREEN, MID_GREEN)
            DISPLAYSURF.blit(highscore_num_two_obj, highscore_num_two_rect_obj)

        if(len(highscores_list) > 2):
            highscore_num_three_obj = highscore_num_font.render('3. ' + str(highscores_list[2]), True, LIGHT_GREEN, MID_GREEN)
            DISPLAYSURF.blit(highscore_num_three_obj, highscore_num_three_rect_obj)
        
        if(len(highscores_list) > 3):
            highscore_num_four_obj = highscore_num_font.render('4. ' + str(highscores_list[3]), True, LIGHT_GREEN, MID_GREEN)
            DISPLAYSURF.blit(highscore_num_four_obj, highscore_num_four_rect_obj)

    except:
        print("failing gracefully")

    
    
def draw_score(final_score):
    draw_side_window()
    score_num_obj = score_font.render(str(final_score), True, LIGHT_GREEN, MID_GREEN)
    score_num_rect_obj = score_num_obj.get_rect()
    score_num_rect_obj.center = (small_window_offset + small_window_size/2, large_window_offset + small_window_offset * 5)
    DISPLAYSURF.blit(score_obj, score_rect_obj)       
    DISPLAYSURF.blit(score_num_obj, score_num_rect_obj)
    DISPLAYSURF.blit(highscore_obj, highscore_rect_obj)
    
    DISPLAYSURF.blit(highscore_num_one_obj, highscore_num_one_rect_obj)
    DISPLAYSURF.blit(highscore_num_two_obj, highscore_num_two_rect_obj)
    DISPLAYSURF.blit(highscore_num_three_obj, highscore_num_three_rect_obj)
    DISPLAYSURF.blit(highscore_num_four_obj, highscore_num_four_rect_obj)
    DISPLAYSURF.blit(progress_obj, progress_rect_obj)
  
    draw_highscores()
       
    pygame.display.update()

def mean(numbers):
    return float(sum(numbers)) / max(len(numbers), 1)

def euc_dist(tup1, tup2):
    return math.sqrt((tup1[0] - tup2[0]) ** 2 + (tup1[1] - tup2[1]) ** 2)

def logarithmic(x):
    y = 1000000/(1.125 ** x)
    
    return y

def generate_three_points():
    three_point_set = [0,0,0]
    for i in range(3):
        x, y = int(random.random() * small_window_size), int(random.random() * small_window_size)
        three_point_set[i] = x, y
    return three_point_set

def mouse_within_large_window(m_x, m_y):
    lower_margin = large_window_offset
    upper_margin = large_window_offset + large_window_size
    if mouse_x > lower_margin and mouse_x < upper_margin and mouse_y > lower_margin and mouse_y < upper_margin:
        return True
    return False

def get_corresponding_points(set_a, set_b):
    
    """
    returns a list of tuples that indicate corresponding indices
    """
    print(set_a, set_b)
    pairs = [0, 0, 0]
    b_found = [0, 0, 0]
    for i in range(len(set_a)):
        least_dist = 10000
        for j in range(len(set_b)):
            if b_found[j] != 1:
                if least_dist > euc_dist(set_a[i], set_b[j]):
                    least_dist = euc_dist(set_a[i], set_b[j])
                    pairs[i] = (i, j)
        b_found[pairs[i][1]] = 1
    print("pairs", pairs)
    return pairs

def compare_point_sets(guess_set, gen_set):
    corresponding_points = get_corresponding_points(guess_set, gen_set)
    accuracy_list = []
    for i in range(len(corresponding_points)):
        distance = euc_dist(guess_set[corresponding_points[i][0]], gen_set[corresponding_points[i][1]])
        accuracy_list.append(distance)
    print("accuracy list:", accuracy_list)
    return mean(accuracy_list)

def terminate():
    pygame.quit()
    sys.exit()

def checkForKeyPress():
    if len(pygame.event.get(QUIT)) > 0:
        terminate()

    keyUpEvents = pygame.event.get(KEYUP)
    if len(keyUpEvents) == 0:
        return None
    if keyUpEvents[0].key == K_ESCAPE:
        terminate()
    return keyUpEvents[0].key

def idle_screen():
    DISPLAYSURF.blit(idle_obj, idle_rect_obj)
    pygame.display.update()
    while True:
        
        for event in pygame.event.get():
            if event.type == MOUSEBUTTONUP:
                if progress_rect_obj.collidepoint(event.pos):
                    draw_graph_window() 
                    pygame.display.update()
            elif event.type == MOUSEMOTION:
                    mouse_x, mouse_y = event.pos
                    if progress_rect_obj.collidepoint(mouse_x, mouse_y):
                        pygame.draw.rect(DISPLAYSURF, RED, (button_corner[0] - 3, button_corner[1] - 3, 176, 36), 2)
                        pygame.display.update()
                    else:
                        pygame.draw.rect(DISPLAYSURF, MID_GREEN, (button_corner[0] - 3, button_corner[1] - 3, 176, 36), 2)
                        pygame.display.update()
        pygame.time.wait(200)
        if checkForKeyPress():
            pygame.event.get()
            pygame.draw.rect(DISPLAYSURF, MID_GREEN, (button_corner[0] - 3, button_corner[1] - 3, 176, 36), 2) 
            return

def generate_quiz_points():
    for i in range(1000): # make sure the points don't overlap and that the angles aren't too sharp - try up to 1000 times 
        gen_point_set = list(generate_three_points())
        angle_set = []
        sharp_angles = False
        for i in range(3):
            rise = abs(gen_point_set[i][1] - gen_point_set[i-1][1])
            run = abs(gen_point_set[i][0] - gen_point_set[i-1][0])
            print("rise, run:", rise, run)
            if run != 0:
                angle = 360 * math.atan(rise/run) / (2 * math.pi)
            else:
                angle = 90
            angle_set.append(angle)
            print("angle:",angle)
        for i in range(3):
            if abs(angle_set[i] - angle_set[i-1]) < 18:
                sharp_angles = True
        if euc_dist(gen_point_set[-1], gen_point_set[0]) > small_dot_size and \
        euc_dist(gen_point_set[0], gen_point_set[1]) > small_dot_size and \
        euc_dist(gen_point_set[1], gen_point_set[2]) > small_dot_size and not \
        sharp_angles:
            break
        print("trying again")
        
    print("Generating points:", gen_point_set)
    
    return gen_point_set

def new_quiz():
    global guess_point_set, not_printed, gen_point_set, controls_disabled
    controls_disabled = True
    guess_point_set = []
    not_printed = True

    DISPLAYSURF.fill(DARK_GREEN)
    draw_smaller_window()
    draw_larger_window()
    draw_top_window()
    draw_side_window()
    draw_highscores()

    
    DISPLAYSURF.blit(title_obj, title_rect_obj)        
    DISPLAYSURF.blit(score_obj, score_rect_obj)        
    DISPLAYSURF.blit(score_num_obj, score_num_rect_obj)        
    DISPLAYSURF.blit(highscore_obj, highscore_rect_obj)        
    DISPLAYSURF.blit(highscore_num_one_obj, highscore_num_one_rect_obj)
    DISPLAYSURF.blit(highscore_num_two_obj, highscore_num_two_rect_obj)
    DISPLAYSURF.blit(highscore_num_three_obj, highscore_num_three_rect_obj)
    DISPLAYSURF.blit(highscore_num_four_obj, highscore_num_four_rect_obj)
    DISPLAYSURF.blit(progress_obj, progress_rect_obj)

    idle_screen()
    gen_point_set = generate_quiz_points()
    for point in gen_point_set:
        pygame.draw.circle(DISPLAYSURF, RED, (point[0] + small_window_offset, point[1] + small_window_offset), small_dot_size, 0)
        #pygame.draw.circle(DISPLAYSURF, BLACK, (2 * point[0] + large_window_offset, 2 * point[1] + large_window_offset), large_dot_size, 0)
        #the above line is useful for debuging   
    for i in range(len(gen_point_set)):
        pygame.draw.line(DISPLAYSURF, RED, (gen_point_set[i-1][0] + small_window_offset, gen_point_set[i-1][1] + small_window_offset), (gen_point_set[i][0] + small_window_offset, gen_point_set[i][1] + small_window_offset), 2)
    global mouse_clicked
    draw_larger_window()
    pygame.display.update()
    for i in range(5,0,-1):
        draw_countdown(i)
    draw_smaller_window()
    draw_larger_window()
    pygame.display.update()    

new_quiz()
last_point = (0, 0)

# Main Loop

while True:
    mouse_clicked = False
    for event in pygame.event.get():
        if euc_dist(last_point, (mouse_x, mouse_y)) < large_dot_size:
            controls_disabled = True
        if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
            pygame.quit()
            sys.exit()
        elif event.type == MOUSEMOTION:
            mouse_x, mouse_y = event.pos
        elif event.type == MOUSEBUTTONUP and not controls_disabled:
            mouse_x, mouse_y = event.pos
            last_point = (mouse_x, mouse_y)
            mouse_clicked = True


    controls_disabled = False
   
    if mouse_clicked and mouse_within_large_window(mouse_x, mouse_y) and len(guess_point_set) < 3:
        pygame.draw.circle(DISPLAYSURF, RED, (mouse_x, mouse_y ), large_dot_size, 0)
        guess_point_set.append((int((mouse_x - large_window_offset)/2), int((mouse_y - large_window_offset)/2)))
        print("Guessing:", guess_point_set)
        if len(guess_point_set) >= 2:
            for j in range(len(guess_point_set)):
                pygame.draw.line(DISPLAYSURF, RED, (guess_point_set[j-1][0] * 2 + large_window_offset, guess_point_set[j-1][1] * 2 + large_window_offset), (guess_point_set[j][0] * 2 + large_window_offset, guess_point_set[j][1] * 2 + large_window_offset), 2)
        pygame.display.update()

            
    if len(guess_point_set) == 3: # round over
        avg_dist = compare_point_sets(guess_point_set, gen_point_set)
        print(avg_dist)
        #score = int(1000000 / max(avg_dist, 1))
        score = int(logarithmic(avg_dist))
        current_time = time.strftime("%d/%m/%Y", time.gmtime()) #day month year
        with open("geomemory_highscores.txt", "a+") as textfile:
            textfile.write(str(score) + " " + current_time + '\n')
        draw_score(score)
        
        pygame.time.wait(3500)
        not_printed = False
        new_quiz()
        
#TODO: show score when mouse hovers over point on graph
#TODO: add 'main' function
#TODO: add comments
#TODO: seperate out functions, optimize for readability
#TODO: add a seperate highscore screen
#TODO: allow guess points to be moved after placement
#TODO: add a difficulty setting and difficulty high scores OR add rounds (with progressive difficulty)
#TODO: add nerdy music, ie chiptune
