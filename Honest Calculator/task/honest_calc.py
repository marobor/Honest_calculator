# Constants declarations.
VALID_OPERATORS = ["+", "-", "*", "/"]
LAZINESS_OPERATORS = ["+", "-", "*"]
MESSAGE_TABLE = ["Enter an equation",
                 "Do you even know what numbers are? Stay focused!",
                 ("Yes ... an interesting math operation."
                  " You've slept through all classes, haven't you?"),
                 "Yeah... division by zero. Smart move...",
                 "Do you want to store the result? (y / n):",
                 "Do you want to continue calculations? (y / n):",
                 " ... lazy", " ... very lazy", " ... very, very lazy",
                 "You are", "Are you sure? It is only one digit! (y / n)",
                 "Don't be silly! It's just one number! Add to the memory? (y / n)",
                 "Last chance! Do you really want to embarrass yourself? (y / n)"]

# Variable declarations
memory = 0.0
msg_index = 0


# Laziness test
def check(operand_1, operand_2, operator):
    msg = ''
    if is_one_digit(operand_1) and is_one_digit(operand_2):
        msg = msg + MESSAGE_TABLE[6]
    elif operand_1 == operand_2 and operator == '/':
        msg = msg + MESSAGE_TABLE[6]
    if operator == '*' and operand_1 == 1 or operand_2 == 1:
        msg = msg + MESSAGE_TABLE[7]
    if (operator in LAZINESS_OPERATORS) and (operand_1 == 0 or operand_2 == 0):
        msg = msg + MESSAGE_TABLE[8]
    if msg != '':
        print(MESSAGE_TABLE[9] + msg)


# Function checks if operand consists of more than two digits
def is_one_digit(operand):
    if -10 < operand < 10 and operand == int(operand):
        return True
    else:
        return False


# Program code.
while True:
    print(MESSAGE_TABLE[0])
    # Input reading and splitting it into variables
    x, oper, y = input().split()
    # Checking if previous result will be used.
    if x == 'M':
        x = str(memory)
    if y == 'M':
        y = str(memory)
    # Operands validation
    if x.isalpha() or y.isalpha():
        print(MESSAGE_TABLE[1])
    # Operator validation
    elif oper not in VALID_OPERATORS:
        print(MESSAGE_TABLE[2])
    else:
        # String to float conversion
        # NOTE: Result type should be float so
        #       operands should be float even if
        #       they can be converted to int
        x = float(x)
        y = float(y)
        # Laziness test performed by check function
        check(x, y, oper)
        # Calculation
        if oper == VALID_OPERATORS[0]:
            result = x + y
            print(result)
        elif oper == VALID_OPERATORS[1]:
            result = x - y
            print(result)
        elif oper == VALID_OPERATORS[2]:
            result = x * y
            print(result)
        elif oper == VALID_OPERATORS[3] and y != 0.0:
            result = x / y
            print(result)
        else:
            # Division by zero message is not a result
            # so the loop should continue.
            print(MESSAGE_TABLE[3])
            continue
        while True:
            # Saving result loop
            print(MESSAGE_TABLE[4])
            answer = input()
            if answer != 'y' and answer != 'n':
                continue
            elif answer == 'y':
                if is_one_digit(result):
                    msg_index = 10
                    answer = input(MESSAGE_TABLE[msg_index])
                    while msg_index < 12:
                        if answer == 'y':
                            msg_index += 1
                            answer = input(MESSAGE_TABLE[msg_index])
                        else:
                            break
                    if msg_index == 13:
                        memory = result
                else:
                    memory = result
            # Continuation loop
            while True:
                print(MESSAGE_TABLE[5])
                answer = input()
                if answer != 'y' and answer != 'n':
                    continue
                else:
                    break
            break
        if answer == "y":
            continue
        else:
            break
