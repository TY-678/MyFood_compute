from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
import cv2
from ultralytics import YOLO
import numpy
import os
import shutil

# 檢查當前路徑中有無temp資料夾，若無則建立一個
current_directory = os.getcwd()
folder_path = os.path.join(current_directory, "temp")
if not os.path.exists(folder_path):
    os.makedirs(folder_path)

app = FastAPI()


@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    try:
        file_path = os.path.join(folder_path, file.filename)

        # Save the uploaded file to the temp folder
        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        # YOLO
        yolo = YOLO("weight/best_1115.pt")
        resultslist = yolo(file_path, conf=0.5)
        scan_list = []

        for result in resultslist:
            ddd = result.boxes.cls.tolist()
            print(ddd)
            for i in ddd:
                scan_list.append(i)

        return JSONResponse(content=scan_list)

    except Exception as e:
        print(f"Error handling file upload: {str(e)}")
        return JSONResponse(
            content={"error": "Error handling file upload"}, status_code=500
        )
