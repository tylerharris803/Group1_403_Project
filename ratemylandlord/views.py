from django.shortcuts import render
from django.http import HttpResponse

def indexPageView(request) :
    return render(request, 'ratemylandlord/index.html')

def viewReviewsPageView(request) :
    return HttpResponse('RateMyLandLord: Welcome to the view reviews page')

def editReviewsPageView(request) :
    return HttpResponse('RateMyLandLord: Welcome to the edit reviews page')
    
def contactPageView(request) :
    return HttpResponse('RateMyLandLord: Contact info goes here')