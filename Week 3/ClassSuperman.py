class Superman:
    def __init__(self, name, weapons, color, power = 0):
        self.name = name
        self.weapons = weapons
        self.color = color
        self.power = power

    def __str__ (self):
        return f"Superman: {self.name:10} | Weapons: {self.weapons:8} | Color: {self.color:6} | Power: {self.power}"

list_ds = []  
while True:
    name = input ("Superman name (Nhan Enter de dung): ")
    if not name: break

    w = input ("Weapons: ")
    c = input ("Color: ")
    
    try:
        p = int(input ("Power: "))
    except ValueError:
        print("Invalid input for power. Please enter a valid integer.")
        continue # Qu
    
    sm = Superman (name, w, c, p)
    list_ds.append(sm)

print ("--- IMPORTED LIST ---")
for i, sm in enumerate (list_ds, 1):
    print (f"{i}.{sm}")
    