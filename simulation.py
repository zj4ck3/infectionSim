class Simulation:
    def __init__(self, SHAPE:tuple) -> None:
        import numpy
        import pygame
        
        self.SHAPE = self.WIDTH, self.HEIGHT = SHAPE
        self.matrix = numpy.zeros(self.SHAPE)
        return

    def draw(self) -> None: # draw the matrix
        pass

    def update(self) -> None: # update the matrix
        pass

    def run(self) -> None: # run the app
        pass

    def info(self) -> None: # display information
        pass