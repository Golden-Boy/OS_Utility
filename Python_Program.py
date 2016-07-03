import argparse,shutil,sys,os
#file = r'C:/Users/Justice/Downloads/NewTextDocument.txt'
#destination = r'C:/Users/Justice/Desktop'

def copy_file(filename, destination):
    try:
        shutil.copy(filename,destination)
        print('File:',filename,'successfully copied to',destination)
    except Exception as exp:
        print(exp)

def delete_file(file_to_delete):
    try:
        os.unlink(file_to_delete)
        print('File:', file_to_delete, 'successfully deleted')
    except Exception as exp:
        print(exp)

def delete_directory(directory):
    try:
        rmdir(directory)

    except Exception as exp:
        print(exp)

def list_contents(contents):
    #listdir(contents)
    pass

def search_file(search_file):
    pass

def make_directory(directx):
    mkdir(directx)

def Main():
    parser = argparse.ArgumentParser(description='Operating System utility')
    parser.add_argument('--filename','--f', type=str, help='Absolute path of the filename')
    parser.add_argument('--destination','--d', type=str, help='Absolute path of destination')
    parser.add_argument('--delete', "--DF", help='Permanently delete file')
    parser.add_argument('--removedir', '--rmdir', help='Permanently delete directory and its contents')
    args = parser.parse_args()

    copy_file(args.filename, args.destination)
    delete_file(args.delete)
    delete_directory(args.removedir)

if __name__ == '__main__':
    Main()


'''
Add ability to search for a specific file and/or extensions and list them
'''
