#compound interest calculator
principle = 0
rate = 0
time = 0

while principle <= 0:
    principle = float(input("Enter the principle Amount: "))
    if principle <= 0:
        print("Principle amount can not be less than or equal to zero")

while rate <= 0:
    rate = float(input("Enter the Interest rate: "))
    if rate <= 0:
        print("Interest rate can not be less than or equal to zero")

while time <= 0:
    time = int(input("Enter the time in years: "))
    if time <= 0:
        print("Time can not be less than or equal to zero")

total = principle * pow((1 + rate/100), time)
print(f"Balance after {time} year's = {total:.2f} ")


