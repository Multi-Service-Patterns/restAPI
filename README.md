# restAPI
# API RESTful para Gerenciamento de Músicas

Esta API permite gerenciar usuários, playlists e músicas. Ela se integra com um banco de dados em tempo real no Firebase.

## Endpoints

### Usuários (Users)

- **GET /users**: Retorna todos os usuários cadastrados.
- **POST /users**: Adiciona um novo usuário.
- **GET /users/{user_id}**: Retorna os detalhes de um usuário específico.
- **PATCH /users/{user_id}**: Atualiza os dados de um usuário.
- **DELETE /users/{user_id}**: Remove um usuário.

### Playlists

- **GET /playlists**: Retorna todas as playlists.
- **POST /playlists**: Adiciona uma nova playlist.
- **GET /playlists/{playlist_id}**: Retorna os detalhes de uma playlist específica.
- **PATCH /playlists/{playlist_id}**: Atualiza os dados de uma playlist.
- **DELETE /playlists/{playlist_id}**: Remove uma playlist.

### Músicas (Songs)

- **GET /songs**: Retorna todas as músicas.
- **POST /songs**: Adiciona uma nova música.
- **GET /songs/{song_id}**: Retorna os detalhes de uma música específica.
- **PATCH /songs/{song_id}**: Atualiza os dados de uma música.
- **DELETE /songs/{song_id}**: Remove uma música.

## Configuração

1. Clone este repositório.
2. Instale as dependências (Flask e requests).
3. Configure a URL do seu banco de dados Firebase em `FIREBASE_DB_URL`.
4. Execute o aplicativo Flask com `python app.py`. 
