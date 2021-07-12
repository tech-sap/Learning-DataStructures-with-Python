def search(nums,target):
        l = 0
        r = len(nums)-1
        pos = -1
        while True:
            m = (l+r)//2
            if l+1==r:
                pivot = r
                break
            elif nums[m]<nums[l]:
                r = m
            else:
                l = m
        
        if target<nums[0]:
            l = pivot
        else:
            r = pivot-1
        while l<=r:
            m = (l+r)//2
            if nums[m]==target:
                pos = m
                break
            elif nums[m]<target:
                l = m+1
            else:
                r = m-1
        print(pos)
        
search([7, 8, 9, 10, 1, 2, 3,4,5,6],3)
