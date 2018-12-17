import json
import boto3
import os

dynamo = boto3.resource('dynamodb')
table_name = os.environ.get('tableName')
table = dynamo.Table(table_name)


def respond(err, res=None):
    return {
        'statusCode': '400' if err else '200',
        'body': err.message if err else json.dumps(res),
        'headers': {
            'Content-Type': 'application/json',
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Credentials": True
        },
    }


def lambda_handler(event, context):
    try:
        result = table.delete_item(
        Key={
            "userId": event['requestContext']['identity']['cognitoIdentityId'],
            "noteId": event['pathParameters']['id']
            }
        )
        return respond(None, {"status":True})
    except:
        return respond(None, {"status": False})
