from django.shortcuts import render
from django.http import JsonResponse
from .serialzers import HospitalSerializer

from .models import Hospital
from datetime import datetime

def hospitals(req):
    hosp1=Hospital()
    hosp1.name="AIIMS"
    hosp1.established_date=1990
    hosp1.address="Sri Aurobindo Marg, Ansari Nagar, Ansari Nagar East, New Delhi, Delhi 110029"
    hosp1.city="New Delhi"

    hosp2=Hospital()
    hosp2.name="Lilavati Hospital And Research Centre"
    hosp2.established_date=1995
    hosp2.address="A-791, Bandra Reclamation Rd, General Arunkumar Vaidya Nagar, Bandra West, Mumbai, Maharashtra 400050"
    hosp2.city="Mumbai"
    list_of_hospital=[hosp1,hosp2]
    return JsonResponse(HospitalSerializer(list_of_hospital,many=True).data,safe=False)

