from datetime import date
from xhtml2pdf import pisa

from django.http import HttpResponse
from django.template.loader import render_to_string
from django.shortcuts import render, redirect, get_object_or_404

from applications.core.functions import link_callback

from .models import Car, Manufacturer, Rental
from .forms import ManufacturerForm, CarForm,RentalForm


def console(request):
    cars = Car.objects.all()
    context={
        'cars':cars
    }

    return render(
        request,
        'cars/console.html',
        context
    )


def new_manufacturer(request):
    if request.method == 'POST':
        form = ManufacturerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('car-console')
    else:
        form = ManufacturerForm()
    
    return render(request, 'cars/new_brand.html', {'form': form})


def new_car(request):
    if request.method == 'POST':
        form = CarForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('car-console')
    else:
        form = CarForm()
    
    return render(request, 'cars/new_car.html', {'form': form})


def car_delete(request, pk):
    car = get_object_or_404(Car, pk=pk)

    if request.method == 'POST':
        car.delete()
        return redirect('car-console')


def car_detail(request, car_id):
    car = get_object_or_404(Car, id=car_id)

    if request.method == 'POST':
        form = CarForm(request.POST, instance=car)
        if form.is_valid():
            form.save()
            return redirect('car_detail', car_id=car.id)

    else:
        form = CarForm(instance=car)

    return render(request, 'cars/car_detail.html', {'car': car, 'form': form})


def brand_detail(request, brand_id):
    brand = get_object_or_404(Manufacturer, id=brand_id)

    if request.method == 'POST':
        form = ManufacturerForm(request.POST, instance=brand)
        if form.is_valid():
            form.save()
            return redirect('brand_detail', brand_id=brand.id)

    else:
        form = ManufacturerForm(instance=brand)

    return render(request, 'cars/brand_detail.html', {'brand': brand, 'form': form})


def brand_delete(request, pk):
    brand = get_object_or_404(Manufacturer, pk=pk)

    if request.method == 'POST':
        brand.delete()
        return redirect('car-console')
    

def rental_console(request):
    loged_user = request.user
    if loged_user.is_superuser:
        rentals = Rental.objects.all()
    else:
        rentals = Rental.objects.filter(user=loged_user)
    context={
        'rentals':rentals
    }

    return render(
        request,
        'cars/rentals.html',
        context
    )


def new_rental(request):
    if request.method == 'POST':
        form = RentalForm(request.POST)
        if form.is_valid():
            rental = form.save(commit=False) 
            rental.customer = request.user  
            rental.save()  
            return redirect('rental-console')
    else:
        form = RentalForm()
    
    return render(request, 'cars/new_rental.html', {'form': form})


def rental_detail(request, rental_id):
    rental = get_object_or_404(Rental, id=rental_id)
    date_today = date.today()
    if request.method == 'POST':
        rating = int(request.POST.get('rating'))
        rental.calification = rating
        if rental.end_date > date_today:
            rental.end_date = date_today   
        rental.save()
        return redirect('rental-console')


    return render(request, 'cars/rental_detail.html', {'rental': rental})


def cars_export_pdf(request):
    
    cars = Car.objects.all()
    
    context = {
        'title': 'CARS',
        'text_footer': 'Car list',
        'car_list': cars,
    }
    template_path = 'cars/pdf/cars_report.html'
    filename = f'pdf.pdf'

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="{filename}"'

    html = render_to_string(template_path, context)
    pisa.CreatePDF(html, dest=response, link_callback=link_callback)

    return response
