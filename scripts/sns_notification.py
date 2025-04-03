# Create an SNS topic for notifications
import boto3

# SNS Client Configuration
sns = boto3.client('sns', region_name='tu-región-01')

# Create the topic
response = sns.create_topic(Name='BillingAlarmTopic')
topic_arn = response['TopicArn']
print(f"Topic created: {topic_arn}")

# Set up email subscription
sns.subscribe(
    TopicArn=topic_arn,
    Protocol='email',
    Endpoint='tu@correo.com'  # Change for your email
)
