line=str(input("Introduceti un sir de caractere:"))
numarator = 0

for litere in line:
    if litere.isupper():
        numarator +=1
print(numarator)