
# def func():
#     a = input('input your name')
#     print('Hello ' + a)
#
#
# def test():

path = 'test/test32'
if path.count('/'):
    path = path.replace('/', '\\')
    print(path)
    i = path.rindex('\\')
    path = path[i + 1:]
print(path)