"""DZ_12_V3"""
from fastapi import FastAPI

PRODUCTS = {
    456: 158.38,
    789: 3000
}

app = FastAPI()


@app.get("/products/{product_id}")
async def return_product(
    product_id: int,
    discount_percentage: int | None = None
):
    """Асинхронная функция"""
    price = PRODUCTS.get(product_id)
    if price is None:
        return {"Eror: not found"}
    elif discount_percentage is None:
        return {
            "product": product_id,
            "price": price
        }
    discount_price = price - price * (discount_percentage / 100)

    return {
        "product": product_id,
        "price": price,
        "discount_price": round(discount_price, 2)
    }
