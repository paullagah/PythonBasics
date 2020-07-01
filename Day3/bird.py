class Bird:
    def __init__(self, fly):
        self.fly = fly

class Owl(Bird):
    def __init__(self, fly, babies):
        Bird.__init__(fly)
        self.babies = babies

    def reproduce(self):
        self.babies += 1