import json
import boto3
from boto3.dynamodb.conditions import Key
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
    response = table.query(
        KeyConditionExpression=Key('userId').eq(event['requestContext']['identity']['cognitoIdentityId'])
    )
    return respond(None, response["Items"])