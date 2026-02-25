def operazione(num: int, op:int) -> int:
    if num % 2 == 0:
        if op == 0:
            return num * num
        if op == 1:
            return 2 * num
        else:
            return num ** 3
    return num

print (operazione(3, 1))