def categories(request):
    from shop.models import Category
    return {'categories': Category.objects.all()}