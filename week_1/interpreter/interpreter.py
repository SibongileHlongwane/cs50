user_input = input("Expression: ")

result = float(eval(user_input))
rounded_result = round(result, 1)
print(rounded_result)