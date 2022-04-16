from django.urls import path

from . import views

urlpatterns = [
	path("", views.index, name="index"),
	path("account/signup/", views.signup, name="signup"),
	path("account/signin/", views.signin, name="signin"),
	path("account/logout/", views.logout_view, name="logout"),
	path("dashboard/", views.dashboard, name="dashboard"),
	path("brands/", views.brands, name="brand"),
	path("brands/list/", views.brand_list, name="brand-list"),
	path("brand/create/", views.create_brand, name="create-brand"),
	path("brand/<id>/edit/", views.edit_brand, name="edit-brand"),
	path("brand/<id>/remove/", views.remove_brand, name="brand_delete"),
	path("categories/", views.categories, name="categories"),
	path("categories/list/", views.categories_list, name="categories-list"),
	path("categories/create/", views.create_categories, name="create-categories"),
	path("categories/<id>/remove/", views.remove_categories, name="remove-categories"),
	path("orders/", views.orders, name="orders"),
	path("report/", views.report, name="report"),
	path("products/", views.products, name="products"),
	path("products/list/", views.products_list, name="products-list"),
	path("products/create/", views.create_product, name="create-product"),
]