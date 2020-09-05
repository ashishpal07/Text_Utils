from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index2.html')

def analyze(request):
    djtext = request.POST.get('text', 'default')

    #check checkbox value
    punc = request.POST.get('analyzer', 'off')
    analyze = request.POST.get('fullcaps', 'off')
    RemoveNewLine = request.POST.get('Remove New Line', 'off')
    spaceremover = request.POST.get('Removeextraspace', 'off')

    #check which checkbox is on
    if(punc == "on"):
        analyze = ""
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        for char in djtext:
            if char not in punctuations:
                analyze = analyze + char
        params = {"purpose":"removepunc", "analyzed_text":analyze}
        djtext = analyze

    if(RemoveNewLine =="on"):
        ana = ""
        for char in djtext:
            if char != "\n" and char != "\r":
                ana = ana + char
        params = {"purpose":"Remove new line", "analyzed_text":ana}
        djtext = ana

    if (analyze == "on"):
        ana = ""
        for char in djtext:
            ana = ana + char.upper()
        params = {"purpose": "Capitalize Everything", "analyzed_text": ana}
        djtext = ana

    if(spaceremover == "on"):
        ana = ""
        for index,char in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index+1] == " "):
                ana = ana + char
        params = {"purpose":"Remove Extra Space", "analyzed_text":ana}
        djtext = ana

    if (punc != "on" and analyze != "on" and RemoveNewLine != "on" and spaceremover != "on"):
        return HttpResponse("Error")

    return render(request, 'analyzed.html', params)
