 # 4- list justine_League.py
# initial list of Justice League members
justice_league = ["Superman", "Batman", "Wonder Woman", "Flash", "Aquaman", "Green Lantern"]

# Step 1: Calculate the number of members in the Justice League
num_members = len(justice_league)
print(f"Number of members in the Justice League: {num_members}")

# Step 2: Add Batgirl and Nightwing to the list
justice_league.append("Batgirl")
justice_league.append("Nightwing")
print("After adding Batgirl and Nightwing:", justice_league)

# Step 3: Move Wonder Woman to the beginning of the list
justice_league.remove("Wonder Woman")
justice_league.insert(0, "Wonder Woman")
print("After moving Wonder Woman to the beginning:", justice_league)

# Step 4: Move either Green Lantern or Superman between Aquaman and Flash
# Let's choose Green Lantern
justice_league.remove("Green Lantern")
aquaman_index = justice_league.index("Aquaman")
justice_league.insert(aquaman_index + 1, "Green Lantern")
print("After moving Green Lantern between Aquaman and Flash:", justice_league)

# Step 5: Replace the existing list with new members
justice_league = ["Cyborg", "Shazam", "Hawkgirl", "Martian Manhunter", "Green Arrow"]
print("After replacing with new members:", justice_league)

# Step 6: Sort the Justice League alphabetically
justice_league.sort()
print("After sorting alphabetically:", justice_league)

# Determine the new leader
new_leader = justice_league[0]
print(f"The new leader of the Justice League is: {new_leader}")

# BONUS: Predicting the new leader
# The new leader will be the first member in the sorted list