"""Task 4: Open the text file, read it, and display its content."""


try:
    with open("sample.txt", "r", encoding="utf-8") as file:
        content = file.read()

    print("Content of sample.txt:\n")
    print(content)
except FileNotFoundError:
    print("sample.txt was not found. Run write_file.py first.")