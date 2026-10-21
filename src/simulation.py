from person import Person
import pygame
import random
import numpy

class Simulation:
    def __init__(self, SHAPE:tuple) -> None:
        self.SHAPE = self.WIDTH, self.HEIGHT = SHAPE
        self.matrix = numpy.full(self.SHAPE, None, dtype=object) # full the matrix with None
        
        self.WINDOW_SIZE = (1200, 800) # width, height
        self.BLACK = (0, 0, 0)
        self.neighbour = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        return

    def prompt_percentage(self, label: str) -> float: # for user handling in ask_pre_info
        while True:
            answer = input(f"[?] {label} (0-100%): ")
            try:
                percentage = int(answer)
            except ValueError:
                print("[X] Please enter a whole number from 0 to 100.\n")
                continue

            if 0 <= percentage <= 100:
                return percentage / 100
            print("[X] Please enter a value from 0 to 100.\n")
        return
    
    def ask_pre_info(self) -> None: # ask user before start some variables
        print("\n[#] Info configuration:")
        self.diseaseConstants = {"density": 0.0, "healthy": 0.0, "vaccinated": 0.0, "carrier": 0.0, "sick": 0.0, "mortality":0.0}
        self.diseaseConstants["density"] = self.prompt_percentage("Population density")

        while True:
            self.diseaseConstants["healthy"] = self.prompt_percentage("Healthy people")
            self.diseaseConstants["vaccinated"] = self.prompt_percentage("Vaccinated people")
            self.diseaseConstants["carrier"] = self.prompt_percentage("Carrier people")
            self.diseaseConstants["sick"] = self.prompt_percentage("Sick people")
            status_total = sum(list(self.diseaseConstants.values())[1:5])

            if status_total == 1:
                break
            print("[X] Those percentages together don't make 100%. Please enter them again.\n")

        self.diseaseConstants["mortality"] = self.prompt_percentage("Mortality rate")        
        print("\n[V] Configuration completed correctly")
        print("[#] Initializing grid...")
        return

    def init__grid(self) -> None: # initialize the grid with people based on the density and proportions
        # Total population based on density
        population = round(self.SHAPE[0] * self.SHAPE[1] * self.diseaseConstants["density"])
        statuses = ["healthy", "vaccinated", "carrier", "sick"]
        proportions = [self.diseaseConstants[s] for s in statuses]

        # Calculate the initial counts
        raw_counts = [population * p for p in proportions]
        counts_list = [int(n) for n in raw_counts]

        # Calculate how many people are missing
        # ES: 3,9 and 2.1 = 3,1 but 1 person is missing
        remaining = population - sum(counts_list)

        # Store each index with its decimal remainder
        # this is for redistribute the missing people based on largest decimal
        remainders = []
        for i in range(len(statuses)):
            remainder = raw_counts[i] - counts_list[i]
            remainders.append((i, remainder))

        # Sort from the largest remainder to the smallest
        remainders.sort(key=lambda item: item[1], reverse=True)

        # Distribute the missing people
        for i in range(remaining):
            index = remainders[i][0]
            counts_list[index] += 1

        counts = dict(zip(statuses, counts_list))
        # Generate all possible positions and shuffle them
        positions = [
            (x, y)
            for x in range(self.SHAPE[0])
            for y in range(self.SHAPE[1])
        ]
        random.shuffle(positions)

        # Assign people to random positions
        for i in range(population):
            while True:
                choice = random.choice(statuses)

                if counts[choice] > 0:
                    counts[choice] -= 1
                    break

            self.matrix[positions[i]] = Person(choice)
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
                    cell_color = person.color

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
        return

    def score_neighbours(self, row: int, column: int) -> tuple: # count the number of positive and negative neighbours for update
        return (0,0)

    def update(self) -> None: # update the matrix
        for row in range(self.SHAPE[0]):
            for column in range(self.SHAPE[1]):

                positive, negative = self.score_neighbours(row,column)
                person = self.matrix[row,column]

                if person is not None:
                    new_type = person.calculate_change()

                    if new_type != person.status:
                        if new_type is not None:
                            self.matrix[row,column] = Person(new_type)
                        else:
                            self.matrix[row,column] = None
        return

    def run(self) -> None:
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

            if not paused:
                self.update()
        pygame.quit()

    def info(self) -> None: # display information
        pass