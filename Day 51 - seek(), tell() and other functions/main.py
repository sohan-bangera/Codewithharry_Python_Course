# with open('file.txt', 'r') as f:
#     print(type(f))
#     #Move to the 10th byte in the file
#     f.seek(10)

#     print(f.tell())
#     #Read the next 5 bytes
#     data = f.read(5)
#     print(data)

with open('file.txt', 'r') as f:
  # Read the first 10 bytes
  data = f.read(10)

  # Save the current position
  current_position = f.tell()

  # Seek to the saved position
  x = f.seek(current_position)
  data1 = f.read(10)
  print(data)
  print(data1)
  print(x)
  print(current_position)