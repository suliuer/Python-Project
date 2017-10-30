from django.test import TestCase

# Create your tests here.

l1 = [(1, '初级'), (2, '中级'), (3, '高级')]
print(l1)

ret = map(lambda x: {"id": x[0], "name": x[1]}, l1)

print(ret)
for item in ret:
    print(item)