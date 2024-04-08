import time, logging
from django.shortcuts import redirect, render
from django.contrib import messages

from App.validators import validate_avatar
from .models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.password_validation import validate_password
from django.core.validators import validate_email
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ValidationError

logger = logging.getLogger(__name__)


# Create your views here.
# --- authorization views ---
def signup_view(request):
    if request.user.is_authenticated:
        return redirect("home_page")

    if request.method == "POST":

        email = request.POST.get("email")
        password = request.POST.get("password")
        fullname = request.POST.get("fullname")

        hasEmailAndPassword = fullname and email and password
        emailAlreadyTaken = User.objects.filter(email=email).exists()
        try:
            valid_email = validate_email(email)
            valid_email = True
        except ValidationError as e:
            valid_email = False
            valid_email_error = e.messages[0]

        try:
            validate_password(password)
            valid_password = True
        except ValidationError as e:
            valid_password = False
            valid_password_error = e.messages[0]

        if not hasEmailAndPassword:
            messages.add_message(
                request,
                messages.WARNING,
                f"Please fill in the form properly.",
                extra_tags=f"{time.time()}",
            )
            return redirect("signup_page")

        elif not valid_email:
            messages.error(
                request,
                valid_email_error,
                extra_tags=f"{time.time()}",
            )
            return redirect("signup_page")

        elif emailAlreadyTaken:
            messages.error(
                request,
                f"The 'Email' address already exists.",
                extra_tags=f"{time.time()}",
            )
            return redirect("signup_page")

        elif not valid_password:
            messages.error(
                request,
                valid_password_error,
                extra_tags=f"{time.time()}",
            )
            return redirect("signup_page")

        else:
            user = User.objects.create_user(
                fullname=fullname, email=email, password=password
            )
            user.save()

            authenticated_user = authenticate(request, email=email, password=password)

            if authenticated_user is not None:
                login(request, authenticated_user)
                messages.success(
                    request,
                    f"The user creation was successful.",
                    extra_tags=f"{time.time()}",
                )
                return redirect("dashboard_overview_page")

            else:
                messages.success(
                    request,
                    "Failed to authenticate user after signup, please try to login manually.",
                    extra_tags=f"{time.time()}",
                )
                return redirect("login_page")

    context = {"active": "register", "navigateTo": "login"}
    return render(request, "pages/signup.html", context)


def login_view(request):
    if request.user.is_authenticated:
        return redirect("home_page")

    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")

        if not email or not password:
            messages.warning(
                request,
                f"Please fill in the form properly.",
                extra_tags=f"{time.time()}",
            )
            return redirect("login_page")

        if not User.objects.filter(email=email).exists():
            messages.error(
                request,
                "The user with this 'Email' address doesn't exists.",
                extra_tags=f"{time.time()}",
            )
            return redirect("login_page")

        user = authenticate(request, email=email, password=password)

        if not user is None:
            login(request, user)
            messages.success(
                request,
                f"Welcome back, `{user.fullname}`. Your log in was successful.",
                extra_tags=f"{time.time()}",
            )
            return redirect("dashboard_overview_page")

        elif user is None:
            messages.error(
                request,
                f"Invalid credentials. Please try again.",
                extra_tags=f"{time.time()}",
            )
            return redirect("login_page")

        elif not user.is_active:
            messages.error(
                request,
                f"The user account is not active. Please contact support..",
                extra_tags=f"{time.time()}",
            )
            return redirect("login_page")

        else:
            messages.error(
                request,
                f"Failed to login. Please try again.",
                extra_tags=f"{time.time()}",
            )
            return redirect("login_page")

    context = {"active": "login", "navigateTo": "signup"}
    return render(request, "pages/login.html", context)


@login_required(login_url="/login")
def logout_view(request):
    logout(request)
    return redirect("login_page")


# --- view to delete user account
@login_required(login_url="/login")
def delete_account_view(request, pk):
    if request.method == "GET":
        try:
            user = User.objects.get(uniqueId=pk)
            if user:
                user.delete()
                logout(request)
                return redirect("login_page")
        except User.DoesNotExist:
            messages.error(
                request,
                f"User with uniqueId '{pk}' doesn't exists.",
                extra_tags=f"{time.time()}",
            )
            logout(request)
            return redirect("login_page")

    messages.error(
        request,
        "Method not allowed except 'GET'.",
        extra_tags=f"{time.time()}",
    )
    return redirect(
        f"{request.META['HTTP_REFERER']}#danger"
    )  # redirect to previous path


# --- authenticated views --------------------------------------------------------------------------


# --- dashboard_overview_view ---
@login_required(login_url="/login")
def dashboard_overview_view(request):
    context = {"active": "overview"}
    return render(request, "pages/dashboard/overview.html", context)


# --- dashboard_activity_view ---
@login_required(login_url="/login")
def dashboard_activity_view(request):
    context = {"active": "activity"}
    return render(request, "pages/dashboard/activity.html", context)


# --- dashboard_usage_view ---
@login_required(login_url="/login")
def dashboard_usage_view(request):
    context = {"active": "usage"}
    return render(request, "pages/dashboard/usage.html", context)


# --- dashboard_settings_view ---
@login_required(login_url="/login")
def dashboard_settings_view(request):
    context = {"active": "settings"}
    return render(request, "pages/dashboard/settings.html", context)


# --- dashboard_notifications_view ---
@login_required(login_url="/login")
def dashboard_notifications_view(request):
    context = {"active": "notifications"}
    return render(request, "pages/dashboard/notifications.html", context)


# --- account_settings_view ---
@login_required(login_url="/login")
def account_settings_view(request):
    sectionIds = [
        "general",
        "danger",
    ]
    context = {"active": "account", "sectionIds": sectionIds}
    return render(request, "pages/user_account/account.html", context)


# --- account_details_edit_view ---
@login_required(login_url="/login")
def account_details_edit_view(request):
    if request.method == "POST":
        formType = request.POST.get("formType")

        if formType == "avatar":
            avatar = request.FILES["avatar"]
            # print(" avatar :: ============================================= :: ", avatar)
            if avatar:
                try:
                    validate_avatar(avatar)
                    request.user.image = avatar
                    request.user.save()
                    messages.success(
                        request,
                        f"The user's 'Avatar' has been updated.",
                        extra_tags=f"{time.time()}",
                    )
                    return redirect(request.META["HTTP_REFERER"])

                except ValidationError as e:
                    messages.error(
                        request,
                        e.messages[0],
                        extra_tags=f"{time.time()}",
                    )
                    return redirect(request.META["HTTP_REFERER"])

        if formType == "name":
            fullname = request.POST.get("fullname")
            if fullname:
                request.user.fullname = fullname
                request.user.save()
                messages.success(
                    request,
                    f"The user's 'Fullname' has been updated.",
                    extra_tags=f"{time.time()}",
                )
                return redirect(request.META["HTTP_REFERER"])

        if formType == "email":
            email = request.POST.get("email")
            if email:
                if not User.objects.filter(email=email).exists():
                    try:
                        validate_email(email)
                        request.user.email = email
                        request.user.save()
                        logout(request)
                        messages.success(
                            request,
                            f"The 'Email' has been updated. Please log in again with the new email address.",
                            extra_tags=f"{time.time()}",
                        )
                        return redirect(request.META["HTTP_REFERER"])
                    except ValidationError as e:
                        messages.error(
                            request,
                            e.messages[0],
                            extra_tags=f"{time.time()}",
                        )
                        return redirect(request.META["HTTP_REFERER"])
                else:
                    messages.error(
                        request,
                        "The user with this 'Email' address already exists.",
                        extra_tags=f"{time.time()}",
                    )
                    return redirect(request.META["HTTP_REFERER"])

        elif formType == "password":
            oldPassword = request.POST.get("oldPassword")
            newPassword = request.POST.get("newPassword")
            if not (oldPassword) or not (newPassword):
                messages.warning(
                    request,
                    f"Please fill in the 'Old password' and 'New Password' field properly.",
                    extra_tags=f"{time.time()}",
                )
                return redirect(request.META["HTTP_REFERER"])

            elif oldPassword and newPassword:
                isOldPasswordValid = request.user.check_password(oldPassword)

                if isOldPasswordValid:
                    try:
                        validate_password(newPassword)
                        request.user.set_password(newPassword)
                        request.user.save()
                        messages.success(
                            request,
                            f"The 'Password' has been updated. Please log in again with the new password.",
                            extra_tags=f"{time.time()}",
                        )
                        return redirect(request.META["HTTP_REFERER"])
                    except ValidationError as e:
                        messages.error(
                            request,
                            e.messages[0],
                            extra_tags=f"{time.time()}",
                        )
                        return redirect(request.META["HTTP_REFERER"])
                else:
                    messages.error(
                        request,
                        f"Old password is incorrect.",
                        extra_tags=f"{time.time()}",
                    )
                    return redirect(request.META["HTTP_REFERER"])

    messages.info(
        request,
        f"Method not allowed except 'POST'.",
        extra_tags=f"{time.time()}",
    )
    return redirect(request.META["HTTP_REFERER"])


# --- base views ---
def home_view(request):
    context = {"active": "home"}
    return render(request, "pages/home.html", context)


def services_view(request):
    context = {"active": "services"}
    return render(request, "pages/services.html", context)


def contact_view(request):
    context = {"active": "contact"}
    return render(request, "pages/contact.html", context)


def about_view(request):
    context = {"active": "about"}
    return render(request, "pages/about.html", context)
