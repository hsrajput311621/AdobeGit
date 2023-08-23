# # set in python
# # set is an unordered and unindexed collection of elements enclosed with {}
# s = {1, 2, 3, 4.6, 'sparta', 4, "Hello"}
# print(type(s))
# print(s)
# # output:<class 'set'>
# # output:{1, 2, 3, 4, 'Hello', 'sparta'}
#
# # add()
# s = {1, 2, 3, 4.6, 'sparta', 4, "Hello"}
# s.add("hercules")
# print(s)
# # output: {1, 2, 3, 4.6, 4, 'hercules', 'sparta', 'Hello'}
#
# # Remove()
# s = {1, 2, 3, 4.6, 4, 'hercules', 'sparta', 'Hello'}
# s.remove('Hello')
# print(s)
# # output: {1, 2, 3, 4.6, 4, 'hercules', 'sparta'}
#
# # Adding Multiple elements in Set
# s = {1, 2, 3, 4.6, 4, 'hercules', 'sparta', 'Hello'}
# s.update([100, 99, "spanish"])
# print(s)
# output: {1, 2, 3, 4.6, 4, 'sparta', 100, 99, 'spanish', 'hercules', 'Hello'}

# union of two sets
s1 = {1, 2, 3, 4, 5, 6}
s2 = {"hello", "sparta", "hercules", 5,6,2}
s1.union(s2)
s1.intersection(s2)


