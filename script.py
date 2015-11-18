#!/usr/bin/env python
# Copyright 2015 James Beedy <jamesbeedy@gmail.com>
# GNU Affero General Public License version 3 (see the file LICENSE).


class ListOps():
    """List operations"""
    def __init__(self, a):
        self.a = a

    def double_list(self):
        """Returns 2* self.a[i]
        """
        for i in range(0, len(self.a)):
            self.a[i] = self.a[i] * 2
	return self.a


if __name__ == "__main__":

    list_a = []
    num_a = 0
    user_input = input("Please enter a number < 100 : ")
    l = ListOps(range(int(user_input)))
    for i in l.double_list():
        print(i)

