from django.shortcuts import render, redirect, get_object_or_404
from .models import Car
from .forms import ManufacturerForm, CarForm

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