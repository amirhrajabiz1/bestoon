from json import JSONEncoder
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from web.models import Token, Expense, Income
import datetime


@csrf_exempt
def submit_expense(request):
    """user submit an expense"""

    # TODO:  validate data. user might be fake. token might be fake. amount might be fake.
    this_token = request.POST["token"]
    this_user = User.objects.filter(token__token=this_token).get()
    if 'date' not in request.POST:
        date = datetime.datetime.now()

    Expense.objects.create(
        user=this_user,
        amount=request.POST["amount"],
        text=request.POST["text"],
        date=date,
    )

    return JsonResponse(
        {
            "status": "ok",
        },
        encoder=JSONEncoder,
    )


@csrf_exempt
def submit_income(request):
    """user submit an income"""

    # TODO:  validate data. user might be fake. token might be fake. amount might be fake.
    this_token = request.POST["token"]
    this_user = User.objects.filter(token__token=this_token).get()
    if 'date' not in request.POST:
        date = datetime.datetime.now()

    Income.objects.create(
        user=this_user,
        amount=request.POST["amount"],
        text=request.POST["text"],
        date=date,
    )

    return JsonResponse(
        {
            "status": "ok",
        },
        encoder=JSONEncoder,
    )
