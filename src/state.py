class GlobalState (object):
    def __init__(self, filename):
        self.x = 0
        self.y = 0
        self.num_lines = 0
        self.filename = filename

    def add_line(self):
        self.num_lines += 1
