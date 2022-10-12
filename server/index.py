from __future__ import annotations

import pickle

from fastapi import FastAPI, File, UploadFile
from model import Image2Vector
import os
import shutil
from sklearn.neighbors import NearestNeighbors
import numpy as np

from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
model = Image2Vector()

from dataclasses import dataclass


@dataclass
class FlowerModel:
    id: int
    filename: str


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
        result_size = len(indicates[0])
        print(indicates.shape)
        result_filename = []
        result_items = []
        for i in range(result_size):
            index = int(indicates[0][i])
            filename = self.filenames[index]
            result_filename.append(filename)
            name = filename.split("/")[-1]
            distance = dist[0][i]
            result_items.append({"name": name, "file_name": filename, "dist": distance})
        return result_items


nn = SimilarImageEngine()


@app.get("/hello")
def hello():
    return {"message": "hello"}


@app.get("/example")
def example():
    return [{'name': 'image_07946.jpg',
             'file_name': '../data/jpg/image_07946.jpg',
             'dist': 13.725820299686056},
            {'name': 'image_07994.jpg',
             'file_name': '../data/jpg/image_07994.jpg',
             'dist': 13.734956026817882},
            {'name': 'image_01984.jpg',
             'file_name': '../data/jpg/image_01984.jpg',
             'dist': 14.09439358802111},
            {'name': 'image_04162.jpg',
             'file_name': '../data/jpg/image_04162.jpg',
             'dist': 14.185943526566387},
            {'name': 'image_04274.jpg',
             'file_name': '../data/jpg/image_04274.jpg',
             'dist': 14.277486524170204},
            {'name': 'image_00464.jpg',
             'file_name': '../data/jpg/image_00464.jpg',
             'dist': 14.309397354289478},
            {'name': 'image_00922.jpg',
             'file_name': '../data/jpg/image_00922.jpg',
             'dist': 14.325964767723049},
            {'name': 'image_04453.jpg',
             'file_name': '../data/jpg/image_04453.jpg',
             'dist': 14.34166030834781}]


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
    return result_items

from pydantic import BaseModel

class Model(BaseModel):
    id: str | None

