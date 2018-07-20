from graphene_django.views import GraphQLView

import rest_framework.authtoken.views
import rest_framework.decorators


class DRFAuthenticatedGraphQLView(GraphQLView):
    def parse_body(self, request):
        if isinstance(request, rest_framework.request.Request):
            return request.data
        return super(DRFAuthenticatedGraphQLView, self).parse_body(request)

    @classmethod
    def as_view(cls, *args, **kwargs):
        view = super(DRFAuthenticatedGraphQLView, cls).as_view(*args, **kwargs)
        view = rest_framework.decorators.permission_classes([rest_framework.permissions.IsAuthenticated])(view)
        view = rest_framework.decorators.authentication_classes(rest_framework.settings.api_settings.DEFAULT_AUTHENTICATION_CLASSES)(view)
        view = rest_framework.decorators.api_view(['GET', 'POST'])(view)
        return view
