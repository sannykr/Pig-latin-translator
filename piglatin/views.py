from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def translate(request):
    original = request.GET['originaltext'].lower()
    translation = ''
    for word in original.split():
        if word[0] in ['a', 'e', 'i', 'o', 'u']:
            translation += word
            translation += 'yay '
        else:
            translation += word[1:] + word[0] + 'ay '

    return render(request, 'translate.html', {'original':original, 'translation':translation})			

def challenge(request):
	return render(request, 'challenge.html')