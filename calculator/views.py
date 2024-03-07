from django.http import JsonResponse
from django.shortcuts import render


def calculate(request):
    if request.method == 'POST':
        num1_str = request.POST.get('num1')
        num2_str = request.POST.get('num2')
        operation = request.POST.get('operation')

        if num1_str is None or num2_str is None or operation is None:
            return JsonResponse({'error': 'Не всі необхідні дані надано'})

        try:
            num1 = float(num1_str)
            num2 = float(num2_str)
        except ValueError:
            return JsonResponse({'error': 'Некоректні дані для обчислення'})

        if operation == 'add':
            result = num1 + num2
        elif operation == 'subtract':
            result = num1 - num2
        elif operation == 'multiply':
            result = num1 * num2
        elif operation == 'divide':
            if num2 == 0:
                return JsonResponse({'error': 'Ділення на нуль неможливе'})
            result = num1 / num2
        elif operation == 'convert':
            result = (num1 * 9 / 5) + 32
        else:
            return JsonResponse({'error': 'Невідома операція'})

        return JsonResponse({'result': result})
    else:
        return render(request, 'assets/index.html')
