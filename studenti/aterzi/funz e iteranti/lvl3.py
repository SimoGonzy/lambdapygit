# Dato l’elenco nums = [10, 15, 20, 25, 30], estrai solo i
# numeri maggiori di 20.
# •Dato l’elenco words = ["ciao", "python", "lambda", "hi",
# "fun"], ottieni la lista delle lunghezze di ogni parola.
# • Dato l’elenco words = ["anna", "bob", "carla", "daniele",
# "eve"], estrai solo le parole che iniziano con la lettera “a”.
# • Dato l’elenco nums = [2, 3, 5, 7, 11], calcola il prodotto di
# tutti i numeri.
from functools import reduce

nums = [10, 15, 20, 25, 30]
print(list(filter(lambda x: x >= 20, nums)))


words = ["ciao", "python", "lambda", "hi", "fun"]
print(list(map(lambda x: len(x), words)))

words2 = ["anna", "bob", "carla", "daniele", "eve"]
print(list(filter(lambda x: x[0] == "a", words2)))

nums2 = [2, 3, 5, 7, 11]
total: int = reduce(lambda x, y: x * y, nums2)
print(total)
