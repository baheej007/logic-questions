ba = bytearray(b"hello ")

ba += b"world"       
print(ba)
ba += " python".encode() 
print(ba)                
