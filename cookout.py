print("Cookout Calculator")

p = int(input("Enter number of people: "))
h = int(input("Enter hot dogs per person: "))

total = p * h

dog_packs = total // 10
if total % 10 != 0:
    dog_packs += 1

bun_packs = total // 8
if total % 8 != 0:
    bun_packs += 1

dogs_left = (dog_packs * 10) - total
buns_left = (bun_packs * 8) - total

print("Hot dog packages needed:", dog_packs)
print("Hot dog bun packages needed:", bun_packs)
print("Hot dogs left over:", dogs_left)
print("Hot dog buns left over:", buns_left)