import pybase64
print("#"*90)
print("\t\t\t\tBase64 Simple Decoder Tool")
print("#"*90)

n= input("\nEnter Base64 Encoded Data: ")
decoded_data = pybase64.b64decode(n)

print("\nDecoded text is ",decoded_data,"\n")
