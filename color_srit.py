import pygame

def main():
    pygame.init()
    screen_widih, screen_height = 600,700
    screen = pygame.display.set_mode((screen_widih, screen_height))
    pygame.display.set_caption('color changing sprite')

    colors = {

        'red':pygame.Color('red'),
        'green':pygame.Color('green'),
        'blue':pygame.Color('blue'),
        'yellow':pygame.Color('yellow'),
        'white':pygame.Color('white'),
        
    }
    current_color = colors['white']

    x, y = 30,30
    sprite_widih, sprite_height = 70 , 70

    clock = pygame.time.Clock()

    done = False
    while not done:
        for event in pygame.event.get():
            if event .type == pygame.QUIT():
                done = True
        pressed = pygame.key.get_pressed()