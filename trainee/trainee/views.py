from django.shortcuts import render, get_object_or_404, redirect
from .models import Trainee, DailyTask, admin_mine
from .forms import TraineeForm, TaskForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth import authenticate, login


def index(request):
    # Retrieve all trainees from the database
    trainees = Trainee.objects.all()
    # Pass trainee data to the template
    return render(request, "trainee/index.html", {"trainees": trainees})


def update_trainee(request, trainee_id):
    trainee = get_object_or_404(Trainee, pk=trainee_id)
    if request.method == "POST":
        form = TraineeForm(request.POST, instance=trainee)
        if form.is_valid():
            form.save()
            return redirect("/trainee")
    else:
        form = TraineeForm(instance=trainee)
    return render(request, "trainee/update_trainee.html", {"form": form})


def view_trainee_details(request, trainee_id):
    trainee = get_object_or_404(Trainee, pk=trainee_id)
    # tasks = DailyTask.objects.filter(trainee=trainee)
    # return render(
    #     request,
    #     "trainee/view_trainee_details.html",
    #     {"trainee": trainee, "tasks": tasks},
    # )
    tasks_list = DailyTask.objects.filter(trainee=trainee)

    # Pagination
    paginator = Paginator(tasks_list, 5)
    page = request.GET.get("page")
    try:
        tasks = paginator.page(page)
    except PageNotAnInteger:
        tasks = paginator.page(1)
    except EmptyPage:
        tasks = paginator.page(paginator.num_pages)

    return render(
        request,
        "trainee/view_trainee_details.html",
        {"trainee": trainee, "tasks": tasks},
    )


def add_task(request, trainee_id):
    trainee = Trainee.objects.get(pk=trainee_id)
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.trainee = trainee
            task.save()
            return redirect("view_trainee_details", trainee_id=trainee_id)
    else:
        form = TaskForm()
    return render(request, "add_task", {"form": form, "trainee": trainee})


def admin_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("/trainee")
        else:
            messages.error(request, "Invalid username or password")
    return render(request, "login.html")


def admin_logout(request):
    logout(request)  # Clear the session
    return redirect("admin_login")  # Redirect to login page
