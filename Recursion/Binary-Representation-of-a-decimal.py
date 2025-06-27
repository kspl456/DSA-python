#Binary Representation of a decimal

def decimal_to_binary(n):
    if n==0:
        return
    decimal_to_binary(n // 2)
    print(n % 2, end='')
decimal_to_binary(10)