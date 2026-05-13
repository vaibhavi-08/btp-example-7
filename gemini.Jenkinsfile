pipeline {
    agent any

    environment {
        VENV = 'venv'
    }

    stages {
        stage('Checkout') {
            steps {
                // Uses the SCM configuration defined in the Jenkins Job UI
                checkout scm
            }
        }

        stage('Setup') {
            steps {
                script {
                    echo 'Setting up Python virtual environment...'
                    sh """
                        python3 -m venv ${VENV}
                        . ${VENV}/bin/activate
                        pip install --upgrade pip
                    """
                    
                    if ("true" == "true") {
                        sh ". ${VENV}/bin/activate && pip install -r requirements.txt"
                    }
                }
            }
        }

        stage('Quality') {
            steps {
                script {
                    // flake8 is false in config
                    echo 'Quality check (Flake8) is disabled. Skipping...'
                }
            }
        }

        stage('Build') {
            steps {
                script {
                    echo 'Compiling Python source...'
                    sh ". ${VENV}/bin/activate && python3 -m compileall ."
                }
            }
        }

        stage('Test') {
            steps {
                script {
                    echo 'Running Tests...'
                    // Since tests is true, we run a standard test runner like pytest or unittest
                    // This assumes you have a testing framework installed via requirements.txt
                    sh ". ${VENV}/bin/activate && python3 -m pytest || python3 -m unittest discover"
                }
            }
        }

        stage('Deploy') {
            steps {
                script {
                    echo 'Deploying to Ubuntu environment...'
                    // Placeholder for your deployment logic
                }
            }
        }
    }

    post {
        always {
            echo 'Pipeline execution finished.'
        }
        failure {
            echo 'Build or Test failed. Reviewing logs is recommended.'
        }
    }
}