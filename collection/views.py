from django.shortcuts import render
from collection.models import Concept

# Return All from DB
#def index(request):
    #concepts = Concept.objects.all().order_by('name')
    #return render(request, 'index.html', {
        #'concepts': concepts,
      #})

# Return Filtered Results from DB


def index(request):
    concepts = Concept.objects.all()
    return render(request, 'index.html', {
        'concepts': concepts,
    })



#def index(request):
#   concepts = Concept.objects.filter(area__contains='test').order_by('name')
#    return render(request, 'index.html', {
#        'concepts': concepts,
#    })


#def database(request):
#   concepts = Concept.objects.filter(area='test2').order_by('name')
#    return render(request, 'database.html', {
#        'concepts': concepts,
#    })
