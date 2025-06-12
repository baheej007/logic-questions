marks = [[70, 80], [65, 75], [90, 85]]

flat = []
for subject in marks:
    for score in subject:
        flat.append(score)

print(flat)