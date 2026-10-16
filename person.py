class Person:
    def __init__(self, status:str) -> None:
        self.status = status

        # to complete, non only with id
        if status == "healty":
            self.id = 1
        elif status == "sick":
            self.id = 2
            self.days = 0 # days of sickness
        elif status == "carrier":
            self.id = 3
            self.days = 0 # days of carrier
        elif status == "vaccinated":
            self.id = 4
        else:
            raise ValueError("invalid status")
        return

    def get_color(self) -> tuple: # from status return the color of cell
        pass

    def calculate_change(self) -> None: # it change the type of person based on probability
        pass