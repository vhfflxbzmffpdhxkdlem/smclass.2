from django.shortcuts import render,redirect
from students.models import Student
from django.urls import reverse

# 학생정보 삭제
def delete(request,name):
  Student.objects.get(name=name).delete()
  return redirect('/students/list')


# 1. 학생수정페이지 2. 학생수정저장
def update(request):
  if request.method =='GET':
    name = request.GET['name']
    qs = Student.objects.get(name=name)
    context={"stu":qs}
    return render(request,'update.html',context)
  else:
    name = request.POST.get('name')
    major = request.POST.get('major')
    grade = request.POST.get('grade')
    age = request.POST.get('age')
    gender = request.POST.get('gender')
    hobby = request.POST.get('hobby')

    qs = Student.objects.get(name=name)
    qs.major=major
    qs.grade=grade
    qs.age=age
    qs.gender=gender
    qs.hobby=hobby
    qs.save()

    return redirect('students:list',name)

# 학생상세보기
def view(request,name):
  qs = Student.objects.get(name=name)
  context={"stu":qs}
  return render(request,'view.html',context)

# 학생전체리스트
def list(request):
  qs = Student.objects.all()
  context={"slist":qs}
  return render(request,'list.html',context)

# 학생입력페이지, 학생저장
def write(request):
  if request.method == "POST":
    name = request.POST.get("name")
    major = request.POST["major"]
    grade = request.POST["grade"]
    age = request.POST["age"]
    gender = request.POST["gender"]
    hobbys = request.POST.getlist("hobby")

    print(name)
    Student.objects.create(name=name,major=major,grade=grade,age=age,gender=gender,hobby=hobbys)
    return redirect('/students/list/')
  else:
    return render(request,'write.html')
  