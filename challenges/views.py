from django.shortcuts import render
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string
# Create your views here.

monthly_challenges = {
    'january': 'January Challenge: Do 20 pushups!',
    'february': 'February Challenge: Run 5km!',
    'march': 'March Challenge: Read a book!',
    'april': 'April Challenge: Write a blog post!',
    'may': 'May Challenge: Learn a new programming language!',
    'june': 'June Challenge: Go for a hike!',
    'july': 'July Challenge: Drink 2 liters of water daily!',
    'august': 'August Challenge: Meditate for 10 minutes daily!',
    'september': 'September Challenge: Start a journal!',
    'october': 'October Challenge: Volunteer for a local charity!',
    'november': 'November Challenge: Cook a new recipe!',
    'december': None
}

def index(request):
    months = list(monthly_challenges.keys())
   
    return render(request, "challenges/index.html", {
        "months": months,
        #Passing the months list to the template
    })

def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())

    if month > len(months) or month < 1:
        return HttpResponse("Invalid month!")
    redirect_month = months[month - 1]
    redirect_path = reverse("month-challenge", args=[redirect_month])

    return HttpResponseRedirect(redirect_path)
    

def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return render(request, "challenges/challenge.html", {
            "text": challenge_text,
            "month_name": month
        })
    except KeyError:
        raise Http404()
    

