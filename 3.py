def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def find_primes_in_range(start, end):
    primes = []
    for num in range(start, end + 1):
        if is_prime(num):
            primes.append(num)
    return primes

if __name__ == "__main__":
    start = 245690
    end = 245756
    primes = find_primes_in_range(start, end)

    for index, prime in enumerate(primes, start=1):
        print(f"{index} {prime}")
