drivers = ["Charles", "Pierre", "Valterri", "Lewis", "George","Lando"]

drivers[2] = "Valtteri"
drivers.append("Esteban")
drivers.extend(["Blue", "Elton", "Colt"])
drivers.pop()
drivers.pop(0)
last = drivers.pop()
drivers.append(last)
drivers.remove("Blue")
drivers.remove("Elton")
drivers.insert(2, "Elton")

podium = drivers[0:3]

for index, driver in enumerate(drivers):
    print(f"# {index + 1}. {driver}")