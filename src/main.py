from string.suffix_string import  SuffixArray
from string.files import ReadTextFile
txtpath = "/home/wenbingu/python/awsome_python/tmp.txt"
notestxtpath = "/home/wenbingu/python/awsome_python/notes.txt"

'''
The main process which could be used to excute
'''
def main():
    print("Main Procedure")
    suffixstring = SuffixArray()
    readfilecontent = ReadTextFile()
    content = readfilecontent.read_content_from_files(notestxtpath)
    strings = suffixstring.build_strings(content)
    defined_string = 
    target_strings = suffixstring.build_strings()

if __name__ == '__main__':
    main()
