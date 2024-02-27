from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .forms import EmailPhoneForm
import pandas as pd

def check_data_in_excel(email, phone_number):
    excel_file_path = 'register/seleted_people_demo_info_table.xlsx'
    df = pd.read_excel(excel_file_path)

    phone_number = str(phone_number).strip()

    # Adjust the comparison to handle the leading zero in the Excel file
    row_exists = (df['Email'].str.strip() == email.strip()) & (df['phone_number'].astype(str).str.strip().str.lstrip('0') == phone_number.lstrip('0'))
    return row_exists.any()


def registry_view(request):
    if request.method == 'POST':
        form = EmailPhoneForm(request.POST)

        if form.is_valid():
            email = form.cleaned_data['email']
            phone_number = form.cleaned_data['phone_number']

            if check_data_in_excel(email, phone_number):
                return redirect('https://live.blogishclub.com/rooms/nkt-k3s-egt-1ah/join/')  # Replace 'redirect()' with your actual URL name
            else:
                form.add_error(None, "No matching data found for the provided email and phone number.")
    else:
        form = EmailPhoneForm()

    return render(request, 'register_template.html', {'form': form})
