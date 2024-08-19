eb-python-flask
===============
Simple Python and Flask sample application from [AWS Elastic Beanstalk Developer Guide](http://docs.aws.amazon.com/elasticbeanstalk/latest/dg/create_deploy_Python_flask.html)

## SQL Init
```
CREATE TABLE user (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(255) NOT NULL UNIQUE,
    email VARCHAR(255)
);

INSERT INTO user (username, email) VALUES ('johndoe', 'johndoe@example.com');
INSERT INTO user (username, email) VALUES ('janedoe', 'janedoe@example.com');
INSERT INTO user (username, email) VALUES ('alice', 'alice@example.com');
INSERT INTO user (username, email) VALUES ('bob', 'bob@example.com');
```
