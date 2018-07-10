from django.shortcuts import render, redirect
from collection.forms import ConceptForm
from collection.models import Concept
from django.template.defaultfilters import slugify
# from django.contrib.auth.decorators import login_required
# from django.http import Http404

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

def concept_detail(request, slug):
    concept = Concept.objects.get(slug=slug)
    return render(request, 'concepts/concept_detail.html', { 
        'concept': concept,
    })

# @login_required
def edit_concept(request, slug):
    concept = Concept.objects.get(slug=slug)
    # if concept.user != request.user:
    #     raise Http404
    form_class = ConceptForm
    if request.method == 'POST':
        form = form_class(data=request.POST, instance=concept)
        if form.is_valid():
            form.save()
            return redirect('concept_detail', slug=concept.slug)

    else:
        form = form_class(instance=concept)
        return render(request, 'concepts/edit_concept.html', {
            'concept': concept,
            'form': form,
        })


def create_concept(request):
    if request.method == "POST":
        form = ConceptForm(request.POST)
        if form.is_valid():
            concept = form.save(commit=False)
            concept.slug = slugify(concept.name)
            concept.save()
            return redirect('concept_detail', slug=concept.slug)
    else:
        form = ConceptForm()
    return render(request, 'concepts/create_concept.html', {
        'form': form
    })

def browse_by_name(request, initial=None):
    if initial:
        concepts = Concept.objects.filter(
            name__istartswith=initial).order_by('name')
    else:
        concepts = Concept.objects.all().order_by('name')

    return render(request, 'search/search.html', {
        'concepts': concepts,
        'initial': initial,
    })



