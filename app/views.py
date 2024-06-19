

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from .models import Category,Product,Cart,Ahuthors,Client
from django.contrib.auth import authenticate, login,logout
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from .forms import LoginForm, RegisterForm,RegisterAdminForm,UpdateUserForm,CreateBooks
from django.contrib.auth.mixins import LoginRequiredMixin
from .permissonmixin import AdminRequiredMixin,SellerRequiredMixin
from .models import User
from django.db.models import Q




# Create your views here.
def index(request):
    count = Cart.objects.count()
    products = Product.objects.filter(in_stock=True)
    categorys = Category.objects.all()
    
    return render (request,'index.html', context={"products": products, 'count':count,'cats':categorys})

def category_books(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    products = category.products.all()
    return render(request, 'index.html', {'products': products,'category':category})

def ShowBooks(request):
    products = Product.objects.all()
    return render(request,'dashboard.html')


def author(request):
    authors=Ahuthors.objects.all()
    
    return render (request,'index.html', context={"authors" : authors})

class ProductCartView(View):
    def get(self, request, product_id):
        product = get_object_or_404(Product, id=product_id)
        count = Cart.objects.count()
        return render(request, 'batafsil.html', {'product':product,'count':count})
    
    def post(self, request, product_id):
        product =get_object_or_404(Product,id=product_id)
        quantity = int(request.POST['cart'])
        if Cart.objects.filter(product=product).exists():
            cart = Cart.objects.filter(product=product).first()
            cart.quantity +=quantity
            cart.save()
        else:
            cart=Cart()
            cart.product=product
            cart.quantity = quantity
            cart.save()
        return redirect('index')       

def add_cart(request):
    cart = Cart.objects.all()
    categorys = Category.objects.all()
    count = Cart.objects.count()
    return render(request, 'cart.html', {'cart': cart, 'categorys':categorys,'count':count})


class LoginView(View):
    def get(self, request):
        form = LoginForm()
        return render(request, 'login.html', {'form': form})

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')

        form = LoginForm()
        return render(request, 'login.html', {'form': form})

class RegisterView(View):

    def get(self, request):
        form = RegisterForm()
        return render(request, 'register.html', {'form': form})

    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

            if user.user_role == 'student':
                new_student = Client()
                new_student.user = user
                new_student.save()

            return redirect('login')
        return render(request, 'register.html', {'form': form})
    
class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('index')



class ProfileView(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, 'profile.html')

def Users(request):
    users = User.objects.all()
    return render(request,'dashboard.html',{'users':users})



def delete(request, id):
    delet = get_object_or_404(User, id=id)
    delet.delete()
    return redirect('dashboard')


class RegisterAdminView(View):

    def get(self, request):
        form = RegisterForm()
        return render(request, 'admin_register.html', {'form': form})

    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

            if user.user_role == 'student':
                new_student = Client()
                new_student.user = user
                new_student.save()

            return redirect('login')
        return render(request, 'admin_register.html', {'form': form})
    
class UpdateUserView(AdminRequiredMixin, View):
    def get(self, request, id):
        user = get_object_or_404(User, id=id)
        form = UpdateUserForm(instance=user)  
        return render(request, 'create.html', { 'form': form})
        

    def post(self, request, id):
        user = get_object_or_404(User, id=id)
        form = UpdateUserForm(request.POST, request.FILES, instance=user)
        if form.is_valid():

            form.save()
            return redirect('dashboard')
        return render(request, 'create.html', {'form': form})
    

class Create(View):
    def get(self, request):
        form = CreateBooks()
        return render(request, 'create.html', {'form': form})

    def post(self, request):
        form = CreateBooks(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')  
        return render(request, 'create.html', {'form': form})

    


def deleteBook(request, id):
    delet = get_object_or_404(Product, id=id)
    delet.delete()
    return redirect('index')

def deleteCart(request, id):
    delet = get_object_or_404(Cart, id=id)
    delet.delete()
    return redirect('index')

