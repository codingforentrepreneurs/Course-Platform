from django.db.models import Q
from .models import Course, Lesson, PublishStatus


def get_publish_courses():
    return Course.objects.filter(status=PublishStatus.PUBLISHED)

def get_course_detail(course_id=None):
    if course_id is None:
        return None
    obj = None
    try:
        obj = Course.objects.get(
            status=PublishStatus.PUBLISHED,
            public_id=course_id
        )
    except:
        pass
    return obj

def get_course_lessons(course_obj=None):
    lessons = Lesson.objects.none()
    if not isinstance(course_obj, Course):
        return lessons
    lessons = course_obj.lesson_set.filter(
        course__status=PublishStatus.PUBLISHED,
        status__in=[PublishStatus.PUBLISHED, PublishStatus.COMING_SOON]
    )
    return lessons


def get_lesson_detail(course_id=None, lesson_id=None):
    if lesson_id is None and course_id is None:
        return None
    obj = None
    try:
        obj = Lesson.objects.get(
            course__public_id=course_id,
            course__status=PublishStatus.PUBLISHED,
            status__in=[PublishStatus.PUBLISHED, PublishStatus.COMING_SOON],
            public_id=lesson_id
        )
    except Exception as e:
        print("lesson detail", e)
        pass
    return obj