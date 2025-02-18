import sys
with open(sys.argv[1], "rb") as f:
    for i, c in enumerate(f.read()):
        if chr(c) == '\n':
            print()
            break
        print(chr(c - i), end='')
