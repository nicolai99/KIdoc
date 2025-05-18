import logging

from django.contrib.auth import authenticate, login, logout as auth_logout
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import ensure_csrf_cookie, csrf_exempt
from dmsAPI.schema.AuthSchema import AuthSchema
from ninja import Router
from ninja.errors import HttpError

authRouter = Router()
log = logging.getLogger(__name__)


@authRouter.get("/csrf-token", auth=None)
@ensure_csrf_cookie
@csrf_exempt
def csrf_token(request) -> HttpResponse:
    return HttpResponse()


@authRouter.post("/login", auth=None)
def loginUser(request, cred: AuthSchema) -> JsonResponse:
    user = authenticate(request, username=cred.username, password=cred.password)
    log.debug("authenticate...")
    if user is not None:
        log.debug("authentication successful")
        log.debug("login user")
        login(request, user)
    else:
        raise HttpError(401, "username or password is incorrect.")
    return JsonResponse({'message': 'Login successful'})


@authRouter.post("/logout")
def logout(request) -> JsonResponse:
    auth_logout(request)
    return JsonResponse({'message': 'Logout successful'})


@authRouter.get("/user")
def getUser(request) -> JsonResponse:
    return JsonResponse({'username': request.user.username})
