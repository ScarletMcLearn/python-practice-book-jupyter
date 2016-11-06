import zipfile
import sys


def compress(zip_filename, files):
    zf = zipfile.ZipFile(zip_filename, 'w')
    for f in files:
        zf.write(f)
    zf.close()

if __name__ == "__main__":
    params = sys.argv[1:]
    try:
        filename = params[1]
        compress(filename, params[1:])
    except:
        print("You must run the program in this format")
        print("python zip.py [zip file] [filenames ...]")



