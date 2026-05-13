from django.urls import path 
from . import views

app_name = 'mediampesa' #namespace 


urlpatterns = [
    # reveals the index page with the payment form to the user : this is the page where the user will input their phone number and the amount they want to pay and then submit the form to trigger the stk push process
    path('', views.index, name='index'),
    # this is the endpoint that we will use to trigger the stk push process : this is where we will accept the post data from the form and then send the request to mpesa to trigger the stk push on the users phone : this is also the endpoint that we will use to create the initial transaction record in our db with pending status before we even send the request to mpesa : this is because we want to capture the transaction details and also have a reference for the transaction on our db to update once we receive the result from mpesa on our callback url
    path('stk-push/', views.stk_push, name='stk_push'),
    # this is the page that we will show to the user while they are waiting for the result of the transaction from mpesa : this is where we will use javascript to poll our backend every few seconds to check the status of the transaction and then update the page accordingly : this is also where we will show a loading spinner to indicate to the user that we are waiting for the result from mpesa and also to prevent the user from refreshing the page or navigating away while we are waiting for the result from mpesa : this is also where we will show a message to the user to check their phone and complete the payment process on their phone : this is important because the user might not know that they need to check their phone and complete the payment process on their phone and they might just wait on the page without doing anything and then wonder why they are not seeing any updates on the page : this is also where we will show a message to the user to check their phone and complete the payment process on their phone : this is important because the user might not know that they need to check their phone and complete the payment process on their phone and they might just wait on the page without doing anything and then wonder why they are not seeing any updates on the page   
    path('waiting/<int:transaction_id>/', views.waiting_page, name='waiting_page'),
    # to read the results of transaction from mpesa servers
    path('callback/', views.callback, name='callback'),
    # update in real time current status of transaction on waiting page
    path('check-status/<int:transaction_id>/', views.check_status, name='check_status'),
    # load the appropriate route according to status of transaction : this is where we will redirect the user once we receive the result from mpesa on our callback url : this is also where we will show a message to the user to check their phone and complete the payment process on their phone : this is important because the user might not know that they need to check their phone and complete the payment process on their phone and they might just wait on the page without doing anything and then wonder why they are not seeing any updates on the page : this is also where we will show a message to the user to check their phone and complete the payment process on their phone : this is important because the user might not know that they need to check their phone and complete the payment process on their phone and they might just wait on the page without doing anything and then wonder why they are not seeing any updates on the page      
    path('payment-success/',views.payment_success, name='payment_success'),
    path('payment-failed/', views.payment_failed, name='payment_failed'),
    path('payment-cancelled', views.payment_cancelled, name='payment_cancelled'),
]