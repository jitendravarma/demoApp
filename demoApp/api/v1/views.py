# create apis here
import json
from collections import OrderedDict

from core.models import Text
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import TextSerializer, UserSerializer


def create_response(response_data):
    """
    method used to create response data in given format
    """
    response = OrderedDict()
    response["header"] = {"status": "1"}
    response["body"] = response_data
    return response


def create_serializer_error_response(errors):
    """
    method is used to create error response for serializer errors
    """
    error_list = []
    for k, v in errors.items():
        if isinstance(v, dict):
            _, v = v.popitem()
        d = {}
        d["field"] = k
        d["field_error"] = v[0]
        error_list.append(d)
    return OrderedDict({"header": {"status": "0"}, "errors": {
        "errorList": error_list}})


class UpdateProfileAPIView(APIView):
    """update user's profile using this view"""

    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        source = UserSerializer(self.request.user)
        return Response(create_response({"results": source.data}))

    def post(self, request, *args, **kwargs):
        user_serializer = UserSerializer(request.user, data=request.data)
        if user_serializer.is_valid():
            user_serializer.save()
            return Response(create_response(
                {"msg": "Profile updated successfully"}))
        else:
            return Response(
                create_serializer_error_response(user_serializer.errors),
                status=403)

    def put(self, request):
        image_file = request.data["image_file"]
        user = request.user
        user.profile_pic = image_file
        user.save()
        return Response(create_response({"msg": "Profile pic updated successfully!"}))


class UploadJson(APIView):
    permission_classes = [
        AllowAny,
    ]
    """
    this view is used to upload json file
    """

    def post(self, request, *args, **kwargs):
        try:

            json_file = request.data.get('file')
            items = json.loads(json_file.read().decode("utf-8"))
            for item in items:
                text, _ = Text.objects.get_or_create(data_id=item['id'])
                text.user_id = item['userId'] if 'userId' in item else ""
                text.title = item['title'] if 'title' in item else ""
                text.body = item['body'] if 'body' in item else ""
                text.save()
            status = 200
            res_data = create_response({"msg": "File uploaded successfully"})
        except Exception as error:
            print(error)
            status = 500
            res_data = create_serializer_error_response({"msg": "Something went wrong"})
        return Response(res_data,  status=status)


class TextAPIView(APIView):
    """api view to render serailized text objects"""

    serializer_class = TextSerializer
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        source = TextSerializer(Text.objects.all(), many=True)
        return Response(create_response({"results": source.data}))
