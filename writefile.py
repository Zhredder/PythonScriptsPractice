#! This file writes extracted data from an API into a file #!

def write_file(data):
    file = open("Sample.txt", "w")
    file.write(data)
    file.close()
    