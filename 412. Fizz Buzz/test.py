class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        ret = []
        for number in range(1,n+1):
            resp = ""

            if number % 3 == 0:
                resp = resp + "Fizz"

            if number % 5 == 0:
                resp = resp + "Buzz"

            if resp == "":
                resp = str(number)
            ret.append(resp)
        return ret

assert Solution().fizzBuzz(15) == [
    "1",
    "2",
    "Fizz",
    "4",
    "Buzz",
    "Fizz",
    "7",
    "8",
    "Fizz",
    "Buzz",
    "11",
    "Fizz",
    "13",
    "14",
    "FizzBuzz"
]
