def check_bit():
    print("Welcome to the Bit Checker Game!")
    print("You will enter a number, and I'll tell you if it's a 0-bit or a 1-bit.\n")

    while True:
        bit = input("Enter a bit (0 or 1), or type 'exit' to quit: ").strip()

        if bit.lower() == 'exit':
            print("Thanks for playing! Bye! 👋")
            break
        elif bit == '0':
            print("You entered 0. That's called **zero bit**!\n")
        elif bit == '1':
            print("You entered 1. That's called **one bit**!\n")
        else:
            print("Oops! That's not a valid bit. Please enter only 0 or 1.\n")
check_bit()