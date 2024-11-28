data_structure = [
  [1, 2, 3],
  {'a': 4, 'b': 5},
  (6, {'cube': 7, 'drum': 8}),
  "Hello",
  ((), [{(2, 'Urban', ('Urban2', 35))}])
]

def calculate_structure_sum (set_):
    sum_elements = 0
    if isinstance(set_, list) or isinstance(set_, tuple) or isinstance(set_, set):
        for item in set_:
            sum_list = calculate_structure_sum(item)
            sum_elements += sum_list
    elif isinstance(set_, dict):
        for key, value in set_.items():
            sum_key = calculate_structure_sum(key)
            sum_values = calculate_structure_sum(value)
            sum_elements += sum_key + sum_values
    elif isinstance(set_, int):
        sum_elements += set_
    elif isinstance(set_, str):
        sum_elements += len(set_)
    return sum_elements


result = calculate_structure_sum(data_structure)
print(result)