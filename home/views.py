from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Note
from django.db.utils import OperationalError
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout, get_user_model
from django.contrib.auth.decorators import login_required

# Simple session-based translations (not using Django i18n)
TRANSLATIONS = {
    'aze': {
        'welcome': 'Xoş gəlmisən,',
        'create': 'Yarat',
        'search': 'Axtar',
        'clear': 'Təmizlə',
        'logout': 'Logout',
        'edit': 'Dəyiş',
        'delete': 'Sil',
        'confirm_delete_title': 'Silmək istədiyinizə əminsiniz?',
        'yes': 'He',
        'no': 'Yox',
        'back': 'Geri',
        'no_records': 'Heç bir qeyd tapılmadı.',
        'login_title': 'Sayta giriş',
        'username_placeholder': 'İstifadəçi adı',
        'password_placeholder': 'Şifrə',
        'login_button': 'Daxil ol',
        'create_title': 'Yeni Qeyd Yarat',
        'edit_title': 'Qeydi Dəyiş'
    },
    'en': {
        'welcome': 'Welcome,',
        'create': 'Create',
        'search': 'Search',
        'clear': 'Clear',
        'logout': 'Logout',
        'edit': 'Edit',
        'delete': 'Delete',
        'confirm_delete_title': 'Are you sure you want to delete?',
        'yes': 'Yes',
        'no': 'No',
        'back': 'Back',
        'no_records': 'No records found.',
        'login_title': 'Login',
        'username_placeholder': 'Username',
        'password_placeholder': 'Password',
        'login_button': 'Sign in',
        'create_title': 'Create Note',
        'edit_title': 'Edit Note'
    },
    'ru': {
        'welcome': 'Добро пожаловать,',
        'create': 'Создать',
        'search': 'Поиск',
        'clear': 'Очистить',
        'logout': 'Выход',
        'edit': 'Изменить',
        'delete': 'Удалить',
        'confirm_delete_title': 'Вы уверены, что хотите удалить?',
        'yes': 'Да',
        'no': 'Нет',
        'back': 'Назад',
        'no_records': 'Записей не найдено.',
        'login_title': 'Вход',
        'username_placeholder': 'Имя пользователя',
        'password_placeholder': 'Пароль',
        'login_button': 'Войти',
        'create_title': 'Создать запись',
        'edit_title': 'Изменить запись'
    }
}

def get_translations(lang_code):
    return TRANSLATIONS.get(lang_code, TRANSLATIONS['aze'])

# Sadə index səhifəsi
def index(request):
    return HttpResponse("""
    <html>
    <head>
        <title>Sadə Sayt</title>
        <style>
            body {
                background-color: #a0d8f1;  /* Açıq mavi background */
                font-family: Arial, sans-serif;
                text-align: center;
                padding-top: 100px;
            }
            .giris {
                background-color: white;
                display: inline-block;
                padding: 30px 50px;
                border-radius: 15px;
                box-shadow: 0 0 20px rgba(0,0,0,0.2);
            }
            h1 { color: #004080; }
            p { color: #333; }
        </style>
    </head>
    <body>
        <div class="giris">
            <h1>Salam Bahram!</h1>
            <p>Saytına xoş gəlmisən 😊</p>
        </div>
    </body>
    </html>
    """)

# Login səhifəsi
def login_page(request):
    error = None
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            request.session['username'] = username
            return redirect('welcome')
        else:
            error = 'Invalid credentials'  # simple message; translated later if needed

    lang = request.session.get('lang', 'aze')
    t = get_translations(lang)
    return render(request, "home/login.html", {'lang': lang, 't': t, 'error': error})

# Welcome səhifəsi – username və notes table göstərir
def welcome(request):
    username = request.session.get('username', 'Qonaq')
    lang = request.session.get('lang', 'aze')
    t = get_translations(lang)

    # Search support: ?search_field=<first_name|last_name|note>&q=<query>
    search_field = request.GET.get('search_field')
    q = request.GET.get('q')

    # Pagination params
    try:
        per_page = int(request.GET.get('per_page', 10))
    except (TypeError, ValueError):
        per_page = 10

    try:
        page_number = int(request.GET.get('page', 1))
    except (TypeError, ValueError):
        page_number = 1

    try:
        notes = Note.objects.all()
    except OperationalError as e:
        # Database schema probably not migrated (created_at column missing etc.)
        notes = Note.objects.none()
        context = {
            'username': username,
            'notes': [],
            'page_obj': None,
            'paginator': None,
            'per_page': per_page,
            'per_page_options': [5,10,25,50],
            'search_field': search_field,
            'q': q,
            'lang': lang,
            't': t,
            'total_count': 0,
            'db_error': str(e),
        }
        return render(request, "home/welcome.html", context)
    allowed = ['first_name', 'last_name', 'note']
    if search_field in allowed and q:
        # case-insensitive contains search
        notes = notes.filter(**{f"{search_field}__icontains": q})

    # order by creation time (newest first)
    notes = notes.order_by('-created_at')

    # paginate
    from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
    paginator = Paginator(notes, per_page)
    try:
        page_obj = paginator.page(page_number)
    except PageNotAnInteger:
        page_obj = paginator.page(1)
    except EmptyPage:
        page_obj = paginator.page(paginator.num_pages)

    context = {
        'username': username,
        'notes': page_obj.object_list,
        'page_obj': page_obj,
        'paginator': paginator,
        'per_page': per_page,
        'per_page_options': [5,10,25,50],
        'search_field': search_field,
        'q': q,
        'lang': lang,
        't': t,
        'total_count': paginator.count,
    }

    # build a condensed page range for display (first 2, last 2, and window around current)
    current = page_obj.number
    last = paginator.num_pages
    display = []
    # always include first two
    for i in range(1, min(3, last+1)):
        display.append(i)

    # left gap
    if current - 2 > 3:
        display.append('...')
    # window around current
    for i in range(max(3, current-2), min(last-1, current+2)+1):
        if i not in display:
            display.append(i)

    # right gap
    if current + 2 < last-2:
        display.append('...')

    # always include last two
    for i in range(max( max(3, last-1), len(display)>0 and display[-1] + 1 or 3 ), last+1):
        if i not in display:
            display.append(i)

    context['page_range_display'] = display

    return render(request, "home/welcome.html", context)

# mövcud welcome view-in altında əlavə et
def logout_view(request):
    request.session.flush()  # sessiyanı təmizləyir
    return redirect('login')  # əsas login səhifəsinə yönləndir

from django.shortcuts import render, redirect, get_object_or_404
from .models import Note

def delete_note(request, id):
    note = get_object_or_404(Note, id=id)
    note.delete()
    return redirect("welcome")


def change_language(request, lang):
    # simple session-based language switch
    if lang in TRANSLATIONS:
        request.session['lang'] = lang
    # redirect back to the page the user was on (next param or referer)
    next_url = request.GET.get('next') or request.META.get('HTTP_REFERER') or '/welcome/'
    return redirect(next_url)


def edit_note(request, id):
    note = get_object_or_404(Note, id=id)
    lang = request.session.get('lang', 'aze')
    t = get_translations(lang)

    if request.method == "POST":
        note.first_name = request.POST.get("first_name")
        note.last_name = request.POST.get("last_name")
        note.note = request.POST.get("note")
        note.save()
        return redirect("welcome")

    return render(request, "home/edit_note.html", {"note": note, 'lang': lang, 't': t})


def create_note(request):
    lang = request.session.get('lang', 'aze')
    t = get_translations(lang)

    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        note_text = request.POST.get('note')
        if first_name and last_name and note_text:
            Note.objects.create(first_name=first_name, last_name=last_name, note=note_text)
            return redirect('welcome')

    return render(request, "home/create_note.html", {'lang': lang, 't': t})


def users_list(request):
    User = get_user_model()
    users = User.objects.all().order_by('id')
    return render(request, 'home/users.html', {'users': users})


def create_user(request):
    User = get_user_model()
    error = None
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if not username or not password:
            error = 'Username and password are required.'
        else:
            if User.objects.filter(username=username).exists():
                error = 'Username already exists.'
            else:
                User.objects.create_user(username=username, password=password)
                return redirect('users_list')

    return render(request, 'home/create_user.html', {'error': error})


def edit_user(request, id):
    User = get_user_model()
    user = get_object_or_404(User, id=id)
    error = None
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        is_staff = True if request.POST.get('is_staff') == 'on' else False
        if not username:
            error = 'Username required.'
        else:
            # check uniqueness
            if User.objects.exclude(id=user.id).filter(username=username).exists():
                error = 'Username already taken.'
            else:
                user.username = username
                user.is_staff = is_staff
                if password:
                    user.set_password(password)
                user.save()
                return redirect('users_list')

    return render(request, 'home/edit_user.html', {'user_obj': user, 'error': error})


def delete_user(request, id):
    from django.views.decorators.http import require_POST
    # accept POST only
    if request.method != 'POST':
        return redirect('users_list')
    User = get_user_model()
    user = get_object_or_404(User, id=id)
    # do not allow deleting superuser or self (basic safety)
    try:
        if request.user.is_authenticated and request.user.id == user.id:
            # cannot delete self via UI
            return redirect('users_list')
    except Exception:
        pass
    user.delete()
    return redirect('users_list')