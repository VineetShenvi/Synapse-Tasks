jumbled_superheroes = ['DocToR_sTRAngE', 'sPidERmaN', 'MoON_KnigHT', 'caPTAIN_aMERIca', 'hULK']

indices = []
decoded_names = []
name_lengths = []


for superhero in jumbled_superheroes:
    superhero = superhero.lower()
    superhero = superhero.replace('_',' ')
    decoded_names.append(superhero)

indices = list(enumerate(decoded_names))
print(f"decoded_names = {decoded_names}\n")
print(f"indices = {indices}\n")

f = lambda a : len(str(a))

name_lengths = list(map(f, decoded_names))
print(f'name_lengths = {name_lengths}\n')

indices.sort(key = f)
print("\nPhase 5 kickoff list : \n")

index = 1
for superhero in indices:
    print(f"{index}. {superhero[1].title()}")
    index += 1