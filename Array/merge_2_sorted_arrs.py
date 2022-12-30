class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # Approach: Write from end of nums 1, traverse nums1 and nums2 from end and fill in empty spaces on nums1
        # TC: O(m+n)
        # SC: O(1)
        
        # Initialize pointers pointing to end of nums1 nums2 and m+n
        write_idx = m+n-1
        m_idx = m-1
        n_idx = n-1
        
        while(write_idx > -1):
            # 1. If start of n reached then nothign else left to process
            if n_idx < 0:
                break
                
            # 2. If m is greater, then swap
            if m_idx > -1 and nums1[m_idx] > nums2[n_idx]:
                nums1[write_idx] = nums1[m_idx]
                m_idx -= 1
                
            else:
                # 3. n will be greater otherwise
                nums1[write_idx] = nums2[n_idx]
                n_idx -= 1
            
            write_idx -= 1