favorite_sushis = ['tempura', 'california', 'cream cheese']
friend_sushis = favorite_sushis[:]

favorite_sushis.append("tempura")
friend_sushis.append('california')

print("My favorite sushis are:")
for sushi in favorite_sushis:
    print("- " + sushi)

print("\nMy friend's favorite sushis are:")
for pizza in friend_sushis:
    print("- " + sushi)