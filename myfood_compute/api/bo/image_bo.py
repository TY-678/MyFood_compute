import os
import shutil
import uuid
from fastapi import File, UploadFile
from fastapi.responses import JSONResponse
from ultralytics import YOLO


class ImageRecognition:
    def __init__(self):
        self.temp_folder = self._create_temp_folder()

    @staticmethod
    def _create_temp_folder():
        current_directory = os.getcwd()
        folder_path = os.path.join(current_directory, "temp")
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
        return folder_path

    def save_image(self, file: UploadFile = File(...)):
        unique_filename = f"{uuid.uuid4()}.jpg"
        file_path = os.path.join(self.temp_folder, unique_filename)

        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        return file_path

    def recognize_image(self, file_path: str) -> list[int]:
        yolo = YOLO("weight/best.pt")
        resultslist = yolo(file_path, conf=0.5)
        scan_list = []

        for result in resultslist:
            scan_list.extend([int(i) for i in result.boxes.cls.tolist()])
        return scan_list
