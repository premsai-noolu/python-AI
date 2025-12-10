def infinite_chai():
    count=1
    while True:
        yield f"Return #{count}"
        count+=1

refill = infinite_chai()

for _ in range(5):
    print(next(refill))


user2 = infinite_chai()

for _ in range(5):
    print(next(user2))