class BaloneyInterpreter(object):
    def __init__(self, prog):
        self.prog = prog
    
    def run(self):
        self.vars = {}            # All variables
        self.lists = {}            # List variables
        self.error = 0              # Indicates program error

        self.stat = list(self.prog)  # Ordered list of all line numbers
        self.stat.sort()
        print(self.stat)
