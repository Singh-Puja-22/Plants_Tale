from django.shortcuts import redirect, render

from cart.models import CartItem
from app.models import Plant

# Create your views here.

def view_cart(request):
    template = "cart.html"
    cart_items = CartItem.objects.filter(user=request.user)
    for c in cart_items:
        c.sub_total = c.quantity * c.plant.price
    total_price = sum(item.plant.price * item.quantity for item in cart_items)
    return render(request, template, {'cart_items': cart_items, 'total_price': total_price})

def add_to_cart(request, plant_id):
    plant = Plant.objects.get(id=plant_id)
    cart_item, created = CartItem.objects.get_or_create(plant=plant, user=request.user)
    cart_item.quantity += 1
    cart_item.save()
    return redirect('cart:view_cart')

def remove_from_cart(request, item_id):
    cart_item = CartItem.objects.get(id=item_id)
    cart_item.delete()
    return redirect('cart:view_cart')