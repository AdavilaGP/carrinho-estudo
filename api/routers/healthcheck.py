from fastapi import APIRouter, JSONResponse, status

router = APIRouter(tags=['Healthcheck'], prefix='/healthcheck')

@router.get('')
def healthcheck():
    return JSONResponse(status_code=status.HTTP_200_OK, content="OK")