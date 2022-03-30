try:
    # take path of image as a input
    path = input(r'Image path: ')

    # taking encryption key as input
    key = int(input('Encryption key: '))

    # print path of image file and encryption key that
    # we are using
    print('Image: ', path)
    print('Key: ', key)

    # open file for reading purpose
    fin = open(path, 'rb')

    # storing image data in variable "image"
    image = fin.read()
    fin.close()

    # converting image into byte array to
    # perform encryption easily on numeric data
    image = bytearray(image)

    # performing XOR operation on each value of bytearray
    for index, values in enumerate(image):
        image[index] = values ^ key

    # opening file for writing purpose
    fin = open(path, 'wb')

    # writing encrypted data in image
    fin.write(image)
    fin.close()
    print('Encryption Done')


except Exception:
    print('Error: ', Exception.__name__)
