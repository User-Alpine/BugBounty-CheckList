#python3.9

import tkinter as tk
from tkinter.constants import RIGHT, VERTICAL
from tkinter import ttk
root = tk.Tk()
root.geometry("750x500")

# Create a Main Frame
frame = tk.Frame(root)
frame.pack(fill=tk.BOTH, expand=1)
# Create A Canvas
canvas  = tk.Canvas(frame)
canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)

#Scrolling commmand
scrollbar = ttk.Scrollbar(frame, orient=VERTICAL, command = canvas.yview)
scrollbar.pack(side=RIGHT, fill=tk.Y)

# Configure The Canvas
canvas.configure(yscrollcommand=scrollbar.set)
canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

# Second frame
Second_Frame = tk.Frame(canvas)

# Add that new frame to a window in the canvas
canvas.create_window((0,0), window=Second_Frame, anchor="nw")

w = tk.Label(Second_Frame, text ='BugBounty Check List', font = "50") 
w.grid(column=2, row=0)

# Column Names

Vulnerability_Name = tk.Label(Second_Frame, text="Vulnerability-Name", font=('Helvetica', 15,'bold'))
Vulnerability_Name.grid(column=1, row=1)

Vulnerable = tk.Label(Second_Frame, text="Vulnerable",font=('Helvetica', 15,'bold'))
Vulnerable.grid(column=2, row=1)

Not_Vulnerable = tk.Label(Second_Frame, text="Not-Vulnerable",font=('Helvetica', 15,'bold'))
Not_Vulnerable.grid(column=3, row=1)

# Vulnerability_Names
Vuln1 = tk.Label(Second_Frame, text="Unrestricted File Upload", font=('Helvetica', 10,'bold')).grid(column=1, row=2)
Vuln2 = tk.Label(Second_Frame, text="SQL injection", font=('Helvetica',10,'bold')).grid(column=1, row=3)
Vuln3 = tk.Label(Second_Frame, text="Account Takeover", font=('Helvetica',10,'bold')).grid(column=1, row=4)
Vuln4 = tk.Label(Second_Frame, text="IDOR", font=('Helvetica',10,'bold')).grid(column=1, row=5)
Vuln5 = tk.Label(Second_Frame, text="CSRF", font=('Helvetica',10,'bold')).grid(column=1, row=6)
Vuln6 = tk.Label(Second_Frame, text="Auth Bypass", font=('Helvetica',10,'bold')).grid(column=1, row=7)
Vuln7 = tk.Label(Second_Frame, text="Stored XSS", font=('Helvetica',10,'bold')).grid(column=1, row=8)
Vuln8 = tk.Label(Second_Frame, text="Reflected XSS", font=('Helvetica',10,'bold')).grid(column=1, row=9)
Vuln9 = tk.Label(Second_Frame, text="No Rate Limit", font=('Helvetica',10,'bold')).grid(column=1, row=10)
Vuln10 = tk.Label(Second_Frame, text="OTP Bypass", font=('Helvetica',10,'bold')).grid(column=1, row=11)
Vuln11 = tk.Label(Second_Frame, text="Open Redirection", font=('Helvetica',10,'bold')).grid(column=1, row=12)
Vuln12 = tk.Label(Second_Frame, text="User Enumeration", font=('Helvetica',10,'bold')).grid(column=1, row=13)
Vuln13 = tk.Label(Second_Frame, text="Session Fixation", font=('Helvetica',10,'bold')).grid(column=1, row=14)
Vuln14 = tk.Label(Second_Frame, text="Sensitive Information Discoluser", font=('Helvetica',10,'bold')).grid(column=1, row=15)
Vuln15 = tk.Label(Second_Frame, text="Security Misconfig", font=('Helvetica',10,'bold')).grid(column=1, row=16)
Vuln16 = tk.Label(Second_Frame, text="Sensitive Date Exposure", font=('Helvetica',10,'bold')).grid(column=1, row=17)
Vuln17 = tk.Label(Second_Frame, text="Session Does Not Timeout", font=('Helvetica',10,'bold')).grid(column=1, row=18)
Vuln18 = tk.Label(Second_Frame, text="Security Headers Missing", font=('Helvetica',10,'bold')).grid(column=1, row=19)
Vuln19 = tk.Label(Second_Frame, text="Improper Cache Management", font=('Helvetica',10,'bold')).grid(column=1, row=20)
Vuln20 = tk.Label(Second_Frame, text="Host Header Injection", font=('Helvetica',10,'bold')).grid(column=1, row=21)
Vuln21 = tk.Label(Second_Frame, text="HTML Injection", font=('Helvetica',10,'bold')).grid(column=1, row=22)
Vuln22 = tk.Label(Second_Frame, text="Improper Input Validation", font=('Helvetica',10,'bold')).grid(column=1, row=23)
Vuln23 = tk.Label(Second_Frame, text="ClickJacking", font=('Helvetica',10,'bold')).grid(column=1, row=24)
Vuln24 = tk.Label(Second_Frame, text="No Captcha Implementation", font=('Helvetica',10,'bold')).grid(column=1, row=25)
Vuln25 = tk.Label(Second_Frame, text="No Account Lockout Policy", font=('Helvetica',10,'bold')).grid(column=1, row=26)
Vuln26 = tk.Label(Second_Frame, text="Cookie Without HttpOnly Flag Set", font=('Helvetica',10,'bold')).grid(column=1, row=27)
Vuln27 = tk.Label(Second_Frame, text="Cookie Without Secure Flag Set", font=('Helvetica',10,'bold')).grid(column=1, row=28)
Vuln28 = tk.Label(Second_Frame, text="Password Auto-Complete Feature Enable", font=('Helvetica',10,'bold')).grid(column=1, row=29)
Vuln29 = tk.Label(Second_Frame, text="Auto Complete Feature is Enabled", font=('Helvetica',10,'bold')).grid(column=1, row=30)
Vuln30 = tk.Label(Second_Frame, text="Banner Grabbing", font=('Helvetica',10,'bold')).grid(column=1, row=31)
Vuln31 = tk.Label(Second_Frame, text="Weak Password Policy", font=('Helvetica',10,'bold')).grid(column=1, row=32)
Vuln32 = tk.Label(Second_Frame, text="OPTIONS Method is Enabled", font=('Helvetica',10,'bold')).grid(column=1, row=33)
Vuln33 = tk.Label(Second_Frame, text="Directory Listing Enabled", font=('Helvetica',10,'bold')).grid(column=1, row=34)
Vuln34 = tk.Label(Second_Frame, text="Improper Session Management on Password Change", font=('Helvetica',10,'bold')).grid(column=1, row=35)
Vuln35 = tk.Label(Second_Frame, text="CSP(Content Security Policy)", font=('Helvetica',10,'bold')).grid(column=1, row=36)
Vuln36 = tk.Label(Second_Frame, text="Weak Cryptographic", font=('Helvetica',10,'bold')).grid(column=1, row=37)
Vuln37 = tk.Label(Second_Frame, text="Unencrypted_VIEWSTATE Parameter only in ASP.NET", font=('Helvetica',10,'bold')).grid(column=1, row=38)
Vuln38 = tk.Label(Second_Frame, text="Password Field Submitted using GET method", font=('Helvetica',10,'bold')).grid(column=1, row=39)
Vuln39 = tk.Label(Second_Frame, text="Microsoft ASP.NET Debugging Enabled", font=('Helvetica',10,'bold')).grid(column=1, row=40)
Vuln40 = tk.Label(Second_Frame, text="Improper Session Validation", font=('Helvetica',10,'bold')).grid(column=1, row=41)
Vuln41 = tk.Label(Second_Frame, text="Vertical Priv-Esc Through Sessionid", font=('Helvetica',10,'bold')).grid(column=1, row=42)
Vuln42 = tk.Label(Second_Frame, text="Bussion Logic Flaws", font=('Helvetica',10,'bold')).grid(column=1, row=43)
Vuln43 = tk.Label(Second_Frame, text="Broken Access Control", font=('Helvetica',10,'bold')).grid(column=1, row=44)
Vuln44 = tk.Label(Second_Frame, text="Broken Authentication and Session Management", font=('Helvetica',10,'bold')).grid(column=1, row=45)


# Check_Box
Checkbutton1= tk.IntVar()  
Checkbutton2= tk.IntVar()  
Checkbutton3= tk.IntVar()  
Checkbutton4= tk.IntVar()  
Checkbutton5= tk.IntVar()  
Checkbutton6= tk.IntVar()  
Checkbutton7= tk.IntVar()  
Checkbutton8= tk.IntVar()  
Checkbutton9= tk.IntVar()  
Checkbutton10= tk.IntVar()  
Checkbutton11= tk.IntVar()  
Checkbutton12= tk.IntVar()  
Checkbutton13= tk.IntVar()  
Checkbutton14= tk.IntVar()  
Checkbutton15= tk.IntVar()  
Checkbutton16= tk.IntVar()  
Checkbutton17= tk.IntVar()  
Checkbutton18= tk.IntVar()  
Checkbutton19= tk.IntVar()  
Checkbutton20= tk.IntVar()  
Checkbutton21= tk.IntVar()  
Checkbutton22= tk.IntVar()  
Checkbutton23= tk.IntVar()  
Checkbutton24= tk.IntVar()  
Checkbutton25= tk.IntVar()  
Checkbutton26= tk.IntVar()  
Checkbutton27= tk.IntVar()  
Checkbutton28= tk.IntVar()  
Checkbutton29= tk.IntVar()  
Checkbutton30= tk.IntVar()  
Checkbutton31= tk.IntVar()  
Checkbutton32= tk.IntVar()  
Checkbutton33= tk.IntVar()  
Checkbutton34= tk.IntVar()  
Checkbutton35= tk.IntVar()  
Checkbutton36= tk.IntVar()  
Checkbutton37= tk.IntVar()  
Checkbutton38= tk.IntVar()  
Checkbutton39= tk.IntVar()  
Checkbutton40= tk.IntVar()  
Checkbutton41= tk.IntVar()  
Checkbutton42= tk.IntVar()  
Checkbutton43= tk.IntVar()  
Checkbutton44= tk.IntVar()


CheckbuttonSecond1= tk.IntVar()  
CheckbuttonSecond2= tk.IntVar()  
CheckbuttonSecond3= tk.IntVar()  
CheckbuttonSecond4= tk.IntVar()  
CheckbuttonSecond5= tk.IntVar()  
CheckbuttonSecond6= tk.IntVar()  
CheckbuttonSecond7= tk.IntVar()  
CheckbuttonSecond8= tk.IntVar()  
CheckbuttonSecond9= tk.IntVar()  
CheckbuttonSecond10= tk.IntVar()  
CheckbuttonSecond11= tk.IntVar()  
CheckbuttonSecond12= tk.IntVar()  
CheckbuttonSecond13= tk.IntVar()  
CheckbuttonSecond14= tk.IntVar()  
CheckbuttonSecond15= tk.IntVar()  
CheckbuttonSecond16= tk.IntVar()  
CheckbuttonSecond17= tk.IntVar()  
CheckbuttonSecond18= tk.IntVar()  
CheckbuttonSecond19= tk.IntVar()  
CheckbuttonSecond20= tk.IntVar()  
CheckbuttonSecond21= tk.IntVar()  
CheckbuttonSecond22= tk.IntVar()  
CheckbuttonSecond23= tk.IntVar()  
CheckbuttonSecond24= tk.IntVar()  
CheckbuttonSecond25= tk.IntVar()  
CheckbuttonSecond26= tk.IntVar()  
CheckbuttonSecond27= tk.IntVar()  
CheckbuttonSecond28= tk.IntVar()  
CheckbuttonSecond29= tk.IntVar()  
CheckbuttonSecond30= tk.IntVar()  
CheckbuttonSecond31= tk.IntVar()  
CheckbuttonSecond32= tk.IntVar()  
CheckbuttonSecond33= tk.IntVar()  
CheckbuttonSecond34= tk.IntVar()  
CheckbuttonSecond35= tk.IntVar()  
CheckbuttonSecond36= tk.IntVar()  
CheckbuttonSecond37= tk.IntVar()  
CheckbuttonSecond38= tk.IntVar()  
CheckbuttonSecond39= tk.IntVar()  
CheckbuttonSecond40= tk.IntVar()  
CheckbuttonSecond41= tk.IntVar()  
CheckbuttonSecond42= tk.IntVar()  
CheckbuttonSecond43= tk.IntVar()  
CheckbuttonSecond44= tk.IntVar() 


C1 = tk.Checkbutton(Second_Frame, text="", variable= Checkbutton1, onvalue=1, offvalue=0, height=1, width=1).grid(column=2, row=2)
C2 = tk.Checkbutton(Second_Frame, text="", variable= Checkbutton2, onvalue=1, offvalue=0, height=1, width=1).grid(column=2, row=3)
C3 = tk.Checkbutton(Second_Frame, text="", variable= Checkbutton3, onvalue=1, offvalue=0, height=1, width=1).grid(column=2, row=4)
C4 = tk.Checkbutton(Second_Frame, text="", variable= Checkbutton4, onvalue=1, offvalue=0, height=1, width=1).grid(column=2, row=5)
C5 = tk.Checkbutton(Second_Frame, text="", variable= Checkbutton5, onvalue=1, offvalue=0, height=1, width=1).grid(column=2, row=6)
C6 = tk.Checkbutton(Second_Frame, text="", variable= Checkbutton6, onvalue=1, offvalue=0, height=1, width=1).grid(column=2, row=7)
C7 = tk.Checkbutton(Second_Frame, text="", variable= Checkbutton7, onvalue=1, offvalue=0, height=1, width=1).grid(column=2, row=8)
C8 = tk.Checkbutton(Second_Frame, text="", variable= Checkbutton8, onvalue=1, offvalue=0, height=1, width=1).grid(column=2, row=9)
C9 = tk.Checkbutton(Second_Frame, text="", variable= Checkbutton9, onvalue=1, offvalue=0, height=1, width=1).grid(column=2, row=10)
C10 = tk.Checkbutton(Second_Frame, text="", variable= Checkbutton10, onvalue=1, offvalue=0, height=1, width=1).grid(column=2, row=11)
C11 = tk.Checkbutton(Second_Frame, text="", variable= Checkbutton11, onvalue=1, offvalue=0, height=1, width=1).grid(column=2, row=12)
C12 = tk.Checkbutton(Second_Frame, text="", variable= Checkbutton12, onvalue=1, offvalue=0, height=1, width=1).grid(column=2, row=13)
C13 = tk.Checkbutton(Second_Frame, text="", variable= Checkbutton13, onvalue=1, offvalue=0, height=1, width=1).grid(column=2, row=14)
C14 = tk.Checkbutton(Second_Frame, text="", variable= Checkbutton14, onvalue=1, offvalue=0, height=1, width=1).grid(column=2, row=15)
C15 = tk.Checkbutton(Second_Frame, text="", variable= Checkbutton15, onvalue=1, offvalue=0, height=1, width=1).grid(column=2, row=16)
C16 = tk.Checkbutton(Second_Frame, text="", variable= Checkbutton16, onvalue=1, offvalue=0, height=1, width=1).grid(column=2, row=17)
C17 = tk.Checkbutton(Second_Frame, text="", variable= Checkbutton17, onvalue=1, offvalue=0, height=1, width=1).grid(column=2, row=18)
C18 = tk.Checkbutton(Second_Frame, text="", variable= Checkbutton18, onvalue=1, offvalue=0, height=1, width=1).grid(column=2, row=19)
C19 = tk.Checkbutton(Second_Frame, text="", variable=Checkbutton19, onvalue=1, offvalue=0, height=1, width=1).grid(column=2, row=45)
C20 = tk.Checkbutton(Second_Frame, text="", variable= Checkbutton19, onvalue=1, offvalue=0, height=1, width=1).grid(column=2, row=20)
C21 = tk.Checkbutton(Second_Frame, text="", variable= Checkbutton20, onvalue=1, offvalue=0, height=1, width=1).grid(column=2, row=21)
C22 = tk.Checkbutton(Second_Frame, text="", variable= Checkbutton21, onvalue=1, offvalue=0, height=1, width=1).grid(column=2, row=22)
C23 = tk.Checkbutton(Second_Frame, text="", variable= Checkbutton22, onvalue=1, offvalue=0, height=1, width=1).grid(column=2, row=23)
C24 = tk.Checkbutton(Second_Frame, text="", variable= Checkbutton23, onvalue=1, offvalue=0, height=1, width=1).grid(column=2, row=24)
C25 = tk.Checkbutton(Second_Frame, text="", variable= Checkbutton24, onvalue=1, offvalue=0, height=1, width=1).grid(column=2, row=25)
C26 = tk.Checkbutton(Second_Frame, text="", variable= Checkbutton25, onvalue=1, offvalue=0, height=1, width=1).grid(column=2, row=26)
C27 = tk.Checkbutton(Second_Frame, text="", variable= Checkbutton26, onvalue=1, offvalue=0, height=1, width=1).grid(column=2, row=27)
C28 = tk.Checkbutton(Second_Frame, text="", variable= Checkbutton27, onvalue=1, offvalue=0, height=1, width=1).grid(column=2, row=28)
C29 = tk.Checkbutton(Second_Frame, text="", variable= Checkbutton28, onvalue=1, offvalue=0, height=1, width=1).grid(column=2, row=29)
C30 = tk.Checkbutton(Second_Frame, text="", variable= Checkbutton29, onvalue=1, offvalue=0, height=1, width=1).grid(column=2, row=30)
C31 = tk.Checkbutton(Second_Frame, text="", variable= Checkbutton30, onvalue=1, offvalue=0, height=1, width=1).grid(column=2, row=31)
C32 = tk.Checkbutton(Second_Frame, text="", variable= Checkbutton31, onvalue=1, offvalue=0, height=1, width=1).grid(column=2, row=32)
C33 = tk.Checkbutton(Second_Frame, text="", variable= Checkbutton32, onvalue=1, offvalue=0, height=1, width=1).grid(column=2, row=33)
C34 = tk.Checkbutton(Second_Frame, text="", variable= Checkbutton33, onvalue=1, offvalue=0, height=1, width=1).grid(column=2, row=34)
C35 = tk.Checkbutton(Second_Frame, text="", variable= Checkbutton34, onvalue=1, offvalue=0, height=1, width=1).grid(column=2, row=35)
C36 = tk.Checkbutton(Second_Frame, text="", variable= Checkbutton35, onvalue=1, offvalue=0, height=1, width=1).grid(column=2, row=36)
C37 = tk.Checkbutton(Second_Frame, text="", variable= Checkbutton36, onvalue=1, offvalue=0, height=1, width=1).grid(column=2, row=37)
C38 = tk.Checkbutton(Second_Frame, text="", variable= Checkbutton37, onvalue=1, offvalue=0, height=1, width=1).grid(column=2, row=38)
C39 = tk.Checkbutton(Second_Frame, text="", variable= Checkbutton38, onvalue=1, offvalue=0, height=1, width=1).grid(column=2, row=39)
C40 = tk.Checkbutton(Second_Frame, text="", variable= Checkbutton39, onvalue=1, offvalue=0, height=1, width=1).grid(column=2, row=40)
C41 = tk.Checkbutton(Second_Frame, text="", variable= Checkbutton40, onvalue=1, offvalue=0, height=1, width=1).grid(column=2, row=41)
C42 = tk.Checkbutton(Second_Frame, text="", variable= Checkbutton41, onvalue=1, offvalue=0, height=1, width=1).grid(column=2, row=42)
C43 = tk.Checkbutton(Second_Frame, text="", variable= Checkbutton42, onvalue=1, offvalue=0, height=1, width=1).grid(column=2, row=43)
C44 = tk.Checkbutton(Second_Frame, text="", variable= Checkbutton43, onvalue=1, offvalue=0, height=1, width=1).grid(column=2, row=44)

#Third Column
CSecond1 = tk.Checkbutton(Second_Frame, text="", variable= CheckbuttonSecond1, onvalue=1, offvalue=0, height=1, width=1).grid(column=3, row=2)
CSecond2 = tk.Checkbutton(Second_Frame, text="", variable= CheckbuttonSecond2, onvalue=1, offvalue=0, height=1, width=1).grid(column=3, row=3)
CSecond3 = tk.Checkbutton(Second_Frame, text="", variable= CheckbuttonSecond3, onvalue=1, offvalue=0, height=1, width=1).grid(column=3, row=4)
CSecond4 = tk.Checkbutton(Second_Frame, text="", variable= CheckbuttonSecond4, onvalue=1, offvalue=0, height=1, width=1).grid(column=3, row=5)
CSecond5 = tk.Checkbutton(Second_Frame, text="", variable= CheckbuttonSecond5, onvalue=1, offvalue=0, height=1, width=1).grid(column=3, row=6)
CSecond6 = tk.Checkbutton(Second_Frame, text="", variable= CheckbuttonSecond6, onvalue=1, offvalue=0, height=1, width=1).grid(column=3, row=7)
CSecond7 = tk.Checkbutton(Second_Frame, text="", variable= CheckbuttonSecond7, onvalue=1, offvalue=0, height=1, width=1).grid(column=3, row=8)
CSecond8 = tk.Checkbutton(Second_Frame, text="", variable= CheckbuttonSecond8, onvalue=1, offvalue=0, height=1, width=1).grid(column=3, row=9)
CSecond9 = tk.Checkbutton(Second_Frame, text="", variable= CheckbuttonSecond9, onvalue=1, offvalue=0, height=1, width=1).grid(column=3, row=10)
CSecond10 = tk.Checkbutton(Second_Frame, text="", variable=CheckbuttonSecond10, onvalue=1, offvalue=0, height=1, width=1).grid(column=3, row=11)
CSecond11 = tk.Checkbutton(Second_Frame, text="", variable=CheckbuttonSecond11, onvalue=1, offvalue=0, height=1, width=1).grid(column=3, row=12)
CSecond12 = tk.Checkbutton(Second_Frame, text="", variable=CheckbuttonSecond12, onvalue=1, offvalue=0, height=1, width=1).grid(column=3, row=13)
CSecond13 = tk.Checkbutton(Second_Frame, text="", variable=CheckbuttonSecond13, onvalue=1, offvalue=0, height=1, width=1).grid(column=3, row=14)
CSecond14 = tk.Checkbutton(Second_Frame, text="", variable=CheckbuttonSecond14, onvalue=1, offvalue=0, height=1, width=1).grid(column=3, row=15)
CSecond15 = tk.Checkbutton(Second_Frame, text="", variable=CheckbuttonSecond15, onvalue=1, offvalue=0, height=1, width=1).grid(column=3, row=16)
CSecond16 = tk.Checkbutton(Second_Frame, text="", variable=CheckbuttonSecond16, onvalue=1, offvalue=0, height=1, width=1).grid(column=3, row=17)
CSecond17 = tk.Checkbutton(Second_Frame, text="", variable=CheckbuttonSecond17, onvalue=1, offvalue=0, height=1, width=1).grid(column=3, row=18)
CSecond18 = tk.Checkbutton(Second_Frame, text="", variable=CheckbuttonSecond18, onvalue=1, offvalue=0, height=1, width=1).grid(column=3, row=19)
CSecond19 = tk.Checkbutton(Second_Frame, text="", variable=CheckbuttonSecond9, onvalue=1, offvalue=0, height=1, width=1).grid(column=3, row=45)
CSecond20 = tk.Checkbutton(Second_Frame, text="", variable=CheckbuttonSecond19, onvalue=1, offvalue=0, height=1, width=1).grid(column=3, row=20)
CSecond21 = tk.Checkbutton(Second_Frame, text="", variable=CheckbuttonSecond20, onvalue=1, offvalue=0, height=1, width=1).grid(column=3, row=21)
CSecond22 = tk.Checkbutton(Second_Frame, text="", variable=CheckbuttonSecond21, onvalue=1, offvalue=0, height=1, width=1).grid(column=3, row=22)
CSecond23 = tk.Checkbutton(Second_Frame, text="", variable=CheckbuttonSecond22, onvalue=1, offvalue=0, height=1, width=1).grid(column=3, row=23)
CSecond24 = tk.Checkbutton(Second_Frame, text="", variable=CheckbuttonSecond23, onvalue=1, offvalue=0, height=1, width=1).grid(column=3, row=24)
CSecond25 = tk.Checkbutton(Second_Frame, text="", variable=CheckbuttonSecond24, onvalue=1, offvalue=0, height=1, width=1).grid(column=3, row=25)
CSecond26 = tk.Checkbutton(Second_Frame, text="", variable=CheckbuttonSecond25, onvalue=1, offvalue=0, height=1, width=1).grid(column=3, row=26)
CSecond27 = tk.Checkbutton(Second_Frame, text="", variable=CheckbuttonSecond26, onvalue=1, offvalue=0, height=1, width=1).grid(column=3, row=27)
CSecond28 = tk.Checkbutton(Second_Frame, text="", variable=CheckbuttonSecond27, onvalue=1, offvalue=0, height=1, width=1).grid(column=3, row=28)
CSecond29 = tk.Checkbutton(Second_Frame, text="", variable=CheckbuttonSecond28, onvalue=1, offvalue=0, height=1, width=1).grid(column=3, row=29)
CSecond30 = tk.Checkbutton(Second_Frame, text="", variable=CheckbuttonSecond29, onvalue=1, offvalue=0, height=1, width=1).grid(column=3, row=30)
CSecond31 = tk.Checkbutton(Second_Frame, text="", variable=CheckbuttonSecond30, onvalue=1, offvalue=0, height=1, width=1).grid(column=3, row=31)
CSecond32 = tk.Checkbutton(Second_Frame, text="", variable=CheckbuttonSecond31, onvalue=1, offvalue=0, height=1, width=1).grid(column=3, row=32)
CSecond33 = tk.Checkbutton(Second_Frame, text="", variable=CheckbuttonSecond32, onvalue=1, offvalue=0, height=1, width=1).grid(column=3, row=33)
CSecond34 = tk.Checkbutton(Second_Frame, text="", variable=CheckbuttonSecond33, onvalue=1, offvalue=0, height=1, width=1).grid(column=3, row=34)
CSecond35 = tk.Checkbutton(Second_Frame, text="", variable=CheckbuttonSecond34, onvalue=1, offvalue=0, height=1, width=1).grid(column=3, row=35)
CSecond36 = tk.Checkbutton(Second_Frame, text="", variable=CheckbuttonSecond35, onvalue=1, offvalue=0, height=1, width=1).grid(column=3, row=36)
CSecond37 = tk.Checkbutton(Second_Frame, text="", variable=CheckbuttonSecond36, onvalue=1, offvalue=0, height=1, width=1).grid(column=3, row=37)
CSecond38 = tk.Checkbutton(Second_Frame, text="", variable=CheckbuttonSecond37, onvalue=1, offvalue=0, height=1, width=1).grid(column=3, row=38)
CSecond39 = tk.Checkbutton(Second_Frame, text="", variable=CheckbuttonSecond38, onvalue=1, offvalue=0, height=1, width=1).grid(column=3, row=39)
CSecond40 = tk.Checkbutton(Second_Frame, text="", variable=CheckbuttonSecond39, onvalue=1, offvalue=0, height=1, width=1).grid(column=3, row=40)
CSecond41 = tk.Checkbutton(Second_Frame, text="", variable=CheckbuttonSecond40, onvalue=1, offvalue=0, height=1, width=1).grid(column=3, row=41)
CSecond42 = tk.Checkbutton(Second_Frame, text="", variable=CheckbuttonSecond41, onvalue=1, offvalue=0, height=1, width=1).grid(column=3, row=42)
CSecond43 = tk.Checkbutton(Second_Frame, text="", variable=CheckbuttonSecond42, onvalue=1, offvalue=0, height=1, width=1).grid(column=3, row=43)
CSecond44 = tk.Checkbutton(Second_Frame, text="", variable=CheckbuttonSecond43, onvalue=1, offvalue=0, height=1, width=1).grid(column=3, row=44)

tk.mainloop() 
