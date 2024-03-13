from django.http import JsonResponse
from django.shortcuts import render


def calculate(request):
    if request.method == 'POST':
        num1_str = request.POST.get('num1')
        num2_str = request.POST.get('num2')
        operation = request.POST.get('operation')

        if num1_str is None or num2_str is None or operation is None:
            return JsonResponse({'error': 'Not all required data is provided'})

        try:
            num1 = float(num1_str)
            num2 = float(num2_str)
        except ValueError:
            return JsonResponse({'error': 'Incorrect data for calculation'})

        if operation == 'add':
            result = '{:.3f}'.format(num1 + num2)
        elif operation == 'subtract':
            result = '{:.3f}'.format(num1 - num2)
        elif operation == 'multiply':
            result = '{:.3f}'.format(num1 * num2)
        elif operation == 'divide':
            if num2 == 0:
                return JsonResponse({'error': 'Division by zero is impossible'})
            result = '{:.3f}'.format(num1 / num2)
        elif operation == 'convert':
            if -273 <= num1 <= 273:
                result = '{:.3f}'.format((num1 * 9 / 5) + 32)
            else:
                return JsonResponse({'error': 'out of range'})
        else:
            return JsonResponse({'error': 'Unknown operation'})

        return render(request, 'assets/index.html', {'result': result})
    else:
        return render(request, 'assets/index.html')
