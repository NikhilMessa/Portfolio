from django.core.mail import EmailMessage
from django.conf import settings

def send_internship_email(email):
    """Send an internship opportunity email to the candidate."""
    
    # Extract candidate name from email (before '@')
    candidate_name = email.split("@")[0].replace(".", " ").title()  # Format name properly
    
    subject = " Exciting Internship Opportunities at NexLume"
    body = f"""
    <html>
    <body style="font-family: Arial, sans-serif; line-height: 1.6; padding: 20px;">
        <p>Dear {candidate_name},</p>

        <p>Thank you for showing interest in <strong>NexLume</strong>! We are excited to offer internship opportunities for passionate individuals like you who are eager to gain hands-on experience in a fast-growing startup environment.</p>

        <p>At <strong>NexLume</strong>, we believe in empowering fresh talent by providing real-world exposure, mentorship, and the chance to work on impactful projects. If you’re ready to grow with us, we’d love to hear from you!</p>

        <h3>🌟 How to Apply?</h3>
        <p>📌 <strong>Fill out our Internship Application Form:</strong> <a href="https://forms.gle/guHb8ZoeM1ybnSe98" style="color: #0073e6; text-decoration: none;">Apply Here</a></p>
        <p>It only takes a few minutes! Once submitted, our team will review your application and reach out to you.</p>

        <h3>💡 Why Intern at NexLume?</h3>
        <ul>
            <li>✅ Work on <strong>real projects</strong> with industry professionals</li>
            <li>✅ Gain <strong>practical experience</strong> in a dynamic startup environment</li>
            <li>✅ Receive <strong>mentorship</strong> and career growth opportunities</li>
            <li>✅ Potential for <strong>full-time placement</strong> based on performance</li>
        </ul>

        <h3">📞 Need Assistance? We're Here to Help!</h3>
        <p style="font-size: 14px; padding: 10px; border-radius: 5px;">
            📞 <strong>Phone:</strong> +91 9834248447 <br>
            📧 <strong>Email:</strong> <a href="mailto:nexlume.co@gmail.com" style="color: #0073e6;">nexlume.co@gmail.com</a> <br>
            ⏰ <strong>Business Hours:</strong> Monday - Saturday | 9 AM - 6 PM IST
        </p>

        <p>Follow us on our social media channels for the latest updates and opportunities! <a href="https://www.instagram.com/nexlume/" style="color: #0073e6;">Connect with us</a></p>

        <p>We look forward to reviewing your application and potentially welcoming you to the NexLume team!</p>

        <p>Best regards,<br>
           <strong>The NexLume Team</strong></p>

        <img src="https://res.cloudinary.com/da2ufcgyv/image/upload/v1738524093/jutgcwfol612xoxfgfnh.jpg" 
             alt="NexLume Logo" 
             style="width: 150px; height: auto; margin-top: 10px;">

        <p style="font-size: 12px; color: #777;">Note: This is an automated email. Please do not reply to this message.</p>
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
