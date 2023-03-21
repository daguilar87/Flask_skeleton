from app import app

from flask import render_template

@app.route('/')
def homePage():
 
    
    
    return render_template('index.html')

@app.route('/Fave5')
def fave5Page():
       fav_artist=[
        {
        'artist': 'Fuerza Regida'},
        {'artist': 'Linkin Park'},
        {'artist': 'Edgardo Nunez'},
        {'artist': 'Conejo'},
        {'artist': 'Junior H'}
    ]
    
       return render_template('fave_5.html', artist=fav_artist)