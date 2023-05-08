import json
import torch


def getSongsData(path):
    path += "song_info.json"
    with open(path, 'r') as f:
        songs = json.load(f)
    songs = {int(k): v for k, v in songs.items()}
    return songs
def getDatasetStats(path):
    path += "dataset_stats.json"
    with open(path, 'r') as f:
        stats = json.load(f)
    return stats["num_playlists"], stats["num_nodes"]
def getEmbeddibngs(path):
    path += 'embeddings/embeddings_epoch_20.pt'
    return torch.load(path, map_location=torch.device('cpu'))