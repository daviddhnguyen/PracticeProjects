from src.py_find_pi_n.find_pi import find_pi

def main():
    try:
        n = int(input('Enter the number of digits of Pi to compute: '))
        print(f"First {n} digits of pi: {find_pi(n)}")
    except ValueError:
        print("Please enter a valid integer.")

if __name__ == "__main__":
    main()