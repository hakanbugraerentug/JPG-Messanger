# JPG-Secret-Messager

[![Header.png](https://i.postimg.cc/Kz2G7Xzp/Header.png)](https://postimg.cc/VSKP1VXX)

Write some hidden messages, read and delete message back.

## Initilize

Create the class instance.

```python
from messenger import JPGHiddenMessager

## Name of the image file.
>>> filename = "Cat.jpg"

>>> messenger = JPGHiddenMessager(filename)
```

## To Write Secret Message to JPG Image

Write the secret message at the end of the JPG byte codes.

```python

>>> mySecretMessage = "The Nuclear Code is: 123456"
>>> messenger.write(mySecretMessage)

```

## To read any Secret Messages

Write the secret message at the end of the JPG byte codes.

```python
>>> messenger.read()
b"The Nuclear Code is: 123456"
```

## To Reset the Image

Write the secret message at the end of the JPG byte codes.

```python
>>> messenger.format()

>>> messenger.read()
b''
```

## Multi-Line

Write the secret message at the end of the JPG byte codes.

```python
>>> messenger.write("bbb")
>>> messenger.write("aaa")

>>> messager.read()
b'aaabbb'
```

## Contribition:

Contributions to this project are welcome! If you would like to contribute, please follow these guidelines:

- Fork the repository and create a new branch for your contribution.
- Make your changes or additions in the branch.
- Ensure your code follows the project's coding style and conventions.
- Write clear and concise commit messages.
- Create a pull request to submit your contribution.
  We appreciate your contributions and will review the pull request as soon as possible. Thank you for helping to improve this project!

## Licence:

This project is licensed under the Apache License.
You are free to use, modify, and distribute this project under the terms of the license.
See the LICENSE file for more details.
