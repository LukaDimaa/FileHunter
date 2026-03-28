import os 
#Import the OS Files Folders Paths etc.

print("=== FileHunter V1 ===")

path =  input("Enter a folder path to scan")

if os.path.exists(path) and os.path.isdir(path): #Checking if the path exists 
    print(F"\nScanning folder: {path}\n")

    for item in os.listdir(path):
        full_path = os.path.join(path, item)

        if os.path.isfile(full_path):
            print(f"[FILE] {item}")
        elif os.path.isdir(full_path):
            print(F"[DIR ] {item}")

else:
    print("Invalid Folder Path.")