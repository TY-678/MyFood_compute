from flask import Flask, request
import cv2
from ultralytics import YOLO
from flask import jsonify
import numpy




app = Flask(__name__)

@app.route('/upload', methods=['POST'])
def upload_file():
    try:
        uploaded_file = request.files['file']
        uploaded_file.save('save/' + uploaded_file.filename)


        #yolo
        yolo = YOLO("weight/best_1115.pt")
        resultslist = yolo(f'save/{uploaded_file.filename}', conf=0.5)
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
