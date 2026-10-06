from django.shortcuts import render
from django.http import JsonResponse
from django.views.generic import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from json import loads


@method_decorator(csrf_exempt, name='dispatch')
class AdditionView(View):
    def post(self, request):
        request_body = request.body
        # print(request_body)
        form_data = loads(request_body)  # convert json to dict
        n1 = form_data.get('num1')
        n2 = form_data.get('num2')
        total = n1 + n2

        result = {
            "Sum": total
        }
        return JsonResponse(result)


@method_decorator(csrf_exempt, name='dispatch')
class SubstractionView(View):
    def post(self, request):
        data = request.body
        form_data = loads(data)
        n1 = form_data.get('num1')
        n2 = form_data.get('num2')
        diff = n1 - n2
        result = {
            'Difference': diff
        }
        return JsonResponse(result)


@method_decorator(csrf_exempt, name='dispatch')
class MultiplicationView(View):
    def post(self, request):
        data = request.body
        form_data = loads(data)
        n1 = form_data.get('num1')
        n2 = form_data.get('num2')
        product = n1 * n2
        result = {
            'Product': product
        }
        return JsonResponse(result)


@method_decorator(csrf_exempt, name='dispatch')
class DivisionView(View):
    def post(self, request):
        data = request.body
        form_data = loads(data)
        n1 = form_data.get('num1')
        n2 = form_data.get("num2")
        quotient = n1 / n2
        result = {
            'Quotient': quotient
        }
        return JsonResponse(result)


@method_decorator(csrf_exempt, name='dispatch')
class ModulusView(View):
    def post(self, request):
        data = request.body
        form_data = loads(data)
        n1 = form_data.get('num1')
        n2 = form_data.get("num2")
        remainder = n1 % n2
        result = {
            "Remainder": remainder
        }
        return JsonResponse(result)


@method_decorator(csrf_exempt, name='dispatch')
class PercentageView(View):
    def post(self, request):
        data = request.body
        form_data = loads(data)
        obtained = form_data.get('obtained')
        total = form_data.get('total')
        percentage = (obtained / total) * 100

        result = {
            "Percentage": percentage
        }
        return JsonResponse(result)


@method_decorator(csrf_exempt, name='dispatch')
class BMIView(View):
    def post(self, request):
        data = request.body
        form_data = loads(data)
        weight = form_data.get('weight')
        height = form_data.get('height')
        bmi = weight / ((height / 100) ** 2)
        result = {
            "BMI": bmi
        }
        return JsonResponse(result)


@method_decorator(csrf_exempt, name='dispatch')
class AreaView(View):
    def post(self, request):
        data = request.body
        form_data = loads(data)
        l = form_data.get('length')
        b = form_data.get('breadth')
        area = l * b
        result = {
            "Area": area
        }
        return JsonResponse(result)


@method_decorator(csrf_exempt, name='dispatch')
class AgeView(View):
    def post(self, request):
        data = request.body
        form_data = loads(data)
        b = form_data.get('birth_year')
        c = form_data.get('current_year')
        age = c - b
        res = {
            "Age": age
        }
        return JsonResponse(res)


@method_decorator(csrf_exempt, name='dispatch')
class InterestView(View):
    def post(self, request):
        data = request.body
        form_data = loads(data)
        p = form_data.get('principal')
        r = form_data.get('rate')
        t = form_data.get('time')
        interest = (p * r * t) / 100
        res = {
            "principal": p,
            "rate": r,
            "time": t,
            "Simple Interest": interest,
        }
        return JsonResponse(res)


@method_decorator(csrf_exempt, name='dispatch')
class ElectricityView(View):
    def post(self, request):
        data = request.body
        form_data = loads(data)
        u = form_data.get("unit")
        r = form_data.get("rate")
        bill = u * r
        res = {
            "Electricity Bill": bill
        }
        return JsonResponse(res)

@method_decorator(csrf_exempt, name='dispatch')
class FactorialView(View):
    def post(self, request):
        data = request.body
        form_data = loads(data)
        n = form_data.get("num")

        fact = 1
        for i in range(1, n + 1):
            fact *= i

        res = {
            "Factorial": fact
        }
        return JsonResponse(res)


@method_decorator(csrf_exempt, name='dispatch')
class ArmstrongView(View):
    def post(self, request):
        data = request.body
        form_data = loads(data)
        n = form_data.get("num")

        temp = n
        sum = 0
        l = len(str(n))
        while temp > 0:
            d = temp % 10
            sum += d ** l
            temp //= 10

        if n == sum:
            res = {
                "Armstrong": True
            }
        else:
            res = {
                "Armstrong": False
            }

        return JsonResponse(res)


@method_decorator(csrf_exempt, name="dispatch")
class ProfitView(View):
    def post(self, request):
        data = request.body
        form_data = loads(data)
        cp = form_data.get("cost_price")
        sp = form_data.get("selling_price")
        q = form_data.get("quantity")

        total_c = cp * q
        total_s = sp * q
        profit = total_s - total_c

        result = {
            "Cost Price": cp,
            "Selling Price": sp,
            "Quantity": q,
            "Total Cost": total_c,
            "Total Sales": total_s,
            "Profit": profit
        }
        return JsonResponse(result)


@method_decorator(csrf_exempt, name="dispatch")
class SalaryView(View):
    def post(self, request):
        data = request.body
        form_data = loads(data)
        h_worked = form_data.get("hours_worked")
        regular_h = form_data.get("regular_hours")
        h_rate = form_data.get("hourly_rate")
        overtime_rate = form_data.get("overtime_rate")

        regular_pay = regular_h * h_rate
        overtime_h = h_worked - regular_h
        overtime_pay = overtime_h * overtime_rate
        total_salary = regular_pay + overtime_pay

        result = {
            "Hours Worked": h_worked,
            "Regular Hours": regular_h,
            "Hourly Rate": h_rate,
            "Overtime Rate": overtime_rate,
            "Regular Pay": regular_pay,
            "Overtime Hours": overtime_h,
            "Overtime Pay": overtime_pay,
            "Total Salary": total_salary
        }
        return JsonResponse(result)


@method_decorator(csrf_exempt, name='dispatch')
class AgeInUnitsView(View):
    def post(self, request):
        data = request.body
        form_data = loads(data)
        age = form_data.get("age")

        months = age * 12
        weeks = age * 52
        days = age * 365

        res = {
            "Age": age,
            "Months": months,
            "Weeks": weeks,
            "Days": days
        }
        return JsonResponse(res)