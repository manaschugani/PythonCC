
guests = ['Ishan', 'Shreyash', 'Faiz']
name = guests[0].title()
print(f"{name}, please come over.")
name = guests[1].title()
print(f"{name}, please come over.")
name = guests[2].title()
print(f"{name}, please come over.")
name = guests[1].title()
print(f"\nSorry, {name} can't come over.")
del(guests[1])
guests.insert(1, 'Uncle Naeem')
name = guests[0].title()
print(f"\n{name}, please come over.")
name = guests[1].title()
print(f"{name}, please come over.")
name = guests[2].title()
print(f"{name}, please come over.")
print("\nInvite more people")
guests.insert(0, 'Amal')
guests.insert(2, 'Vandita')
guests.append('Diva')
name = guests[0].title()
print(f"{name}, please come over.")
name = guests[1].title()
print(f"{name}, please come over.")
name = guests[2].title()
print(f"{name}, please come over.")
name = guests[3].title()
print(f"{name}, please come over.")
name = guests[4].title()
print(f"{name}, please come over.")
name = guests[5].title()
print(f"{name}, please come over.")