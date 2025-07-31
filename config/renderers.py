from rest_framework.renderers import JSONRenderer


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
