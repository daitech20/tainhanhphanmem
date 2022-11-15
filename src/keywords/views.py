from django.shortcuts import render
from django.views import View, generic
from .models import Program, DataTable, IpAddressUser
from .forms import CodeForm
from projects.models import Project
from easy_timezones.utils import get_ip_address_from_request, is_valid_ip, is_local_ip
# Create your views here.

class Index(View):
    def get(self, request):
        data = {
            'program': Program.objects.all()
        }
        return render(request, 'core/index.html', data)

def get_ip_address_from_request(request):
    """ Makes the best attempt to get the client's real IP or return the loopback """
    PRIVATE_IPS_PREFIX = ('10.', '172.', '192.', '127.')
    ip_address = ''
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR', '')
    if x_forwarded_for and ',' not in x_forwarded_for:
        if not x_forwarded_for.startswith(PRIVATE_IPS_PREFIX) and is_valid_ip(x_forwarded_for):
            ip_address = x_forwarded_for.strip()
    else:
        ips = [ip.strip() for ip in x_forwarded_for.split(',')]
        for ip in ips:
            if ip.startswith(PRIVATE_IPS_PREFIX):
                continue
            elif not is_valid_ip(ip):
                continue
            else:
                ip_address = ip
                break
    if not ip_address:
        x_real_ip = request.META.get('HTTP_X_REAL_IP', '')
        if x_real_ip:
            if not x_real_ip.startswith(PRIVATE_IPS_PREFIX) and is_valid_ip(x_real_ip):
                ip_address = x_real_ip.strip()
    if not ip_address:
        remote_addr = request.META.get('REMOTE_ADDR', '')
        if remote_addr:
            if not remote_addr.startswith(PRIVATE_IPS_PREFIX) and is_valid_ip(remote_addr):
                ip_address = remote_addr.strip()
    if not ip_address:
        ip_address = '127.0.0.1'
    return ip_address

class DetailProgram(View):
    def get(self, request, slug):

        ip = get_ip_address_from_request(self.request)
        user = IpAddressUser.objects.filter(ip=ip)
        if not user:
            user = IpAddressUser.objects.create(ip=ip, access=True)
        else:
            user = user[0]

        c = CodeForm()

        try:
            projects = Project.objects.all()
            project_of_program = []

            for pj in projects:
                programs = pj.programs.all()
                for pg in programs:
                    if pg.slug == slug:
                        project_of_program.append(pj)
                        break

            keywords = []
            if project_of_program != None:
                for pj in project_of_program:
                    for keyword in pj.keywords.filter(status=1):
                        keywords.append(keyword)


            def myFunc(e):
                return e.prioritize

            data_table_all = list(keywords)
            data_table_all.sort(key=myFunc)

            print(data_table_all)

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
            print('false')

        data = {
            'program': Program.objects.get(slug=slug),
            'f': c,
            'data_table': data_table,
            'user': user,
        }
        return render(request, 'core/detail.html', data)

    def post(self, request, slug):

        ip = get_ip_address_from_request(self.request)
        user = IpAddressUser.objects.filter(ip=ip)
        if not user:
            user = IpAddressUser.objects.create(ip=ip, access=True)
        else:
            user = user[0]
        user.entered_password = True
        user.save()
        c = CodeForm(request.POST)
        code = ''
        if c.is_valid():
            code = c.cleaned_data['code']
        else:
            print("loi")

        data = {'f': c, 'program': Program.objects.get(slug=slug), 'check': False}
        
        keyword_id = request.GET.get('props')
        
        try:
            data_table = DataTable.objects.filter(id=keyword_id, code=code)[0]

            if data_table != None:
                data['check'] = True
                if (user.access == True):
                    data_table.hits += 1
                    data_table.hits_today += 1
                    data_table.prioritize_quantity_temp += 1
                    data_table.save()
                    user.access = False
                    user.save()
        except:
            print("code error")
            data['notifi'] = 'Pass sai rồi, vui lòng làm theo hướng dẫn!!!'

        try:
            projects = Project.objects.all()
            project_of_program = []

            for pj in projects:
                programs = pj.programs.all()
                for pg in programs:
                    if pg.slug == slug:
                        project_of_program.append(pj)
                        break

            keywords = []
            if project_of_program != None:
                for pj in project_of_program:
                    for keyword in pj.keywords.filter(status=1):
                        keywords.append(keyword)

            def myFunc(e):
                return e.prioritize

            data_table_all = list(keywords)
            data_table_all.sort(key=myFunc)

            # print(data_table_all)

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
        data['f'] = CodeForm()
        data['user'] = user
        return render(request, 'core/detail.html', data)


# HTTP Error 400
def bad_request(request, exception):
    return render(request, '400.html', {})

def handler404(request, exception):
    return render(request, '404.html', {})

def handler500(request):
    return render(request, '500.html')

