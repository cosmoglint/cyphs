import base64
# Creating a string
s = "Hello World!"

# Encoding the string into bytes
b = s.encode("UTF-8")
# print(b)

# Base64 Encode the bytes
e = base64.b64encode(b)
print(e)

# Decoding the Base64 bytes to string
s1 = e.decode("UTF-8")

# Printing Base64 encoded string
print("Base64 Encoded:", s1)

# Encoding the Base64 encoded string into bytes
b1 = s1.encode("UTF-8")
print(b1)

# Decoding the Base64 bytes
d = base64.b64decode(b1)
print(d)

# Decoding the bytes to string
s2 = d.decode("UTF-8")
print(s2)
