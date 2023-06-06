from django.shortcuts import render
from django.http import JsonResponse
import logging
import os
import datetime

logger = logging.getLogger(__name__)

# Configure log file path and name
log_folder = os.path.join(os.path.dirname(__file__), 'logs')
os.makedirs(log_folder, exist_ok=True)

log_file = datetime.date.today().strftime('%Y-%m-%d') + '.log'
log_path = os.path.join(log_folder, log_file)

# Create your views here.
def calculate(request, operation, num1, num2):
    if operation == 'addition':
        result = int(num1) + int(num2)
        logger.info(f"Performed addition: {num1} + {num2} = {result}")
    elif operation == 'subtraction':
        result = int(num1) - int(num2)
        logger.info(f"Performed subtraction: {num1} - {num2} = {result}")
    elif operation == 'multiplication':
        result = int(num1) * int(num2)
        logger.info(f"Performed multiplication: {num1} * {num2} = {result}")
    elif operation == 'division':
        try:
            result = int(num1) / int(num2)
            logger.info(f"Performed division: {num1} / {num2} = {result}")
        except ZeroDivisionError:
            return JsonResponse({'error': 'Division by zero not allowed'})
    else:
        return JsonResponse({'error': 'Invalid operation'})

    return JsonResponse({'result': result})
	
	
