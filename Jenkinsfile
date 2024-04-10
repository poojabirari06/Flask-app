pipeline {
    agent any
    stages{
        stage('code'){
            steps{
                git url: 'https://github.com/poojabirari06/Flask-app.git', branch: 'main', credentialsId: 'poojabirari06'
            }
        }
        
        stage('Build'){
            steps{
                sh 'docker build -t  my-ecr-repo .'
            }
        }
        stage('Tag'){
            steps{
                sh 'docker tag my-ecr-repo:latest 211125338459.dkr.ecr.us-east-1.amazonaws.com/my-ecr-repo:latest'
            }
        }
        stage('Login'){
            steps{
                sh 'aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin 211125338459.dkr.ecr.us-east-1.amazonaws.com'
            }
        }
        stage('Push'){
            steps{
                sh 'docker push 211125338459.dkr.ecr.us-east-1.amazonaws.com/my-ecr-repo:latest'
            }
        }
        stage('Deploy'){
            steps{
                sh 'aws autoscaling start-instance-refresh --auto-scaling-group-name terraform_asg' 
            }
    }
}
}