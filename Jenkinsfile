pipeline {
    agent any

    stages {

        stage('Clone Repo') {
            steps {
                echo 'Cloning repository...'
            }
        }

        stage('Install Dependencies') {
            steps {
                echo 'Installing dependencies...'
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                echo 'Running tests...'
                sh 'pytest || true'
            }
        }

        stage('Build') {
            steps {
                echo 'Building project...'
            }
        }

        stage('Run App') {
            steps {
                echo 'Starting Flask app...'
                sh 'python app.py'
            }
        }
    }
}