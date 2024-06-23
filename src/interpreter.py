import unicodedata
from emoji_script import Machine

_tokens = {
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
    "1️⃣": "1",
    "2️⃣": "2",
    "3️⃣": "3",
    "4️⃣": "4",
    "5️⃣": "5",
    "6️⃣": "6",
    "7️⃣": "7",
    "8️⃣": "8",
    "9️⃣": "9",
    "0️⃣": "0",
}
tokens = {
    "\U0001F51B": "CODE_START",
    "\U0001F6D1": "CODE_END",
    "\U0001F4A6": "COMMAND_END",
    "\U0000270D": "ASSIGNMENT",
    "\U00002795": "SUM",
    "\U00002796": "SUBTRACTION",
    "\U0001F6AB": "ASSIGN_ZERO",
    "\U000027A1": "MOVE_RIGHT",
    "\U00002B05 ": "MOVE_LEFT",
    "\U0001F346": "PRINT_NUMBER",
    "\U0001F351": "PRINT_CHAR",
    "\U0001F923": "COPY",
    "\U0001F480": "PASTE",
}
numbers = {
    "DIGIT ONE": "1",
    "DIGIT TWO": "2",
    "DIGIT THREE": "3",
    "DIGIT FOUR": "4",
    "DIGIT FIVE": "5",
    "DIGIT SIX": "6",
    "DIGIT SEVEN": "7",
    "DIGIT EIGHT": "8",
    "DIGIT NINE": "9",
    "DIGIT ZERO": "0",
}
IGNORED_CHARACTERS = [
    "\n",
    ",",
    ";",
    "?",
    "¿",
    "!",
    "¡",
    "(",
    ")",
    "\t",
    " ",
    "\r",
    "\b",
]


def remove_ignored_characters(command_content: str, ignored_characters: list) -> str:
    """Takes a string and returns the same string, but not including any of the character
    in IGNORED_CHARACTERS."""

    modified_content = command_content

    for letter in command_content:
        if letter in ignored_characters:
            modified_content = modified_content.replace(letter, "")

    return modified_content


def numbers_to_value(str: str) -> int:
    number_list = []
    for char in str:
        if unicodedata.name(char) in numbers:
            number_list.append(numbers[unicodedata.name(char)])
    # print(int("".join(number_list)))
    return int("".join(number_list))


def read_file(file_path: str) -> list[str]:
    with open(file_path, "r", encoding="utf-8") as file:
        file_code = file.read().split("💦")

    return [command.strip() for command in file_code]


def interpret(commands: list[str]):
    # print("\U0000270D")
    translated_commands = []
    for emoji_command in commands:
        command = tokens[emoji_command[0]]
        if command == "ASSIGNMENT" or command == "SUM" or command == "SUBTRACTION":
            number_str = emoji_command[1:]
            value = numbers_to_value(number_str)
            translated_commands.append((command, value))
        else:
            translated_commands.append((command, 0))
    ES = Machine(translated_commands)

    ES.run()


if __name__ == "__main__":
    archivo1 = "../ejemplos/hola_mundo.txt"
    print("corriendo el archivo:", archivo1)
    commands = read_file(archivo1)
    interpret(commands)

    archivo2 = "../ejemplos/suma.txt"
    print("corriendo el archivo:", archivo2)
    commands = read_file(archivo2)
    interpret(commands)
