# for beer in range(100, 0, -1):
#     print(f"{beer} bottles of beer on the wall.")
#     print(f"{beer} bottles of beer.")
#     print(f"Take one down, pass it around, {beer} bottles of beer on the wall.")
#     print("**********")

beers = 100
while beers >= 1:
    print(f"{beers} bottles of beer on the wall.")
    print(f"{beers} bottles of beer.")
    print(f"Take one down, pass it around, {beers} bottles of beer on the wall.")
    print("**********")
    beers -= 1