import pywhatkit

from contactList import contact_number, contact_names
from message import myMessage

hour = int(input("Kitna Baza "))
hour=hour%24
minute = int(input("Kitna Minute Pa"))
minute= minute%60

times = len(contact_names)

for cn in range(times):

    cno="+91"+f"{contact_number[cn]}"
    message=str(myMessage(cn))

    pywhatkit.sendwhatmsg(cno, message, hour, minute)
    minute=minute+0.5
    if minute>=59:
        minute=1
        hour=hour+1


