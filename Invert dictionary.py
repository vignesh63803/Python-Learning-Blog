original_dict = {
    'file1.txt': ['apple', 'banana', 'orange'],
    'file2.txt': ['banana', 'grape'],
    'file3.txt': ['apple', 'kiwi']
}

inverted_dict = {}

for original_key, value_list in original_dict.items():
    for value in value_list:
        inverted_dict.setdefault(value, []).append(original_key)

print(inverted_dict)
