from string.suffix_string import SuffixArray
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
     
    defined_content = readfilecontent.read_content_from_files(txtpath)
    defined_string = suffixstring.build_strings(defined_content.strip())
    searched_strings = []

    lsr = ""
    for string in defined_string:
        if suffixstring.rank(strings, string):
            if len(string) > len(lsr):
                lsr = string

    print("The longest substring is:{}".format(lsr))


if __name__ == '__main__':
    main()
