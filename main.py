import pygame
import random
pygame.init()

class screen_information:
    BLACK = 0, 0, 0
    WHITE = 255, 255, 255
    GREY = 128, 128, 128
    RED = 255, 0, 0
    GREEN = 0, 255, 0
    BACKGROUND_COLOR = WHITE

    RECTANGULAR_GRADIENTS = [
        (128, 128, 128),
        (160, 160, 160),
        (192, 192, 192)
    ]

    SIDE_PAD = 100
    TOP_PAD = 150

    def __init__(self, height, width, lst):
        self.height = height
        self.width = width
        self.window = pygame.display.set_mode((width, height)) ## display a window
        pygame.display.set_caption("Sorting Algorothm")
        self.set_list(lst)
    
    def set_list(self, lst):
        self.lst = lst
        self.min_value = min(lst)
        self.max_value = max(lst)

        self.pixel_width = round((self.width - self.SIDE_PAD) / len(lst)) ##determines the width of each pixel that will represent the values of the list
        self.pixel_height = round((self.height - self.TOP_PAD) / (self.max_value - self.min_value))
        self.start_draw_x = self.SIDE_PAD // 2

##generate the list that is going to be sorted
def generation_list(n, min_val, max_val):
    lst = []

    for _ in range(n):
        val = random.randint(min_val, max_val)
        lst.append(val)
    
    return lst

##change tha screen attributes
def draw(draw_information):
    draw_information.window.fill(draw_information.BACKGROUND_COLOR)
    draw_list(draw_information)
    pygame.display.update()

    ##--------------------------

def draw_list(draw_information):
    lst = draw_information.lst
    
    for i, val in enumerate(lst):
        x = draw_information.start_draw_x + i * draw_information.pixel_width  ###
        y = draw_information.height - (val - draw_information.min_value) * draw_information.pixel_height ###

        color = draw_information.RECTANGULAR_GRADIENTS[i % 3]

        pygame.draw.rect(draw_information.window, color, (x, y, draw_information.pixel_width, draw_information.height))

##main function where is going to draw the algorithm process
def main():
    run = True
    clock = pygame.time.Clock()
    lst = generation_list(100, 1, 20)
    draw_information = screen_information(500, 600, lst)

    while run:
        clock.tick(60)
        draw(draw_information)

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

    pygame.quit()

if __name__ == "__main__":
    main() 


