from decimal import Decimal
from app.commands import Command


class SubtractCommand(Command):
    def execute(self):
        print("\n---------------\nSubtraction operation (type 'stop' for main menu)\n")
        isWorking = True
        while isWorking:  #REPL Read, Evaluate, Print, Loop
            a = input("Enter A:\n>>> ").strip()
            if a == 'stop':
                print("Operation cancelled\n---------------\n")
                isWorking = False
                break
            b = input("Enter B:\n>>> ").strip()
            if a == 'stop':
                print("Operation cancelled\n---------------\n")
                isWorking = False
                break
            try:
                print(f"Result is:\na - b = {a} - {b} = {subtract(Decimal(a), Decimal(b))}\n---------------\n")
                isWorking = False
            except Exception as e: # Catch-all for unexpected errors
                print(f"An error occurred: {e}\n---------------\n")
                isWorking = False

def subtract(a: Decimal, b: Decimal) -> Decimal:
    return a - b
