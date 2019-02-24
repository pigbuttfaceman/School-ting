# School-ting
#ver 1.0
#ver 1.2
#ver 1.3
#ver 1.4
#ver 1.5

from bottle import run, route, view, get, post, request
from itertools import count

class Ticket:

    _ids = count (0)

    def __init__(self, name, email, date_of_birth, check_in):
        self.id = next(self._ids)
        self.name = name
        self.email = email
        self.dob = date_of_birth
        self.check_in = check_in
        
tickets = [
    Ticket("Ethan Stace", "staceethan@gmail.com", "26/07/02", False),
    Ticket("Bob Ross", "bobross@gmail.com", "27/07/02", False),
    Ticket("Steve Ewrin", "STEVE@gmail.com", "25/01/89", False),
    Ticket("Bill Cosby", "freedrinks@gmail.com", "18/02/69", False)
    ]


#index page
@route("/")
@view ("index")
def index():

    pass


#check in
@route("/check-in")
@view ("check-in")
def check_in():
    data = dict (ticket_list = tickets)
    return data






run(host='0.0.0.0', port=8080, reloader = True, debug = True)