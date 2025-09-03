### Blog Creation using GenAI on AWS
This project is a **serverless Generative AI-powered blog creator** built with **AWS Bedrock + Lambda + API Gateway + S3**.   

This project demonstrates how to build a Generative AI-powered blog creation system on AWS using a serverless architecture. 
The system allows users to provide a prompt or topic, and a blog post is generated with the help of a Large Language Model (LLM). 
The generated blogs are stored in Amazon S3, and all API requests are handled through API Gateway with a Lambda backend.

### Tech Stack

Backend: Python (Lambda function)

API Management: Amazon API Gateway

Storage: Amazon S3 (for storing generated blogs)

AI/ML:

Amazon Bedrock (LLM access) / OpenAI API (if configured)

Monitoring & Logging: Amazon CloudWatch

Testing Tool: Postman (for API calls & validation)


## Features

Generate a blog post using GenAI based on user input prompt

Serverless backend using Lambda (Python)

API Gateway for secure and scalable API management

Store generated blogs as text/JSON files in S3

Monitor requests and responses with CloudWatch

Tested end-to-end using Postman

## AWS Services Used  
- **Amazon Bedrock** → Generative AI (Claude model)  
- **AWS Lambda** → Backend function (Python)  
- **Amazon API Gateway** → REST API endpoint  
- **Amazon S3** → Stores generated blog content  
- **Amazon CloudWatch** → Logs & monitoring

<img width="782" height="460" alt="image" src="https://github.com/user-attachments/assets/02963c57-452b-406c-a5de-93336c042de2" />

### Project Structure
├── app.py               # Lambda handler code
├── requirements.txt     # Python dependencies
├── botolayer.zip        # Lambda layer for boto3/botocore
└── README.md            # Documentation

### Code information (app.py): 

blog_generate_using_bedrock(blogtopic)
Calls Claude on Amazon Bedrock to generate ~200 words blog.

save_blog_details_s3()
Saves blog text into S3 under blog_output/<timestamp>_blog.txt.

lambda_handler(event, context)
Handles API Gateway requests, extracts blogtopic, generates blog, saves result.


## How to Deploy & Test:
1. Setup Lambda

Create a new Lambda function (Python 3.12).

Upload app.py.

configuration for Admin access in Lambda function

2. Add Lambda Layer

Upload botolayer.zip as a Lambda Layer.

Integrate to lambda function.

<img width="1440" height="788" alt="image" src="https://github.com/user-attachments/assets/005e4cfa-0ed4-400e-92c3-a7e8b7aea6cb" />


3. Configure API Gateway

Create a POST method in API Gateway → connect to Lambda.
<img width="1440" height="788" alt="image" src="https://github.com/user-attachments/assets/9d6c3c4a-6374-47bd-a67d-95b5b19dba0a" />

<img width="1440" height="788" alt="image" src="https://github.com/user-attachments/assets/e883683c-cc67-4169-9a0a-440e4f89eac6" />

Deploy API and copy Invoke URL.

4. Create an S3 bucket
   <img width="1440" height="788" alt="image" src="https://github.com/user-attachments/assets/92baecea-87fb-4f61-b0cd-aec9a5374a3a" />


   <img width="1440" height="788" alt="image" src="https://github.com/user-attachments/assets/b3dd29e9-700e-4918-9def-15c6c5d447d9" />


5. Test with Postman
   <img width="2000" height="1096" alt="image" src="https://github.com/user-attachments/assets/803603bd-234a-4e48-8338-77bb9cb52bd6" />
  once the request is success we can see the generated output in our S3 Bucket
6. Montitor the logs using cloud watch
   <img width="1440" height="788" alt="image" src="https://github.com/user-attachments/assets/ed8b9cfb-80ae-409e-96d0-6ee806e19fb9" />

  once the request is success we can see the generated output in our S3 Bucket

