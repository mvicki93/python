import os, time
import datetime
import smtplib

# read file and store the data in date class
# now am not using this class
class user_data:
    def __init__(self, dob, name, mail_id):
        self.dob = dob
        self.name = name
        self.mail_id = mail_id

#list
my_object = []

class file_operation:
    # temp file desc

    def __init__(self, flag):
        self.open_file(flag)

    def open_file(self, flag):
        self.fd = open("user_input.txt", "r")
        self.R_file(flag)
        self.recent_modify_check()

    def R_file(self, flag):
        i = 0
        if flag == 1:
            my_object.clear()
        for data in self.fd.readlines():
            my_object.append(data.split())
            #print(my_object[i][0])
            i = i + 1

    def recent_modify_check(self):
        stat = os.stat("user_input.txt")
        return stat.st_birthtime


# now we have decide when we read the file
file1 = file_operation(0)
old_stat = file1.recent_modify_check()
#print(old_stat)

def current_date_is_birth_date(current_date):
    i = 0
    for data in my_object:
        #print(data[0])
        data1 = data[0]
        #print(type(data[0]))
        if current_date[0:5] == data1[0:5]:
            #print()
            send_mail(data[2], data[1])


def send_mail(target_mail, name):
    smtp = server = smtplib.SMTP('smtp.gmail.com', 587)
    smtp.starttls()
    # Next, log in to the server
    server.login("bdayuwish@gmail.com", "sansel123")
    msg = "Smile Plz!!"
    message = 'Subject: {}\n\n{}'.format('Happy Birth Day ' + name, msg)
    # Send the mail

    server.sendmail("bdayuwish@gmail.com", target_mail, message)
    print(message)

temp = 0
sen_mail_count = 0
while True:
    if (old_stat != file1.recent_modify_check()):
        file1.__init__(1)
        old_stat = file1.recent_modify_check()
    else:
        d = datetime.datetime.today()
        #current_date = d.strftime('%d/%m/%Y')
        t2 = d.hour
        time.sleep(2)
        #print(t2)
        if t2 == 0 and sen_mail_count == 0:
            print("send wish")
            print(sen_mail_count)
            current_date = d.strftime('%d/%m/%Y')
            current_date_is_birth_date(current_date)
            sen_mail_count = 1
        if t2 != 0:
            sen_mail_count = 0

    temp = temp + 1
