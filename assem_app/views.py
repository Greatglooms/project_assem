# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render

from .forms import RadioForm

# tetstt
def index(request):
    return HttpResponse("Hello, world! You're at the polls index.")
def calculate(request):
    result = ""
    price = 0
    weight = 0
    if request.method == 'POST':
        price = float(request.POST.get('price', 0))
        weight = float(request.POST.get('weight', 0))
        result = round(price * weight, 2)
    return render(request, 'training_app/calculate.html', {'result': result, 'price': price, 'weight': weight})
def clear(request):
    result = ""
    price = ""
    weight = ""
    return render(request, 'training_app/calculate.html',
                  {'price': price, 'weight': weight, 'result': result})
def run(request):
    volume = ""
    a = 0
    b = 0
    c = 0
    if request.method == 'POST':
        a = float(request.POST.get('length', 0))
        b = float(request.POST.get('width', 0))
        c = float(request.POST.get('height', 0))
        volume = round(a * b * c, 2)
    return render(request, 'training_app/dom.html',
                  {'volume': volume, 'length': a, 'width': b, 'height': c})
WORD_RADIO_MAPPING = {
    'Русское радио': 'Радиоволна 101.7',
    'Казахское радио': 'Радиоволна 102.7',
    'Радио FM': 'Радиоволна 103.7',
    'Той-думан': 'Радиоволна 104.7',
    'Ретро радио': 'Радиоволна 105.7',
    'Europa +': 'Радиоволна 106.7',
}
def radiobutton(request):
    radio = None

    if request.method == 'POST':
        form = RadioForm(request.POST)
        if form.is_valid():
            word_choice = form.cleaned_data['word_choice']
            radio = WORD_RADIO_MAPPING.get(word_choice)
    else:
        form = RadioForm()
    return render(request, 'training_app/radiobutton.html',
                  {'result': radio, 'form': form})
# WORD_RAINBOW_MAPPING ={
#      'Каждый': 'red',
#      'Охотник': 'orange',
#      'Желает': 'yellow',
#      'Знать': 'green',
#      'Где': 'cyan',
#      'Сидит': 'blue',
#      'Фазан': 'violet',
#  }
#
# def raduga(request):
#      color = None
#
#      if request.method == 'POST':
#          form = Rainbow(request.POST)
#          if form.is_valid():
#              word_choice = form.cleaned_data['word_choice']
#              color = WORD_RAINBOW_MAPPING.get(word_choice)
#      else:
#          form = Rainbow()
#      return render(request, 'trainingApp/raduga.html',
#                    {'result':radio,'form': form})
def combobox(request):
    Color = None
    if (request.method == 'POST'):
        Color = request.POST['raduga']
    return render(request, 'training_app/select.html',
                  {'color': Color})
def choose_computer_model(request):
    image_path = None  # Инициализируем image_path значением None
    if request.method == 'POST':
        selected_model = request.POST.get('models')
        if selected_model == 'hp':
            image_path = 'C://Users//Аскар//Desktop//hp.PNG'
        elif selected_model == 'acer':
            image_path = 'C://Users//Аскар//Desktop//acer.PNG'
        elif selected_model == 'apple':
            image_path = 'C://Users//Аскар//Desktop//apple.PNG'
        elif selected_model == 'dell':
            image_path = 'C://Users//Аскар//Desktop//dell.PNG'
    return render(request, 'kaspi_computer.html',
                  {'image_path': image_path})
def raduga(request, Color="white"):
    return render(request, 'training_app/rainbow.html', {"color": Color})
def radio_select(request, Result="rus"):
    return render(request, 'training_app/radioselect.html', {"result": Result})
def sum_numbers(request):
    total_sum = None
    if request.method == 'POST':
        selected_numbers = request.POST.getlist('selected_numbers')
        total_sum = sum([int(number) for number in selected_numbers])
    return render(request, 'training_app/checkbox.html', {'total_sum': total_sum})
def select(request, Result="rus"):
    return render(request, 'training_app/select.html', {"result": Result})


# noinspection PyRedeclaration
def index(request):
    return render(request, 'training_app/index.html')
def select(request, Result="rus"):
    return render(request, 'training_app/selectcombobox.html', {"result": Result})
def handle_dates(request):
    dates = []
    spring_dates = []
    if request.method == 'POST' and 'read_file' in request.POST:
        with open("E:/training/dates.txt", 'r') as file:
            dates = file.readlines()
    elif request.method == 'POST' and 'show_spring_dates' in request.POST:
        with open("E:/training/dates.txt", 'r') as file:
            lines = file.readlines()
            for line in lines:
                date_parts = line.strip().split('.')
                day = int(date_parts[0])
                month = int(date_parts[1])
                year = int(date_parts[2])
                if 3 <= month <= 5:
                    spring_dates.append(f"{day:02d}.{month:02d}.{year:04d}")
    context = {
        'dates': dates,
        'spring_dates': spring_dates,
    }
    return render(request, 'training_app/fail.html', context)