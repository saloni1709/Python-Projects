HISTORY_FILE = "history.txt"

def show_history():
    # 👉 ensure file exists
    open(HISTORY_FILE, 'a').close()

    file = open(HISTORY_FILE, 'r')
    lines = file.readlines()
    file.close()

    if len(lines) == 0:
        print("No history found.")
    else:
        print("\n--- History ---")
        for line in lines:
            print(line.strip())

def clear_history():
    file = open(HISTORY_FILE, 'w')
    file.close()
    print("History cleared.")

def save_to_history(equation, result):
    file = open(HISTORY_FILE, 'a')
    file.write(equation + " = " + str(result) + "\n")
    file.close()

def calculate(user_input):
    parts = user_input.split()

    if len(parts) != 3:
        print("Invalid input. Use format: number operator number (e.g. 8 + 8)")
        return

    num1 = float(parts[0])
    operator = parts[1]
    num2 = float(parts[2])

    if operator == "+":
        result = num1 + num2
    elif operator == "-":
        result = num1 - num2
    elif operator == "*":
        result = num1 * num2
    elif operator == "/":
        if num2 == 0:
            print("Cannot divide by zero.")
            return
        result = num1 / num2
    else:
        print("Invalid operator. Use + - * /")
        return

    print("Result:", result)
    save_to_history(user_input, result)

def main():
    print("--SIMPLE CALCULATOR (type history, clear or exit)")

    # 👉 file auto-create at start
    open(HISTORY_FILE, 'a').close()

    while True:
        user_input = input("Enter calculator (+ - * /) or command (history, clear, exit) = ")

        if user_input == "exit":
            print("Goodbye!")
            break
        elif user_input == "history":
            show_history()
        elif user_input == "clear":
            clear_history()
        else:
            calculate(user_input)

main()