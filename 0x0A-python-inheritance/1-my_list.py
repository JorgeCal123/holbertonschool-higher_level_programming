#!/usr/bin/python3
"""class MyList"""


class MyList(list):
    """prints the list, but sorted"""

    def print_sorted(self):
        """print_sorted"""

        print(sorted(self))
