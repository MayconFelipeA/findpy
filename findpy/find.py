import glob, os, time

def findString(folder, string, tfile) -> object:

    directory = {
        'folders': [],
        'found': []
    }   

    for (root, dirs, file) in os.walk(folder, topdown=True):
        if dirs != 0:
            for d in dirs:
                directory['folders'].append(f'{root}\\{d}')

    directory['folders'].append(f'{folder}\\')

    for f in directory['folders']:
        for file in glob.glob(f'{f}\\*{tfile}'):
            with open(file, "r", encoding="ANSI") as fd:
                text = fd.read()
                if string in text:
                    directory['found'].append(file)
            fd.close()

    return directory['found']


def findFolder(folder, folderSearch) -> object:
    directory = {
        'folder': [],
        'time': []
    }
    
    t = time.time()
    for (root, dirs, _) in os.walk(folder, topdown=True):
        for d in dirs:
            if d == folderSearch:
                directory['folder'].append(f'{root}\\{d}')
                directory['time'].append(time.time()-t)

    return directory