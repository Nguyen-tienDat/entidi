import os
import pickle
import gzip

def compress_files():
    data = {
        'students': read_file("student.txt"),
        'courses': read_file("course.txt"),
        'marks': read_file("mark.txt")
    }
    with gzip.open("student.dat", "wb") as f:
        pickle.dump(data, f)

def decompress():
    with gzip.open("student.dat", "rb") as f:
        data = pickle.load(f)
    write_file("student.txt", data['students'])
    write_file("course.txt", data['courses'])
    write_file("mark.txt", data['marks'])

def check():
    return "student.dat" in os.listdir(".") and \
           "student.txt" in os.listdir(".") and \
           "course.txt" in os.listdir(".") and \
           "mark.txt" in os.listdir(".")

def read_file(filename):
    with open(filename, "rb") as f:
        return f.read()

def write_file(filename, data):
    with open(filename, "wb") as f:
        f.write(data)

        

