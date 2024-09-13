from django.http import Http404
from django.shortcuts import render

from . import services

def course_list_view(request):
    queryset = services.get_publish_courses()
    return render(request, "courses/list.html", {})


def course_detail_view(request, course_id=None, *args, **kwarg):
    course_obj = services.get_course_detail(course_id=course_id)
    if course_obj is None:
        raise Http404
    return render(request, "courses/detail.html", {})


def lesson_detail_view(request, course_id=None, lesson_id=None, *args, **kwargs):
    lesson_obj = services.get_lesson_detail(
        course_id=course_id,
        lesson_id=lesson_id
    )
    if lesson_obj is None:
        raise Http404
    return render(request, "courses/lesson.html", {})