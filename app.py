import os
from dotenv import load_dotenv
from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

load_dotenv()
db_url = os.getenv('DATABASE_URL')

FIREBASE_DB_URL = db_url

@app.route('/users', methods=['GET', 'POST'])
def users():
    if request.method == 'GET':
        response = requests.get(f'{FIREBASE_DB_URL}/users.json')
        return jsonify(response.json()), response.status_code
    
    if request.method == 'POST':
        data = request.json
        response = requests.post(f'{FIREBASE_DB_URL}/users.json', json=data)
        return jsonify(response.json()), response.status_code

@app.route('/users/<user_id>', methods=['GET', 'PATCH', 'DELETE'])
def user_detail(user_id):
    if request.method == 'GET':
        response = requests.get(f'{FIREBASE_DB_URL}/users/{user_id}.json')
        return jsonify(response.json()), response.status_code
    
    if request.method == 'PATCH':
        data = request.json
        response = requests.patch(f'{FIREBASE_DB_URL}/users/{user_id}.json', json=data)
        return jsonify(response.json()), response.status_code
    
    if request.method == 'DELETE':
        response = requests.delete(f'{FIREBASE_DB_URL}/users/{user_id}.json')
        return jsonify(response.json()), response.status_code

@app.route('/playlists', methods=['GET', 'POST'])
def playlists():
    if request.method == 'GET':
        response = requests.get(f'{FIREBASE_DB_URL}/playlists.json')
        return jsonify(response.json()), response.status_code
    
    if request.method == 'POST':
        data = request.json
        response = requests.post(f'{FIREBASE_DB_URL}/playlists.json', json=data)
        return jsonify(response.json()), response.status_code

@app.route('/playlists/<playlist_id>', methods=['GET', 'PATCH', 'DELETE'])
def playlist_detail(playlist_id):
    if request.method == 'GET':
        response = requests.get(f'{FIREBASE_DB_URL}/playlists/{playlist_id}.json')
        return jsonify(response.json()), response.status_code
    
    if request.method == 'PATCH':
        data = request.json
        response = requests.patch(f'{FIREBASE_DB_URL}/playlists/{playlist_id}.json', json=data)
        return jsonify(response.json()), response.status_code
    
    if request.method == 'DELETE':
        response = requests.delete(f'{FIREBASE_DB_URL}/playlists/{playlist_id}.json')
        return jsonify(response.json()), response.status_code

@app.route('/songs', methods=['GET', 'POST'])
def songs():
    if request.method == 'GET':
        response = requests.get(f'{FIREBASE_DB_URL}/songs.json')
        return jsonify(response.json()), response.status_code
    
    if request.method == 'POST':
        data = request.json
        response = requests.post(f'{FIREBASE_DB_URL}/songs.json', json=data)
        return jsonify(response.json()), response.status_code

@app.route('/songs/<song_id>', methods=['GET', 'PATCH', 'DELETE'])
def song_detail(song_id):
    if request.method == 'GET':
        response = requests.get(f'{FIREBASE_DB_URL}/songs/{song_id}.json')
        return jsonify(response.json()), response.status_code
    
    if request.method == 'PATCH':
        data = request.json
        response = requests.patch(f'{FIREBASE_DB_URL}/songs/{song_id}.json', json=data)
        return jsonify(response.json()), response.status_code
    
    if request.method == 'DELETE':
        response = requests.delete(f'{FIREBASE_DB_URL}/songs/{song_id}.json')
        return jsonify(response.json()), response.status_code

if __name__ == '__main__':
    app.run(debug=True)
