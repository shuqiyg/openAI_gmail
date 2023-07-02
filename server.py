#this file is just for testing the api end point, not a part of the final deployment 

import requests

# print(
#     requests.post(
#         "http://127.0.0.1:5000/sq"
#     ).json()
# )
print(
    requests.post(
        "http://127.0.0.1:5000",
        json={
            "from_email": "Sahil.Anand@mnp.ca",
            "content": """
                Hello Shuqi, 

Thank you for applying for the Software Engineer 2 ( Full-stack) position. We’re reviewing your eligibility, experience, and qualifications for this position and will contact you shortly.

In the meantime, visit the “Candidate Home” page using the link below to view your application status. If you have not already done so, you will need to create an account using the email address you used to apply. 

https://usbank.wd1.myworkdayjobs.com/US_Bank_Careers/login?Job_Application_ID=cc1ee769e81d9001aaf5adeda20a0001 

Follow us on Twitter @usbankcareers or LinkedIn for the latest U.S. Bank and Elavon Europe global job opportunities, career resources and hiring events.

Thank you for exploring what's possible with your career.

Talent Acquisition 
            
            """
        }
    ).json()
)