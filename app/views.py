from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.template.loader import render_to_string
from django.views.decorators.csrf import csrf_exempt
from .models import Brand, Category, Product

# Create your views here.

@login_required(login_url="/account/signin/")
def index(request):
	return render(request, "index.html", {})


def signup(request):
	if request.method == "POST":
		if request.POST.get("pwd1") == request.POST.get("pwd2"):
			print(request.POST.get("pwd1"))
			user = User.objects.create(
				username=request.POST.get("username")
			)
			user.set_password(request.POST.get("pwd1"))
			user.save()
			return redirect("/account/signin/")
		else:
			return redirect("/account/signup/")
	return render(request, "signup.html", {})


def signin(request):
	if request.method == "POST":
		pass
		user = authenticate(request, username=request.POST.get("username"), password=request.POST.get("password"))
		if user:
			login(request, user)
			return redirect("/dashboard/")
		else:
			messages.error(request, "Username or password error!")
			return redirect("/account/signin/")
	return render(request, "login.html", {})


def logout_view(request):
	logout(request)
	return redirect("/account/signin/")


@login_required(login_url="/account/signin/")
def dashboard(request):
	return render(request, "dashboard.html", {})

@csrf_exempt
@login_required(login_url="/account/signin/")
def products(request):
	return render(request, "product.html", {})

@login_required(login_url="/account/signin/")
def categories(request):
	return render(request, "categories.html", {})

def categories_list(request):
	categories_lists = Category.objects.all()
	html = render_to_string('modules/tables_categories.html', {"categories": categories_lists})
	return JsonResponse({"message": "Ok", "html": html})

@csrf_exempt
def create_product(request):
	data = dict()
	if request.method == "GET":
		categories_lists = Category.objects.all()
		brands_lists = Brand.objects.all()
		data['html'] = render_to_string('modules/add_product.html', {"categories": categories_lists, "brands": brands_lists})
	else:
		print(request.FILES)
		Product.objects.create(
			name=request.POST["name"],
			brand=Brand.objects.get(id=request.POST["brand"]),
			category=Category.objects.get(id=request.POST["category"]),
			code=request.POST["code"],
			quantity=request.POST["quantity"],
			rate=request.POST["rate"],
			status=request.POST["status"],
		)
		products_lists = Product.objects.all()
		data['html'] = render_to_string('modules/tables_products.html', {"products": products_lists})
	return JsonResponse(data)

@csrf_exempt
def products_list(request):
	products_lists = Product.objects.all()
	html = render_to_string('modules/tables_products.html', {"products": products_lists})
	return JsonResponse({"message": "Ok", "html": html})

@login_required(login_url="/account/signin/")
def orders(request):
	return render(request, "orders.html", {})


@login_required(login_url="/account/signin/")
def report(request):
	return render(request, "report.html", {})

@csrf_exempt
def create_brand(request):
	data = dict()
	brand_name = request.POST.get("brandName")
	brand_status = request.POST.get("brandStatus")
	Brand.objects.create(name=brand_name, status=brand_status)
	brands_list = Brand.objects.all()
	data['html'] = render_to_string('modules/tables.html', {"brands": brands_list})
	return JsonResponse(data)

@csrf_exempt
def create_categories(request):
	data = dict()
	category_name = request.POST.get("categoryName")
	category_status = request.POST.get("categoryStatus")
	Category.objects.create(name=category_name, status=category_status)
	categories_lists = Category.objects.all()
	data['html'] = render_to_string('modules/tables_categories.html', {"categories": categories_lists})
	return JsonResponse(data)

@csrf_exempt
def remove_categories(request, id):
	data = dict()
	category = Category.objects.get(id=id)
	category.delete()
	categories_lists = Brand.objects.all()
	data['html'] = render_to_string('modules/tables_categories.html', {"categories": categories_lists})
	return JsonResponse(data)

@csrf_exempt
def edit_brand(request, id):
	data = dict()
	brand_name = Brand.objects.get(id=id)
	if request.method == "GET":
		data['html'] = render_to_string('modules/edit.html', {"brand": brand_name})
	else:
		brand_name.name = request.POST["brandName"]
		brand_name.status = request.POST["brandStatus"]
		brand_name.save()
		brands_list = Brand.objects.all()
		data['html'] = render_to_string('modules/tables.html', {"brands": brands_list})
	return JsonResponse(data)

@csrf_exempt
def remove_brand(request, id):
	data = dict()
	brand = Brand.objects.get(id=id)
	brand.delete()
	brands_list = Brand.objects.all()
	data['html'] = render_to_string('modules/tables.html', {"brands": brands_list})

	return JsonResponse(data)

@login_required(login_url="/account/signin/")
def brand_list(request):
	brands_list = Brand.objects.all()
	html = render_to_string('modules/tables.html', {"brands": brands_list})
	return JsonResponse({"message": "Ok", "html": html})

@csrf_exempt
@login_required(login_url="/account/signin/")
def brands(request):
	return render(request, "brand.html", {})

