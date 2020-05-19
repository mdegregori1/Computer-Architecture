# print('test')

# Given an object/dictionary with keys and values that consist of both strings and integers, design an algorithm to calculate and return the sum of all of the numeric values. 
# For example, given the following object/dictionary as input:
# ```
# {
#   "cat": "bob",
#   "dog": 23,
#   19: 18,
#   90: "fish"
# }
# ```
# Your algorithm should return 41, the sum of the values 23 and 18. 
# function that allows me to pass in the dictionary
# inside of the function = loop through dictionary values
# if the value is an integer
# return sum(i)


example_dictionary = {
  "cat": "bob",
  "dog": 23,
  19: 18,
  90: "fish"
}


def value_sum(example_dictionary):
    int_values = []
    for i in example_dictionary.values():
        if type(i) == int:
            int_values.append(i)

    return sum(int_values)

print(value_sum(example_dictionary))

#switched strategies too early