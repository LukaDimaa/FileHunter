import os 

path = input("Enter Folder path: ")
search_name = input("Enter File Name to Search: ")

if os.path.exists(path) and os.path.isdir(path):
    print(F"\nScanning: {path}\n")

    found = False

    for root, dirs, files in os.walk(path):
        for file in files:
            if files == search_name:
                full_path = os.path.join(root, file)
                print(F"[FOUND] {full_path}")
                found = True

            if not found:
                print("file not Found. ")
        else:
            print("invalid Folder Path sorry. ")