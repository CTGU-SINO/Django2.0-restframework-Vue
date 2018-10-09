from django.forms.models import model_to_dict
from django.views.generic.base import View
from django.http import HttpResponse, JsonResponse
from django.core import serializers
from goods.models import Goods
import json


class GoodsListView(View):
    def get(self, request):
        goods = Goods.objects.all()[:10]
        # json_list = [{
        #     'name': good.name,
        #     'category': good.category.name,
        #     'market_price': good.market_price
        # } for good in goods]

        # json_list = [model_to_dict(good) for good in goods]
        # return HttpResponse(json.dumps(json_list), content_type='application/json')

        json_list = serializers.serialize('json', goods)
        json_list = json.loads(json_list)

        return JsonResponse(json_list, safe=False)


