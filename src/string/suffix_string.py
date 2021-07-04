class SuffixArray(object):
    def __init__(self):
        '''
        The suffixarray search method for strings
        record my own footsteps
        '''
        self.sa = []
    

    def build_strings(self, Strings):
        '''
        Generate the suffix substrings
        '''
        length = len(Strings)
        substrings = []
        for i in range(length):
            substrings.append(Strings[i:])
        return sorted(substrings)

    def lcp(self, AString, BString):
        '''
        return the longest prefix string of two string
        '''
        length = min(len(AString),  len(BString))
        for i in range(length):
            if AString[i] != BString[i]:
                return AString[:i]
        return AString[:length]
    
    def compare_string(self, StringA, StringB):
        '''
        return: 1, 0, -1
        StringA > StringB: 1
        StringA = StringB: 0
        StringA < StringB: -1
        '''
        if StringB.startswith(StringA):
            return 0
        elif StringA > StringB:
            return 1
        else:
            return -1

    def rank(self, StringArray, Target):
        '''
        search the target string in substrings
        Target: string
        StringArray: [string]
        note: need be carefule with the mid value
        '''
        lo = 0
        high = len(StringArray) - 1
        while lo <= high:
            mid = lo + (high - lo)/2
            cmp = self.compare_string(Target, StringArray[mid])
            if cmp == 0:
                return True
            elif cmp > 0:
                lo = mid + 1
            else:
                high = mid - 1
        return False
