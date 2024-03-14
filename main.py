import random

# Function to generate random operation
def random_operation():
    operators = ['+', '-', '*', '/']
    return random.choice(operators)

# Function to generate random integer from min_val to max_val
def random_int(min_val, max_val):
    return random.randint(min_val, max_val)


def main():
    # Input from user the number of calculation exercises
    n_exercises = int(input("Please enter the number of exercises: "))

    # Opening result.txt file for writing
    with open("result.txt", "w") as fp:
        # Write Student ID on result.txt
        fp.write("2256328\n")

        for i in range(n_exercises):
            operand1 = random_int(0, 100)
            n_operands = random_int(3, 5)

            if n_operands < 3 or n_operands > 5:
                print('operands out of range')
                exit(-1)
            # start building the string for the mathematical expression
            expression = str(operand1)

            # Derive number of operations from number of operands
            n_operations = n_operands - 1

            for j in range(n_operations):
                operand2 = random_int(0, 100)
                sign = random_operation()
                expression += f"{sign}{operand2}"

            try:
                fp.write(f"{expression}={eval(expression):.2f}\n")
            except Exception as error:
                fp.write(str(error)+"\n")


if __name__ == '__main__':
   main()


