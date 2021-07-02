class ReadTextFile(object):
    def __init__(self):
        self.defined = []
    
    def read_content_from_files(self, file):
        with open(file) as f:
            content = f.read()
        return content

    def read_strings_from_files(self, file):
        '''
        read content from file
        return the strings
        '''
        with open(file) as f:
            pass