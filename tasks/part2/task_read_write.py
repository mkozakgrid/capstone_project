def read_write_file():
    output_file = open("output.txt", "w")
    for i in range(19):
        with open(f"files/file{i+1}.txt", "r") as file:
            file_content = file.read()
            output_file.write(file_content)

    output_file.close()