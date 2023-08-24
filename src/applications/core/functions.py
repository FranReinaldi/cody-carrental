from smtplib import SMTPException
from django.core.mail import send_mail

# Es usado por xhtml2pdf para levantar assets de media & static
def link_callback(uri, rel):
    import os
    from django.conf import settings
    from django.contrib.staticfiles import finders
    """
    Convert HTML URIs to absolute system paths so xhtml2pdf can access those
    resources
    """
    result = finders.find(uri)
    if result:
        if not isinstance(result, (list, tuple)):
            result = [result]
        result = list(os.path.realpath(path) for path in result)
        path=result[0]
    else:
        sUrl = settings.STATIC_URL        # Typically /static/
        sRoot = settings.STATIC_ROOT      # Typically /home/userX/project_static/
        mUrl = settings.MEDIA_URL         # Typically /media/
        mRoot = settings.MEDIA_ROOT       # Typically /home/userX/project_static/media/

        if uri.startswith(mUrl):
            path = os.path.join(mRoot, uri.replace(mUrl, ""))
            print('PATH M', path)
        elif uri.startswith(sUrl):
            path = os.path.join(sRoot, uri.replace(sUrl, ""))
            print('PATH S', path)
        else:
            print('URI', uri)
            return uri


def send_email(subject, txt, html, recipient):

    try:
        send_mail(
            subject=subject,
            message=txt,
            from_email='notify@carrental.com',
            recipient_list=[recipient, ],
            html_message=html,
            fail_silently=False,
        )
    except SMTPException as error:
        print(error)