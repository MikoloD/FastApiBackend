import json
import torch
import songsData

def Recommend(track_uri = 'spotify:track:0UaMYEvWZi0ZqiDOoHU3YI',k=10):
    with open("dataset_stats.json", 'r') as f:
        stats = json.load(f)
    num_playlists, num_nodes = stats["num_playlists"], stats["num_nodes"]

    songs = songsData.getSongsData()

# Load the .pt file containing the learned embeddings

    embeddings = torch.load('embeddings/embeddings_epoch_20.pt', map_location=torch.device('cpu'))

    for id in songs:
        if songs[id]['track_uri'] == track_uri:
            mySongId = id
            break

    # Get the embedding of the target playlist
    target_playlist_embedding = embeddings[mySongId]

    # torch TopK
    _, torch_top_k = torch.topk(target_playlist_embedding, k+1)
    torch_top_k += num_playlists

    torch_top_k = torch_top_k[1:k+1]
    torch_top_k = torch_top_k.numpy()

    recommendedSongs = []

    for i in torch_top_k:
        track_name = songs[i]['track_name']
        artist_name = songs[i]['artist_name']
        recommendedSongs.append(songsData.Song(artist_name,track_name))
    return recommendedSongs