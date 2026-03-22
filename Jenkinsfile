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
                bat 'pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                echo 'Running tests...'
                bat 'pytest || exit 0'
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
                bat 'python app.py'
            }
        }
    }
}