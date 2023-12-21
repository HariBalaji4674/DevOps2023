import os

for path,dirs,files in os.walk("C:\\Users\'KRISHNA HARI'"):
    for f in dirs:
        print(f)