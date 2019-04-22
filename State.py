class State:
    def __init__(self, name = 'error'):
        self.name = name

    def getName(self):
        return self.name

    def __eq__(self, other):
        return self.name == other.getName()

    def __repr__(self):
        return self.name

    def __hash__(self):
        return hash(self.name) 

    def __str__(self):
        return self.name