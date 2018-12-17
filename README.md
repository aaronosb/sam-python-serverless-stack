# sam-python-serverless-stack
In this project I set up the backend and AWS Services needed to 
build the serverless Notes application found [here](https://serverless-stack.com/) 
but instead of using a Node.js backend and the serverless.com framework
I use a Python backend and the AWS SAM framework.   
  
The combination of this project and the frontend put together [here](https://github.com/AnomalyInnovations/serverless-stack-demo-client)
serve as a good example project for a Serverless Web Application built on AWS with the SAM Framework. 

### AWS Services Used
- Lambda
- DynamoDB
- API Gateway
- Cognito 
- IAM
- S3
- Amplify

### Prerequisites 
1. [AWS SAM CLI (and its prereqs Docker and AWS CLI)](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html)
1. Optional see notes [PyCharm IDE](https://www.jetbrains.com/pycharm/) or
of the other IDEs that have an AWS Toolkit Plugin
1. [AWS Toolkit Plugin for PyCharm](https://aws.amazon.com/pycharm/) 
you should also be able to find this on the Pycharm Plugins Marketplace. 
Settings -> Plugins -> Marketplace


### Notes
- Python Version 3.6 used 
- You can used SAM CLI for all the build and deployment I used 
the [AWS Toolkit for PyCharm](https://aws.amazon.com/pycharm/)
because the deployment is built into the IDE and you can use
it to set breakpoints and debug lambda functions locally or 
deployed remotely.

### Steps

#### Environment Setup
Clone the repo  
``` bash
$ git clone https://github.com/aaronosb/sam-python-serverless-stack
```

Open the project in PyCharm [Insert Photo]

Mark the lambda folder as sources root (right click folder ->
 Mark Directory As -> Sources Root) [Insert Photo]

 
#### Backend Deployment 

To deploy the stack right click on the project and select 
**Deploy Serverless Application** [Insert Photo]

Select **Create Stack** and give the stack a name like sam-serverless-test

Create an S3 Bucket to be used to upload the code for your lambda functions [Inset Photo]

Then select **Deploy**

After it is completed you should be able to go into the AWS Console
see the stack deployed as well as get the outputs from the **Outputs** 
that will be needed when configuring the React frontend application.
 
#### Frontend Deployment
Now you are ready to connect the react frontend to these services 
you've deployed via [AWS Amplify](https://aws-amplify.github.io/).

The first step is to clone the repository with the frontend application
(into a seperate directory) and install the NPM packages .
``` bash
$ git clone clone https://github.com/AnomalyInnovations/serverless-stack-demo-client
$ npm install
```

Then replace **serverless-stack-demo-client/src/config.js** with the
following fill in all the outputs from the stack that was deployed
with the SAM. Ignore the STRIPE_KEY and BUCKET for now if you would 
like to see info on how to implement them check out https://serverless-stack.com:
``` javascript
export default {
  MAX_ATTACHMENT_SIZE: 5000000,
  STRIPE_KEY: "not_implemented",
  s3: {
    REGION: "us-east-1",
    BUCKET: "not_implemented"
  },
  apiGateway: {
    REGION: "us-east-1",
    URL: "SAM_TEMPLATE_OUTPUT_1"
  },
  cognito: {
    REGION: "us-east-1",
    USER_POOL_ID: "SAM_TEMPLATE_OUTPUT_4",
    APP_CLIENT_ID: "SAM_TEMPLATE_OUTPUT_5",
    IDENTITY_POOL_ID: "SAM_TEMPLATE_OUTPUT_3"
  }
};

```

Once that is done you can run it locally
``` bash
$ npm run start
```

#### Using the Application

First thing you will need to do is sign up. You can do so by 
either using a real email address so that you can verify it
when it goes to create the coginto user or use the AWS CLI 
to create a test user [guide on this here](https://serverless-stack.com/chapters/create-a-cognito-test-user.html).

Then when you log in you should be able to Create, Edit, and Delete
notes in the notes application. 

[Insert GIF here]

*with S3 bucket not set up adding attachments will not work* 

After playing around a bit and creating some notes, go back into
the AWS Console and check on the DynamoDB Table to see the records
being stored there.

That's it, from here edit away or use this project as a template
for your next AWS SAM Serverless Web Application.

 
### Tips
- Debugging errors on deployment (deleting stack if in Rollback_Complete)
- Testing/Debugging Lambda with AWS Toolkit on PyCharm 
- Cloud watch logs


### Resources
- https://github.com/AnomalyInnovations/serverless-stack-demo-api
- https://github.com/AnomalyInnovations/serverless-stack-demo-client
- https://github.com/aws-samples/aws-cognito-apigw-angular-auth
- https://github.com/awslabs/serverless-application-model

### TODOs
- Finish S3 bucket for attachments
- Write Unit Tests for Lambda Functions
- Attempt to get template.yaml to work by using implicit API Gateway provisioned with AWS::Serverless::Function rather than specifing explicitly NotesApi as a AWS::Serverless::Api resource
- Tailor Dynamo permissions per lambda function