def mass():
    mass_kg = int(input("m: "))
    c = 3e8
    energy_joules = mass_kg * c ** 2
    print("E:", int(energy_joules))
mass()
