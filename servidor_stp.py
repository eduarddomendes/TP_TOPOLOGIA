import smtplib 

servidor_email = smtplib.SMTP('smtp.gmail.com',587)

print(servidor_email.starttls())

servidor_email.login("emdbm.10@gmail.com", 'hocn kyuh xvgn ahwi')

remetente = 'emdbm.10@gmail.com'
destinatarios = ['gleison.batista@prozeducacao.com.br']

conteudo = 'Oi! Oi eu sou gente boa!'

servidor_email.sendmail(remetente,destinatarios, conteudo)

servidor_email.quit()