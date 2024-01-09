from django.shortcuts import render
import pickle
import numpy as np
# Create your views here.


def index(request):
    return render(request, 'index.html')

def prediction(request):
    return render(request, 'predictionForm.html')

def getPrediction(N, P, k, temperature, humidity, ph, rainfall):
    model = pickle.load(open('model.pkl', 'rb'))
    ms = pickle.load(open('minmaxscaler.pkl', 'rb'))
    sc = pickle.load(open('standscaler.pkl', 'rb'))

    input_data = np.array([[N, P, k, temperature, humidity, ph, rainfall]])
    scaled_data_minmax = ms.transform(input_data)
    scaled_data_standard = sc.transform(scaled_data_minmax)

    prediction = model.predict(scaled_data_standard)

    if prediction == 1:
        return 'rice'
    elif prediction == 2:
        return 'maize'
    elif prediction == 3:
        return 'jute'
    elif prediction == 4:
        return 'cotton'
    elif prediction == 5:
        return 'coconut'
    elif prediction == 6:
        return 'papaya'
    elif prediction == 7:
        return 'orange'
    elif prediction == 8:
        return 'apple'
    elif prediction == 9:
        return 'muskmelon'
    elif prediction == 10:
        return 'watermelon'
    elif prediction == 11:
        return 'grapes'
    elif prediction == 12:
        return 'mango'
    elif prediction == 13:
        return 'banana'
    elif prediction == 14:
        return 'pomegranate'
    elif prediction == 15:
        return 'lentil'
    elif prediction == 16:
        return 'blackgram'
    elif prediction == 17:
        return 'mungbean'
    elif prediction == 18:
        return 'mothbeans'
    elif prediction == 19:
        return 'pigeonpeas'
    elif prediction == 20:
        return 'kidneybeans'
    elif prediction == 21:
        return 'chickpea'
    elif prediction == 22:
        return 'coffee'
    else:
        return 'error'


def result(request):
    N = request.GET['N']
    P = request.GET['P']
    k = request.GET['k']
    temperature = request.GET['temperature']
    humidity = request.GET['humidity']
    ph = request.GET['ph']
    rainfall = request.GET['rainfall']

    result = getPrediction(N, P, k, temperature, humidity, ph, rainfall)

    return render(request, 'result.html', {'result': result})