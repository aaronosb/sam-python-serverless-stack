import json
import uuid
import boto3
import datetime
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
    json.loads(event['body'])
    data = json.loads(event['body'])
    return respond(None, table.put_item(Item={
        "userId": event['requestContext']['identity']['cognitoIdentityId'],
        "noteId": str(uuid.uuid1()),
        "content": data['content'],
        "attachment": data['attachment'],
        "createdAt": datetime.datetime.now().isoformat()
    }))