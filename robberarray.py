



nums=[0]
def rob( nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        sum = 0
        print(len(nums))

        iteration = 0

        if len(nums) > 2:

            for i in nums:
                iteration += 1

                if iteration % 2 == 0:

                    continue



                else:
                    sum = sum + i


        elif len(nums) == 1:
            return sum



        else:
            sum += nums[1]

        return sum



print(rob(nums))


