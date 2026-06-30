s = open('enc').read()

for c in s:
    print(chr(ord(c) >> 8) + chr(ord(c) & 0xFF), end='')
