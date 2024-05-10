import random
super_heros = ["Spider-Man", "Iron Man", "Captain America", "Thor", "Hulk", "Black","Black Panther","Doctor Starnge", "Vision"]
super_vilians=["Magneto", "Doctor doom", "Thanos", "Thanos", "Loki", "Galactus","Kingpin","Green Goblin", "Venom"]
vitória = ["hero"], ["vilan"]
for i in range(9):
    hero = random.choice(super_heros)
    vil = random.choice(super_vilians)
    vitoria = random.choice(vitória) 
    if vitoria == "hero":
        pass
    print (f"{hero} lutou contra {vil} o vencedor foi o {vitoria}")
    super_heros.remove(hero)
    super_vilians.remove(vil)