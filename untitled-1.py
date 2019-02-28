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
    Ticket("Bob Ross", "bobross@gmail.com", "27/07/02", True),
    Ticket("Steve Ewrin", "STEVE@gmail.com", "25/01/89", False),
    Ticket("Bill Cosby", "freedrinks@gmail.com", "18/02/69", True)
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

@route('/check-in-success/<ticket_id>')
@view ('check-in-success')
def check_in_success(ticket_id):
    
    ticket_id = int(ticket_id)
    found_ticket = None
    for ticket in tickets:
        if ticket.id == ticket_id:
            found_ticket = ticket
    data = dict (ticket = found_ticket)
    found_ticket.check_in = True
    return data

@route("/sign-up")
@view ("sign-up")
def sign_up():
    pass
    
@route("/sign-up-success")
@view ("sign-up-success")
def sign_up_success():
    name = request.forms.get('name')
    email = request.forms.get('email')
    date_of_birth = request.forms.get('dob')
    
    new_ticket = Ticket(name, email, date_of_birth, False)
    tickets.append(new_tickets)






run(host='0.0.0.0', port=8080, reloader = True, debug = True)