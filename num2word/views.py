from decimal import Decimal
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views.generic import View
from num2words import num2words

import json


class ConvView(View):

    def get(self, request, *args, **kwargs):
        """
        Get number and language code from url
        :return: json HttpResponse
        """

        try:
            number = Decimal(self.kwargs['number'], 10) if 'number' in self.kwargs else None
        except:
            number = None

        lang = self.kwargs['lang'].lower() if 'lang' in self.kwargs else 'en'
        res = {'error': 'Wrong url parameters. Example main_url/float_number/lang_code/'}

        if number:
            try:
                res = {"number": num2words(number, lang=lang).replace('-', ' ')}
            except NotImplementedError:
                res = {
                    "number": num2words(number, lang='en').replace('-', ' '),
                    'message': 'Lang not supported used default en'
                }

        return HttpResponse(json.dumps(res, ensure_ascii=False),  content_type="application/json;charset=utf-8")