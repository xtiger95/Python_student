def register():

    i = 1
    while i==1:
        uname = "username:" + input("请输入用户名:").strip()
        with open("aaa.txt","r") as f:
            for username in f:
                if username[9:].strip() == uname[9:].strip():
                    print("用户已存在!")
                    break
                else:
                    i=0
            continue

    upasswd = "password:" + input("请输入密码:")
    with open("aaa.txt",'a') as f:
        f.write("%s\n%s\n" % (uname,upasswd))

def login():
    uname_passwd = {}
    uname_passwd = save_data()
    print(uname_passwd)
    uname = input("请输入用户名:")
    upaswd = input("请输入密码:")
    if uname_passwd[uname] == upaswd:
        print("登录成功!")
    else:
        print("登录失败!")
    exit()

def save_data():

    uname_list = []
    upasswd_list = []
    a_dict = {}
    pwd = ''
    with open("aaa.txt") as f:
        for data in f:
           # print(data)
            if data[:8] == "username":
                username = data[9:].strip()
                uname_list.append(username)
            else:  # data[:8] == "password":
                pwd = data[9:].strip()
                upasswd_list.append(pwd)
        a_dict = dict(zip(uname_list, upasswd_list))
    return a_dict
def show_menu():

    prompt="""案例2:模拟用户登录信息系统
(0)注册
(1)登录
(2)退出
请输入(0,1,2):"""
    cmd = {"0": register, "1": login}
    while 1:
        choice = input(prompt)
        #cmd = {"0":register,"1":login}
        if choice == "2":
            exit()
        elif choice not in "012":
            print("无效输入!")
            continue
        else:
            break

    cmd[choice]()

if __name__ == '__main__':
    show_menu()
