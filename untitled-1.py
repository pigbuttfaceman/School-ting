# School-ting


from bottle import run, route, view, get, post, request
from itertools import count

class Ticket:

    _ids = count (0)

    def __init__(self, name, email, date_of_birth, check_in):
        self.id = next(self._ids)
        self.name = name
        self_email = email
        self_dob = date_of_birth
        self_check_in = check_in
        
tickets = [
    Ticket("Ethan Stace", "staceethan@gmail.com", "26/07/02", False),
    Ticket("Bob Ross", "bobross@gmail.com", "27/07/02", False),
    Ticket("Steve Ewrin", "STEVE@gmail.com", "25/01/89", False),
    Ticket("Morgan Freeman", "sooth@gmail.com", "18/02/69", False)
    ]


#index page
@route("/")
@view ("index")
def index():

    pass








run(host='0.0.0.0', port=8080, reloader = True, debug = True)