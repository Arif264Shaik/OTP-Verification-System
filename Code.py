import random
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import tkinter as tk 
from tkinter import messagebox
import tkinter.font as tkfont

# Generating 6 digit OTP
def generate_otp() :
  return f"{random.randint(100000, 999999)}"

# Send otp to receviers email
def send_otp(receiver_email, otp) :
    try :
        sender_email = "Enter from Email you need to send OTP"
        sender_password = "App Password"

        smtp_server = "smtp.gmail.com"
        smtp_port = 587

        subject = "Your OTP for verification"
        body = f"Your OTP is: {otp}"

        message = MIMEMultipart()
        message["From"] = sender_email
        message["To"] = receiver_email
        message["Subject"] = subject
        message.attach(MIMEText(body, "plain"))
        
        with smtplib.SMTP(smtp_server, smtp_port) as server :
          server.starttls()
          server.login(sender_email, sender_password)
          server.send_message(message)

        return True
    except Exception as e :
          print(f"Error sending otp: {e}")
          return False

# Define GUI
class OTPApp :
  def __init__(self, root) :
    self.root = root
    self.root.title("OTP Verification")
    self.root.geometry("300x250")
    self.otp = ""
    self.attempts = 3

    font_style = tkfont.Font(family = "Arial Bold", size = 10)
    font_style2 = tkfont.Font(family = "Arial Bold", size = 9)

    # Email input
    self.email_label = tk.Label(root, text = "Enter your email:", font = font_style)
    self.email_label.pack(pady = 4)

    self.email_entry = tk.Entry(root, width = 30)
    self.email_entry.pack(pady = 4)

    #Send otp button
    self.send_otp_button = tk.Button(root, text = "Send OTP", command = self.send_otp, bg = "#4CAF50", fg = "#fff", font = font_style2) # Green background
    self.send_otp_button.pack(pady = 10)

    # OTP input
    self.otp_label = tk.Label(root, text = "Enter OTP: ", font = font_style)
    self.otp_label.pack(pady = 4)

    self.otp_entry = tk.Entry(root, width = 15, bg = "#fff", fg = "#333") # White background
    self.otp_entry.pack(pady = 4)

    # Verify OTP button
    self.verify_otp_button = tk.Button(root, text = "Verify OTP", command = self.verify_otp, bg = "#2196F3", fg = "#fff", font = font_style2) # Blue Background
    self.verify_otp_button.pack(pady = 10)

  def send_otp(self) :
    email = self.email_entry.get()
    if not email :
      messagebox.showerror("Error", "Please enter valid email ID")
      return
    self.otp = generate_otp()
    if send_otp(email, self.otp) :
      messagebox.showinfo("Success", "OTP sent successfully")
    else:
      messagebox.showerror("Error", "Enter valid email. Try again")

  def verify_otp(self) :
    user_otp = self.otp_entry.get()
    if user_otp == self.otp :
      messagebox.showinfo("Success", "OTP verified successfully. Access Granted")
      self.attempts = 3
      self.root.quit()
    
    else:
        self.attempts -= 1
        if self.attempts > 0:
            messagebox.showerror("Error", f"Incorrect OTP. You have {self.attempts} attempts left.")
        else:
           messagebox.showerror("Error", "No attempts left. Access denied.")
           self.root.quit()

if __name__ == "__main__" :
  root = tk.Tk()
  app = OTPApp(root)
  root.mainloop()


  