# Devops position - Practical task Walkthrough
## Python Application
* Clone the following repository locally: https://github.com/Thomas2499/my-flask-application
* In the working directory - build a new image from the appended _Dockerfile_:
````
docker build -t my-flask-application:0.1 .
````

* Run a container with the newly created image:
````
docker run -d -p 8000:2499 my-flask-application:0.1
````

## AWS URLs
* **Cloudfront:** https://dqtfg5p8bwuqh.cloudfront.net
* **ECS cluster:** https://eu-central-1.console.aws.amazon.com/ecs/home?region=eu-central-1#/clusters/flask-message-response/services
* **S3 bucket:** https://s3.console.aws.amazon.com/s3/buckets/www.salt-security-homepage?region=eu-central-1&tab=objects