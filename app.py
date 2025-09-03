import boto3 #used to invoke foundation model from AWS Bedrock
import botocore.config 
import json
from datetime import datetime


# i need to create a blog

def blog_generate_using_bedrock(blogtopic:str)->str:
    prompt=f"""
    <s>[INST]Human: Write a 200 words blog on the topic {blogtopic}
    Assistant:[/INST]
"""
    # body =  {
    #     "inputText":prompt,
    #     "dimensions": 512,
    #     "normalize": True
    # } #amazon.titan-embed-text-v2:0 model for text embedding

    #using boto to invoke bedrock foundation model amazon.titan-embed-text-v2:0


    body ={
    "anthropic_version": "bedrock-2023-05-31",
    "max_tokens": 200,
    "top_k": 250,
    "stop_sequences": [],
    "temperature": 1,
    "top_p": 0.999,
    "messages": [
      {
        "role": "user",
        "content": [
          {
            "type": "text",
            "text": prompt
          }
        ]
      }
    ]
  }

    try:
        bedrock = boto3.client("bedrock-runtime", region_name="eu-north-1",
                               config=botocore.config.Config(read_timeout=300, 
                                                             retries={"max_attempts": 3}))
        # response=bedrock.invoke_model(body=json.dumps(body), modelId="amazon.titan-embed-text-v2:0") for text embedding
        response=bedrock.invoke_model(body=json.dumps(body), modelId="eu.anthropic.claude-sonnet-4-20250514-v1:0")
        response_content=response.get("body").read()
        response_data=json.loads(response_content)
        print(response_data)
        blog_details=response_data["content"][0]["text"]
        return blog_details
    except Exception as e:
        print(e)
        return "Error generating blog"

def save_blog_details_s3(s3_key, s3_bucket,generate_blog):
    s3=boto3.client("s3")
    try:
        s3.put_object(Bucket=s3_bucket, Key=s3_key, Body=generate_blog) #
        print(f"Blog saved to S3 bucket {s3_bucket} with key {s3_key}")
        return True
    except Exception as e:
        print(e)
        return False

def lambda_handler(event, context):
    event=json.loads(event['body'])
    blogtopic=event["blogtopic"]
    generate_blog=blog_generate_using_bedrock(blogtopic)

    if generate_blog:
        #save it in S3 bucket
        current_time=datetime.now().strftime("%H%M%S")
        s3_key=f"blog_output/{current_time}_blog.txt"
        s3_bucket="awsbedrocklearning"
        save_blog_details_s3(s3_key, s3_bucket,generate_blog)
    else:
        print("no blog generated")

    return {
        'statusCode': 200,
        'body': json.dumps('blog generated!')
    }

    