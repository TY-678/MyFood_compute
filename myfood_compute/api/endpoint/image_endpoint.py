from fastapi import File, UploadFile, APIRouter
from myfood_compute.api.bo.image_bo import ImageRecognition

ImageRouter = APIRouter()
img = ImageRecognition()


@ImageRouter.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    img_path = img.save_image(file)
    return img.recognize_image(img_path)
