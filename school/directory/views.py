import os
import csv
import io
from django.shortcuts import render, reverse, redirect
from django.contrib import messages
from django.views.generic import ListView, View
from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import TeacherModel, ProPic, PhoneModel, SubjectModel
from django.forms import inlineformset_factory
from .forms import TeacherForm, PhoneForm, SubjectForm, ProPicForm, ImporterForm


class DirectoryListView(ListView):
    model = TeacherModel
    template_name = 'directory/allTeachers.html'
    context_object_name = 'teachers_list'
    paginate_by = 5


class TeacherDetailView(DetailView):
    model = TeacherModel
    context_object_name = "teacher_info"
    template_name = "directory/teacherInfo.html"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        pk = self.kwargs.get('pk')
        context["teacher_phone"] = PhoneModel.objects.get(teacher__id=pk)
        context["teacher_subject"] = ','.join(
            list(SubjectModel.objects.get(
                teacher__id=pk).subject))
        context["teacher_propic"] = ProPic.objects.get(teacher__id=pk)

        return context


class AddTeacherBulkView(LoginRequiredMixin, View):
    login_url = '/login/'

    def post(self, request):
        BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        pic_path = os.path.join(BASE_DIR, 'teachers')
        error_flag = 0

        form = ImporterForm(request.POST, request.FILES)

        if form.is_valid():
            csvfile = request.FILES['filename'].read().decode('utf-8')
            io_string = io.StringIO(csvfile)
            line_num = 0
            for line in csv.DictReader(io_string):
                line_num += 1
                if line["First Name"].strip() == '':
                    break

                d = {}
                d["fname"] = line["First Name"]
                d["lname"] = line["Last Name"]
                d["propic"] = line["Profile picture"]
                d["pic_path"] = os.path.join(pic_path, line["Profile picture"])
                d["email"] = line["Email Address"]
                d["phone_number"] = line["Phone Number"]
                d["room_number"] = line["Room Number"]
                subs = line["Subjects taught"]
                subs_list = subs.strip().split(',')
                subs_list_titlize = [x.strip().title() for x in subs_list]
                d["subject"] = ['Mathematics' if x.lower() == 'maths' else x for x in subs_list_titlize]


                teacher_form = TeacherForm(d)
                phone_form = PhoneForm(d)
                subject_form = SubjectForm(d)
                pro_pic_form = ProPicForm(d)

                if teacher_form.is_valid() and phone_form.is_valid() and subject_form.is_valid():
                    teacher = teacher_form.save()

                    ph_f = phone_form.save(commit=False)
                    ph_f.teacher_id=teacher.id
                    ph_f.save()

                    s_f = subject_form.save(commit=False)
                    s_f.teacher_id=teacher.id
                    s_f.save()

                    p_pic = ProPic(teacher_id=teacher.id)
                    if os.path.isfile(d["pic_path"]):
                        p_pic.propic.save(d["propic"], open(d["pic_path"], 'rb'))
                    else:
                        p_pic.propic = 'pro-pics/placeholder.jpeg'
                        p_pic.save()
                else:
                    error_flag = 1
                    messages.add_message(request, messages.ERROR, "Line Number: %s - %s%s%s" % (
                        line_num,
                        teacher_form.errors,
                        phone_form.errors,
                        subject_form.errors))

            if not error_flag:
                messages.add_message(request, messages.SUCCESS, 'Bulk Upload Success.')

            return redirect(reverse('add-teacher'))
        else:
            return render(request, 'directory/addTeacher.html', {
                'teacherForm': TeacherForm,
                'phoneForm': PhoneForm,
                'subjectForm': SubjectForm,
                'proPicForm': ProPicForm,
                'ImporterForm': form
            })


class AddTeacherView(LoginRequiredMixin, View):
    login_url = '/login/'

    def get(self, request):
        return render(request, 'directory/addTeacher.html', {
            'teacherForm': TeacherForm,
            'phoneForm': PhoneForm,
            'subjectForm': SubjectForm,
            'proPicForm': ProPicForm,
            'ImporterForm': ImporterForm
        })

    def post(self, request):
        teacher_form = TeacherForm(request.POST)
        phone_form = PhoneForm(request.POST)
        subject_form = SubjectForm(request.POST)
        pro_pic_form = ProPicForm(request.POST, request.FILES)

        if teacher_form.is_valid() and phone_form.is_valid() and subject_form.is_valid() and pro_pic_form.is_valid():

            teacher = teacher_form.save()

            ph_f = phone_form.save(commit=False)
            ph_f.teacher_id=teacher.id
            ph_f.save()

            s_f = subject_form.save(commit=False)
            s_f.teacher_id=teacher.id
            s_f.save()

            pp_f = pro_pic_form.save(commit=False)
            pp_f.teacher_id=teacher.id
            pp_f.save()

            messages.add_message(request, messages.SUCCESS, 'Teacher info added successfully.')

            return redirect(reverse('add-teacher'))
        else:
            messages.add_message(request, messages.ERROR, 'Error in submission')
            return render(request, 'directory/addTeacher.html', {
                'teacherForm': teacher_form,
                'phoneForm': phone_form,
                'subjectForm': subject_form,
                'proPicForm': pro_pic_form
            })
