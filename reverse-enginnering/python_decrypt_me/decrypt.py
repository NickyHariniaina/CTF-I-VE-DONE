import base64

f = open("helloworld_encrypted.py", "r")
text = f.read()

def find_string(text):
    i = -1
    while True:
        i = i + 1
        if text[i] == "\'":
            start = i + 1
            break
    while True:
        i = i + 1
        if text[i] == "\'":
            end = i
            break
    string = text[start:end]
    return string

while True:
    string = find_string(text)
    if string:
        try:
            text = base64.b64decode((base64.b32decode((base64.b16decode((string))))))
            text = text.decode()
        except:
            break

print(text)
