try:
    with open("sample.txt", "rt") as fh:
        content = fh.readlines()
    for data in content:
        i = 1
        print(f"Line{i}: {data}", end="")
        i += 1
except FileNotFoundError:
    print("Error: The file \'sample.txt\' was not exist.")