#!/bin/bash
git pull
source venv/bin/activate
pip install -r requirements.txt
python src/manage.py migrate
sudo supervisorctl reread
sudo supervisorctl update
sudo supervisorctl restart all
