
import datetime

class Request:

    #creating a request for help
    def __init__(self,req_name,req_desc,event_id, user_id, date, time, city, number_of_participants):
        self.req_name=req_name
        self.req_desc=req_desc
        self.event_id = event_id
        self.creator_id = user_id
        self.date = date
        self.time = time
        self.city = city
        self.number_of_participants = number_of_participants
        self.status = "Before event"
        self.volunteer_list = []
        self.is_full = False

    #add volunteer to the request
    def add_volunteer(self, user_id):
        if not self.is_full:
            if self.volunteer_list.index(user_id) == 0:
                self.volunteer_list.append(user_id)

        if len(self.volunteer_list) == self.number_of_participants:
            self.is_full = True

    #remove volunteer from request
    def remove_volunteer(self, user_id):
        self.volunteer_list.remove(user_id)

        if self.is_full:
            self.is_full = False

    #change the status of the event
    def change_status (self):
        date_now = datetime.datetime.now()
        event_date = self.date()
        event_time = self.time()
        if event_date.strftime("%Y-%m-%d") < date_now.strftime("%Y-%m-%d"):
            self.status = "Before event"
        elif event_date.strftime("%Y-%m-%d") == date_now.strftime("%Y-%m-%d"):
            if event_time < date_now.strftime("%H:%M"):
                self.status = "Before event"
            elif event_time == date_now.strftime("%H:%M"):
                self.status = "During event"
            elif event_time > date_now.strftime("%H:%M"):
                self.status = "After event"
        elif event_date.strftime("%Y-%m-%d") > date_now.strftime("%Y-%m-%d"):
            self.status = "After event"