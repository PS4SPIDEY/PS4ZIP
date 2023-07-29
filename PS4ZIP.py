import zipfile
print(
"""
|----------------   |---------- |           |
|               |   |           |           |
|               |   |           |           |
|               |   |           |           |
|               |   |           |           |
|---------------|   |---------- |----------------- 
|                             |             |      
|                             |             |
|                   ----------|             |
      
THIS WAS CREATED BY SHAMEEL(CEO OF EVERYONE LEARN TECH PS4 YOUTUBE CHANNEL)
SUBSCRIBE MY CHANNEL TO GET MORE VIDEOS ABOUT HACKING

BYE THANK YOU TO USE ME
https://youtube.com/@everyonelearntech
https://everyonelearntechps4.w3spaces.com/
""")

zip = zipfile.ZipFile(input("Enter the zip file name:"))
with open("shamee.txt",'rb') as file:
    for line in file:
        line=line.strip()
        try:
            zip.extractall(pwd=line)

            print("Password is ",line.decode())
            print("THANK YOU TO USE ME -SHAMEEL-")
            break
        except:
            print("Password not found")