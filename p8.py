input_string='python is a programming language it is also a sripting language'
d1={word:input_string.split().count(word) for word in input_string.split()}

print(d1)