# with open("demo1.txt") as f1:
#     file_data_1 = f1.read()

# with open("demo2.txt") as f2:
#     file_data_2 = f2.read()

# with open("demo3.txt", mode="w") as f3:
#     f3.write(file_data_1)
#     f3.write(file_data_2)

files_name = ["demo1.txt", "demo2.txt", "demo3.txt"]
files_data = []

for f_name in files_name:
    with open(f_name) as f:
        files_data.append(f.read())

with open("demo4.txt", mode="w") as f:
    for data in files_data:
        f.write(data)
