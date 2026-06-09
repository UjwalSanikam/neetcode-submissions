class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product_list = []
        length = len(nums)
        i = 0
        while i < length:
            prefix_product = 1
            suffix_product = 1
            j = i - 1
            k = i + 1
            while j >= 0:
                prefix_product = prefix_product * nums[j]
                j = j - 1
            while k < length:
                suffix_product = suffix_product * nums[k]
                k = k + 1
            product_list.append(suffix_product*prefix_product)
            i = i + 1
        return product_list


