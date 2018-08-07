import os

each = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'Download')
path = os.listdir(each)
# print(path)
file = os.path.join(each, path[-1])
print(file)
# print(each)
# a=each + '//'+'Download//个人投资者模板.xlsx'
# print(a)


