def local_chai():
    yield "masala Chai"
    yield "Ginger chai"

def imported_chai():
    yield "Matcha"
    yield "oolang"

def full_menu():
    yield from local_chai()
    yield from imported_chai()

chais=full_menu()
print(chais)

for chai in chais:
    print(chai)