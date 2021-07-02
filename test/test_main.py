import unittest
import sys

sys.path.insert(1, '/home/wenbingu/python/awsome_python/')
from src.string.suffix_string import SuffixArray
from src.string.files import ReadTextFile
txtpath = "/home/wenbingu/python/awsome_python/tmp.txt"

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
        self.assertEqual(self.suffixarray.compare_string("ccc", "ccc"), 0)
        self.assertEqual(self.suffixarray.compare_string("ccb", "cca"), 1)
    
    def test_rank(self):
        suffixstrings = self.suffixarray.build_strings("abc")
        self.assertEqual(self.suffixarray.rank(suffixstrings, "cc"), False)
        self.assertEqual(self.suffixarray.rank(suffixstrings, "bc"), True)

    def test_read_content(self):
        contentfunc = ReadTextFile()
        content = contentfunc.read_content_from_files(txtpath)
        self.assertEqual(content, "wenbingu\n")




if __name__ == '__main__':
    unittest.main()