from fastapi import APIRouter
from .info.router import info_router
from .prices.router import price_router
from .images.router import img_router

api_router_v2 = APIRouter()

api_router_v2.include_router(info_router, prefix="/info")
api_router_v2.include_router(price_router, prefix="/price")
api_router_v2.include_router(img_router, prefix="/images")
