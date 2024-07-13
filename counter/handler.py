import json
import boto3
import os

# initializing code
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(os.environ['TABLE_NAME'])

def lambda_handler(event, context):
    # Increment the counter
    response = table.update_item(
        Key={'id': 'counter'},
        UpdateExpression='ADD visitorCount :incr',
        ExpressionAttributeValues={':incr': 1},
        ReturnValues='UPDATED_NEW'
    )

    # Get the new counter value
    new_value = round(response['Attributes']['visitorCount'])

    # return count
    return {
        'statusCode': 200,
        'headers': {
            'Access-Control-Allow-Headers' : 'Accept, Content-Type',
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'GET, POST, OPTIONS',
        },
        'body': json.dumps({
            'counter': new_value,
        }),
    }
