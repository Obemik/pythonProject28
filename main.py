# def func1(string, number, sign):
#     print(f"{string:{sign}^{number}}")
# func1(input(), input(), input())

import os
# path = "C:\Windows\Web"
# for path, dirnames, filenames in os.walk(path):
#     print(f"path - {path}")
#     print(f"dirnames - {dirnames}")
#     print(f"filenames - {filenames}")

# os.path.isabs()
# open()
# rename(path1, path2)
# renames(path1, path2)
# replace(path1, path2)
# getctime()
# getmtime()

# import os
# path = os.path.normpath("C:\Windows\Web")
# for path, dirnames, filenames in os.walk(path):
#     print(f"path - {path}")
#     print(f"dirnames - {dirnames}")
#     print(f"filenames - {filenames}")

# dir1 = "Windows"
# dir2 = "Web"
# path = os.path.join(dir1, dir2)
# print(path)

# print(os.path.isabs(path))
# print(os.path.isfile(path))
# print(os.path.isdir(path))
# print(os.path.islink(path))

# path = os.path.normpath("new_dir")
# os.rmdir(path)
# os.mkdir(path)

# file = open("fil.txt", "w")
# file.write("Hello World! ")
# file.close()
# file = open("file.txt", "a")
# file.write("Hello user!")
# file.close()
# file = open("file.txt", "r")
# print(file.read())
# file.close()

# with open("file.txt", "a") as file:
#     file.write(" Hello somebody!")
#
# print(os.path.getctime("file.txt"))
# print(os.path.getmtime("file.txt"))

# import os
# path = os.path.normpath(input("Введіть шлях: "))
# def func1(string, number, sign):
#     print(f"{string:{sign}^{number}}")
# func1(input(), input(), input())

# import os
# path = "C:\Windows\Web"
# for path, dirnames, filenames in os.walk(path):
#     print(f"path - {path}")
#     print(f"dirnames - {dirnames}")
#     print(f"filenames - {filenames}")

# os.path.isabs()
# open()
# rename(path1, path2)
# renames(path1, path2)
# replace(path1, path2)
# getctime()
# getmtime()

# import os
# path = os.path.normpath("C:\Windows\Web")
# for path, dirnames, filenames in os.walk(path):
#     print(f"path - {path}")
#     print(f"dirnames - {dirnames}")
#     print(f"filenames - {filenames}")

# dir1 = "Windows"
# dir2 = "Web"
# path = os.path.join(dir1, dir2)
# print(path)

# print(os.path.isabs(path))
# print(os.path.isfile(path))
# print(os.path.isdir(path))
# print(os.path.islink(path))

# path = os.path.normpath("new_dir")
# os.rmdir(path)
# os.mkdir(path)

# file = open("file.txt", "w")
# file.write("Hello World! ")
# file.close()
# file = open("file.txt", "a")
# file.write("Hello user!")
# file.close()
# file = open("file.txt", "r")
# print(file.read())
# file.close()
#
# with open("file.txt", "a") as file:
#     file.write(" Hello somebody!")
#
# print(os.path.getctime("file.txt"))
# print(os.path.getmtime("file.txt"))

# import os
# filename = "my_file.txt"
# path = os.path.normpath(input("Введіть шлях: "))
# with open(filename, "w") as file:
#     for path, dirnames, filenames in os.walk(path):
#         file.write(f"path - {path}\n")
#         file.write(f"dirnames - {dirnames}\n")
#         file.write(f"filenames - {filenames}\n")

# import datetime
#
# date_now = os.path.getctime("file.txt")
# # time_stamp = date_now.timestamp()
# print(f"Timestamp = {datetime.datetime.fromtimestamp(date_now)}")

# import os
# filename = "file_new.txt"
# filename2 = "file_new.txt"
# sentence = input("Введіть речення: ")
# def find_longest_word(sentence):
#     words = sentence.split()
#     longest_word = " "
#     for word in words:
#         if len(word) > len(longest_word):
#             longest_word = word
#     return longest_word
# with open(filename, "w") as file:
#     file.write(sentence)
# with open(filename, "r") as file:
#     sentence2 = file.read()
#     def find_longest_word(sentence):
#         words = sentence.split()
#         longest_word = " "
#         for word in words:
#             if len(word) > len(longest_word):
#                 longest_word = word
#         return longest_word
# longest = find_longest_word(sentence2)
# with open(filename2, "w") as file:
#     file.write(longest)

# sentence = input("Введіть речення: ")
# with open("fileread.txt", "w") as f:
#     f.write(sentence)
# def longest_word(filename):
#     with open(filename, "r") as f:
#         data = f.read()
#         words = data.split()
#         longest = max(words, key=len)
#         return longest
# print(longest_word("fileread.txt"))

# import os
# def func_1():
#     root_dir = "Dir_1"
#     os.mkdir(root_dir)
#     with open(os.path.join(root_dir, "file_1"), "w") as file:
#         file.write("Hello, World! It's me")
#     dir_2 = os.path.join(root_dir, "Dir_2")
#     os.mkdir(dir_2)
#     with open(os.path.join(dir_2, "file_2"), "w") as file:
#         file.write("This is file number 2.")
#     with open(os.path.join(dir_2, "file_3"), "w") as file:
#         file.write("This is file number 3.")
#     dir_3 = os.path.join(root_dir, "Dir_3")
#     os.mkdir(dir_3)
#     with open(os.path.join(dir_3, "file_4"), "w") as file:
#         file.write("This is file number 4.")
# func_1()

# def func_2():
#     filename = input("Введіть назву файлу для збереження запису: ")
#     sentance = input("Введіть текст, який ви хочете записати: ")
#     with open(filename, "w") as file:
#         file.write(sentance)
#     print(f"Текст {sentance} успішно було збережено у файлі з назвою: {filename}")
# func_2()