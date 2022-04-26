from django.shortcuts import render,get_object_or_404
from django.http import HttpResponseRedirect
from .models import Place 
from .forms import SearchForm,SearchCollaborativeForm
from django.db.models import Q
import recommendator,content_recommender

# Create your views here.
def index(request):
    return render(request, 'map/home.html',{
        'places': Place.objects.all()[:20]
    })

def recommend(request):
    return render(request, 'map/recommend.html',{
        'places': Place.objects.all()
    })

def detail(request, place_id):
    place = get_object_or_404(Place, id=place_id)
    context = {
        'place': place
    }
    return render(request, 'map/detail.html', context)

def search_recommend(request):
    places = Place.objects.all()
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            # query = recommendator.rec(request.POST['search'])
            query = content_recommender.get_content_based_recommendations(request.POST['search'])
            place = Place.objects.filter(name__in=query).distinct()
            return render(request, 'map/recommend.html',{
                'places': place
            })
    else:
        form = SearchForm()
    return render(request, 'map/search.html', {'form': form,'places':places})

def searchcollaborative_recommend(request):
    places = Place.objects.all()
    if request.method == 'POST':
        form = SearchCollaborativeForm(request.POST)
        if form.is_valid():
            query = recommendator.rec(request.POST['search'])
            # query = content_recommender.get_content_based_recommendations(request.POST['search'])
            place = Place.objects.filter(name__in=query).distinct()
            return render(request, 'map/recommend.html',{
                'places': place
            })
    else:
        form = SearchCollaborativeForm()
    return render(request, 'map/search-collaborative.html', {'form': form,'places':places})
        