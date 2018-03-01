from state import GlobalState

class Editor(object):
    def __init__(self, filename):
        self.state = GlobalState(filename)
        self.read_file(filename)

    def read_file(self, filename):
        temp_file = open(filename, 'r')

        #check if file exists
        if not temp_file:
            temp_file.close()
            print("Nothing in here...")
            return

        #read file line by line
        for line in temp_file:
            self.state.add_line()
            print(line)
