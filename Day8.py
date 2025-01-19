#Write a script that reads a text file and counts how many lines and words are in the file.
def count_lines_and_words(file_path):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
            num_lines = len(lines)
            num_words = sum(len(line.split()) for line in lines)

        print(f"Number of lines: {num_lines}")
        print(f"Number of words: {num_words}")
    except FileNotFoundError:
        print("The file was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Prompt user for file name
file_path = input("Enter the file name: ")
count_lines_and_words(file_path)

