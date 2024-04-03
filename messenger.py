# -*- coding: utf-8 -*-
# Author: Cypherr


# Define the start and end bytes for the JPG file format
START_BYTES = ['FF', 'D8', 'FF', 'E0']
END_BYTES = ['FF', 'D9']


class JPGHiddenMessager(object):
    def __init__(self, image: str):
        self._image = image

    def write(self, message):
        # Open the image file in append binary mode
        with open(self._image, "ab") as f:
            # Write the message to the file in UTF-8 encoding
            f.write(message.encode('utf-8'))

    def read(self):
        # Open the image file in read binary mode
        with open(self._image, "rb") as f:
            # Read the entire content of the file
            content = f.read()

            # Check if the file starts with the expected start bytes
            assert 0 == content.index(bytes.fromhex(
                "".join(START_BYTES))), "Error in JPG format."

            # Find the offset of the end bytes
            offset = content.index(bytes.fromhex("".join(END_BYTES)))

            # Move the file pointer to the position after the end bytes
            f.seek(offset+2)

            # Read and return the remaining content
            return f.read()

    def format(self):
        try:
            # Open the image file in read binary mode
            with open(self._image, "rb") as file:
                # Read the entire content of the file
                content = file.read()

                # Find the offset of the end bytes
                offset = content.index(bytes.fromhex("".join(END_BYTES)))

                # Extract the content up to and including the end bytes
                updated_content = content[:offset+2]

            # Reopen the image file in write binary mode
            with open(self._image, "wb") as file:
                # Write the updated content back to the file
                file.write(updated_content)

            # Return True to indicate successful formatting
            return True
        except:
            # Return False if an exception occurs during formatting
            return False
