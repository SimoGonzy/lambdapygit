from functools import reduce


#esercizio1.1

def esercizio1_1():
    print((lambda x: x * x)(3))


#esercizio1.2

def esercizio1_2():
    print((lambda x, y: x + y)(3,4))


#esecizio1.3

def esercizio1_3():
    print((lambda x, y: x + " " + y)("mario", "rossi"))


#esercizio1.4

def esercizio1_4():
    print((lambda x: len(x) % 2 == 0 )("marione"))


#esercizio2.1

def esercizio2_1():
    fun = lambda x: x*x

    def apply_to_sum(fun, val1, val2):
        return fun(val1 + val2)

    print(apply_to_sum(fun, 5, 5))



#eseercizio2.2

def esercizio2_2():
    fun = lambda x: x+x

    def apply_twice(fun, val):
        return fun(fun(val))

    print(apply_twice(fun, 2))


#esercizio2.3

def esercizio2_3():
    def incrementer(n):
        return lambda x: x + n

    print(incrementer(3)(4))



#esercizio3.1
def esercizio3_1():
    nums = [10, 15, 20, 25, 30]

    print(list(filter(
        lambda x: x >= 20,
        nums
    )))


#esercizio3.2

def esercizio3_2():
    words = ["ciao", "python", "lambda", "hi", "fun"]

    print(list(map(
        lambda x: len(x),
        words
    )))



#esercizio3.3

def esercizio3_3():
    words = ["anna", "bob", "carla", "daniele", "eve"]

    print(list(filter(
        lambda x: x[0] == "a",
        words
    )))


#esercizio3.4

def esercizio3_4():
    nums = [2, 3, 5, 7, 11]

    print(reduce(
        lambda x, y: x * y,
        nums
    ))


#esrercizio4.1

def esercizio4_1():
    pairs = [(1, 2), (3, 4), (5, 6), (7, 8)]

    print(reduce(
        lambda x, y: x + [y[0] + y[1]],
        pairs,
        []
    ))

x = ""

while x != "stop":
    x = str(input("Inserisci il valore del gruppo di esercizi (1-4) o 'stop' per stoppare: "))
    if x == "1":
        y = str(input("inserisci il numero dellesercizio del gruppo 1 (1-4)" ))
        if y == "1":
            print("Es 1")
            esercizio1_1()
        elif y == "2":
            print("Es 2")
            esercizio1_2()
        elif y == "3":
            print("Es 3")
            esercizio1_3()
        elif y == "4":
            print("Es 4")
            esercizio1_4()
    elif x == "2":
        y = str(input("inserisci il numero dellesercizio del gruppo 2 (1-3)" ))
        if y == "1":
            print("Es 1")
            esercizio2_1()
        elif y == "2":
            print("Es 2")
            esercizio2_2()
        elif y == "3":
            print("Es 3")
            esercizio2_3()
    elif x == "3":
        y = str(input("inserisci il numero dellesercizio del gruppo 2 (1-4)" ))
        if y == "1":
            print("Es 1")
            esercizio3_1()
        elif y == "2":
            print("Es 2")
            esercizio3_2()
        elif y == "3":
            print("Es 3")
            esercizio3_3()
        elif y == "4":
            print("Es 4")
            esercizio3_4()
    elif x == "4":
        y = str(input("inserisci il numero dellesercizio del gruppo 2 (1-4)" ))
        if y == "1":
            print("Es 1")
            esercizio4_1()