from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string

# Create your views here.

# def january(request):
#     return HttpResponse("Get up early morning everyday !")

# def february(request):
#     return HttpResponse("Exercise for atleast 30 minutes daily !")

monthly_challenges = {
    "january" : "Get up early morning everyday !",
    "february" : "Exercise for atleast 30 minutes daily !",
    "march" : "read book daily!",
    "april" : "Get up early morning everyday !",
    "may" : "Exercise for atleast 30 minutes daily !",
    "june" : "read book daily!",
    "july" : "Get up early morning everyday !",
    "august" : "Exercise for atleast 30 minutes daily !",
    "september" : "read book daily!",
    "october" : "Get up early morning everyday !",
    "november" : "Exercise for atleast 30 minutes daily !",
    "december" : None,
}

def index(request):
    months = list(monthly_challenges.keys())
    return render(request, "challenges/index.html", { "months" : months })

def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())
    if month > len(months):
        return HttpResponseNotFound("This month is not supported!")
    redirect_month = months[month - 1]
    redirect_path = reverse("month-challenge", args=[redirect_month])
    return HttpResponseRedirect(redirect_path)

def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        # challenge_data = render_to_string("challenges/challenge.html")
        return render(request, "challenges/challenge.html", {
             "month" : month,
             "challenge" : challenge_text
             })
    except:
        return HttpResponseNotFound("<h1>This month is not supported!</h1>")
