from fastapi import FastAPI

catalog = {
    "tomatoes": {
        "units": "boxes",
        "quantity": 1000,
        "color": "red"
    },
    "wine": {
        "units": "bottle",
        "quantity": 500,
        "color": "white"
    }
}

app = FastAPI(title="New Jersey API Server")


@app.get("/warehouse/{product}")
async def load_truck(product: str, order_quantyty: int, color: str):

    return {
        "product": product,
        "order_quantyty": order_quantyty,
        "units": catalog[product]["units"],
        "color": catalog[product]["color"]
    }

#--------------------------------------------------- comments
#run server
# uvicorn nj_server:app
#--------------------------------------------------
# http://127.0.0.1:8000/docs
#--------------------------------------------------
