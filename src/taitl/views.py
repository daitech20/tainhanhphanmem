from django.shortcuts import render
from django.views import View, generic
from .models import Program, DataTable
from .forms import CodeForm
from django.template import RequestContext
# Create your views here.

class Index(View):
    def get(self, request):
        data = {
            'program': Program.objects.all()
        }
        return render(request, 'core/index.html', data)


class DetailProgram(View):
    def get(self, request, slug):
        c = CodeForm()
        # try:
        #     data_table = DataTable.objects.filter(prioritize=1)[0]
        # except:
        #     data_table = False

        try:
            def myFunc(e):
                return e.prioritize
            data_table_all = list(DataTable.objects.all())
            data_table_all.sort(key=myFunc)

            if data_table_all[-1].prioritize_quantity <= data_table_all[-1].prioritize_quantity_temp:
                for i in range(0, len(data_table_all)):
                    data_table_all[i].prioritize_quantity_temp = 0
                    data_table_all[i].save()

            for i in range(0, len(data_table_all)):
                if data_table_all[i].prioritize_quantity > data_table_all[i].prioritize_quantity_temp:
                    break
            data_table = data_table_all[i]
        except:
            data_table = False

        data = {
            'program': Program.objects.get(slug=slug),
            'f': c,
            'data_table': data_table,
        }
        return render(request, 'core/detail.html', data)

    def post(self, request, slug):
        c = CodeForm(request.POST)
        code = ''
        if c.is_valid():
            code = c.cleaned_data['code']
        else:
            print("loi")

        # try:
        #     data_table = DataTable.objects.filter(prioritize=1)[0]
        # except:
        #     data_table = False
        data = {'f': c, 'program': Program.objects.get(slug=slug), 'check': False}

        try:
            data_table = DataTable.objects.filter(code=code)[0]
            if data_table != None:
                data['check'] = True
                data_table.hits += 1
                data_table.hits_today += 1
                data_table.prioritize_quantity_temp += 1
                data_table.save()
        except:
            print("code error")
            data['notifi'] = 'Pass sai rồi, vui lòng làm theo hướng dẫn!!!'
	    print(data['notifi'])
        data_table = False
        try:
            def myFunc(e):
                return e.prioritize
            data_table_all = list(DataTable.objects.all())
            data_table_all.sort(key=myFunc)

            if data_table_all[-1].prioritize_quantity <= data_table_all[-1].prioritize_quantity_temp:
                for i in range(0, len(data_table_all)):
                    data_table_all[i].prioritize_quantity_temp = 0
                    data_table_all[i].save()

            for i in range(0, len(data_table_all)):
                if data_table_all[i].prioritize_quantity > data_table_all[i].prioritize_quantity_temp:
                    break
            data_table = data_table_all[i]

        except:
            data_table = False

        data['data_table'] = data_table
        return render(request, 'core/detail.html', data)


# HTTP Error 400
def bad_request(request, exception):
    return render(request, '400.html', {})

def handler404(request, exception):
    return render(request, '404.html', {})

def handler500(request):
    return render(request, '500.html')

