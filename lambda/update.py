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
    data = json.loads(event['body'])
    return respond(None, table.update_item(
        Key={
            "userId": event['requestContext']['identity']['cognitoIdentityId'],
            "noteId": event['pathParameters']['id']
        },
        UpdateExpression= "SET content = :content, attachment = :attachment",
        ExpressionAttributeValues= {
            ":attachment": data['attachment'],
            ":content": data['content']
        },
        ReturnValues= "ALL_NEW"
    ))