from django.shortcuts import render, redirect
from .models import KYC, Account
from .forms import KYCForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required


#@login_required
def account(request):

    if request.user.is_authenticated:
        try:
            kyc = KYC.objects.get(user=request.user)
        except:
            messages.warning(request, "You need to submit your kyc")
            print('aqui')
            return redirect('kyc-reg')
    else:
        messages.warning(request, "You need to Login to access the dashboard")
        return redirect('sign-in')
    
    account = Account.objects.get(user=request.user)
    context = {
        'kyc':kyc,
        'account': account
    }
    return render(request, 'account/account.html', context)

def dashboard(request):
    return render(request, 'account/dashboard.html')

@login_required
def kyc_registration(request):
    user = request.user
    account =Account.objects.get(user=user)

    try:
        kyc = KYC.objects.get(user=user)
    except:
        kyc = None

    if request.method == 'POST':
        form = KYCForm(request.POST, request.FILES, instance=kyc)
        if form.is_valid():
            new_form = form.save(commit=False)
            new_form.user = user
            new_form.account = account
            new_form.save()
            messages.success(request, "KYC Form submitted successfully, In review now")
            return redirect('account')
        
    else:
        form = KYCForm(instance=kyc)


    context = {
        'account': account,
        'form': form,
        'kyc':kyc,
    }
    return render(request, 'account/kyc-form.html', context)

