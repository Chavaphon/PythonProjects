import time
z = list(str(input("String of letters: ")))
if len(z) == 0:
    z = ["o", "o", "o", "o", "o", "o", "o", "o", "o", "o"]
try:
    while 1:
        for i in range(len(z)):
            if z[i] != " ":
                z[i] = z[i].upper()
                print(f"\r{''.join(x for x in z)}", end="")
                z[i] = z[i].lower()
                time.sleep(0.3)
        for i in range(2, len(z)):
            if z[-i] != " ":
                z[-i] = z[-i].upper()
                print(f"\r{''.join(x for x in z)}", end="")
                z[-i] = z[-i].lower()
                time.sleep(0.3)
except KeyboardInterrupt:
    print(f"\rTerminated")