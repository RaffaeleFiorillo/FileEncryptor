from random import randint
import os

valid_characters = "abcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ _,.'"


# encrypts a letter based on a given key_value
def encrypt_letter(letter: str, key: int) -> str:
    new_index = (valid_characters.index(letter) + key) % len(valid_characters)
    return valid_characters[new_index]


# given a string, returns the encrypted version of it
def encrypt_line(data: str, key: int) -> str:
    data = data.strip() if "\n" not in data else data[:-1]
    encrypted_data = "".join(reversed([encrypt_letter(char, key) for char in data]))
    return encrypted_data


# encrypts a file given his directory
def encrypt_file(directory: str) -> None:
    with open(directory, "r") as file:  # get file content
        lines = file.readlines()
    if len(lines) == 0:  # prevents list index error if file is empty
        return None
    with open(directory, "w") as file:
        for line in lines:
            key = randint(1, len(valid_characters) - 1)
            if line is not lines[-1]:
                file.write(f"{key} {encrypt_line(line, key)}\n")
            else:
                file.write(f"{key} {encrypt_line(lines[-1], key)}")


# encrypts a letter based on a given key_value
def decrypt_letter(letter: str, key: int) -> str:
    new_index = (valid_characters.index(letter) - key) % len(valid_characters)
    return valid_characters[new_index]


# given a string, returns the decrypted version of it
def decrypt_line(data: str, key) -> str:
    data = data if "\n" not in data else data[:-1]
    decrypted_data = "".join(reversed([decrypt_letter(char, key) for char in data]))
    return decrypted_data


# de crypts a file given his directory
def decrypt_file(directory: str) -> None:
    with open(directory, "r") as file:  # get file content
        lines = file.readlines()
    if len(lines) == 0:  # prevents list index error if file is empty
        return None
    with open(directory, "w") as file:
        for line in lines:
            key = int(line.split(" ")[0])
            start_index = line.index(" ") + 1
            if line is not lines[-1]:
                file.write(f"{decrypt_line(line[start_index:], key)}\n")
            else:
                file.write(decrypt_line(lines[-1][start_index:], key))


# encrypts all .txt files  in a list of directories passed as parameter
def encrypt_all_files(directories: [str]) -> None:
    for directory in directories:
        print(f"encrypting: {directory}")
        try:
            encrypt_file(directory)
        except ValueError:
            print(f"!!! Error in current directory: {directory} !!!")


# decrypts all .txt files  in a list of directories passed as parameter
def decrypt_all_files(directories: [str]) -> None:
    for directory in directories:
        print(f"decrypting: {directory}")
        try:
            decrypt_file(directory)
        except ValueError:
            print(f"!!! Error in current directory: {directory} !!!")


if __name__ == "__main__":
    information = "encrypt file: --> *complete_file_directory* -e <--\n" \
                "decrypt file: --> *complete_file_directory* -d <--\n" \
                "encrypt file: --> *relative_file_directory* -re <--\n" \
                "decrypt file: --> *relative_file_directory* -rd <--\n" \
                "help: --> -h <--\n" \
                "exit:         --> exit"

    print(information)
    while True:
        command = input("Enter Encryption Comand: ")
        if "exit" in command:
            break
        file_dir, action = command.split("-")
        if action == "d":
            decrypt_file(file_dir.strip())
        elif action == "e":
            encrypt_file(file_dir.strip())
        elif action == "rd":
            decrypt_file(f"{os.getcwd()}\\{file_dir.strip()}")
        elif action == "re":
            encrypt_file(f"{os.getcwd()}\\{file_dir.strip()}")
        elif action == "h":
            help_info = "encrypt file Example --> C:\\Users\\You\\Desktop\\Projects\\file.txt -e \n" \
                        "decrypt file Example --> C:\\Users\\You\\Desktop\\Projects\\file.txt -d \n" \
                        "encrypt file Example --> \\Projects\\file.txt -re \n" \
                        "decrypt file Example --> \\Projects\\file.txt -rd \n"
            print(help_info)
        else:
            print("invalid command")
