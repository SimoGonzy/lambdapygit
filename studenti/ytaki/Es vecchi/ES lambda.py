from functools import reduce
import os

# Su Windows
os.system('cls')

# Es 1
def esercizio1_1():
    print("Es 1.1")
    print((lambda x: x*x)(2))

def esercizio1_2():
    print("Es 1.2")
    print((lambda x,y: x+y)(10, 3))

def esercizio1_3():
    print("Es 1.3")
    print((lambda x, y: x+" "+y)("Mario", "Rossi"))

def esercizio1_4():
    print("Es 1.4")
    print((lambda x: len(x)%2 == 0)("ciao"))


# Es 2
def esercizio2_1():
    print("Es 2.1")
    def apply_to_sum(fun, val1, val2):
        return fun(val1 + val2)
    f = lambda x: x*x
    print(apply_to_sum(f, 10, 10))

def esercizio2_2():
    print("Es 2.2")
    def apply_twice(fun, val):
        return fun(fun(val))
    fun = lambda x: x * x
    print(apply_twice(fun, 10))

def esercizio2_3():
    print("Es 2.3")
    def incrementer(n):
        return lambda x: x + n
    print(incrementer(1)(2))


# Es 3
def esercizio3_1():
    print("Es 3.1")
    nums = [10, 15, 20, 25, 30]
    print(list(filter(lambda x: x>20, nums)))

def esercizio3_2():
    print("Es 3.2")
    words = ["ciao", "python", "lambda", "hi", "fun"]
    print(list(map(lambda x: len(x), words)))

def esercizio3_3():
    print("Es 3.3")
    words = ["anna", "bob", "carla", "daniele", "eve"]
    print(list(filter(lambda x: x[0] == "a", words)))

def esercizio3_4():
    print("Es 3.4")
    nums = [2, 3, 5, 7, 11]
    print(reduce(lambda x, y: x * y, nums))


# Es 4
def esercizio4_1():
    print("Es 4.1")
    pairs = [(1, 2), (3, 4), (5, 6), (7, 8)]
    print(list(map(lambda x: x[0] + x[1], pairs)))

def esercizio4_2():
    print("Es 4.2")
    people = [
        {"name": "Mario", "age": 23},
        {"name": "Giovanni", "age": 18},
        {"name": "Paolo", "age": 6},
        {"name": "Pippo", "age": 5},
        {"name": "Gianluca", "age": 22},
        {"name": "Gianluigi", "age": 21}
    ]
    maggiorenni = list(filter(lambda x: x["age"]>=18, people))
    nomi = [i["name"] for i in maggiorenni]
    print(nomi)


# --- ESECUZIONE ---
esercizio4_2()