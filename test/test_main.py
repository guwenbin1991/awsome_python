import unittest
import sys

sys.path.insert(1, '/home/wenbingu/python/awsome_python/')
from src.string.suffix_string import SuffixArray
from src.string.files import ReadTextFile
txtpath = "/home/wenbingu/python/awsome_python/tmp.txt"
notestxtpath = "/home/wenbingu/python/awsome_python/notes.txt"


class TestStringMethods(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(TestStringMethods, self).__init__(*args, **kwargs)
        self.suffixarray = SuffixArray()

    def test_suffix(self):
        self.assertEqual(self.suffixarray.build_strings("a"),["a"])
        self.assertEqual(self.suffixarray.build_strings("ab"),["ab","b"])
        self.assertEqual(self.suffixarray.build_strings("ca"),["a","ca"])

    def test_lcp(self):
        self.assertEqual(self.suffixarray.lcp("wenbingu", "wenbinyan"), "wenbin")
        self.assertEqual(self.suffixarray.lcp("wenbin", "wenbin"), "wenbin")

    def test_compare_str(self):
        self.assertEqual(self.suffixarray.compare_string("wenbingu", "wenbinyan"), -1)
        self.assertEqual(self.suffixarray.compare_string("cc c", "cc c"), 0)
        self.assertEqual(self.suffixarray.compare_string("ccb", "cca"), 1)
        self.assertEqual(self.suffixarray.compare_string("book", "book that"), 0)
    
    def test_rank(self):
        suffixstrings = self.suffixarray.build_strings("a book that")
        self.assertEqual(self.suffixarray.rank(suffixstrings, "book"), True)

    def test_read_content(self):
        contentfunc = ReadTextFile()
        content = contentfunc.read_content_from_files(txtpath)
        self.assertEqual(content, "wenbingu a book that\n")

    def test_has_specific_string_in_notes(self):
        contentfunc = ReadTextFile()
        content = contentfunc.read_content_from_files(notestxtpath)
        suffix_strings = self.suffixarray.build_strings(content)
        self.assertEqual(self.suffixarray.rank(suffix_strings, "a book that"), True)


if __name__ == '__main__':
    unittest.main()