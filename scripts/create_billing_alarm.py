import boto3

# Configure CloudWatch client
cloudwatch = boto3.client('cloudwatch', region_name='tu-región-01')

# Define alarm parameters
alarm_name = 'BillingAlarm_5Euros'
metric_name = 'EstimatedCharges'
namespace = 'AWS/Billing'
threshold = 5.0  # Euros threshold

# Replace with your SNS topic ARN
topic_arn = 'arn:aws:sns:tu-región-01:TUCUENTAID:BillingAlarmTopic'

# Create the alarm
response = cloudwatch.put_metric_alarm(
    AlarmName=alarm_name,
    ComparisonOperator='GreaterThanThreshold',
    EvaluationPeriods=1,
    MetricName=metric_name,
    Namespace=namespace,
    Period=86400,  # 1 day in seconds
    Statistic='Maximum',
    Threshold=threshold,
    ActionsEnabled=True,
    # Replace with your SNS topic ARN
    AlarmActions=['arn:aws:sns:tu-región-01:TUCUENTAID:BillingAlarmTopic'],
    AlarmDescription='Alarm when estimated charges exceed 5 Euros',
    Dimensions=[
        {
            'Name': 'Currency',
            'Value': 'EUR'
        },
    ],
    Unit='None'
)

print(f"Alarm created: {response}")
