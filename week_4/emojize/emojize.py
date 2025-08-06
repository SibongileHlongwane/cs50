import emoji


user_input = input("Input: ").strip()

emojized_text = emoji.emojize(user_input, language="alias")
print("Output: ", emojized_text)
