class Symbol:
    def __init__(self, char = 'e'):
        if len(char) > 1 or not isinstance(char, str):
            raise Exception('Symbol is must large')
        self.char = char

    def getChar(self):
        return self.char

    def __eq__(self, other):
        return self.char == other.getChar()
    
    def __str__(self):
        return self.char

