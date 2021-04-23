# tedify
Like Spotify but you pay Ted for a more limited music selection

## Setup
pip install -r requirements.txt
python manage.py seed music --number=20
python manage.py shell
    from music.util.random_genres import random_data
    random_data()