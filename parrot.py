prompt = "\nTell me something and I will repeat it back at you:"
prompt += "\nEnter 'quit' to end program."

message = ""
while message != 'quit':
    message = input(prompt)

if message != 'quit':
    print(message)