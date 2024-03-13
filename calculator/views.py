from django.shortcuts import render
from calculator.myapp.module import calculate


def calculate_index(request):
    if request.method == 'POST':
        num1_str = request.POST.get('num1')
        num2_str = request.POST.get('num2')
        operation = request.POST.get('operation')

        if num1_str is None or num2_str is None or operation is None:
            return render(request, 'assets/index.html', {'error': 'Not all required data is provided'})

        result = calculate(num1_str, num2_str, operation)

        return render(request, 'assets/index.html', {'result': result})
    else:
        return render(request, 'assets/index.html')
