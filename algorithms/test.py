def reverse(x):
        """
        :type x: int
        :rtype: int
        """
        sign = -1 if x<0 else 1
        factor = 1
        rev_num = []
        while (x/factor)%10 > 0:
            y = (x/factor)%10
            rev_num.append(y)
            factor *= 10
        print(rev_num)

reverse(123)        
