# a = {} # Dictionary
# b = set() # Set
# print(a, type(a))
# print(b, type(b))

# dict1 = {"Name":"Paras Mehra","Boy":"True"}
# print(dict1)
# print(dict1['Name'])

marks = {"Paras":"95", "Karan":89, "Bharat":83}
print(marks["Paras"])
marks["Mukul"] = 86
print(marks)

print(marks.get("Karan"))
print(marks.keys())
print(marks.values())
print(marks.items())