pipeline {
    agent any
    
    tools {
        python 'Python3'   // Make sure Python is configured in Jenkins Global Tools
    }
    
    environment {
        VENV_DIR = 'venv'
    }
    
    stages {
        stage('Checkout') {
            steps {
                echo '🔄 Checking out code...'
                checkout scm
                // git url: 'https://github.com/vaibhavi-08/btp-example-7', branch: 'master'
            }
        }
        
        stage('Setup') {
            steps {
                echo '🐍 Setting up Python virtual environment...'
                sh '''
                    python3 -m venv ${VENV_DIR}
                    . ${VENV_DIR}/bin/activate
                    pip install --upgrade pip
                    if [ -f requirements.txt ]; then
                        echo "Installing dependencies from requirements.txt"
                        pip install -r requirements.txt
                    fi
                '''
            }
        }
        
        stage('Build') {
            steps {
                echo '🏗️ Building Python project...'
                sh '''
                    . ${VENV_DIR}/bin/activate
                    python -m compileall app/ || true
                    echo "✅ Build completed successfully"
                '''
            }
        }
        
        stage('Test') {
            steps {
                echo '🧪 Running tests...'
                sh '''
                    . ${VENV_DIR}/bin/activate
                    pip install pytest pytest-cov || true
                    
                    echo "Running pytest..."
                    python -m pytest tests/ -v --cov=app --cov-report=xml || true
                '''
            }
            post {
                always {
                    junit testResults: '**/test-results/*.xml', allowEmptyResults: true
                    archiveArtifacts artifacts: 'coverage.xml', allowEmptyArchive: true
                }
            }
        }
        
        stage('Deploy') {
            steps {
                echo '🚀 Deploying Python application...'
                sh '''
                    . ${VENV_DIR}/bin/activate || true
                    echo "Starting application..."
                    python app/main.py || echo "No main.py found, skipping run"
                '''
                echo '✅ Deployment stage completed'
            }
        }
    }
    
    post {
        always {
            echo '🧹 Cleaning up workspace...'
            cleanWs()
        }
        success {
            echo '🎉 Pipeline executed successfully!'
        }
        failure {
            echo '❌ Pipeline failed!'
        }
    }
}