import sys

from editor import Editor

def main():
    if len(sys.argv) < 2:
        print("This isn't terminal 101... what the file?")
        return(1)
    filename = sys.argv[1]
    editor_in = Editor(filename)
    return(0)

if __name__ == "__main__":
    main()
