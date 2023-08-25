import torch
from Data import DataProvider
from Models import song


def Recommend(path, mySongId, k=10):
    num_playlists, num_nodes = dataProvider.getDatasetStats(path)

    songs = dataProvider.getSongsData(path)
    # Load the .pt file containing the learned embeddings

    embeddings = dataProvider.getEmbeddibngs(path)
    songs_emb = embeddings[num_playlists:, :]

    # Get the embedding of the target playlist
    target_song_embedding = embeddings[mySongId]

    ratings = torch.sigmoid(torch.matmul(target_song_embedding, songs_emb.t()))

    # torch TopK
    _, torch_top_k = torch.topk(ratings.cpu(), k=k + 1, dim=0)
    torch_top_k += num_playlists

    torch_top_k = torch_top_k[0:k + 1]
    torch_top_k = torch_top_k.numpy()

    recommendedSongs = []
    i = 0
    for id in torch_top_k:
        if id != mySongId:
            i += 1
            track_name = songs[id]['track_name']
            artist_name = songs[id]['artist_name']
            spotify_uri = songs[id]['track_uri']
            addedSong = song.Model(artist_name, track_name, id.item(), spotify_uri)
            addedSong.UriReplace()
            recommendedSongs.append(addedSong)
        if i == 10:
            break

    return recommendedSongs
