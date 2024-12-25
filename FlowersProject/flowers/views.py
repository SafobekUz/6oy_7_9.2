from django.shortcuts import render, redirect
from .forms import TurForm, GulForm

def create_tur(request):
    if request.method == 'POST':
        form = TurForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tur_list')
    else:
        form = TurForm()
    return render(request, 'create_tur.html', {'form': form})

def create_gul(request):
    if request.method == 'POST':
        form = GulForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('gul_list')
    else:
        form = GulForm()
    return render(request, 'create_gul.html', {'form': form})
