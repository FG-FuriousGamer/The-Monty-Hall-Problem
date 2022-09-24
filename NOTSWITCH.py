import random
i = 0
WIN = 0
LOOSE = 0
while i<=100:
    doors = ["goat", "goat", "PRIZE"]
    SELECTION = random.choice(doors)
    doors.remove(SELECTION)
    doors.remove("goat")
    print(doors)
    if "PRIZE" in doors and "goat" in SELECTION:
        print("Should have switched")
        LOOSE += 1
    elif "PRIZE" in SELECTION and "goat" in doors:
        print("not switching was the right choice")
        WIN += 1
    i+=1
print("your losses by not switching were:" + str(LOOSE))
print("Your wins by not switching were:" + str(WIN))