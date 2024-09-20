from django.shortcuts import render
from django.http import HttpResponse

from .models import Authors

import requests
import datetime

def Home(request):
    return HttpResponse('Hello World from Django.')

def igtagdemo(request):

    data = {
        'name': 'James Anderson',
        'is_visible': True,
        'logge_in': True,
        'country_code': 'PE',
        'work_experience': 35
    }
    template_file_name = 'djangobasicsapp/if_tag_demo.html'
    dict = {
        'data': data
    }

    return render(request, template_file_name, dict)

def ShowProducts(request):

    products = [
        {
            'product_id': 1,
            'product_name': 'AMD Ryzen 3970',
            'quantity': 100,
            'units_in_stock': 50,
            'discontinued': True,
            'cost': 3000
        },
        {
            'product_id': 2,
            'product_name': 'AMD Ryzen 3970',
            'quantity': 100,
            'units_in_stock': 50,
            'discontinued': True,
            'cost': 3000
        },
        {
            'product_id': 3,
            'product_name': 'AMD Ryzen 3970',
            'quantity': 100,
            'units_in_stock': 50,
            'discontinued': False,
            'cost': 3000
        },
        {
            'product_id': 4,
            'product_name': 'AMD Ryzen 3970',
            'quantity': 100,
            'units_in_stock': 50,
            'discontinued': False,
            'cost': 3000
        },
        {
            'product_id': 5,
            'product_name': 'AMD Ryzen 3970',
            'quantity': 100,
            'units_in_stock': 50,
            'discontinued': True,
            'cost': 3000
        },
        {
            'product_id': 6,
            'product_name': 'AMD Ryzen 3970',
            'quantity': 100,
            'units_in_stock': 50,
            'discontinued': True,
            'cost': 3000
        },
        {
            'product_id': 7,
            'product_name': 'AMD Ryzen 3970',
            'quantity': 100,
            'units_in_stock': 50,
            'discontinued': True,
            'cost': 3000
        },
        {
            'product_id': 8,
            'product_name': 'AMD Ryzen 3970',
            'quantity': 100,
            'units_in_stock': 50,
            'discontinued': False,
            'cost': 3000
        }   
    ]

    template_file_name = 'djangobasicsapp/show_products.html'

    dict = {
        'products': products,
        'total_products': len(products)
    }

    return render(request, template_file_name, dict)

def LoadUsers(request):
    template_file_name = 'djangobasicsapp/show_users.html'

    response = call_rest_api()

    dict = {
        'users': response.json()
    }

    return render(request, template_file_name, dict)

def LoadUsers2(request):

    template_file_name = 'djangobasicsapp/show_users_as_cards.html'
    image = 'https://i.pravatar.cc'
    response = call_rest_api()


    dict = {
        'users': response.json(),
        'image': image
    }

    return render(request, template_file_name, dict)


def Index(request):
    template_file_name = 'djangobasicsapp/index.html'
    
    return render(request, template_file_name)

def call_rest_api():
    BASE_URL = 'https://fakestoreapi.com'
    response = requests.get(f'{BASE_URL}/users')

    return response

def call_rest_api_2(userid):
    BASE_URL = 'https://fakestoreapi.com'
    response = requests.get(f'{BASE_URL}/users/{userid}')
    return response


def LoadUserDetails(request):

    if request.method == 'POST':
        counter = int(request.POST.get('useridcounter'))
        if(request.POST.get('btnNext')):
            counter += 1
            if counter >= 11:
                counter = 1
        elif(request.POST.get('btnPrevious')):
            counter -= 1
            if counter == 0:
                counter = 1
    else:
        counter = 1

    template_file_name = 'djangobasicsapp/show_user_details.html'
    response = call_rest_api_2(counter)
    image = 'https://i.pravatar.cc'
    dict = {
        'user': response.json(),
        'image': image
    }

    return render(request, template_file_name, dict)


def PassModelToTemplate(request):
    # instantiated model class object
    obj = Authors('Chad Mendis', 'USA', 'UFC')
    template_file_name = 'djangobasicsapp/pass_model.html'

    authors = []

    authors.append(Authors('Flavio', 'PE', 'flavio'))
    authors.append(Authors('Flavio', 'PE', 'flavio'))
    authors.append(Authors('Flavio', 'PE', 'flassvio'))
    authors.append(Authors('Flavio', 'PE', 'flavio'))
    authors.append(Authors('Flavio', 'PE', 'flavio'))
    authors.append(Authors('Flavio', 'PE', 'flavi11o'))

    dict = {
        'author': obj,
        'authors': authors
    }

    return render(request, template_file_name, dict)

def BuiltInFiltersDemo(request):
    processors = [
        { 'name': 'Ryzen 3970', 'cores': 32 },
        { 'name': 'Ryzen 3950', 'cores': 16 },
        { 'name': 'Ryzen 3990', 'cores': 64 }
    ]

    dict = {
        'probation_period': 4,
        'first_name': 'Connors',
        'last_name': 'McGregor',
        'pay_for_fight': 100000,
        'first_quarter': ['Jan', 'Feb', 'Mar'],
        'second_quarter': ['Apr', 'May', 'Jun'],
        'f_quarter': [1, 2, 3],
        's_quarter': [4, 5, 6],
        'about_me': 'i\'am Notorious and I\'am Ruthless too!',
        'now': datetime.datetime.now(),
        'previous_fight': '',
        'next_fight': None,
        'processors': processors,
        'message': '<h1>I\'am using escape</h1>',
        'website': 'http://example.com'
        }
    
    return render(request, 'djangobasicsapp/bif_demo.html', dict)

def TestStaticFiles(request):
    return render(request, 'djangobasicsapp/test_static_files.html')