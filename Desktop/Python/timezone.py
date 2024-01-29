from datetime import datetime
from pytz import timezone
fmt="%D-%M-%Y  %h:%m:%s"
now_utc=datetime.now(timezone('UTC'))
print('UTC:',now_utc)
k=now_utc.astimezone(timezone('Asia/Kolkata'))
print ("kolkata:",k)
