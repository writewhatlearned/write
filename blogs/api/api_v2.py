from ninja import NinjaAPI


api = NinjaAPI(version='2.0.0')


@api.get('/hello')
def hello(request):
    return {'message': 'Hello from V2'}
