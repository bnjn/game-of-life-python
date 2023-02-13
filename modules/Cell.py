class Cell():
    
    def __init__(self) -> None:
        self.alive = True

    def die(self) -> bool:
        self.alive = False