import shutil
def main():
    # Copy file to another directory
    newPath = shutil.copy('sample1.txt', '/home/varung/test')
    print("Path of copied file : ", newPath)
    #Copy a file with new name
    newPath = shutil.copy('sample1.txt', '/home/varung/test/sample2.txt')
    print("Path of copied file : ", newPath)
    # Copy a symbolic link as a new link
    newPath = shutil.copy('/home/varung/test/link.csv', '/home/varung/test/sample2.csv')
    print("Path of copied file : ", newPath)
    # Copy target file pointed by symbolic link
    newPath = shutil.copy('/home/varung/test/link.csv', '/home/varung/test/newlink.csv', follow_symlinks=False)
    print("Path of copied file : ", newPath)
if __name__ == '__main__':
    main()
