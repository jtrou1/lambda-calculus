import arithmetic as ar
import boolean as bl
import pair as pr

def increase(x):
    return x + 1

def print_number(func):
    print func(increase)(0)

def print_boolean(func):
    print func(True)(False)

def main():
    print_number(ar._nth_fibo(ar._10))

if __name__ == "__main__":
    main()
