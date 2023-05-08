import torch
from Data import dataProvider
from Models import song
import songsService

def Recommend(path, mySongId=0, k=10):
    num_playlists, num_nodes = dataProvider.getDatasetStats(path)

    songs = dataProvider.getSongsData(path)

    # Load the .pt file containing the learned embeddings

    embeddings = dataProvider.getEmbeddibngs(path)

    if mySongId == 0:
        track_uri = 'spotify:track:0UaMYEvWZi0ZqiDOoHU3YI'
        for id in songs:
            if songs[id]['track_uri'] == track_uri:
                mySongId = id
                break

    # Get the embedding of the target playlist
    target_playlist_embedding = embeddings[mySongId]

    # torch TopK
    _, torch_top_k = torch.topk(target_playlist_embedding, k + 1)
    torch_top_k += num_playlists

    torch_top_k = torch_top_k[1:k + 1]
    torch_top_k = torch_top_k.numpy()

    recommendedSongs = []
    print(torch_top_k)

    for id in torch_top_k:
        track_name = songs[id]['track_name']
        artist_name = songs[id]['artist_name']
        recommendedSongs.append(song.Model(artist_name, track_name, id))
    print(recommendedSongs)
    return recommendedSongs
