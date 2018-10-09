from rest_framework.views import APIView
from rest_framework import mixins, generics, viewsets
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework import status
from .models import Goods
from .serializer import GoodsSerializer


# Create your views here.

# class GoodsPagination(PageNumberPagination):
#     page_size = 10
#     page_size_query_param = 'page_size'
#     page_query_param = "page"
#     max_page_size = 100


class GoodsListViewSet(generics.ListAPIView):
    queryset = Goods.objects.all()
    serializer_class = GoodsSerializer
    # pagination_class = GoodsPagination


class GoodsListViewSet1(viewsets.ModelViewSet):
    queryset = Goods.objects.all()
    serializer_class = GoodsSerializer
    # pagination_class = GoodsPagination


class GoodsListView(APIView):
    def get(self, request, format=None):
        goods = Goods.objects.all()[:10]
        goods_serializer = GoodsSerializer(goods, many=True)
        return Response(goods_serializer.data)

    def post(self, request, format=None):
        serializer = GoodsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GoodsListView1(mixins.ListModelMixin, generics.GenericAPIView):
    """
    商品列表页
    """
    queryset = Goods.objects.all()[:10]
    serializer_class = GoodsSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
