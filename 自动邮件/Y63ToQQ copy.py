import smtplib
import traceback
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

# 发件人邮箱地址
from_email = ""
# 收件人邮箱地址
to_email = ""
# 163邮箱的密码或授权码
password = ""

def send_email():
    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = "我的日报"

    body = "Dear Boss,\n\n测试邮件发送。\n\nBest regards,\n"
    msg.attach(MIMEText(body, 'plain'))

#文件名
    #filename = "会输出bin的写法"
#文件路径
    file_path = r"C:\Users\Nymphet\Desktop\abc.xlsx"
    if not os.path.exists(file_path):
        print(f"文件不存在: {file_path}")
    else:
        with open(file_path, "rb") as file:
            attachment = file.read()
    #part = MIMEBase('application', 'octet-stream')
    part = MIMEBase('application', 'vnd.openxmlformats-officedocument.spreadsheetml.sheet')  # 修改Content-Type
    part.set_payload(attachment)
    encoders.encode_base64(part)
   # part.add_header('Content-Disposition', f"attachment;  filename={filename}")
    part.add_header('Content-Disposition', 'attachment', filename='abc.xlsx')

    msg.attach(part)

    try:
        with smtplib.SMTP_SSL('smtp.163.com', 465) as server:
            server.login(from_email, password)
            text = msg.as_string()
            server.sendmail(from_email, to_email, text)
        print('邮件发送成功！')
    except smtplib.SMTPAuthenticationError as e:
        print(f"邮件发送失败：认证失败 ({e.smtp_code}, {e.smtp_error.decode('utf-8')})")
    except Exception as e:
        print(f"邮件发送失败：{e}")
        traceback.print_exc()

send_email()