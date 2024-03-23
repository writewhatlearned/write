from ninja import NinjaAPI


api = NinjaAPI(version='1.0.0')


@api.get('/hello')
def hello(request):
    return {'message': 'Hello from V1'}


@api.get("/add")
def add(request, a: int, b: int):
    return {"result": a + b}
