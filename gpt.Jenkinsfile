pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Setup') {
            steps {
                sh '''
                python3 -m venv venv
                . venv/bin/activate

                pip install --upgrade pip
                pip install -r requirements.txt
                '''
            }
        }

        stage('Build') {
            steps {
                sh '''
                . venv/bin/activate

                python -m py_compile *.py
                '''
            }
        }

        stage('Test') {
            steps {
                sh '''
                . venv/bin/activate

                pytest
                '''
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deploy stage placeholder'
            }
        }
    }
}