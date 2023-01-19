
notes = []
coefficients = []

for i in range(5):
    user = input(f"Veuillez entrer la note du module 1 et le coefficient {i+1} :" )
    note, coefficient = user.split()
    notes.append(float(note))
    coefficients.append(int(coefficient))

total = 0
for i in range(5):
    total += notes[i] * coefficients[i]

note_total = total / sum(coefficients)

if note_total >= 10 :
    print(f"L'étudiant est admis avec  {note_total} de moyenne ")
else:
    print(f"L'étudiant n'est pas admis avec  {note_total} de moyenne ")