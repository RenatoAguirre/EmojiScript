tokens = {
    "🔛": "CODE_START",
    "🛑": "CODE_END",
    "💦": "COMMAND_END",
    "✍️": "ASSIGNMENT",
    "➕": "SUM",
    "➖": "SUBTRACTION",
    "‼️": "ASSIGN_ZERO",
    "➡️": "MOVE_RIGHT",
    "⬅️": "MOVE_LEFT",
    "🍆": "PRINT_NUMBER",
    "🍑": "PRINT_CHAR",
    "🤣": "COPY",
    "💀": "PASTE",
}


def read_file(file_path: str) -> str:
    with open(file_path, "r", encoding="utf-8") as file:
        file_code = file.read().lower()
    return file_code


print(read_file("../ejemplos/hola_mundo.txt"))
