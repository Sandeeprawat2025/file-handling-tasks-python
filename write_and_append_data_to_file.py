filename = 'output.txt'
with open("output.txt", "w") as file2:
    writing_file = file2.write(input("Enter text to write to the file: "))
    print("Data successfully written to", filename,'.')
    print()
with open("output.txt", "a") as file2:
    append_file = file2.write('\n' + input("Enter additional text to append: "))
    print("Data successfully appended.")
    print()
with open("output.txt", "r") as file2:
    print("Final content of ",filename,':')
    reading_file = file2.read()
    print(reading_file)
