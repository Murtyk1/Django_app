from django.shortcuts import render
from .models import Ticket

def ticket_list(request):
    tickets = Ticket.objects.all().order_by('price')
    return render(request, 'tickets/list.html', {'tickets': tickets})
