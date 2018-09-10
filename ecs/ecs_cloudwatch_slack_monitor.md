# Cloudwatch slack integration


1. send cloudwatch events to SNS

2. then configure your lambda using template 'cloudwatch-alarm-to-slack' and node 4.3

3. change your code with this  & replace your url in the code

```
'use strict';

/**
 * Follow these steps to configure the webhook in Slack:
 *
 *   1. Navigate to https://<your-team-domain>.slack.com/services/new
 *
 *   2. Search for and select "Incoming WebHooks".
 *
 *   3. Choose the default channel where messages will be sent and click "Add Incoming WebHooks Integration".
 *
 *   4. Copy the webhook URL from the setup instructions and use it in the next section.
 *
 *
 * To encrypt your secrets use the following steps:
 *
 *  1. Create or use an existing KMS Key - http://docs.aws.amazon.com/kms/latest/developerguide/create-keys.html
 *
 *  2. Click the "Enable Encryption Helpers" checkbox
 *
 *  3. Paste <SLACK_HOOK_URL> into the kmsEncryptedHookUrl environment variable and click encrypt
 *
 *  Note: You must exclude the protocol from the URL (e.g. "hooks.slack.com/services/abc123").
 *
 *  4. Give your function's role permission for the kms:Decrypt action.
 *      Example:

{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "Stmt1443036478000",
            "Effect": "Allow",
            "Action": [
                "kms:Decrypt"
            ],
            "Resource": [
                "<your KMS key ARN>"
            ]
        }
    ]
}

 */

const AWS = require('aws-sdk');
const url = require('url');
const https = require('https');

// The base-64 encoded, encrypted key (CiphertextBlob) stored in the kmsEncryptedHookUrl environment variable
const kmsEncryptedHookUrl = process.env.kmsEncryptedHookUrl;
// The Slack channel to send a message to stored in the slackChannel environment variable
const slackChannel = process.env.slackChannel;
let hookUrl;


function postMessage(message, callback) {
    const body = JSON.stringify(message);
    const options = url.parse(hookUrl);
    options.method = 'POST';
    options.headers = {
        'Content-Type': 'application/json',
        'Content-Length': Buffer.byteLength(body),
    };

    const postReq = https.request(options, (res) => {
        const chunks = [];
        res.setEncoding('utf8');
        res.on('data', (chunk) => chunks.push(chunk));
        res.on('end', () => {
            if (callback) {
                callback({
                    body: chunks.join(''),
                    statusCode: res.statusCode,
                    statusMessage: res.statusMessage,
                });
            }
        });
        return res;
    });

    postReq.write(body);
    postReq.end();
}

function processEvent(event, callback) {
    const message = JSON.parse(event.Records[0].Sns.Message);

    const alarmName = message.AlarmName;
    //var oldState = message.OldStateValue;
    const newState = message.NewStateValue;
    const reason = message.NewStateReason;

    const slackMessage = {
        channel: slackChannel,
        text: `${alarmName} state is now ${newState}: ${reason}`,
    };

    postMessage(slackMessage, (response) => {
        if (response.statusCode < 400) {
            console.info('Message posted successfully');
            callback(null);
        } else if (response.statusCode < 500) {
            console.error(`Error posting message to Slack API: ${response.statusCode} - ${response.statusMessage}`);
            callback(null);  // Don't retry because the error is due to a problem with the request
        } else {
            // Let Lambda retry
            callback(`Server error when processing message: ${response.statusCode} - ${response.statusMessage}`);
        }
    });
}


exports.handler = (event, context, callback) => {
    if (hookUrl) {
        // Container reuse, simply process the event with the key in memory
        processEvent(event, callback);
    } 
    hookUrl = `https://hooks.slack.com/services/XXX/XX/XXXXX`;
    processEvent(event, callback);
};

```


### Sample input to test

```
{
  "Records": [
    {
      "EventSource": "aws:sns",
      "EventVersion": "1.0",
      "EventSubscriptionArn": "arn:aws:sns:us-west-2:123456789123:CloudWatchNotifications:00000000-0000-0000-0000-000000000000",
      "Sns": {
        "Type": "Notification",
        "MessageId": "00000000-0000-0000-0000-000000000000",
        "TopicArn": "arn:aws:sns:us-west-2:123456789123:CloudWatchNotifications",
        "Timestamp": "2016-08-11T07:24:05.959Z",
        "Subject": "ALARM: \"awsrds-app-High-DB-Connections\" in US West - Oregon",
        "Message": "{\"AlarmName\":\"awsrds-app-High-DB-Connections\",\"AlarmDescription\":null,\"AWSAccountId\":\"123456789123\",\"NewStateValue\":\"ALARM\",\"NewStateReason\":\"Threshold Crossed: 1 datapoint (10.0) was greater than or equal to the threshold (10.0).\",\"StateChangeTime\":\"2016-07-24T22:05:19.737+0000\",\"Region\":\"US West - Oregon\",\"OldStateValue\":\"OK\",\"Trigger\":{\"MetricName\":\"DatabaseConnections\",\"Namespace\":\"AWS/RDS\",\"Statistic\":\"AVERAGE\",\"Unit\":null,\"Dimensions\":[{\"name\":\"DBInstanceIdentifier\",\"value\":\"app\"}],\"Period\":300,\"EvaluationPeriods\":1,\"ComparisonOperator\":\"GreaterThanOrEqualToThreshold\",\"Threshold\":10.0}}",
        "MessageAttributes": {}
      }
    }
  ]
}
```


Reference:

+ http://notes.webutvikling.org/send-aws-cloudwatch-alarms-to-slack/
