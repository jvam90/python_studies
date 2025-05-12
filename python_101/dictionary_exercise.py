# The exercise uses the following "peak" dictionary:
peak = {
    "name": "Castle Peak",
    "height": 14264,
    "summit_log": [],
    "cell_reception": {
        "AT&T": "no reception",
        "T-Mobile": "poor"
    }
}

peak["range"] = "Elk Mountains"
peak["first_climbed"] = 1873
peak["height"] = 14265
peak["cell_reception"]["Verizon"] = "good"
peak["summit_log"].append("João Víctor")

height = peak["height"]
peak.pop("height")
peak["elevation"] = height

for pair in peak.items():
    print(f"{pair[0]} -> {pair[1]}")

peak.clear()

print(peak)