from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import logging
import os
import datetime

# Assuming you have a model named 'Log' in your logger.models module
from logger.models import Log

logger = logging.getLogger(__name__)

# Configure log file path and name
log_folder = os.path.join(os.path.dirname(__file__), 'logs')
os.makedirs(log_folder, exist_ok=True)

log_file = datetime.date.today().strftime('%Y-%m-%d') + '.log'
log_path = os.path.join(log_folder, log_file)

@csrf_exempt  # This decorator exempts the view from CSRF protection
def calculate(request, operation, num1, num2):
    try:
        num1 = int(num1)
        num2 = int(num2)
    except ValueError:
        return JsonResponse({'error': 'Invalid input. Please provide integers for num1 and num2.'}, status=400)

    if operation == 'addition':
        result = num1 + num2
        log_message = f"Performed addition: {num1} + {num2} = {result}"
    elif operation == 'subtraction':
        result = num1 - num2
        log_message = f"Performed subtraction: {num1} - {num2} = {result}"
    elif operation == 'multiplication':
        result = num1 * num2
        log_message = f"Performed multiplication: {num1} * {num2} = {result}"
    elif operation == 'division':
        if num2 == 0:
            return JsonResponse({'error': 'Division by zero not allowed'}, status=400)
        result = num1 / num2
        log_message = f"Performed division: {num1} / {num2} = {result}"
    else:
        return JsonResponse({'error': 'Invalid operation'}, status=400)
        
    log_entry = Log(route=request.path, operation=operation, num1=num1, num2=num2, result=result)
    log_entry.save()  

    logger.info(log_message)

    return JsonResponse({'result': result})
