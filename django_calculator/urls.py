"""
URL configuration for django_calculator project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from calculatorApp.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('addition/', AdditionView.as_view()),
    path('substraction/', SubstractionView.as_view()),
    path('multiplication/', MultiplicationView.as_view()),
    path('division/', DivisionView.as_view()),
    path('modulus/', ModulusView.as_view()),
    path('percentage/', PercentageView.as_view()),
    path('bmi/', BMIView.as_view()),
    path('area/', AreaView.as_view()),
    path('age/', AgeView.as_view()),
    path('simple-interest/', InterestView.as_view()),
    path('electricity-bill/', ElectricityView.as_view()),
    path('factorial/', FactorialView.as_view()),
    path('armstrong/', ArmstrongView.as_view()),
    path('product-profit/', ProfitView.as_view()),
    path('work-salary/', SalaryView.as_view()),
    path('age-in-units/', AgeInUnitsView.as_view())
]
