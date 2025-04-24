from fastapi import APIRouter, status

main_route = APIRouter()


@main_route.post(
    '/make_request',
    status_code=status.HTTP_201_CREATED
)
async def make_request():
    pass


@main_route.post(
    '/',
    status_code=status.HTTP_200_OK
)
async def get_data():
    pass