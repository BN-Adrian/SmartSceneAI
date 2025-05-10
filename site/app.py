from flask import Flask, render_template, request,jsonify 
import requests
import os
from dotenv import load_dotenv 


load_dotenv()


app=Flask(__name__)

TMDB_APY_KEY=os.getenv("TMDB_API_KEY")
@app.route('/')
def index():
    return render_template("index.html")

@app.route('/search',methods=['POST'])
def search():
    description=request.form.get['description','']
    results=[]

    for media_type in ['movie','tv']:
        url="fhttps://api.themoviedb.org/3/search/{media_type}"
        response=requests.get(url,params={
            'api_key':TMDB_APY_KEY,
            'query':description,
            'language':'en-US'
        })
        data=response.json()
        if data.get('results'):
            match=data['results'][0]
            results.append({
                'title':match.get('title') or match.get('name'),
                'overview':match.get('overview','No description available.'),
                'type':'Movie'if media_type=='movie' else 'TV Show'
            })
    if results:
        return jsonify(results)
    else:
        return jsonify({'error':'no matching movie or show founds.'}),404
if __name__=='__main__':
    app.run(debug=True)