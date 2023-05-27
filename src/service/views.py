from django.shortcuts import render

class CreateUser(APIView):
    permission_classes = [permissions.AllowAny, ]

    def post(self, request):

        username = request.data.get("username")
        password = request.data.get("password")
        email = request.data.get("email")

        if User.objects.filter(username=username).exists():
            return Response(status=400)
        if User.objects.filter(email=email).exists():
            return Response(status=400)

        user = User.objects.create_user(username=username, password=password, email=email)
        user.save()
        return Response(status=200)
