class Listinfo():

    def __init__(self, list):
        self.list = list

    def add_key(self, item):
        self.list.append(item)
        print(self.list)

    def get_key(self, index):
        if index >=0 and index < len(self.list):
            return print(self.list[index])
        return print("输入有误")

    def update_list(self,list):
        self.list.extend(list)
        print(self.list)

    def del_key(self, key):
        if key not in self.list:
            print("元素不在列表中")
        else:
            self.list.remove(key)
            print(self.list)
            return print(self.list[-1])


l = Listinfo(['1','2','3'])
l.add_key('4')
l.get_key(3)
lplus = ['4','5']
l.update_list(lplus)
l.del_key("6")