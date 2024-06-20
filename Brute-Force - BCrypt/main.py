import bcrypt
import itertools
import string

combinations = string.ascii_letters + string.digits + string.punctuation


def bruteForce(inputHash=None):
    if inputHash == None:
        inputHash = input("Please enter hash to brute force: ")

    encodedHash = inputHash.encode("utf-8")
    i = 1
    while True:
        for op in itertools.product(combinations, repeat=i):
            op = "".join(op)
            print(op)

            if bcrypt.checkpw(op.encode("utf-8"), encodedHash):
                print(f"Password Found: {op}")
                exit()
        i += 1


if __name__ == "__main__":
    bruteForce()
