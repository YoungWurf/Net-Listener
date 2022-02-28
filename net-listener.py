import subprocess 
import smtplib
import time

def find_devices():
  default_devices=[["Device_Name","Device_IP"]]
  connected_devices=[]
  proc_output_text=[]
  proc = subprocess.Popen(["nmap","-sP",'192.168.1.*'],stdout=subprocess.PIPE)
  while True:
      proc_output = proc.stdout.readline()
      if not proc_output:
        break
      proc_output_text.append(proc_output.decode('utf-8'))
  for line in range(len(proc_output_text)):
    for device in default_devices:
      if device[1] in proc_output_text[line] and device[1] not in connected_devices:
        connected_devices.append(device[0])
  return connected_devices

def send_email(message):
  server=smtplib. SMTP ('smtp.gmail.com',587) 
  server.starttls()
  server.login('Your_email', 'Your_emails_password')
  server.sendmail('Your_email', 'Email_to_alarm',str(message))

def activate_listener():
    devices=[]
    while True:
      if time.daylight:
        previous_devices=devices
        devices=[]
        for i in range (5):
          devices=devices+find_devices()
          time.sleep(10)
        set_devices=set(devices)
        devices=list(set_devices)
        if previous_devices != devices:
          msg = """
              Subject: <Connected devices at Home>\n
              Connected devices:"""+str(devices)+"""\n"""   
          send_email(msg)
        time.sleep(3600)

def main():
    activate_listener()

main()
  
