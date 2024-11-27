from django.shortcuts import render
from board.models import Board
from member.models import Member
from datetime import datetime
from django.db.models import Q
from django.db.models import F
from django.core.paginator import Paginator

# 글수정페이지, 글수정저장
def bupdate(request,bno):
  if request.method == "GET":
    qs = Board.objects.get(bno=bno)
    context = {"board":qs}
    return render(request,'bupdate.html',context)
  else:
    bno = request.POST.get("bno")
    btitle = request.POST.get('btitle')
    bcontent = request.POST.get('bcontent')
    bfile = request.FILES.get('bfile','')
    qs = Board.objects.get(bno=bno)
    qs.btitle = btitle
    qs.bcontent = bcontent
    if bfile:
      qs.bfile = bfile
    qs.save()
    context = {"umsg":bno}
    return render(request,'bupdate.html',context)


# 글삭제
def bdelete(request,bno):
  Board.objects.get(bno=bno).delete()
  context = {"dmsg":bno}
  return render(request,'blist.html',context)


# 글상세보기
def bview(request,bno):
  npage = request.GET.get('npage',1)
  qs = Board.objects.get(bno=bno)
  prev_qs = Board.objects.filter(Q(bgroup__lt=qs.bgroup,bstep__lte=qs.bstep)| Q(bgroup=qs.bgroup,bstep__gt=qs.bstep)).order_by("-bgroup","bstep").first()
  next_qs = Board.objects.filter(Q(bgroup__lt=qs.bgroup,bstep__lte=qs.bstep)| Q(bgroup=qs.bgroup,bstep__gt=qs.bstep)).order_by("bgroup","-bstep").first()
  day1 = datetime.replace(datetime.now(),hour=23,minute=59,second=59)
  expires = datetime.strftime(day1,"%a, %d-%b-%Y %H:%M:%S GMT")
  context = {"board":qs,"prev_board":prev_qs,"next_board":next_qs,"npage":npage}
  response = render(request,'bview.html',context)
  if request.COOKIES.get("cookie_boardNo") is not None:
    cookies = request.COOKIES.get("cookie_boardNo")
    cookies_list = cookies.split("|")
    if str(bno) not in cookies_list:
      response.set_cookie("cookie_boardNo",cookies + f"|{bno}",expires=expires)
      qs.bhit +=1
      qs.save()
  else: 
    response.set_cookie("cookie_boardNo",bno,expires=expires)
    qs.bhit += 1
    qs.save()
  return response


# 글쓰기, 글저장
def bwrite(request):
  if request.method == "GET":
    return render(request,'bwrite.html')
  else:
    id = request.session['session_id']
    member = Member.objects.get(id=id)
    btitle = request.POST.get('btitle')
    bcontent = request.POST.get("bcontent")
    bfile = request.FILES.get("bfile",'')
    qs = Board.objects.create(member=member,btitle=btitle,bcontent=bcontent,bfile=bfile)
    qs.bgroup = qs.bno
    qs.save()
    context = {"wmsg":"1"}
    return render(request,'bwrite.html',context)


# 게시판 리스트
def blist(request):
  qs = Board.objects.all().order_by("-bgroup","bstep")
  context = {"blist":qs}
  return render(request,'blist.html',context)