from flask import Flask, request
import cv2
from ultralytics import YOLO
from flask import jsonify
import numpy

import os


# 檢查當前路徑中有無temp資料夾，若無則建立一個
current_directory = os.getcwd()
folder_path = os.path.join(current_directory, 'temp')
if not os.path.exists(folder_path):
    os.makedirs(folder_path)


app = Flask(__name__)

@app.route('/upload', methods=['POST'])
def upload_file():
    try:
        uploaded_file = request.files['file']
        uploaded_file.save('temp/' + uploaded_file.filename)


        #yolo
        yolo = YOLO("weight/best_1115.pt")
        resultslist = yolo(f'temp/{uploaded_file.filename}', conf=0.5)
        scan_list = []

        for result in resultslist:
            ccc = result.boxes.cls.numpy().tolist()
            print(ccc)
            ddd = result.boxes.cls.tolist()
            print(ddd)
            for i in ddd:
                scan_list.append(i) 

        return jsonify(scan_list)
        

    except Exception as e:
        print(f'Error handling file upload: {str(e)}')
        return 'Error handling file upload', 500




if __name__ == '__main__':
    app.run(debug=True)
