from django.shortcuts import render, redirect
from .models import Attendance
from django.utils.timezone import now
import qrcode
from io import BytesIO
import base64

# Generate QR Code
def generate_qr():
   # qr = qrcode.make("http://0.0.0.0:8000/attendance/")
    qr = qrcode.make(f"http://192.168.29.208:8000/attendance/")
    buffer = BytesIO()
    qr.save(buffer, format="PNG")
    return base64.b64encode(buffer.getvalue()).decode()


import qrcode

local_ip = "192.168.29.208"  # Replace this with your actual local IP address
qr_url = f"http://192.168.29.208:8000/attendance/"

# Generate and save the QR code
qr = qrcode.make(qr_url)
qr.save("attendance_qr.png")  # Save as an image


# Display QR Code on Homepage
def home(request):
    qr_code = generate_qr()
    return render(request, 'home.html', {'qr_code': qr_code})

from django.shortcuts import render

#def home(request):
 #   return render(request, "home.html")  # Create home.html in templates


# Attendance Form Submission
'''def submit_attendance(request):
    if request.method == "POST":
        name = request.POST['name']
        roll_number = request.POST['roll_number']
        Attendance.objects.create(name=name, roll_number=roll_number, date=now().date())
        return redirect('success')

    return render(request, 'attendance_form.html')'''

from django.shortcuts import render, redirect
from .models import Attendance

def submit_attendance(request):
    if request.method == "POST":
        name = request.POST.get("name")
        roll_number = request.POST.get("roll_number")

        if name and roll_number:
            Attendance.objects.create(name=name, roll_number=roll_number)
            return redirect("attendance_list")  # Redirect to the attendance list page

    return render(request, "attendance_form.html")




# Success Page
def success(request):
    return render(request, 'success.html')

# Display Attendance Records
def attendance_list(request):
    records = Attendance.objects.all().order_by('-date')
    return render(request, 'attendance_list.html', {'records': records})


# Create your views here.
