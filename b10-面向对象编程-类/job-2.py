class DictClass():

    def __init__(self, dict):
        self.dict = dict

    def del_key(self, key):
        #判断key是否在字典里
        if key not in self.dict.keys():
            return print("key不在字典里")
        else:
            self.dict.pop(key)

    def get_dict(self, key):
        if key not in self.dict.keys():
            return print("not found")
        else:
            return print(self.dict[key])

    def get_key(self):
        return print(list(self.dict.keys()))

    def update_dict(self, dict):
        self.dict.update(dict)
        return print(list(self.dict.values()))

d = DictClass({"a":1, "b":2})
d.del_key("c")
d.get_dict("b")
d.get_key()
dict1 = {"c":3}
d.update_dict(dict1)



