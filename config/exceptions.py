from django.http import Http404
from rest_framework import status
from rest_framework.exceptions import APIException, NotAuthenticated, ValidationError
from rest_framework.exceptions import AuthenticationFailed


class BizException(APIException):
    status_code = 400
    default_detail = "业务异常"
    default_code = "biz_error"

    def __init__(self, detail=None, code=None, status_code=None):
        if status_code is not None:
            self.status_code = status_code
        super(BizException, self).__init__(detail=detail, code=code)


class PermissionDeniedException(BizException):
    """权限不足"""

    status_code = 403
    default_detail = "权限不足"
    default_code = "permission_denied"


class NotFoundException(BizException):
    """资源不存在"""

    status_code = 404
    default_detail = "资源不存在"
    default_code = "not_found"


def vben_exception_handler(exc, context):
    """自定义异常处理器"""
    from rest_framework.views import exception_handler

    response = exception_handler(exc, context)
    if response is not None:
        if isinstance(exc, Http404):
            response.code = 404
            response.message = "资源不存在"
            response.status_code = 200
            response.data = None
        elif isinstance(exc, BizException):
            response.code = exc.status_code
            response.message = exc.detail
        elif isinstance(exc, ValidationError):
            response.code = 400
            detail = exc.detail
            errors = None
            if isinstance(detail, dict):
                keys = list(detail.keys())
                if len(keys) > 0:
                    errors = detail[keys[0]]
                    # response.message = f"{keys[0]}: {exc.detail[keys[0]][1]}"
            elif isinstance(detail, list):
                errors = detail[0]
                # response.message = detail[0]
            if errors is None:
                response.message = "参数错误"
            if isinstance(errors, dict):
                keys = list(errors.keys())
                if len(keys) > 0:
                    response.message = errors[keys[0]]
            elif isinstance(errors, list):
                response.message = errors[0]
            else:
                response.message = errors
            response.data = None
        elif isinstance(exc, NotAuthenticated):
            response.code = 401
            response.status_code = status.HTTP_401_UNAUTHORIZED
            response.message = "请先登录"
            response.data = None
        elif isinstance(exc, AuthenticationFailed):
            if exc.default_code == "authentication_failed":
                if exc.args[0] == "User not found":
                    response.code = 401
                    response.status_code = status.HTTP_401_UNAUTHORIZED
                    response.message = "Token 错误"
                    response.data = None
                else:
                    response.data = None
                    response.code = 400
                    response.status_code = 400
                    response.message = "用户名密码错误"
            elif exc.default_code == "token_not_valid":
                response.code = 401
                response.status_code = status.HTTP_401_UNAUTHORIZED
                response.message = "Token 错误或者过期"
                response.data = None
            else:
                response.code = 401
                response.status_code = status.HTTP_401_UNAUTHORIZED
                response.message = "Token 错误或者过期"
                response.data = None
        else:
            response.code = 500
            response.message = "系统异常"
    return response
