from person import Person
import pygame
import numpy

class Simulation:
    def __init__(self, SHAPE:tuple) -> None:
        self.SHAPE = self.WIDTH, self.HEIGHT = SHAPE
        self.matrix = numpy.zeros(self.SHAPE)
        
        self.WINDOW_SIZE = (1200, 800) # width, height
        self.BLACK = (0, 0, 0)
        return
    
    def init_grid(self) -> None: # for random population based on constant
        pass

    def draw(self) -> None: # draw the matrix
        screen_width, screen_height = self.screen.get_size()
        cell_width = screen_width / self.SHAPE[0]
        cell_height = screen_height / self.SHAPE[1]

        for row in range(self.SHAPE[1]):
            for column in range(self.SHAPE[0]):
                cell = pygame.Rect(
                    round(column * cell_width),
                    round(row * cell_height),
                    round((column + 1) * cell_width) - round(column * cell_width),
                    round((row + 1) * cell_height) - round(row * cell_height),
                )
        
                # change the color based on type of cell
                if self.matrix[row,column] == 0:
                    cell_color = self.BLACK
                else:
                    cell_color = self.matrix[row,column].get_color()
                
                pygame.draw.rect(self.screen, cell_color, cell)
                pygame.draw.rect(self.screen, (255,255,255), cell, width=1)

    def update(self) -> None: # update the matrix
        pass

    def run(self) -> None: # run the app
        pygame.init()
        self.screen = pygame.display.set_mode(self.WINDOW_SIZE, pygame.RESIZABLE)
        pygame.display.set_caption("Infection simulation")
        self.clock = pygame.time.Clock()
        
        running = True
        paused = False

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                elif event.type == pygame.KEYDOWN:
                    # SPACE -> pause / resume
                    if event.key == pygame.K_SPACE:
                        paused = not paused

            self.screen.fill(self.BLACK)
            self.draw()
            pygame.display.flip()
            self.clock.tick(5)

        pygame.quit()

    def info(self) -> None: # display information
        pass