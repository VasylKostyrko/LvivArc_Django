import os
from django.shortcuts import render, get_object_or_404
import json


# Отримуємо абсолютний шлях до файлу lvivarc.json
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
json_file_path = os.path.join(BASE_DIR, 'lvivarc.json')

# Завантаження бази з файлу lvivarc.json
with open(json_file_path, encoding='utf-8') as f:  # Додано кодування 'utf-8'
    data = json.load(f)

def main_view(request):
    # Фільтруємо за "arctype"
    types = [item for item in data if item["table"] == "arctype"]
    types.sort(key=lambda x: x['tipe_id'])
    return render(request, 'index.html', {'types': types})

def arc_object(request, id):
    obj = next((item for item in data if item["table"] == "arcobj" and item["id"] == id), None)
    if obj:
        return render(request, 'object.html', {'object': obj})
    else:
        return render(request, '404_error.html')

def list_objects(request, id):
    objects = [item for item in data if item["table"] == "arcobj" and item["tipe_id"] == id]
    type_info = next((item for item in data if item["table"] == "arctype" and item["tipe_id"] == id), None)
    return render(request, 'objects.html', {'type': type_info, 'objects': objects})

def error404(request):
    return render(request, '404_error.html')
