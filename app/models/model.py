import random
from random import shuffle


def password(hash):
    arr = []
    num = 0
    count = -1
    word = ""
    chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    special = "!@#$%^&*"
    if hash['characters'] == "10":
        arr = ['','','','','','','','','','']
        if hash['uppercase'] == "Yes":
            letter = random.choice(chars)
            arr[0] = letter
            letter = random.choice(chars)
            arr[1] = letter
            letter = random.choice(chars)
            arr[2] = letter
        if hash['numbers'] == "Yes":
            num = str(random.randint(0,9))
            arr[3] = num
            num = str(random.randint(0,9))
            arr[4] = num
        if hash['special'] == "Yes":
            special = random.choice(special)
            arr[5] = special
        if len(str(arr)) != 10:
            for n in arr:
                count += 1
                if arr[count] == '':
                    new = random.choice(chars.lower())
                    arr[count] = arr[count].replace(arr[count],new)
    elif hash['characters'] == "8":
        arr = ['','','','','','','','']
        if hash['uppercase'] == "Yes":
            letter = random.choice(chars)
            arr[0] = letter
            letter = random.choice(chars)
            arr[1] = letter
            letter = random.choice(chars)
            arr[2] = letter
        if hash['numbers'] == "Yes":
            num = str(random.randint(0,9))
            arr[3] = num
            num = str(random.randint(0,9))
            arr[4] = num
        if hash['special'] == "Yes":
            special = random.choice(special)
            arr[5] = special
        if len(str(arr)) != 8:
            for n in arr:
                count += 1
                if arr[count] == '':
                    new = random.choice(chars.lower())
                    arr[count] = arr[count].replace(arr[count],new)
    else:
        arr = ['','','','','','']
        if hash['uppercase'] == "Yes":
            letter = random.choice(chars)
            arr[0] = letter
            letter = random.choice(chars)
            arr[1] = letter
            letter = random.choice(chars)
            arr[2] = letter
        if hash['numbers'] == "Yes":
            num = str(random.randint(0,9))
            arr[3] = num
            num = str(random.randint(0,9))
            arr[4] = num
        if hash['special'] == "Yes":
            special = random.choice(special)
            arr[5] = special
        if len(str(arr)) != 6:
            for n in arr:
                count += 1
                if arr[count] == '':
                    new = random.choice(chars.lower())
                    arr[count] = arr[count].replace(arr[count],new)
    word = "".join(arr)
    return word
