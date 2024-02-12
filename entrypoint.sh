python manage.py migrate
# python manage.py runserver
python -m uvicorn charting_library_charts.asgi:application --host "0.0.0.0" --port 8001