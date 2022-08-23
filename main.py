import math
import pygame
import random
pygame.init()

class screen_information:
    BLACK = 0, 0, 0
    WHITE = 255, 255, 255
    GREY = 128, 128, 128
    YELLOW = 255,196,12
    BLUE = 65,105,225
    RED = 	(255,0,0)
    BACKGROUND_COLOR = WHITE

    RECTANGULAR_GRADIENTS = [
        (128, 128, 128),
        (160, 160, 160),
        (198, 198, 198)
    ]

    STANDAR_FONT = pygame.font.SysFont("arial", 30)
    LARGE_FONT = pygame.font.SysFont("arial", 45)
    SIDE_PAD = 100
    TOP_PAD = 150

    def __init__(self, height, width, lst):
        self.height = height
        self.width = width
        self.window = pygame.display.set_mode((width, height)) ## display a window
        pygame.display.set_caption("Sorting Algorithms")
        self.set_list(lst)
    
    def set_list(self, lst):
        self.lst = lst
        self.min_value = min(lst)
        self.max_value = max(lst)

        self.pixel_width = round((self.width - self.SIDE_PAD) / len(lst)) ##determines the width of each pixel that will represent the values of the list
        self.pixel_height = math.floor((self.height - self.TOP_PAD) / (self.max_value - self.min_value))
        self.start_draw_x = self.SIDE_PAD // 2

##generate the list that is going to be sorted
def generation_list(n, min_val, max_val):
    lst = []

    for _ in range(n):
        val = random.randint(min_val, max_val)
        lst.append(val)
    
    return lst

##change tht screen attributes
def draw(draw_information, sort_algo_name, ascending):
    draw_information.window.fill(draw_information.BACKGROUND_COLOR)

    ##Titles - top of the screen
    title_algo = draw_information.STANDAR_FONT.render(f"{sort_algo_name} - {'Ascending' if ascending else 'Descending'}", 1, draw_information.RED)
    draw_information.window.blit(title_algo, (draw_information.width/2 - title_algo.get_width()/2, 0))

    title_controls = draw_information.STANDAR_FONT.render(">>> R = Restart || Space = Init sorting || A = Ascending sorting || D = Descending sorting <<<", 1, draw_information.BLACK)
    draw_information.window.blit(title_controls, (draw_information.width/2 - title_controls.get_width()/2, 35))  ## blit the tittle
    
    sorting = draw_information.STANDAR_FONT.render("I = Insertion sort || B = Bubble sort || S = Shell sort" , 1, draw_information.BLACK)
    draw_information.window.blit(sorting, (draw_information.width/2 - sorting.get_width()/2, 65))

    draw_list(draw_information)
    pygame.display.update()

    ##--------------------------

def draw_list(draw_information, position_color = {}, clear_background = False):
    lst = draw_information.lst

    ##Clear the part of the window
    if clear_background:
        clear_square = (draw_information.SIDE_PAD // 2, draw_information.TOP_PAD, 
                        draw_information.width - draw_information.SIDE_PAD, draw_information.height - draw_information.TOP_PAD)

        pygame.draw.rect(draw_information.window, draw_information.BACKGROUND_COLOR, clear_square)

    
    for i, val in enumerate(lst):
        x = draw_information.start_draw_x + i * draw_information.pixel_width  ###
        y = draw_information.height - (val - draw_information.min_value) * draw_information.pixel_height ###

        color = draw_information.RECTANGULAR_GRADIENTS[i % 3]

        if i in position_color:
            color = position_color[i]

        pygame.draw.rect(draw_information.window, color, (x, y, draw_information.pixel_width, draw_information.height))
        
    
    if clear_background:
        pygame.display.update()


def bubble_sort(draw_information, ascending = True):
    lst = draw_information.lst

    for i in range(len(lst) - 1):
        for j in range(len(lst) - 1 - i):
            num_1 = lst[j]
            num_2 = lst[j + 1]

            if (num_1 > num_2 and ascending) or (num_1 < num_2 and not ascending):
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
                draw_list(draw_information, {j: draw_information.BLUE, j + 1: draw_information.YELLOW}, True)
                print(lst)
                yield True
    print("\n###------------------------------------------###")
    return lst


def shell_sort(draw_information, ascending = True):
    lst = draw_information.lst
    n = len(lst)

    # Rearrange elements at each n/2, n/4, n/8, ... intervals
    interval = n // 2
    while interval > 0:
        for i in range(interval, n):
            temp = lst[i]
            j = i
            
            while (j >= interval and lst[j - interval] > temp and ascending) or (j >= interval and lst[j - interval] < temp and not ascending):
                lst[j] = lst[j - interval]
                j -= interval

            lst[j] = temp
            draw_list(draw_information, {j - 1: draw_information.YELLOW, j: draw_information.BLUE}, True)
            print(lst)
        interval //= 2
        yield True

    print("\n###------------------------------------------###")
    return lst


def insertion_sort(draw_information, ascending = True):
    lst = draw_information.lst

    for i in range(1, len(lst)):
        current = lst[i]

        while True:
            ascending_sort = i > 0 and lst[i - 1] > current and ascending
            descending_sort = i > 0 and lst[i - 1] < current and not ascending

            if not ascending_sort and not descending_sort:
                break

            lst[i] = lst[i - 1]
            i = i - 1
            lst[i] =  current
            draw_list(draw_information, {i - 1: draw_information.YELLOW, i: draw_information.BLUE}, True)
            print(lst)
            yield True

    print("\n###------------------------------------------###")
    return lst

##main function: draw the algorithm process
def main():
    run = True
    sorting = False
    ascending = False
    clock = pygame.time.Clock()
    min_list = 1
    max_list = 100
    num_iterations = 50
    lst = generation_list(num_iterations, min_list, max_list)
    draw_information = screen_information(600, 1200, lst)

    sort_algo = insertion_sort
    sort_algo_name = "Insertion Sort Algorithm"
    sort_algo_generator = None

    while run:
        clock.tick(120)
        
        if sorting:
            try:
                next(sort_algo_generator)
            except StopIteration:
                sorting = False
        else:
            draw(draw_information, sort_algo_name, ascending) ## now you can use another instruction(control)

        pygame.display.update()

        ##Controls
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            
            if event.type != pygame.KEYDOWN:
                continue

            if event.key == pygame.K_r:  ## charge a new list and restart the visualization  
                lst = generation_list(num_iterations, min_list, max_list)
                draw_information.set_list(lst)
                sorting = False
            
            elif event.key == pygame.K_SPACE and sorting == False:
                sorting = True
                sort_algo_generator = sort_algo(draw_information, ascending)
            
            elif event.key == pygame.K_a and not sorting: 
                ascending = True
            elif event.key == pygame.K_d and not sorting: 
                ascending = False

            elif event.key == pygame.K_i and not sorting: 
                sort_algo = insertion_sort
                sort_algo_name = "Insertion Sort Algorithm"
            elif event.key == pygame.K_b and not sorting: 
                sort_algo = bubble_sort
                sort_algo_name = "Bubble Sort Algorithm"
            elif event.key == pygame.K_s and not sorting: 
                sort_algo = shell_sort
                sort_algo_name = "Shell Sort Algorithm"
            

    pygame.quit()

if __name__ == "__main__":
    main() 


