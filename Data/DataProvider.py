import json
import os

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
    path += 'embeddings/'
    files = os.listdir(path)
    path = os.path.join(path, files[0])
    return torch.load(path, map_location=torch.device('cpu'))