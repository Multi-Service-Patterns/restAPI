import os
from flask import Flask, request, jsonify

app = Flask(__name__)

# Stores data in memory
data_store = {
    "users": {},
    "playlists": {},
    "songs": {}
}

@app.route('/users', methods=['GET', 'POST'])
def users():
    if request.method == 'GET':
        return jsonify(data_store['users']), 200
    
    if request.method == 'POST':
        user_id = str(len(data_store['users']) + 1)
        data_store['users'][user_id] = request.json
        return jsonify(data_store['users'][user_id]), 201

@app.route('/users/<user_id>', methods=['GET', 'PATCH', 'DELETE'])
def user_detail(user_id):
    if request.method == 'GET':
        return jsonify(data_store['users'].get(user_id, {})), 200 if user_id in data_store['users'] else 404
    
    if request.method == 'PATCH':
        if user_id in data_store['users']:
            data_store['users'][user_id].update(request.json)
            return jsonify(data_store['users'][user_id]), 200
        return jsonify({'error': 'User not found'}), 404

    if request.method == 'DELETE':
        if user_id in data_store['users']:
            del data_store['users'][user_id]
            return jsonify({'success': 'User deleted'}), 200
        return jsonify({'error': 'User not found'}), 404

@app.route('/playlists', methods=['GET', 'POST'])
def playlists():
    if request.method == 'GET':
        return jsonify(data_store['playlists']), 200
    
    if request.method == 'POST':
        playlist_id = str(len(data_store['playlists']) + 1)
        data_store['playlists'][playlist_id] = request.json
        return jsonify(data_store['playlists'][playlist_id]), 201

@app.route('/playlists/<playlist_id>', methods=['GET', 'PATCH', 'DELETE'])
def playlist_detail(playlist_id):
    if request.method == 'GET':
        return jsonify(data_store['playlists'].get(playlist_id, {})), 200 if playlist_id in data_store['playlists'] else 404

    if request.method == 'PATCH':
        if playlist_id in data_store['playlists']:
            data_store['playlists'][playlist_id].update(request.json)
            return jsonify(data_store['playlists'][playlist_id]), 200
        return jsonify({'error': 'Playlist not found'}), 404

    if request.method == 'DELETE':
        if playlist_id in data_store['playlists']:
            del data_store['playlists'][playlist_id]
            return jsonify({'success': 'Playlist deleted'}), 200
        return jsonify({'error': 'Playlist not found'}), 404

@app.route('/songs', methods=['GET', 'POST'])
def songs():
    if request.method == 'GET':
        return jsonify(data_store['songs']), 200
    
    if request.method == 'POST':
        song_id = str(len(data_store['songs']) + 1)
        data_store['songs'][song_id] = request.json
        return jsonify(data_store['songs'][song_id]), 201

@app.route('/songs/<song_id>', methods=['GET', 'PATCH', 'DELETE'])
def song_detail(song_id):
    if request.method == 'GET':
        return jsonify(data_store['songs'].get(song_id, {})), 200 if song_id in data_store['songs'] else 404

    if request.method == 'PATCH':
        if song_id in data_store['songs']:
            data_store['songs'][song_id].update(request.json)
            return jsonify(data_store['songs'][song_id]), 200
        return jsonify({'error': 'Song not found'}), 404

    if request.method == 'DELETE':
        if song_id in data_store['songs']:
            del data_store['songs'][song_id]
            return jsonify({'success': 'Song deleted'}), 200
        return jsonify({'error': 'Song not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)
