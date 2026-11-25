from django.shortcuts import render

# Create your views here.
import random
def menu(request):
    foods = ['국밥', '국수', '카레', '탕수육']

    picked = random.choice(foods)

    context = {
        'picked': picked,
        'foods': foods,
    }

    return render(request, 'dinners/index.html', context)
