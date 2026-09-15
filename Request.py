
import datetime

class Request:

    #creating a request for help
    def __init__(self, user_id, date, time, city, number_of_participants):
        self.user_id = user_id
        self.date = date
        self.time = time
        self.city = city
        self.number_of_participants = number_of_participants
        self.status = "Before event"
        self.volunteer_list = []
        self.is_full = False

    #getters
    def get_user_id(self):
        return self.user_id

    def get_date(self):
        return self.date.strftime("%Y-%m-%d")

    def get_time(self):
        return self.time.strftime("%H:%M")

    def get_city(self):
        return self.city

    def get_number_of_participants(self):
        return self.number_of_participants

    def get_volunteer_list(self):
        return self.volunteer_list

    def get_is_full(self):
        return self.is_full

    def set_status(self, status):
        self.status = status

    #setters
    def set_user_id(self, user_id):
        self.user_id = user_id

    def set_date(self, date):
        self.date = date

    def set_time(self, time):
        self.time = time

    def set_city(self, city):
        self.city = city

    def set_number_of_participants(self, number_of_participants):
        self.number_of_participants = number_of_participants

    #add volunteer to the request
    def add_volunteer(self, user_id):
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
        event_date = self.get_date()
        event_time = self.get_time()
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

