import random

from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404

from connect_a_ton.utils import checkin_required
from home.models import UserConfig, Question, Answer, UserAnswer, campuses


@login_required
@checkin_required()
def index(request):
    # get the user's question config

    config, _ = UserConfig.objects.get_or_create(user=request.user)

    if not config.campus:
        return redirect('campus_dropdown')


    is_self = random.choice([False, True])

    question, answer = None, None

    user_campus = config.campus

    if is_self:
        question = Question.objects.exclude(id__in=config.self_questions.all()).first()

    if question:
        answer, _ = Answer.objects.get_or_create(question=question, user=request.user)
    else:
        is_self = False
        ids = list(UserConfig.objects.filter(campus=user_campus).values_list("user__id", flat=True))
        answer = Answer.objects.exclude(
            Q(id__in=config.other_answers.all()) | Q(user=request.user) | Q(answer=None)).filter(
                user__id__in=ids).first()

    if answer is None:
        return render(request, 'home/index.html', context={"points": config.points})

    question = answer.question
    name = "you" if is_self else answer.user.first_name + " " + answer.user.last_name
    team = get_object_or_404(UserConfig, user=answer.user).team if not is_self else None
    team = team or "Organizer"

    context = {
        "question": question.question_text.replace("%USER%", name),
        "options": question.options,
        "answer": answer.id,
        "is_self": is_self,
        "points": config.points,
        "team": team,
        "swags": settings.SWAGS
    }
    return render(request, 'home/index.html', context=context)

@login_required
@checkin_required()
def campus_dropdown(request):
    if request.method == 'POST':
        campus = request.POST.get('campus')
        if campus:
            config =  get_object_or_404(UserConfig, user=request.user)
            config.campus = campus
            config.save()
            return redirect('home')  
    return render(request, 'home/campus_dropdown.html', {'campuses': campuses})


@login_required
@checkin_required()
def answer_view(request):
    if request.method != "POST":
        return redirect('home')

    answer = get_object_or_404(Answer, id=request.POST.get('answer_id'))
    answer_value = int(request.POST.get('answer'))
    is_self = answer.user == request.user

    if (answer_value < 0 or answer_value > 3) and is_self:
        return redirect('home')

    # get the user's question config
    config = get_object_or_404(UserConfig, user=request.user)
    # question = None
    # if not is_self:
    #     if config.campus:
    #         questions = Question.objects.filter(campus=config.campus).exclude(id__in=config.self_questions.all())
    #         if questions.exists():
    #             question = random.choice(questions)
    #     else:
    #         questions = Question.objects.exclude(id__in=config.self_questions.all())
    #         if questions.exists():
    #             question = random.choice(questions)
    # else:
    #     question = answer.question

    if is_self:
        answer.answer = answer_value
        answer.save()
        config.self_questions.add(answer.question)

    else:
        UserAnswer.objects.get_or_create(
            answer_value=answer_value,
            answer=answer,
            question_config=config,
    )

    return redirect('home')


@login_required
def check_in(request):
    conf = UserConfig.objects.get(user=request.user)
    if conf.checked_in:
        if request.GET.get('next'):
            return redirect(request.GET.get('next'))

        return redirect('home')

    if request.user.is_staff:
        return redirect('admin:index')

    return render(request, 'home/checkin.html')
