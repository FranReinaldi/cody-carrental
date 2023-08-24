import multiprocessing

from django.utils.html import strip_tags
from django.template.loader import render_to_string

from applications.core.functions import send_email

from applications.users.models import CustomUser
from .models import Rental


def send_rental_email(customer):

    rental_list = Rental.objects.filter(customer=customer)
    template = 'cars/email/rental_customer.html'
    context = {
        'customer': customer.get_full_name(),
        'rental_list': rental_list,
    }

    html_rendered = render_to_string(
        template_name=template, 
        context=context
    )

    txt_rendered = strip_tags(html_rendered)

    print('SEND MAIL: ', customer.email)

    send_email(
        subject='Your rental list',
        recipient=customer.email,
        txt=txt_rendered,
        html=html_rendered,
    )


def send_rental_all_customers():
    customer_list = [ x for x in CustomUser.objects.all() if x.user_type == 'C' ]
    
    # Cantidad de procesos en paralelo
    pool = multiprocessing.Pool(processes=4)

    pool.map(send_rental_email, customer_list)

    pool.close()
    pool.join()

    return customer_list
