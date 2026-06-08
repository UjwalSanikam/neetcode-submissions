class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""
        for i in range(len(strs)):
            encoded_string = encoded_string + str(len(strs[i])) + "#" + strs[i]
        return encoded_string

    def decode(self, s: str) -> List[str]:
        decoded_list = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j = j + 1
            length = int(s[i:j])
            start_index = j + 1
            end_index = start_index + length
            decoded_list.append(s[start_index:end_index])
            i = end_index
        return decoded_list
