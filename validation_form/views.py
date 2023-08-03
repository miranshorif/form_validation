from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import PostForm
# Create your views here.
def home_view(request):
    if request.method == 'POST':
        details = PostForm(request.POST)
        if details.is_valid():
            post = details.save(commit=False)
            post.save()
            return HttpResponse('Data submited successfully')
        else:
            return render(request, 'validation_form/home.html', {'form':details})
    else:
        form = PostForm()
    return render(request, 'validation_form/home.html', {'form':form})