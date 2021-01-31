# 解释：这里的难点在于使用哈希存储jk乘积，然后cnt += jk_products_2[_square]
# 而非list，jk_products_2.count(_square)--->超时
class Solution:
    def numTriplets(self, nums1, nums2):
        jk_products_1 = self.get_products(nums1)
        jk_products_2 = self.get_products(nums2)

        square_1 = [num**2 for num in nums1]
        square_2 = [num**2 for num in nums2]

        cnt = 0
        for _square in square_1:
            if _square in jk_products_2:
                cnt += jk_products_2[_square]  # jk_products_2.count(_square)
        for _square in square_2:
            if _square in jk_products_1:
                cnt += jk_products_1[_square]
        return cnt
        
    def get_products(self, nums):
        products = {}
        for j in range(len(nums)-1):
            for k in range(j+1, len(nums)):
                val = nums[j]*nums[k]
                if val not in products:
                    products[val] = 1
                else:
                    products[val] += 1
        return products



nums1 = [1, 1]
nums2 = [1, 1, 1]
s = Solution()
print(s.numTriplets(nums1, nums2))

