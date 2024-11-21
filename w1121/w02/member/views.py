from django.shortcuts import render,redirect
from member.models import Member


def membership1(request):
  return render(request,'membership1.html')

def membership2(request):
  return render(request,'membership2.html')

def membership3(request):
  return render(request,'membership3.html')

#로그아웃
def logout(request):
  request.session.clear()
  return redirect("/")


# 로그인
def login(request):
  if request.method == "GET":
    return render(request,'login.html')
  else:
    id = request.POST.get("id")
    pw = request.POST.get("pw")

    qs = Member.objects.filter(id=id,pw=pw)

    if qs:
      msg = '1'  # 로그인성공
      request.session['session_id'] = id
      request.session['session_nickname'] = qs[0].nickname
    else:
      mge = '0'  # 로그인실패
    return render(request,'login.html',{"msg":msg})
def event(request):
  return render(request,'event.html')