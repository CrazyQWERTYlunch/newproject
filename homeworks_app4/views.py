from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.db import transaction
from django.forms import ValidationError

from homeworks_app3.models import Order, Product, OrderItem
from homeworks_app4.forms import CreateOrderForm, ClientLoginForm
