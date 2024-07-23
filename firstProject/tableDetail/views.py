from django.shortcuts import render
from tableDetail.models import Project

# Create your views here.
def home(request):
    return render(request, "tableDetail/home.html", {})


def table_index(request):
    # projects = [["Issue ID","conversation ID", "Title", "Analysis", "Comments"], ["ABC-4578", "67676676767", "Not working", "No Logs", "This is a CC issue"]]
    projects = Project.objects.all()
    context = {
        "projects": projects
    }
    return render(request, "tableDetail/table_index.html", context)


def table_detail(request, pk):
    project = Project.objects.get(pk=pk)
    context = {
        "project": project
    }
    return render(request, "tableDetail/table_detail.html", context)