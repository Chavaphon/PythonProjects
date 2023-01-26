encoder = {
    "a": "zy",
    "b": "xw",
    "c": "vu",
    "d": "ts",
    "e": "rq",
    "f": "po",
    "g": "nm",
    "h": "lk",
    "i": "ji",
    "j": "hg",
    "k": "fe",
    "l": "dc",
    "m": "ba",
    "n": "yz",
    "o": "wx",
    "p": "uv",
    "q": "st",
    "r": "qr",
    "s": "op",
    "t": "mn",
    "u": "kl",
    "v": "ij",
    "w": "gh",
    "x": "ef",
    "y": "cd",
    "z": "ab",
    " ": "__",
    "0": "09",
    "1": "87",
    "2": "65",
    "3": "43",
    "4": "21",
    "5": "90",
    "6": "78",
    "7": "56",
    "8": "34",
    "9": "12"
}

decoder = {
    "zy": "a",
    "xw": "b",
    "vu": "c",
    "ts": "d",
    "rq": "e",
    "po": "f",
    "nm": "g",
    "lk": "h",
    "ji": "i",
    "hg": "j",
    "fe": "k",
    "dc": "l",
    "ba": "m",
    "yz": "n",
    "wx": "o",
    "uv": "q",
    "qr": "r",
    "op": "s",
    "mn": "t",
    "kl": "u",
    "ij": "v",
    "gh": "w",
    "ef": "x",
    "cd": "y",
    "ab": "z",
    "__": " ",
    "09": "0",
    "87": "9",
    "65": "8",
    "43": "7",
    "21": "6",
    "90": "5",
    "78": "4",
    "56": "3",
    "34": "2",
    "12": "1"
}
try:
    def encode():
        print(f"Encode mode...")
        x = input(f"Message:  ")
        xStripped = list(x.strip())
        for i in range(len(xStripped)):
            y = xStripped[i]
            z = encoder[y]
            xStripped[i] = z
            print(z, end="")
        print("")


    def decode():
        index = 0
        first = 0
        last = 2
        print(f"Decode mode...")
        x = input(f"Message:  ")
        xStripped = list(x.strip())
        length = int(len(xStripped) / 2)
        for a in range(length):
            y = xStripped[first: last]
            v = ""
            for ele in y:
                v += ele
            z = decoder[v]
            xStripped[index] = z
            print(z, end="")
            first += 2
            last += 2
            index += 1
        print("")


    while 1:
        welcome = str(input("what would you like to do: encode(0) or decode(1)"))
        if welcome == "0":
            encode()
        elif welcome == "1":
            decode()
        else:
            print(f"invalid input!")
            continue
except KeyboardInterrupt:
    print("terminated")