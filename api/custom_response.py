from rest_framework.response import Response

class CustomResponse(Response):
    def __init__(self, status, message=None, data=None, *args, **kwargs):
        response_data = {
            "status": status,
        }
        if message is not None:
            response_data['message']=message
       
        if data is not None:
            response_data["data"] = data
        super().__init__(response_data, *args, **kwargs)
