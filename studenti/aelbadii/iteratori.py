from functools import reduce

nums:list[int]=[10, 15, 20, 25, 30]
nums_maggiori_venti:list[int]=list(filter(lambda x:x>20,nums))
print(nums_maggiori_venti)
words :list = ["ciao", "python", "lambda", "hi","fun"]
lunghezza_parole:list=list(map(lambda x:len(x),words))
print(lunghezza_parole)
words1:list=["anna", "bob", "carla", "daniele","eve"]
lettera_iniziale:list=list(filter(lambda x: x[0]=='a',words1))
print(lettera_iniziale)
nums1:list[int]=[2, 3, 5, 7, 11]
prodotto:int=reduce(lambda x,y : x*y,nums1)
print(prodotto)
