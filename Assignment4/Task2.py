user_input = input("Enter text to write to the file: ")
with open("output.txt", "wt") as fh:
    fh.write(user_input)
print("Data succussfully written to output.txt.")
input_append = input("Enter additional text to append: ")
with open("output.txt", "at") as fh:
    fh.write("\n")
    fh.write(input_append)
print("Data successfullu appended.")
print("Final content of output.txt")
with open("output.txt", "rt") as fh:
    content = fh.readlines()
print(content)
for data in content:
    print(data, end="")
