from django.shortcuts import render, redirect
from django.db.models import Avg
from .models import PilatesClass, Instructor
from .forms import PilatesClassForm


def log_class(request):

    if request.method == "POST":
        form = PilatesClassForm(request.POST)

        if form.is_valid():
            pilates = form.save(commit=False)

            new_instructor = form.cleaned_data["new_instructor"]

            if new_instructor:
                instructor = Instructor.objects.create(
                    name=new_instructor
                )
                pilates.instructor = instructor

            pilates.save()

            return redirect("history")

    else:
        form = PilatesClassForm()

    return render(request, "classes/log_class.html", {"form": form})


def history(request):

    classes = PilatesClass.objects.order_by("-date")

    return render(request, "classes/history.html", {
        "classes": classes
    })


def stats(request):

    stats = PilatesClass.objects.aggregate(
        arms_avg=Avg("arms"),
        legs_avg=Avg("legs"),
        abs_avg=Avg("abs"),
    )

    total = PilatesClass.objects.count()

    return render(request, "classes/stats.html", {
        "stats": stats,
        "total": total
    })