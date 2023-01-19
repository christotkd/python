
notes = []

for i in range(5):
    user = input(f"Veuillez entrer la note du module {i + 1} et le coefficient correspondant : ")
    note, coefficient = user.split()
    notes.append((float(note), int(coefficient)))

total = 0
for note in notes:
    total += note[0] * note[1]

final_note = total / sum(coefficient for note, coefficient in notes)
print(f"Note finale : {final_note}")
