# Prime Number Checker

while True:
    def is_prime(num):
        if num <= 1 :
            return "Not a prime number"

        # Check for divisibility from 2 up to the square root of num

        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:            # If divisible by any number other than 1 and itself, it's not prime

                return "Not a prime number"
        else:
            return "It's a prime number"

    print(is_prime(int(input("Enter a number: "))))

    another_number = input("Continue 'y' or 'n': ").lower()
    if another_number != "y":
        break
