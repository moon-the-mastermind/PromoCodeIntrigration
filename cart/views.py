
from django.shortcuts import render
from django.http import JsonResponse

PROMO_CODES = {"ostad10": 0.10, "ostad5": 0.05, "moon" : 50, "moonthemastermind" : 100 }

def checkout(request):
    cart_total = request.session.get('cart_total', 100)
    discount = request.session.get('discount', 0)
    final_total = cart_total - discount
    return render(request, 'cart/checkout.html', {
        'cart_total': cart_total,
        'discount': discount,
        'final_total': final_total,
        'year': 2025
    })

def apply_promo(request):
    if request.method == "POST":
        import json
        data = json.loads(request.body)
        code = data.get("code", "").strip()
        cart_total = request.session.get("cart_total", 100)
        used_codes = request.session.get("used_codes", [])

        if code in used_codes:
            return JsonResponse({"error": "This promo code has already been used."})
        if code in PROMO_CODES:
            discount = cart_total * PROMO_CODES[code]
            final_total = cart_total - discount
            used_codes.append(code)
            request.session["used_codes"] = used_codes
            request.session["discount"] = discount
            return JsonResponse({"discount": discount, "final_total": final_total})
        return JsonResponse({"error": "Invalid promo code."})
    
    return JsonResponse({"message": "Please use POST to apply a promo code."})
