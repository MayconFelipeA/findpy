# Findpy

Simple package in python.

# How is?

Search folders, and search folders in subfolders.
Search string in files this type is .txt, or .cfg, etc...

# Example

**findFolder**
result = findFolder('C:\\Users\\[YourName]\\Desktop', 'hello') #This code go searching your folder 'hello' in your desktop 
print(f'folder: {result['folder'][0]} time: {result['time'][0]}')

* return 
    {'folder': ['C:\\Users\\Maycon\\Desktop\\hello'], 'time': [0.0]} -> folder and time

* parameters
    findFolder(folder, folderSearch)

    folder = initial folder for searching
    folderSearch = folder for search


**findString**
result = findString('C:\\Users\\[YourName]\\Desktop', 'hello, my name is maycon!', '.txt')
print(result['folder'][0])

* return
    ['C:\\Users\\Maycon\\Desktop\\hello'] -> folder

* parameters
    findString(folder, string, tfile)

    folder = inital folder for searching
    string = string for search
    tfile = type file for search


** GOOD USE **
This is my first package, suggestion contact me.