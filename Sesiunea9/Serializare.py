def read(filename):
    f = open(filename, "r")
    try:
        return f.readline()
    except:
        print("Error reading file")
    finally:
        f.close()


def read_safe(filename):
    with open(filename, "r") as f:
        return f.readlines()


read("data.txt")
print(read("data.txt"))
print(read_safe("data.txt"))


def write(filename, data):
    with open(filename, "w") as f:
        f.writelines(data)


write("data2.txt", ["abc\n", "123\n", "per\n"])


def append(filename, data):
    with open(filename, "a") as f:
        f.writelines(data)


append("data2.txt", ["2345\n", "absds"])
