import zlib

string = "hello world!hello world!hello world!hello world!"

# compress string
compressed_string = zlib.compress(string.encode())

# decompress string
decompressed_string = zlib.decompress(compressed_string).decode()

print("Original String: ", string)
print("Compressed String: ", compressed_string)
print("Decompressed String: ", decompressed_string)
