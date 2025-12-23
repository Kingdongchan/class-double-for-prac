store = [
    {"분류 1":["콜라","사이다","환타"]},
    {"분류 2":["포카칩", "홈런볼"]},
    {"분류 3":["신라면", "불닭볶음면", "진라면"]}
    ]

for i in range(len(store)):
    store_type = store[i]
    # print(store_type)

    for j in store_type:
        store_in_object = store_type[j]

        print(store_in_object)