parola = ""
max = int(parola[0] + parola[1])
for i in range(len(parola)):
    for j in range(1, len(parola) - i):
        if int(parola[i] + parola[j + i]) > max:
            max = int(parola[i] + parola[j + i])
