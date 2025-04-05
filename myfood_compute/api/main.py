from fastapi import FastAPI
from myfood_compute.api.endpoint import (
    image_endpoint as img,
    user_histort_endpoint as user,
    food_endpoint as food,
)


app = FastAPI(title="MyFood API", docs_url="/docs")
app.include_router(img.ImageRouter, prefix="/image", tags=["image"])
app.include_router(user.UserHistoryRouter, prefix="/user", tags=["user"])
app.include_router(food.FoodRouter, prefix="/food", tags=["food"])
