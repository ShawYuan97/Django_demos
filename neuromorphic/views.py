from django.shortcuts import render


# Create your views here.
def index_View(request):
    return render(request, 'neuromorphic/index.html', locals())


def neuronsimu_View(request):
    return render(request, 'neuromorphic/simulation.html', locals())
