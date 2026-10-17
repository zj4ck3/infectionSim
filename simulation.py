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
        print("\n[#] Info configuration:")
        self.diseaseConstants = {"density": 0.0, "gathering": 0.0, "healthy": 0.0, "vaccinated": 0.0, "carrier": 0.0, "sick": 0.0, "mortality":0.0}
        self.diseaseConstants["density"] = round(int(input("[1/7 - ?] Insert your population density (0 - 100): "))/100,2)
        self.diseaseConstants["gathering"] = round(int(input("[2/7 - ?] Insert your gathering density (0-100): "))/100,2)
        self.diseaseConstants["healthy"] = round(int(input("[3/7 - ?] Insert your healthy people density (0-100): "))/100,2)
        self.diseaseConstants["vaccinated"] = round(int(input("[4/7 - ?] Insert your vaccinated people density (0-100): "))/100,2)
        self.diseaseConstants["carrier"] = round(int(input("[5/7 - ?] Insert your carrier people density (0-100): "))/100,2)
        self.diseaseConstants["sick"] = round(int(input("[6/7 - ?] Insert your sick people density (0-100): "))/100,2)
        self.diseaseConstants["mortality"] = round(int(input("[7/7 - ?] Insert your mortality rate (0-100): "))/100,2)

        control = list(self.diseaseConstants.values())
        for value in control:
            if value < 0 or value > 1:
                raise ValueError("[X] All values must be between 0 and 100.")
        if sum(control[2:5]) > 1:
            raise ValueError("[X] The sum of all values must not exceed 100.")
        
        print("[V] Configuration completed correctly")
        print("[#] Initializing grid...")
        return

    def draw(self) -> None:
        screen_width, screen_height = self.screen.get_size()
        rows, columns = self.matrix.shape

        # Calculate a single size for square cells
        cell_size = min(
            screen_width / columns,
            screen_height / rows
        )

        # Center the grid in the window
        grid_width = columns * cell_size
        grid_height = rows * cell_size
        offset_x = (screen_width - grid_width) / 2
        offset_y = (screen_height - grid_height) / 2

        # Draw the cells
        for row in range(rows):
            for column in range(columns):
                x = round(offset_x + column * cell_size)
                y = round(offset_y + row * cell_size)
                next_x = round(offset_x + (column + 1) * cell_size)
                next_y = round(offset_y + (row + 1) * cell_size)

                cell = pygame.Rect(
                    x,
                    y,
                    next_x - x,
                    next_y - y
                )

                person = self.matrix[row, column]

                if person is None or person == 0:
                    cell_color = self.BLACK
                else:
                    cell_color = person.get_color()

                pygame.draw.rect(self.screen, cell_color, cell)

        # Draw subtle grid lines only once
        grid_color = (45, 45, 45)

        for column in range(columns + 1):
            x = round(offset_x + column * cell_size)
            pygame.draw.line(
                self.screen,
                grid_color,
                (x, round(offset_y)),
                (x, round(offset_y + grid_height)),
                1
            )

        for row in range(rows + 1):
            y = round(offset_y + row * cell_size)
            pygame.draw.line(
                self.screen,
                grid_color,
                (round(offset_x), y),
                (round(offset_x + grid_width), y),        1
            )

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