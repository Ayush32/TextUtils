# I have created this file
from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'index.html')

def analyze(request):
    #get the text
    textwrap=request.POST.get('text','default')
    # check checkBox value
    removepunc=request.POST.get('removepunc','off')
    fullcaps=request.POST.get('fullcaps','off')
    newlineremover = request.POST.get('newlineremover', 'off')
    spaceremover = request.POST.get('spaceremover', 'off')
    charcount= request.POST.get('charcount', 'off')
    #analyzed=textwrap

    #check with checkbox is on
    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed=""
        for char in textwrap:
            if char not in punctuations:
                analyzed=analyzed+char
        parameter={'purpose':'Remove Punctuation','analyze_text':analyzed}
        # analyze the text
        textwrap=analyzed
        #return render(request,'analyze.html',parameter)

    if fullcaps == "on":
        analyzed = ""
        for char in textwrap:
                analyzed = analyzed+char.upper()
        parameter = {'purpose': 'Captalize', 'analyze_text': analyzed}
        # analyze the text
        textwrap=analyzed
        #return render(request, 'analyze.html', parameter)


    if (spaceremover == "on"):
        analyzed = ""
        for index,char in enumerate(textwrap):
            if textwrap[index]== "" and textwrap[index + 1]=="":
                pass
            else:
                analyzed = analyzed + char

        parameter = {'purpose': 'Space Remover', 'analyze_text': analyzed}
        # analyze the text
        textwrap=analyzed
        #return render(request, 'analyze.html', parameter)

    if(newlineremover=="on"):
        analyzed=""
        for char in textwrap:
            if char!="\n" and char!="\r":
                analyzed = analyzed + char


        parameter = {'purpose': 'Removed New Lines', 'analyze_text': analyzed}
        # analyze the text
        textwrap = analyzed

    return render(request, 'analyze.html', parameter)


