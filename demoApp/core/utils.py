from weasyprint import HTML

from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.db.models.functions import ExtractWeekDay


# get map for a given currency for all weekdays
def get_map_for_transactions(transactions, currency):
    return transactions.filter(
        currency_sent=currency).annotate(
            weekday=ExtractWeekDay('date_added')
    ).values('weekday').annotate(count=Count('amount')).values('count', 'weekday')


def send_order_mail(data):
    file_path = get_order_statement(data, 'Transaction Statement')
    email_subject = f"You have received transfer from {data['to_user_full_name']}"
    email_body = f"""
        <html>
            <head></head>
            <body>
            <p>
            Hello {data["to_user_full_name"]},
            <br>
            <p>We are happy to tell you that, {data['to_user_full_name']} has transferred {data['amount']} in your account</p>
            <p><a href="{settings.SERVER_URL}/wallet">Check your new balance</a></p>
            <p>Please find the attached statement with this mail.</p>
            <br>
            Thanks,<br>
            Team CX<br>
            </p>
            </body>
        </html>
    """
    email = EmailMultiAlternatives(
        email_subject, "", settings.EMAIL_HOST_USER, [data["to_email"]]
    )
    email.attach_alternative(email_body, "text/html")
    email.attach_file(file_path)
    email.send()


def get_order_statement(item, title):
    html_string = render_to_string(
        'order_pdf_template.html',
        {'item': item, 'title': title})
    html = HTML(string=html_string)
    file_path = f'/tmp/tx_statement.pdf'
    html.write_pdf(target=file_path)
    return file_path


def send_monthly_statement(items, title, date, user):
    file_path = get_monthly_statement_pdf(items, title, date)
    email_subject = f"Your monthly statement for currency exchange is here"
    email_body = f"""
        <html>
            <head></head>
            <body>
            <p>
            Hello {user.full_name},
            <br>
            <p>Please find the attached statement with this mail.</p>
            <br>
            Thanks,<br>
            Team CX<br>
            </p>
            </body>
        </html>
    """
    email = EmailMultiAlternatives(
        email_subject, "", settings.EMAIL_HOST_USER, [user.email]
    )
    email.attach_alternative(email_body, "text/html")
    email.attach_file(file_path)
    email.send()


def get_monthly_statement_pdf(items, title, date):
    html_string = render_to_string(
        'pdf_template.html',
        {'history': items, 'title': title, 'date': date})
    html = HTML(string=html_string)
    file_path = f'/tmp/cx_statement.pdf'
    html.write_pdf(target=file_path)
    return file_path
