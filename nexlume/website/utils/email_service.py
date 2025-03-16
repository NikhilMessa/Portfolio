from django.core.mail import EmailMessage
from django.conf import settings

def send_contact_email(name, organization, email, contact_number, services, investment, message):
    """Send a confirmation email to the user after submitting the contact form."""

    subject = "Thank you for your interest in our services | Nexlume"
    body = f"""
    <html>
    <body style="font-family: Arial, sans-serif; color: #333;">
        <p>Dear {name},</p>

        <p>Thank you for reaching out to us through our website contact form. We appreciate your interest in our services and have received your inquiry successfully.</p>

        <p><strong>Here's a confirmation of the details you provided:</strong></p>

        <h3>Personal Information:</h3>
        <ul>
            <li><strong>Name:</strong> {name}</li>
            <li><strong>Organization:</strong> {organization}</li>
            <li><strong>Email:</strong> {email}</li>
            <li><strong>Contact Number:</strong> {contact_number}</li>
        </ul>

        <h3>Services Interest:</h3>
        <ul>
            <li><strong>Selected Services:</strong> {services}</li>
            <li><strong>Investment Range:</strong> {investment}</li>
            <li><strong>Your Message to us:</strong> {message}</li>
        </ul>

        <p><strong>For immediate assistance:</strong></p>
        <p>📞 Phone: +91 9834248447 <br>
           📧 Email: nexlume.co@gmail.com <br>
           ⏰ Business Hours: Monday-Saturday, 9 AM - 6 PM IST</p>

        <p>Best regards, <br>
           <strong>The Nexlume Team</strong></p>

        <img src="https://res.cloudinary.com/da2ufcgyv/image/upload/v1738524093/jutgcwfol612xoxfgfnh.jpg" 
             alt="Nexlume Logo" 
             style="width: 150px; height: auto; display: block; margin-top: 10px;">
        
        <p style="font-size: 12px;">Note: This is an automated response. Please do not reply to this email.</p>
    </body>
    </html>
    """

    # Prepare the email with HTML content
    email_message = EmailMessage(
        subject,
        body,
        settings.DEFAULT_FROM_EMAIL,  # Sender email
        [email],  # Recipient email
    )
    email_message.content_subtype = "html"  # Set email content type to HTML

    # Send the email
    email_message.send(fail_silently=False)
