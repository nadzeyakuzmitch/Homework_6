import sys
from app.commands import Command


class MenuCommand(Command):
    def execute(self):
        print(f'\n---------------\nAvailable commands:\n\nadd - Addition operation\nsubtract - Subtraction operation\nmultiply - Multiplication operation\ndivide - Division operation\n\nexit - Exit application\n---------------\n')