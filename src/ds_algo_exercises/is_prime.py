def is_prime(num: int) -> bool:
    if num == 1:
        return False

    counter = 2

    for i in range(2, num-1):
        if (num % i == 0):
            counter += 1

    if counter == 2:
        return True;
    else:
        return False;
