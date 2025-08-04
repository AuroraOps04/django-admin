from rest_framework.renderers import JSONRenderer

def to_camel_case(val: str):
    if not val:
        return val
    components = val.split("_")
    return components[0] + "".join([x.title() for x in components[1:]])

def to_snake_case(val: str):
    if not val:
        return val
    snake_chars = []
    for i, char in enumerate(val):
        if char.isupper() and i != 0:  # 首字母不大写，后续大写字母前加下划线
            snake_chars.append('_')
        snake_chars.append(char.lower())
    return ''.join(snake_chars)

def recursion(value, transform):
    if isinstance(value, dict):
        d = {}
        for k ,v in value.items():
           d[transform(k)] = recursion(v, transform)
        return d
    elif isinstance(value, list):
        d = []
        for v in value:
           d.append(recursion(v, transform))
        return d
    else:
        return value

class VbenJsonRenderer(JSONRenderer):
    def render(self, data, accepted_media_type=None, renderer_context=None):
        """
               统一返回格式：
               {
                   "code": 0,
                   "message": "success",
                   "data": { ... }
               }
        """
        # data = recursion(data, to_camel_case)
        response_data = {
            "code": 0,
            "message": "success",
            "data": data
        }
        if renderer_context and "response" in renderer_context:
            response = renderer_context["response"]
            if hasattr(response, "code"):
                response_data['code'] = response.code
            elif hasattr(response, "status_code"):
                status_code = response.status_code
                if 200 <= status_code < 300:
                    response_data['code'] = 0
                else:
                    response_data['code'] = status_code
            else:
                response_data['code'] = 500
            if hasattr(response, "message"):
                response_data['message'] = response.message

        return super().render(response_data, accepted_media_type, renderer_context)
