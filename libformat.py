def format(dict):
    pass
    
def create_user(info):
    user = {}
    for data in info:
        print(data + ':')
        opc = input()
        user.update({data : opc})
    return user
        
