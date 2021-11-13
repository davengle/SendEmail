import yagmail
import os
import time

sender = '1q2w3e4r6900@gmail.com'
receiver = 'nourwkbrc@emlhub.com'

subject = """
  This is the subject!
"""

contents = """
  HI! Again.  This is a multiline 
  content message
"""

while True:
  yag = yagmail.SMTP(user=sender, password = os.environ['PWGM'])
  yag.send(to=receiver, subject=subject, contents=contents)
  print("Email Sent!")
  time.sleep(60)
