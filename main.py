import pywhatkit

from contactList import contact_Names,contact_Number
from message import myMessage

hour=int(input("Kitna ghnata ma Bheuu :"))
minute=int(input("Kitna Minute pa Bhezuu  :"))


times=len(contact_Names)

for cn in range(times):
    cno="+91"+f"{contact_Number[cn]}"
    message=str(myMessage(cn))

    pywhatkit.sendwhatmsg(cno,message,hour,minute)
    minute=minute+1/2