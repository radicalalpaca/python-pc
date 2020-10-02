import timeit

def simple_gen():
    yield "oh"
    yield "hello"
    yield "there"


correct_combo = (3, 6, 1)
# found_combo = False

# for c1 in range(10):
#     if found_combo:
#         break
#     for c2 in range(10):
#         if found_combo:
#             break
#         for c3 in range(10):
#             if (c1, c2, c3) == correct_combo:
#                 print(f"Combo found: {c1} {c2} {c3}")
#                 found_combo = True
#                 break

def combo_gen():
    for c1 in range(10):
        for c2 in range(10):
            for c3 in range(10):
                yield (c1, c2, c3)


for (c1, c2, c3) in combo_gen():
    if (c1, c2, c3) == correct_combo:
        print("done")
        break

