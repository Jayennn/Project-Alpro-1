
program_running = True
while program_running:
    program_input = input("Terminate the program: [Y]/[N]")
    if program_input.lower() == "y":
        print("Program terminated.")
        program_running = False
        break

    print("Program is running...")

print("Thank you")