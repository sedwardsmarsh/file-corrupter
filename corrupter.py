# This script is called from main.py
# function for corrupting a file

def corrupt_file(path: str) -> None:
    f = open(path, 'wb') # open the file in binary mode for writing
    for offset in range(1, 3):
        f.seek(offset)
        f.write(bytes('garbage', 'utf-8')) # write anything into the file
    f.close()