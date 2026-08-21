import json
import os
import boto3

# Initialize DynamoDB resource outside handler for execution environment reuse
TABLE_NAME = os.environ.get('TABLE_NAME', 'cloud-resume-stats')
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(TABLE_NAME)

def lambda_handler(event, context):
    try:
        # Atomically increment the views count for id='visits'
        response = table.update_item(
            Key={'id': 'visits'},
            UpdateExpression='ADD #v :val',
            ExpressionAttributeNames={'#v': 'views'},
            ExpressionAttributeValues={':val': 1},
            ReturnValues='UPDATED_NEW'
        )
        
        views = response['Attributes']['views']
        
        return {
            'statusCode': 200,
            'headers': {
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Headers': 'Content-Type',
                'Access-Control-Allow-Methods': 'GET,OPTIONS'
            },
            'body': json.dumps({'views': int(views)})
        }
    except Exception as e:
        print(f"Error updating item: {str(e)}")
        return {
            'statusCode': 500,
            'headers': {
                'Access-Control-Allow-Origin': '*'
            },
            'body': json.dumps({'error': 'Could not update visitor count'})
        }