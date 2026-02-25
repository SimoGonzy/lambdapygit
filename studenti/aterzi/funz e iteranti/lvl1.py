# Scrivi una lambda function che, preso un numero, ne restiuisca
# il quadrato;
# • Scrivi una lambda function che, presi due numeri, ne restiuisca
# la somma;
# • Scrivi una lambda function che, prese due stringhe con un
# nome e un cognome, restituisca la stringa con il nome completo
# (es. «Mario» e «Rossi» → «Mario Rossi»).
# • Scrivi una lambda function che, presa una stringa, restituisca
# True se la stringa ha lunghezza pari, False altrimenti;


print((lambda val: val * val)(2))


print((lambda x, y: x + y)(5, 6))

print((lambda nome, cognome: nome + " " + cognome)("Antonio", "Fraccaro"))

print((lambda word: len(word) % 2 == 0)("Simone"))
