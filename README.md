Advanced Charts Save and Load Storage Example
================

This is a backend implementing a chart storage with Python and PostgreSQL.
You can run this storage on your server to process users' saved data such as [chart layouts], [drawing templates], and [indicator templates].
For more information, refer to the [Saving and loading charts] section of the Advanced Charts documentation.

## Security notice

This backend is a **reference implementation** and has **no authentication or authorization**.
Data is scoped only by the `client` and `user` query parameters, which are supplied by the caller.
Anyone who knows or guesses a `client`/`user` pair can read, overwrite, or delete that data.

Before using it in production, you must:

- Put it behind your own authentication (for example, a reverse proxy that validates a session or token) and derive or verify `user` server-side instead of trusting the query parameter.
- Restrict `Access-Control-Allow-Origin` to your own domains (it is `*` by default, see `api/v11/common.py`).
- Set `SECRET_KEY` and `ALLOWED_HOSTS`, and serve the storage over HTTPS with a production WSGI server.
- Avoid exposing the Prometheus `/metrics` endpoint publicly.

**Demo server:** `https://saveload.tradingview.com`, used in our examples, is a public demo for testing only.
Anything saved there can be read, modified, or deleted by anyone, and may be wiped at any time.
Do not use it in production.

## Requirements

Python 3.10 or later, pip, Django, PostgreSQL

## How to start

1. Clone the repository to your host machine.
2. Install Python 3.10 or later and pip. Use a virtual environment if your host has an older Python version that cannot be upgraded.
3. Install PostgreSQL or any other Django-friendly database engine. You can also install pgAdmin or any other administrative tool for your database.
4. Go to your chart storage folder and install the required dependencies: `pip install -r requirements.txt`. The `psycopg[binary]` PostgreSQL driver ships prebuilt, so no compiler is needed. For production, consider `psycopg[c]` instead, which uses your system's `libpq` and its security updates (see the [psycopg installation guide]).
5. Create an empty database in PostgreSQL using either the command line or pgAdmin.
6. Configure your database connection in `charting_library_charts/settings.py` (see `DATABASES` at [line 16]).
7. Generate a secret key by running `python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'`.
8. Set your secret key to your environment variables `export SECRET_KEY='...'`. This is required: the storage does not start without it.
9. Run `python manage.py migrate` to create the database schema without any data.
10. Start a test instance of your database by running `python manage.py runserver`. Note that for production environments, you should avoid using `runserver` and instead use a suitable WSGI (Web Server Gateway Interface) server like Gunicorn.
11. Set [`charts_storage_url`] in the [Widget Constructor] to the URL of your chart storage. Additionally, ensure to set [`client_id` and `user_id`]. Note that these values only partition data; they do not secure it (see [Security notice](#security-notice)).

[chart layouts]: https://www.tradingview.com/charting-library-docs/latest/saving_loading/#chart-layouts
[`charts_storage_url`]: https://www.tradingview.com/charting-library-docs/latest/api/interfaces/Charting_Library.ChartingLibraryWidgetOptions/#charts_storage_url
[`client_id` and `user_id`]: https://www.tradingview.com/charting-library-docs/latest/saving_loading/save-load-rest-api/#manage-access-to-saved-charts
[drawing templates]: https://www.tradingview.com/charting-library-docs/latest/saving_loading/#drawing-templates
[indicator templates]: https://www.tradingview.com/charting-library-docs/latest/saving_loading/#indicator-templates
[line 16]: https://github.com/tradingview/saveload_backend/blob/master/charting_library_charts/settings.py#L16
[psycopg installation guide]: https://www.psycopg.org/psycopg3/docs/basic/install.html
[Saving and loading charts]: https://www.tradingview.com/charting-library-docs/latest/saving_loading/
[Widget Constructor]: https://www.tradingview.com/charting-library-docs/latest/core_concepts/Widget-Constructor/
