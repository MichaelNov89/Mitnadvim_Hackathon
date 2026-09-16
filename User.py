

# class for user that will be in the firebase
class User:
    uid=""
    username=""
    volunteer_times=0
    rating=0
    created_req_list=[]
    vol_list=[]



    def __init__(self,username,uid):
        self.username = username
        self.uid=uid
        self.volunteer_times=0
        self.rating=0
        self.created_req_list=[]
        self.vol_list=[]


#
