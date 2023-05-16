Divisor = {
    3 : "Fizz",
    5 : "Buzz"
}
for i in range(1, 100):
    x = ""
    for ele in Divisor:
        if i % ele == 0:
            x += Divisor[ele]
    if x == "":
        x += str(i)
    print(f"{x}\n")
