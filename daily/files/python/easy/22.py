#!/usr/bin/env python3

list1, list2 = ["a", "b", "c", 1, 4], ["a", "x", 34, "4"]
print(list1 + [i for i in list2 if i not in list1])
