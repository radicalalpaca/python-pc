with open("../movies.txt", "r") as in_file, \
    open("../movies_lowercase.txt", "w") as out_file:
    for line in in_file:
        out_file.write(line.lower())