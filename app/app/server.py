"""
This file should be used to be the main entry point for your app.
In here shouldn't be any logic, besides the logic to start your app.
"""
from appName.exampleFile import Adder, add

if __name__ == "__main__":
    adder = Adder(1, 2)
    print(adder.result())

    print(add(1, 2))
