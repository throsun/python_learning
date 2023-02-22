# f = open('./demo.txt', mode='r', encoding='UTF-8')
# data = f.read()
# print(data)
# f.close()


with open('./demo.txt', mode='r', encoding='UTF-8') as f:
    data = f.read()

print(data)