import smtplib
import parameterek
from datetime import datetime



def emailkuldes(temp,humidity,pressure):
    kuldo=parameterek.kuldo
    fogado=parameterek.fogado
    pw=parameterek.pw
    server=parameterek.server


    szoveg = 'Üzenet'+'Üzenet'
    
    
    if temp <= 0:
        targy = 'Fagypont alatt a hőmérséklet!'
    elif 0< temp <= 10:
        targy = 'Hideg időre számíthatunk!'
    elif 10< temp <= 20:
        targy = 'Hűvös időre lehet számítani!'
    elif 20<temp<=30:
        targy = 'Kellemes idő vár odakint!'
    elif 30 < temp:
        targy = 'Nagyon meleg időnek nézünk elébe!'
    else:
        targy = 'Nincs rendelkezésre álló adat.'
    szoveg= 'Aktuális idő:\n'
    szoveg+= 'Ebben a pillanatban, Győr városában mért hőmérséklet '+ str(temp)+'°C.\n'
    szoveg+='A levegő páratartalma '+str(humidity)+'%-os.\n'
    szoveg+='A légnyomás pedig '+str(pressure)+'hPa.'


    content = "From: %s\nTo: %s\nSubject: %s\n\n%s" % (kuldo, fogado, targy, szoveg)


    mail = smtplib.SMTP (server,587) 
    mail.ehlo()
    mail.starttls()
    mail.login(kuldo , pw )
    mail.sendmail (kuldo , fogado , content.encode("utf-8"))
    mail.close()
