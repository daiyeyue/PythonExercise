goods = [{"name":"good1", "price":200, "sale":100, "stars":5, "comment":400},{"name":"good2", "price":200, "sale":300, "stars":5, "comment":400},{"name":"good3", "price":200, "sale":120, "stars":4, "comment":500}, {"name":"good4", "price":500, "sale":3000, "stars":5, "comment":398},{"name":"good5", "price":899, "sale":99, "stars":5, "comment":2000}]
#print(goods)
#价格权重40%，销售权重17%，评级权重13%，评论权重30%

#使用sorted进行排序

def my_sorted(arg):
    price = arg['price']
    sale = arg['sale']
    stars = arg['stars']
    comment = arg['comment']

    data = price * 0.4 + sale * 0.17 + stars * 0.13 + comment * 0.3
    return data


print(sorted(goods, key=my_sorted))

r = sorted(goods, key = lambda x:x['price']*0.4 + x['sale']*0.17 + x['stars']*0.13 + x['comment']*0.3 )
print(list(r))

