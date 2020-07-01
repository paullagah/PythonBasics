class Bird:
    def __init__(self, wingspan):
        self.wingspan = wingspan

    def __len__(self):
        return self.wingspan

Eagle = Bird(104)

print(len(Eagle))
