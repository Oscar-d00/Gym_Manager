
class Athletes:
    def __init__(self, name, weight, session, stage):
        self.name = str(name)
        self.weight = int(weight)
        self.session = int(session)
        self.stage = str(stage)

f = open("athletes.txt", "r")
print(f)
