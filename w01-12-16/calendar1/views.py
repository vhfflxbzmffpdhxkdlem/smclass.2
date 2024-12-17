from django.shortcuts import render, redirect
from calendar1.models import Event
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
from loginpage.models import Member
from datetime import timedelta
from datetime import datetime
from django.db.models import Q
from itertools import chain

@csrf_exempt
def update_event(request):
  if request.method == 'POST':
    event_id = request.POST.get('event_id')
    title = request.POST.get('title')
    color = request.POST.get('color')  # 색상 받아오기
    start_date = request.POST.get('start_date')
    end_date = request.POST.get('end_date')
    location = request.POST.get('location')
    repeat = request.POST.get('repeat')
    memo = request.POST.get('memo')



    event = Event.objects.get(no=event_id)  # 이벤트 찾기
    # 기존 이벤트를 삭제하기 전에 반복 이벤트도 함께 삭제
    if event.repeat != 'none':
      Event.objects.filter(no=event_id).delete()

    event.title = title
    event.color = color  # 색상 수정 (튜플 쉼표 제거)
    event.start_date = start_date
    event.end_date = end_date
    event.location = location
    event.repeat = repeat
    event.memo = memo
    event.save()  # 수정된 내용 저장

    # 반복 처리
    if repeat != 'none':
      current_start_date = timezone.datetime.fromisoformat(start_date)
      current_end_date = timezone.datetime.fromisoformat(end_date)

      for _ in range(1, 2):  # 예시로 최대 12번 반복 (필요에 따라 수정)
        if repeat == 'daily':
          current_start_date += timedelta(days=1)
          current_end_date += timedelta(days=1)
        elif repeat == 'weekly':
          current_start_date += timedelta(weeks=1)
          current_end_date += timedelta(weeks=1)
        elif repeat == 'monthly':
          current_start_date = current_start_date.replace(month=current_start_date.month % 12 + 1)
          current_end_date = current_end_date.replace(month=current_end_date.month % 12 + 1)
        elif repeat == 'yearly':
          current_start_date = current_start_date.replace(year=current_start_date.year + 1)
          current_end_date = current_end_date.replace(year=current_end_date.year + 1)

        # 반복 이벤트 생성
        Event.objects.create(
          title=title,
          color=color,
          start_date=current_start_date,
          end_date=current_end_date,
          location=location,
          repeat=repeat,
          memo=memo,
        )


    return JsonResponse({'success': True}, status=200)

  return JsonResponse({'error': '잘못된 요청입니다.'}, status=400)

# 모든 이벤트를 JSON 형식으로 반환
def son(request):
  events = Event.objects.all()  # 모든 이벤트 가져오기
  events_data = []
  for event in events:
    events_data.append({
      'id': event.no,
      'title': event.title,
      'color': event.color,
      'start': event.start_date.isoformat(),
      'end': event.end_date.isoformat(),
      'location': event.location,
      'memo': event.memo,
      'repeat': event.repeat,
    })
  return JsonResponse(events_data, safe=False)

# 캘린더 페이지 렌더링 및 이벤트 생성
def cal(request):
  if request.method == "POST":
    title = request.POST.get('title')
    color = request.POST.get('color')  # 색상 받아오기
    start_date = request.POST.get('start_date')
    end_date = request.POST.get('end_date')
    location = request.POST.get('location')
    repeat = request.POST.get('repeat')
    memo = request.POST.get('memo')

    # datetime 형식으로 변환
    start_date = timezone.datetime.fromisoformat(start_date)
    end_date = timezone.datetime.fromisoformat(end_date)

    # 이벤트 생성
    Event.objects.create(
      title=title,
      color=color,  # 색상 저장
      start_date=start_date,
      end_date=end_date,
      location=location,
      repeat=repeat,
      memo=memo,
    )

    # 반복 설정에 따른 추가 이벤트 생성
    if repeat != 'none':
      current_start_date = start_date
      current_end_date = end_date

      for _ in range(1, 3):  # 예시로 최대 12번 반복 (필요에 따라 수정)
        if repeat == 'daily':
          current_start_date += timedelta(days=1)
          current_end_date += timedelta(days=1)
        elif repeat == 'weekly':
          current_start_date += timedelta(weeks=1)
          current_end_date += timedelta(weeks=1)
        elif repeat == 'monthly':
          current_start_date = current_start_date.replace(month=current_start_date.month % 12 + 1)
          current_end_date = current_end_date.replace(month=current_end_date.month % 12 + 1)
        elif repeat == 'yearly':
          current_start_date = current_start_date.replace(year=current_start_date.year + 1)
          current_end_date = current_end_date.replace(year=current_end_date.year + 1)

        # 반복 이벤트 생성
        Event.objects.create(
          title=title,
          color=color,
          start_date=current_start_date,
          end_date=current_end_date,
          location=location,
          repeat=repeat,
          memo=memo,
        )

    return redirect(f'/calendar1/cal/')
  else:
    id = request.session.get('session_id')
    user = Member.objects.get(id=id)
    context = {'user':user}
    created_group = user.created_group or ''
    joined_group = user.joined_group or ''
    joined_group_members = Member.objects.filter(joined_group=created_group) if created_group else []
    created_group_members = Member.objects.filter(Q(created_group=joined_group) | Q(joined_group=joined_group)) if joined_group else []
    
    members = list({member.id: member for member in chain(joined_group_members, created_group_members)}.values())
    members.append(user)

    # 현재 members 목록에 없는 생일 이벤트 삭제
    member_names = [member.name for member in members]  # 현재 members의 이름 리스트
    Event.objects.filter(title__endswith="의 생일").exclude(
    title__startswith=tuple(member_names)
    ).delete()

    for member in members:

      # **생일 정보가 변경되었을 때 이전의 생일 이벤트 삭제하고 새로 저장**
      if isinstance(member.birthday, str):
          member_birthday = datetime.strptime(member.birthday, '%Y-%m-%d')  # 문자열을 datetime으로 변환
      else:
          member_birthday = member.birthday  # 이미 datetime 객체라면 그대로 사용


      # 생일 이벤트가 이미 있다면 삭제
      Event.objects.filter(title=f'{member.name}의 생일', start_date__year=member_birthday.year).delete()
      

      # 생일 이벤트 생성 (반복 설정 포함)
      if isinstance(member.birthday, str):
          member_birthday = datetime.strptime(member.birthday, '%Y-%m-%d')  # 문자열을 datetime으로 변환
      else:
          member_birthday = member.birthday  # 이미 datetime 객체라면 그대로 사용

      Event.objects.create(
        title=f'{member.name}의 생일',  # 이벤트 제목
        color='yellow',  # 색상
        start_date=member.birthday,  # 생일 날짜 (시작)
        end_date=member.birthday,  # 생일 날짜 (끝)
        repeat='yearly'
      )

      # 생일 이벤트가 처음 생성될 때, 이후에도 반복되도록 추가 이벤트 생성
      current_start_date = member_birthday
      current_end_date = member_birthday

      for _ in range(1, 50):  # 예시로 최대 12년 반복 (필요에 따라 수정)
        current_start_date = current_start_date.replace(year=current_start_date.year + 1)
        current_end_date = current_end_date.replace(year=current_end_date.year + 1)

        # 반복 생일 이벤트 생성
        Event.objects.create(
          title=f'{member.name}의 생일',
          color='yellow',
          start_date=current_start_date,
          end_date=current_end_date,
          repeat='yearly',
          memo=f'{member.name}의 생일입니다.',
        )

    return render(request, 'calendar.html',context)

@csrf_exempt
def delete_event(request):
  if request.method == 'POST':
    event_id = request.POST.get('event_id')

    try:
      event = Event.objects.get(no=event_id)  
      event.delete()
      return JsonResponse({'success': True}, status=200)
    except Event.DoesNotExist:
      return JsonResponse({'error': '이벤트를 찾을 수 없습니다.'}, status=404)

  return JsonResponse({'error': '잘못된 요청입니다.'}, status=400)

