Advanced Charts Save and Load Storage Example
================

This is a backend implementing a chart storage with Python and PostgreSQL.
You can run this storage on your server to process users' saved data such as [chart layouts], [drawing templates], and [indicator templates].
For more information, refer to the [Saving and loading charts] section of the Advanced Charts documentation.

## Requirements

Python 3x, pip, Django, PostgreSQL

## How to start

1. Clone the repository to your host machine.
2. Install Python 3.x and pip. Use a virtual environment if your host has an older Python version that cannot be upgraded.
3. Install PostgreSQL or any other Django-friendly database engine. You can also install pgAdmin or any other administrative tool for your database.
4. Go to your chart storage folder and install the required dependencies: `pip install -r requirements.txt`. For Unix users: you should have the python-dev package to install `psycopg2`.
5. Create an empty database in PostgreSQL using either the command line or pgAdmin.
6. Configure your database connection in `charting_library_charts/settings.py` (see `DATABASES` at [line 16]).
7. Run `python manage.py migrate` to create the database schema without any data.
8. Generate a secret key by running `python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'`.
9. Set your secret key to your environment variables `export SECRET_KEY='...'`.
10. Start a test instance of your database by running `python manage.py runserver`. Note that for production environments, you should avoid using `runserver` and instead use a suitable WSGI (Web Server Gateway Interface) server like Gunicorn.
11. Set [`charts_storage_url`] in the [Widget Constructor] to the URL of your chart storage. Additionally, ensure to set [`client_id` and `user_id`].

[chart layouts]: https://www.tradingview.com/charting-library-docs/latest/saving_loading/#chart-layouts
[`charts_storage_url`]: https://www.tradingview.com/charting-library-docs/latest/api/interfaces/Charting_Library.ChartingLibraryWidgetOptions/#charts_storage_url
[`client_id` and `user_id`]: https://www.tradingview.com/charting-library-docs/latest/saving_loading/save-load-rest-api/#manage-access-to-saved-charts
[drawing templates]: https://www.tradingview.com/charting-library-docs/latest/saving_loading/#drawing-templates
[indicator templates]: https://www.tradingview.com/charting-library-docs/latest/saving_loading/#indicator-templates
[line 16]: https://github.com/tradingview/saveload_backend/blob/master/charting_library_charts/settings.py#L16
[Saving and loading charts]: https://www.tradingview.com/charting-library-docs/latest/saving_loading/
[Widget Constructor]: https://www.tradingview.com/charting-library-docs/latest/core_concepts/Widget-Constructor/
