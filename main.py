from messenger import JPGHiddenMessager

messenger = JPGHiddenMessager("Cat.jpg")

# Read the message
message = messenger.read()
print(message)


# Delete the message
messenger.format()


# Write the message
# messenger.write("<your-message>")
