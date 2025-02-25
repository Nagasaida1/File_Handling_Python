user_input = input("Enter text to write to the file: ")

with open("output.txt", "w") as file:
    file.write(user_input + "\n")

print("Data successfully written to output.txt.")

extra_input = input("Enter additional text to append: ")

with open("output.txt", "a") as file:
    file.write(extra_input + "\n")

print("Data successfully appended.")

print("\nFinal content of output.txt:")
with open("output.txt", "r") as file:
    print(file.read())
