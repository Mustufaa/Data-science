kahani = ""
while True:
    data = input('Enter a story=>')
    if len(data) == 0:
        print("the end!")
        break
    kahani += data + "\n"
print("the real story:")
print(kahani)