store_list = [
    {"분류 1":["콜라","사이다","환타"]},
    {"분류 2":["포카칩", "홈런볼"]},
    {"분류 3":["신라면", "불닭볶음면", "진라면"]}
    ]

for i in range(len(store_list)):
    store_type = store_list[i]
    # print(store_type)

    for j in store_type:
        store_in_object = store_type[j]

        for z in range(len(store_in_object)):
            store_in_object_name = store_in_object[z]

            print(f"위치 [{i}][{z}] -> {store_in_object_name}")