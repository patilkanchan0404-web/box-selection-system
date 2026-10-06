from django.shortcuts import render
from .models import Product, Box

# Create your views here.

def home(request):
    products = Product.objects.all()
    boxes = Box.objects.all()

    selected_product = None
    recommended_box = None

    if request.method == 'POST':
        product_id = request.POST.get("product")

        if product_id:
            selected_product = Product.objects.get(id=product_id)

            suitable_boxes = []

            for box in boxes:

                dimensions_fit = (
                    box.length >= selected_product.length
                    and box.width >= selected_product.width
                    and box.height >= selected_product.height
                )

                weight_fit = ( 
                    box.max_weight >= selected_product.weight
                )

                if dimensions_fit and weight_fit:
                    suitable_boxes.append(box)

            if suitable_boxes:
                recommended_box = min(
                    suitable_boxes,
                    key=lambda box : box.cost
                )

    return render(
        request,
        "home.html",
        {
            "products": products,
            "selected_product": selected_product,
            "recommended_box": recommended_box,
        }
    )