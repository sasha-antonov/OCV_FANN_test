# coding=utf-8

def create_data(in_img, out):
    file = open("in.data", "w")
    for l in range(len(in_img)):
        file.write(str(in_img[l]) + " ")
    file.write("\n")
    file.write(str(out))
    file.close()

def add_data(in_img, out):
    file = open("in.data", "a")
    file.write("\n")
    for l in range(len(in_img)):
        file.write(str(in_img[l]) + " ")
    file.write("\n")
    file.write(str(out))
    file.close()

