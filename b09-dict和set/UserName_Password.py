#模拟从数据库里面取出来的用户名和密码
user_pass = {"laotie":"password","huniu":"adminf"}

def create_user(username,password):
    """
    
    :param username:用户建立账号的用户名 
    :param password: 用户建立账号的密码
    :return: 
    """
    #判断 用户输入的账号是不是存在
    usernames = user_pass.keys()
    print(usernames)

    if username in usernames:
        print("用户已经被注册")
    else:
       #没有被注册，那么更新我们的user_pass
       #实际情况是会做持久化存储到数据库中
        print("恭喜你，你已经很荣幸的成为了我们的会员")
        user_pass[username] = password

#create_user("daiye","123456")
#print(user_pass)

def login_user(username,password):
    #首先判断登录的用户名是否存在
    usernames = user_pass.keys()
    if username not in usernames:
        print("您还不是我们的会员")
    elif password != user_pass[username]:
        #判断用户的密码是否正确
        print("登录密码错误")
    else:
        print("恭喜你登录成功")

login_user("laotie","password")
