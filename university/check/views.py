from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def check_subject(request):
    return HttpResponse('หน้าจอรายการวิชาที่มีการสอนในวันนั้น ๆ ของ อ. ที่ login เข้ามา')

def course_descript(request, id):
    return HttpResponse('หน้าจอรายละเอียดของแต่ละวิชา (วิชานี้สอนอะไร, มีจำนวนนักเรียนกี่คน, มีคนมาเรียน และขาดกี่คน)')

def qrcode(request):
    return HttpResponse('หน้าจอเช็คชื่อของแต่ละวิชาที่สามารถเช็คชื่อได้ด้วย QR code')