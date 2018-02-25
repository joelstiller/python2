# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

class CourseManager(models.Manager):
    def validate(self, post_data):
        errors = {}

        # check all fields for emptyness
        for field, value in post_data.iteritems():
            if len(value) < 1:
                errors[field] = "{} field is required".format(field.replace('_', ' '))

            # check name fields for min length
            if field == "course_name":
                if not field in errors and len(value) < 5:
                    errors[field] = "{} field must bet at least 5 characters".format(field.replace('_', ' '))
            if field == "description":
                if not field in errors and len(value) < 15:
                    errors[field] = "{} field must bet at least 15 characters".format(field.replace('_', ' '))               
        return errors

class Course(models.Model):
    course_name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = CourseManager()