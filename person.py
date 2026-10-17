class Person:
    def __init__(self, status:str) -> None:
        self.status = status

        # to complete, non only with id
        if status == "healty":
            self.id = 1
            self.color = (0, 255, 0) # green
        elif status == "sick":
            self.id = 2
            self.days = 0 # days of sickness
            self.color = (255, 0, 0) # red
        elif status == "carrier":
            self.id = 3
            self.days = 0 # days of carrier
            self.color = (255, 255, 0) # yellow
        elif status == "vaccinated":
            self.id = 4
            self.color = (0, 0, 255) # blue
        else:
            raise ValueError("invalid status")
        return

    def calculate_change(self) -> None: # it change the type of person based on probability
        pass