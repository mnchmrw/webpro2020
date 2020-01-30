from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def student(request, std_id):
    return HttpResponse('หน้าจอรายการนักเรียนทั้งหมด รหัสนักเรียน: %s' % std_id)

def add_student(request, std_id):
    return HttpResponse('หน้าจอเพิ่มนักเรียน รหัสนักเรียน: %s' % std_id)

def edit_student(request, std_id):
    return HttpResponse('หน้าจอแก้ไขข้อมูลนักเรียน รหัสนักเรียน: %s' % std_id)

def subject(request, sub_id):
    return HttpResponse('หน้าจอรายการวิชาเรียนทั้งหมด รหัสวิชา: %s' % sub_id)

def add_subject(request, sub_id):
    return HttpResponse('หน้าจอเพิ่มวิชาเรียน รหัสวิชา: %s' % sub_id)

def edit_subject(request, sub_id):
    return HttpResponse('หน้าจอแก้ไขข้อมูลวิชาเรียน รหัสวิชา: %s' % sub_id)