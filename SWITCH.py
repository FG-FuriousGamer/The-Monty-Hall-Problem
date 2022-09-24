import random
i = 0
WIN = 0
LOOSE = 0
while i<=1000:
    doors = ["goat", "goat", "PRIZE"]
    SELECTION = random.choice(doors)
    doors.remove(SELECTION)
    doors.remove("goat")
    print(doors)
    if "goat" in doors and "PRIZE" in SELECTION:
        print("switch didnt work")
        LOOSE += 1
    elif "goat" in SELECTION and "PRIZE" in doors:
        print("switching was successful")
        WIN += 1
    i+=1
print("your losses were:"+str(LOOSE))
print("your wins were:"+str(WIN))