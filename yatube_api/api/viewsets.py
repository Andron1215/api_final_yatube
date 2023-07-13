from rest_framework import mixins, viewsets


class CreateRetrieveViewSet(
    mixins.CreateModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet
):
    pass
