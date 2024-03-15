
import os
import zipfile

def compress_files():
    with zipfile.ZipFile("student.dat", "w") as zipf:
        zipf.write("student.txt")
        zipf.write("course.txt")
        zipf.write("mark.txt")

def decompress():
    with zipfile.ZipFile("student.dat", "r") as zipf:
        zipf.extractall()

def check():
    return "student.dat" in os.listdir(".") and \
           "student.txt" in os.listdir(".") and \
           "course.txt" in os.listdir(".") and \
           "mark.txt" in os.listdir(".")

