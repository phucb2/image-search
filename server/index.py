import pickle

from fastapi import FastAPI, File, UploadFile
from model import Image2Vector
import os
import shutil
from sklearn.neighbors import NearestNeighbors
import numpy as np
app = FastAPI()

model = Image2Vector()

from dataclasses import dataclass

class SimilarImageEngine:
    def __init__(self):
        file = '/Users/phucbb/PycharmProjects/image-search/notebooks/vectorDict.pickle'
        with open(file, 'rb') as file:
            data = pickle.load(file)
        # print(data)
        self.filenames = [i for i, _ in data.items()]
        self.features = np.array([j for _, j in data.items()])
        print(len(self.filenames))
        print(len(self.features))
        # print(self.features)
        self.nbrs = NearestNeighbors(n_neighbors=2, algorithm='ball_tree').fit(self.features)

    def find_nearest_neighbors(self, input):

        dist, indicates = self.nbrs.kneighbors(input, n_neighbors=8)
        result_size = len(indicates)
        print(indicates.shape)
        result_filename = []
        result_items = []
        for i in range(result_size):
            index = int(indicates[0][i])
            filename = self.filenames[index]
            result_filename.append(filename)
            result_items.append({"file_name": filename, "dist": dist[0][i]})
        return result_items


nn = SimilarImageEngine()


@app.get("/hello")
def hello():
    return {"message": "hello"}


@app.post("/api")
async def similar_image(file: UploadFile = File(...)):
    temp = '/tmp/uploaded/'
    os.makedirs(temp, exist_ok=True)
    temp_path = os.path.join(temp, file.filename)
    with open(temp_path, 'wb') as fin:
        shutil.copyfileobj(file.file, fin)

    img = open(temp_path, 'rb')
    features = model.encode(img)
    print(features.shape)
    result_items = nn.find_nearest_neighbors(features.reshape(1, -1))
    print(result_items)
    return {"msg": "Success"}
