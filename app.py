"""
This file is the main script of the lambda. The handler function will be executed every time lambda is triggered.

This Plug & Play script currently contains some dummy code for demonstration purpose.

To convert your custom code into a lambda, just add your modules, import them and make call to your logic, that has to executed every time lambda is triggerd, in the handler function.

Author: Pranay Chandekar
"""

def handler(event, context):
    """
    This function will be triggerd on every lambda invocation.

    :param event: The request that triggered the lambda.
    :param context: The context object received along with the request.
    :return: The response
    """

    return {
        "statusCode": 200,
        "requestId": context.aws_request_id,
        "request": event
    }
