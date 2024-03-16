from django.shortcuts import render, redirect
from .models import Question, Choice

# Create your views here.
def index(request):
    return render(request, 'index.html')

def result(request):
    score = request.session.get("score", 0)
    total_questions = Question.objects.count()
    # Clear session for a new attempt
    request.session.flush()
    return render(request, 'result.html', {
        'score': score,
        'total_questions': total_questions,
    })

def test(request):
    if "current_question_id" not in request.session:
        # Starting the test
        first_question = Question.objects.first()
        request.session["current_question_id"] = first_question.id
        request.session["score"] = 0
        is_last_question = Question.objects.count() == 1
    else:
        # Processing answer and fetching next question
        current_question_id = request.session["current_question_id"]
        #current_question = Question.objects.get(id=current_question_id)
        selected_choice_id = request.POST.get('choice')
        
        if selected_choice_id:
            selected_choice = Choice.objects.get(id=selected_choice_id)
            if selected_choice.is_correct:
                request.session["score"] += 1
                
        next_question = Question.objects.filter(id__gt=current_question_id).first()
        
        if next_question:
            request.session["current_question_id"] = next_question.id
            is_last_question = not Question.objects.filter(id__gt=next_question.id).exists()
        else:
            # This was the last question
            return redirect('result')

    context = {
        'question': Question.objects.get(id=request.session["current_question_id"]),
        'question_id': request.session["current_question_id"],
        'choices': Choice.objects.filter(question_id=request.session["current_question_id"]),
        'is_last_question': is_last_question,
    }
    return render(request, 'test.html', context)
