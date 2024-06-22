class Machine:
    def __init__(self) -> None:
        self.current_position: int = 0
        self.memory: list[int] = [0] * 30000
        self.clipboard: int = 0

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
        print(self.memory[self.current_position])

    def show_char_at_position(self):
        print(chr(self.memory[self.current_position]))

    def copy_to_clipboard(self):
        self.clipboard = self.memory[self.current_position]

    def assign_from_clipboard(self):
        self.memory[self.current_position] = self.clipboard
