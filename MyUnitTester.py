import unittest

class tester(unittest.TestCase): # Build a reuseable unit tester for all these problems
    """ Reuseable unit-tester class for leetcode problems
    """
    def test(self,func, *args, **kwargs): # pass in function, test args, and testnum:answer
        """
        func: function with a return
        *args: pass array of values to test
        **kwargs: in format of tx=y, x = test numbers starting at 1,
                                     y = correct answer
        """
        answers = []
        for key in range(len(kwargs)): #turn kwargs into list of ans
            ans = "t"+f"{key+1}"
            answers.append(kwargs.get(ans))
        for i , n in enumerate(args):
            try:
                f = func(n) # test function with each arg
                self.assertEqual(f, answers[i]) #check that it matches the answer
                print(f"Test: {i+1} passed")
            except AssertionError:
                print(f"Test: {i+1} failed (expected: {answers[i]} received: {f})")
            