"""

This is an example file, you can delete it, but it showcases how you should write functions and classes.

"""

class Adder:
    """
    This is an example class. This class gets two numbers and adds them together.
    """

    def __init__(self, a, b):
        """
        This is the constructor of the class. It gets two numbers and saves them as attributes.

        :param a: The first number.
        :type a: float
        :param b: The second number.
        :type b: float
        """
        self.a = a
        self.b = b

    def result(self):
        """
        This function returns the result of the addition.

        :return: The result of the addition.
        :rtype: float
        """
        return self.a + self.b

def add(a, b):
    """
    This is an example function. It gets two numbers and adds them together.

    :param a: The first number.
    :type a: float
    :param b: The second number.
    :type b: float
    :return: The result of the addition.
    :rtype: float
    """
    return a + b