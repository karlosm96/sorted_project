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
    SIDE_PAD = 100
    TOP_PAD = 120

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

        self.pixel_width = round((self.SIDE_PAD - self.width) / len(lst)) ##determines the width of each pixel that will represent the values of the list
        self.pixel_height = round((self.height - self.TOP_PAD) / (self.max_value - self.min_value))
        self.start_draw_x = self.SIDE_PAD // 2

##generate the list that is going to be sorted
def generation_list(n, min_val, max_val):
    lst = []

    for _ in range(n):
        val = random.randint(min_val, max_val)
        lst.append(val)
    
    return lst

##main function where is going to draw the algorithm process
def main():
    run = True
    clock = pygame.time.Clock()
    lst = generation_list(50, 1, 50)
    draw_information = screen_information(600, 400, lst)

    while run:
        clock.tick(60)

        pygame.display.update()

        for event in pygame.event.get():
            if event == pygame.QUIT:
                run = False

    pygame.quit()

if __name__ == "__main__":
    main() 


