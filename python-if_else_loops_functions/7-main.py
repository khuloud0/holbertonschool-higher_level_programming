#!/usr/bin/env python3
islower = __import__('7-islower').islower

print("{} is {}".format("a", "lower" if islower("a") else "upper"))
print("{} is {}".format("H", "lower" if islower("H") else "upper"))
print("{} is {}".format("A", "lower" if islower("A") else "upper"))
print("{} is {}".format("3", "lower" if islower("3") else "upper"))
print("{} is {}".format("g", "lower" if islower("g") else "upper"))
