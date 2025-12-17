from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages


# =========================
# الصفحة الشخصية / الرئيسية
# =========================
def profile(request):
    return render(request, "home.html")


# =========================
# إنشاء حساب
# =========================
def register(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")

        if User.objects.filter(username=username).exists():
            messages.error(request, "اسم المستخدم موجود بالفعل")
        else:
            User.objects.create_user(
                username=username,
                email=email,
                password=password
            )
            messages.success(request, "تم إنشاء الحساب بنجاح، يمكنك تسجيل الدخول الآن")
            return redirect("accounts:login")

    return render(request, "accounts/register.html")


# =========================
# تسجيل الدخول
# =========================
def user_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("accounts:profile")

        messages.error(request, "اسم المستخدم أو كلمة المرور غير صحيحة")

    return render(request, "accounts/login.html")


# =========================
# تسجيل الخروج
# =========================
def user_logout(request):
    logout(request)
    return redirect("/")


# =========================
# فيو جديد
# =========================
def dashboard(request):
    return render(request, "dashboard.html")
