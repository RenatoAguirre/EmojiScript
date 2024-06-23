import time


class Machine:
    def __init__(self, commands) -> None:
        self.current_position: int = 0
        self.memory: list[int] = [0] * 30000
        self.clipboard: int = 0
        self.commands = commands  # recibe una lista de tuplas, la tupla [0] es el comando y [1] es el valor

    def assing_to_memory(self, value: int):
        self.memory[self.current_position] = value

    def increment_memory(self, value: int):
        self.memory[self.current_position] += value

    def decrease_memory(self, value: int):
        self.memory[self.current_position] -= value

    def erease_memory_at_position(self):
        self.memory[self.current_position] = 0

    def move_right(self):
        self.current_position += 1

    def move_left(self):
        self.current_position -= 1

    def show_number_at_position(self):
        print(self.memory[self.current_position], end="")

    def show_char_at_position(self):
        print(chr(self.memory[self.current_position]), end="")

    def copy_to_clipboard(self):
        self.clipboard = self.memory[self.current_position]

    def assign_from_clipboard(self):
        self.memory[self.current_position] = self.clipboard

    def run(self):

        # print(self.commands)
        for command in self.commands:
            t0 = time.time()
            # print(command[0])
            if command[0] == "CODE_START":
                continue
            elif command[0] == "ASSIGNMENT":
                self.assing_to_memory(command[1])
            elif command[0] == "SUM":
                self.increment_memory(command[1])
            elif command[0] == "SUBTRACTION":
                self.decrease_memory(command[1])
            elif command[0] == "MOVE_RIGHT":
                self.move_right()
            elif command[0] == "MOVE_LEFT":
                self.move_left()
            elif command[0] == "PRINT_NUMBER":
                self.show_number_at_position()
            elif command[0] == "PRINT_CHAR":
                self.show_char_at_position()
            elif command[0] == "COPY":
                self.copy_to_clipboard()
            elif command[0] == "ASSIGN_FROM_CLIPBOARD":
                self.assign_from_clipboard()
            elif command[0] == "ERASE":
                self.erease_memory_at_position()
            elif command[0] == "CODE_END":
                t1 = time.time()
                print(f"\nFinsished in {t1-t0} seconds...")
            else:
                print("Command not found")
                break
