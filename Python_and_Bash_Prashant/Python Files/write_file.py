"""Task 3: Create a text file and write content to it."""
text = input("Enter text to write to file: ").strip().title()

with open("sample.txt", "w", encoding="utf-8") as file:
    file.write("Hello, this file was created using Python.\n")
    file.write("It demonstrates the open() and write() functions.\n")
    file.write(f"{text}\n")

print("Content was written to sample.txt successfully.")

print("Content written:")
with open("sample.txt", "r", encoding="utf-8") as file:
    content = file.read()
    print(content)
