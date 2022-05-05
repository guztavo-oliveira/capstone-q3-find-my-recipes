from mailjet_rest import Client
import os

mailjet = Client(auth=(os.getenv("API_KEY"), os.getenv("API_SECRET")), version="v3.1")


def send_email(
    link,
    user_email=None,
    user_name=None,
):
    data = {
        "Messages": [
            {
                "From": {
                    "Email": "gu.machado.oliveira@gmail.com",
                    "Name": "Find Recipe",
                },
                "To": [
                    {
                        "Email": "find.recipe.capstone@gmail.com",
                        "Name": f"{user_name}",
                    }
                ],
                "Subject": "Please confirm your email to be able to use our app.",
                # "TextPart": f"{body}",
                "HTMLPart": f"<h3>Hi {user_name}, thanks for using our app!</h3></br> <h2>Please confirm your registration by clicking on the link: {link}.</h2>",
                # "CustomID": "AppGettingStartedTest",
            }
        ]
    }

    result = mailjet.send.create(data=data)
