import sys


def indices(l1, l2, matrix):
    for i in range(5):
        for j in range(5):
            if matrix[i][j] == l1:
                x1 = i
                y1 = j
            if matrix[i][j] == l2:
                x2 = i
                y2 = j
    return x1, y1, x2, y2


def createMatrix(keyword):
    keyword = "".join(sorted(set(keyword), key=keyword.index))
    matrix = [[0 for x in range(5)] for y in range(5)]
    row = 0
    col = 0
    for letter in keyword:
        matrix[row][col] = letter
        if col == 4:
            row += 1
            col = 0
        else:
            col += 1
    for num in range(65, 91):
        if num == 74:
            continue
        if chr(num) not in keyword:
            matrix[row][col] = chr(num).upper()
            if col == 4:
                row += 1
                col = 0
            else:
                col += 1
    return matrix


def divide(text):
    text = "".join(text.split())
    text.replace("J", "I")
    text = "".join(l for l in text if l.isalpha())
    tmp = []
    i = 0
    while i < len(text):
        if i == len(text) - 1:
            tmp.append(text[i] + "X")
            i += 1
        else:
            tmp.append(text[i : i + 2])
            i += 2
    return tmp


def cipher(msg, key, encrypt=True):
    mv = 1 if encrypt == True else -1
    matrix = createMatrix(key)
    msg = divide(msg)
    result = ""
    for pair in msg:
        letter1 = pair[0]
        letter2 = pair[1]
        x1, y1, x2, y2 = indices(letter1, letter2, matrix)
        if x1 == x2:
            result += matrix[x1][(y1 + mv) % 5]
            result += matrix[x2][(y2 + mv) % 5]
        elif y1 == y2:
            result += matrix[(x1 + mv) % 5][y1]
            result += matrix[(x2 + mv) % 5][y2]
        else:
            result += matrix[x1][y2]
            result += matrix[x2][y1]
    return result


def takeInput(msg, opt1, opt2):
    valid = False
    while not valid:
        inp = input(msg).lower()
        valid = True if inp == opt1 or inp == opt2 else False
        if not valid:
            print("Error: Incorrect input\n")
    return inp


if __name__ == "__main__":
    action = takeInput("Enter e to encode the text or d to decode it: ", "e", "d")
    if len(sys.argv) > 1:
        try:
            inputFile = open(sys.argv[1], "r")
            keyword = inputFile.readline().upper().strip()
            message = inputFile.read().upper().strip()
        except:
            print("Error: Problem with reading from file")
            sys.exit()
    else:
        keyword = input("Enter the keyword: ").upper()
        message = (
            input("Enter the message to encrypt: ").upper()
            if action == "e"
            else input("Enter the message to decrypt: ").upper()
        )

    if action == "e":
        result = cipher(message, keyword, True)
        if len(sys.argv) > 2:
            outputFile = open(sys.argv[2], "w")
            outputFile.write(result)
        else:
            print("--------------------------\nEncrypted message: \n" + str(result))
    else:
        result = cipher(message, keyword, False)
        if len(sys.argv) > 2:
            outputFile = open(sys.argv[2], "w")
            outputFile.write(result)
        else:
            print("--------------------------\nDecrypted message: \n" + str(result))
