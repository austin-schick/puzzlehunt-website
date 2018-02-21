# imagesDemo3a.py
# create base64 encoding
# for use in imagesDemo3b.py

import base64

def readBinaryFile(path):
    with open(path, "rb") as f: return f.read()

def getBase64(filename):
    return base64.encodebytes(readBinaryFile(filename))

print(getBase64("sampleImage1.gif").decode('ascii'))
