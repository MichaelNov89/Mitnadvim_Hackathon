

# class for user that will be in the firebase
class User:
    uid=""
    username=""
    volunteer_times=0
    rating=0



    def __init__(self,username,uid):
        self.username = username
        self.uid=uid
        self.volunteer_times=0
        self.rating=0
#getters
    def get_uid (self):
        return self.uid
    def get_username (self):
        return self.username
    def get_volunteer_times (self):
        return self.volunteer_times
    def get_rating (self):
#setters
    def set_uid(self,uid):
        self.uid=uid
    def set_username(self,username):
        self.username=username
    def set_volunteer_times(self,volunteer_times):
        self.volunteer_times=volunteer_times
    def set_rating(self,rating):
        self.rating=rating

#
