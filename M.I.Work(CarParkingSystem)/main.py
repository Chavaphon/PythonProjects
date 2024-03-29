

discount = 1
DaysPassed = 1
SpotUsed = []
frequency = {}
dailyTotal = 0
sameDay = False
MaxStayHour = {
    "sunday"    : 8,
    "sun"    : 8,
    "monday"    : 2,
    "mon"    : 2,
    "tuesday"    : 2,
    "tue"    : 2,
    "wednesday"    : 2,
    "wed"    : 2,
    "thursday"    : 2,
    "thu"    : 2,
    "friday"    : 2,
    "fri"    : 2,
    "saturday"  : 4,
    "sat"  : 4,
}
PricePerHour = {
    "sunday"    : 2,
    "sun"    : 2,
    "monday"    : 10,
    "mon"    : 10,
    "tuesday"    : 10,
    "tue"    : 10,
    "wednesday"    : 10,
    "wed"    : 10,
    "thursday"    : 10,
    "thu"    : 10,
    "friday"    : 10,
    "fri"    : 10,
    "saturday"  : 3,
    "sat"  : 3,
}
try:
    while 1:

#New day
        print(f"day {DaysPassed}")

        if sameDay == True:
            day = today
            print(f"Today is {day}")
        else:
            day = input(f"Day: ")
            today = day

        if day.lower() in MaxStayHour:
            try:
                time = float(input(f"Time of arrival: "))
                while time > 24 or time < 8:
                    time = float(input(f"That time is closed: "))
                    continue
                duration = float(input(f"Duration: "))
            except ValueError:
                print("Those are not numbers!")
                continue
            spotSelected = int(input(f"Parking spot(4-digits): "))
            z = str(spotSelected)
            z = [i for i in z]
            while len(z) < 4 or len(z) > 4:
                spotSelected = int(input(f"4-digits please: "))
                z = str(spotSelected)
                z = [i for i in z]

# Modulo 11
            z4 = spotSelected % 10
            spotSelected = spotSelected // 10
            z3 = spotSelected % 10
            spotSelected = spotSelected // 10
            z2 = spotSelected % 10
            spotSelected = spotSelected // 10
            z1 = spotSelected
            sum = z1 + z2 + z3 + z4
            SpotOccupied = sum % 11
            SpotUsed.append(SpotOccupied)

# Spot frequency check
            for spot in SpotUsed:
                if spot in frequency:
                    frequency[spot] += 1
                else:
                    frequency[spot] = 1

#Morning
            if time <= 16 and time >= 8:
                if duration <= MaxStayHour[day]:

#Discount
                    if frequency[SpotOccupied] > 3:
                        discount = 0.9
                        print("Discount applied!")
                    else:
                        discount = 1
                    price = duration * PricePerHour[day] * discount
                    print(f"Price: {price}\n")
                else:
                    print(f"You can't stay THAT long\n")
                    print("\n")
                    continue

#Evening
            elif time > 16:
                MidnightMaxStayHour = 24 - time
                if duration <= MidnightMaxStayHour:

#Discount
                    if frequency[SpotOccupied] > 3:
                        discount = 0.5
                        print("Discount applied!")
                    else:
                        discount = 1
                    price = duration * 2 * discount
                    print(f"Price: {price}\n")
                else:
                    print(f"You can't stay THAT long\n")
                    print("\n")
                    continue

#Amount to pay
            amountPayed = float(input("How much will you pay: "))
            while amountPayed < price:
                amountPayed = int(input("That amount is less than the price, enter again: "))
            dailyTotal += int(amountPayed)
            endDay = str(input("Payed. Next day?: "))
            if endDay == "" or endDay == "yes":
                sameDay = False
                print("\n")
                print(f"Amount of money we got today: {dailyTotal}$")
                dailyTotal = 0
                DaysPassed += 1
            else:
                sameDay = True
        else:
            print(f"What day is {day}?!\n")
            print("\n")
except KeyboardInterrupt:
    print(f"Terminated")
