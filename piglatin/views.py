from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, 'home.html')

def translate(request):
    original = request.GET['originalText'].lower()

    translation = ''

    for word in original.split():
        if word[0] in ['a', 'e', 'o', 'u', 'i']:
            #vowel
            translation += word
            #yay
            translation += 'yay '
        else:
            #consonant
            #get the rest of the word
            translation += word[1:]

            #append the first letter to the end of the translated word
            translation += word[0]

            #ay
            translation += 'ay '

    return render(request, 'translate.html', {'original':original, 'translation':translation})

def about(request):
    return render(request, 'about.html')
