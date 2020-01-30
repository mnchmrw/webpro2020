from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def dashboard(request):
    return HttpResponse('หน้าจอ dashboard สามารถดูภาพรวมของระบบได้ว่า ในวันนั้น ๆ แต่ละวิชามีจำนวนคนเข้าเรียนกี่คน ขาดกี่คน')

def search(request, id):
    return HttpResponse('หน้าจอค้นหา และ export ข้อมูลการเข้าห้องเรียน ทั้งในเทอมปัจจุบัน และ ย้อนหลัง')