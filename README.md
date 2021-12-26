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
* **ECS Service:** http://ec2co-ecsel-1fynt14td8kh1-1056333738.eu-central-1.elb.amazonaws.com:2499/v1/test