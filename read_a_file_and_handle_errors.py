filename= "sample.txt"
try:
    with open("sample.txt", "r") as file1:
        print("Reading file content:")
        for index, line in enumerate(file1, start=1):
            print(f"Line {index}: {line.strip()}")

except FileNotFoundError:
    print(f"Error: The file '{filename}' was not found.")
