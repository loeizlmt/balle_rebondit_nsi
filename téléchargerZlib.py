import zlib

# Exemple : Compression et décompression d'une chaîne
data = b'This is a test string for zlib compression'
compressed_data = zlib.compress(data)
decompressed_data = zlib.decompress(compressed_data)

print('Original:', data)
print('Compressed:', compressed_data)
print('Decompressed:', decompressed_data)