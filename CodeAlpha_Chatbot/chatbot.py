print("TEST RUNNING")
def chatbot_response(user_input):
    if  user_input == "hello":
        return "Hi"
    elif user_input == "how are you?":
        return "I'm fine, thanks!"
    elif user_input == "bye" :
        return "Goodbye!"
    else:
        return "Sorry, I don't understand "


print("Simple Rules-Based Chatbot")
print("Type 'bye'to exit\n")

while True:
        user_input = input("you: ") .strip()  .lower()
        response = chatbot_response(user_input)
        print("Bot:" , response)
        if user_input == "bye":
            break

