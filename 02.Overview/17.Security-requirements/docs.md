---
title: Security Requirements
taxonomy:
    category: docs
---

### Amazon S3 IAM policies
If you are using Amazon S3 bucket for storing Mender Artifacts, you can use the following minimum policy set:

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Action": [
                "s3:GetAccessPoint",
                "s3:ListAllMyBuckets"
            ],
            "Effect": "Allow",
            "Resource": "*"
        },
        {
            "Action": [
                "s3:*"
            ],
            "Effect": "Allow",
            "Resource": "arn:aws:s3:::BUCKET-NAME"
        },
        {
            "Action": [
                "s3:*"
            ],
            "Effect": "Allow",
            "Resource": "arn:aws:s3:::BUCKET-NAME/*"
        },
    ]
}
```
