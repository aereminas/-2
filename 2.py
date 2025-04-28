data_dict = {1: 11, 2: 22, 3: 33, 4: 4, 5: 33, 6: 1}

key_collection = set(data_dict.keys())
value_collection = set(data_dict.values())
combined_collection = key_collection.union(value_collection)

print("Набор ключей:", key_collection)
print("Набор значений:", value_collection)
print("Объединенный набор:", combined_collection)
