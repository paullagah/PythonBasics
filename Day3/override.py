class Bird:
    babies = 0

    def reproduce(self):
        self.babies += 1

class Pigeon(Bird):
    def reproduce(self):
        self.babies += 6

pidgey = Pigeon()
pidgey.reproduce()
print(pidgey.babies)