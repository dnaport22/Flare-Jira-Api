# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .service import Service

@api_view(['GET', 'POST'])
def request_handler(request):
  type = request.GET.get('type')
  ser = Service()

  if type == 'log_time':
    return Response(request.data)
  if type == 'comment':
    return Response(ser.leave_comment(request.data))
  if type == 'test':
    return Response(ser.test(request.data))
  else:
    return Response('Error!')
