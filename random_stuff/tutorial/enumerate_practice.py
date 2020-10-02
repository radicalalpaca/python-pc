

example = ["left", "right", "up", "down"]

# for i in range(len(example)):
#     print(i, example[i])


for i in enumerate(example):
    print(i[0])

new_dict = dict(enumerate(example))

print(new_dict)

