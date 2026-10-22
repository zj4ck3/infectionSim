class Person:
    def __init__(self, status:str) -> None:
        self.change_status(status)
        return

    def change_status(self, status: str):
        self.days_in_state = 0

        if status == "susceptible":
            self.status = status
            self.id = 1
            self.color = (0, 0, 255) # blue
        elif status == "infected":
            self.status = status
            self.id = 2
            self.color = (255, 0, 0) # red
        elif status == "carrier":
            self.status = status
            self.id = 3
            self.color = (255, 255, 0) # yellow
        elif status == "immune":
            self.status = status
            self.id = 4
            self.color = (0, 255, 0) # green
        elif status == "dead":
            self.status = status
            self.id = 5
            self.color = (64,32,0) # brown
        elif status == "recovered":
            self.status = status
            self.id = 6
            self.color = (255,0,255) # fucsia
        else:
            raise ValueError("invalid status")
        return

    def calculate_change(self) -> str: # it change the type of person based on probability
        return self.status