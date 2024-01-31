# l1 = [1, 2, 3]
# l2 = l1
# l1 = l1 + [4]
# print(l2)
# def increment(n):
#     n += 1

# a = 1
# increment(a)
# print(a)
# def assign_value(n, v):
#     n = v

# l1 = [1, 2, 3]
# l2 = [4, 5, 6]
# assign_value(l1, l2)
# print(l1)
# s1 = "Best"
# s2 = s1
# print(s1 is s2)
#!/usr/bin/python3
class LockedClass:
    __slots__ = ('first_name',)
    