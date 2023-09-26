#Oppgave 6.7

humans = {}

with open("human_evolution.txt") as infile:
    for line in infile:
        if line[0] == "H":
            name = line[:20].strip()
            when = line[21:35].strip()
            height = line[37:47].strip()
            mass = line[50:59].strip()
            brain = line[61:].strip()

            humans[name] = {'when': when, 'height': height, 'mass':mass, 'brain':brain}

for name in humans:
    h = humans[name]
    print(f"{name:20} {h['when']: 15} {h['height']: 15} {h['mass']:15} {h['brain']: 15}")
