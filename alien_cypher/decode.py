import base64


with open("./alien_cypher.txt","rb") as fl:
    # fl.seek(2)
    cyph = fl.read()

# print(cyph)

# de = cyph.decode('utf-8')

de = base64.b64decode(cyph)

print(de)
# ans = de.decode('utf-8')

# print(ans)

# print(cyph)
# cp = cyph.decode('utf-8')
# print(base64.b64decode(cp))
