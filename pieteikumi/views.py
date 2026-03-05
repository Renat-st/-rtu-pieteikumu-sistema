from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from django.db.models import Q
from django.http import HttpResponseRedirect
from .models import Pieteikums

def pieteikumu_saraksts(request):
    q = request.GET.get('q', '').strip()
    status = request.GET.get('status', '').strip()

    qs = Pieteikums.objects.all()

    if q:
        qs = qs.filter(
            Q(nosaukums__icontains=q) |
            Q(apraksts__icontains=q)
        )

    if status:
        qs = qs.filter(statuss=status)

    qs = qs.order_by('-id')

    paginator = Paginator(qs, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'pieteikumi': page_obj,
        'page_obj': page_obj,
        'q': q,
        'status': status,
    }
    return render(request, 'pieteikumi/saraksts.html', context)

def jauns(request):
    if request.method == 'POST':
        Pieteikums.objects.create(
            nosaukums=request.POST['nosaukums'],
            apraksts=request.POST['apraksts'],
            statuss=request.POST['statuss']
        )
        return redirect('/')
    return render(request, 'pieteikumi/form.html', {'title': 'Jauns pieteikums'})

def rediget(request, id):
    pieteikums = get_object_or_404(Pieteikums, id=id)
    if request.method == 'POST':
        pieteikums.nosaukums = request.POST['nosaukums']
        pieteikums.apraksts = request.POST['apraksts']
        pieteikums.statuss = request.POST['statuss']
        pieteikums.save()
        return redirect('/')
    return render(request, 'pieteikumi/form.html', {
        'title': 'Rediģēt pieteikumu',
        'pieteikums': pieteikums
    })

def dzest(request, id):
    pieteikums = get_object_or_404(Pieteikums, id=id)
    if request.method == 'POST':
        pieteikums.delete()
        return redirect('/')
    return render(request, 'pieteikumi/dzest.html', {
        'pieteikums': pieteikums
    })
