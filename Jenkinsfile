pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                checkout([$class: 'GitSCM', branches: [[name: 'main']], extensions: [], u
                serRemoteConfigs: [[url: 'https://github.com/vastevenson/pytest-intro-vs.git']]])
            }
        }

        stage('Pre-commit Build') {
                steps {
                    // Install pre-commit
                    sh 'pip3 install pre-commit'
                    //sh '/usr/bin/pip3 install pre-commit'
                    
                    // Run pre-commit checks
                    
                    sh 'python3 -m pre-commit run --all-files'
                    //sh '/usr/bin/python3 -m pre-commit run --all-files'
                    
                    //sh 'trailing-whitespace'
                    //sh 'check_added_large_files'
                }
        }

        stage('Build') {
            steps {
                git branch: 'main', url: 'https://github.com/vastevenson/pytest-intro-vs.git'
                sh 'python3 ops.py'
            }
        }

        stage('Lint') {
            agent {
                docker {
                    image 'python:3.9.9' // Use appropriate Python version
                    }
            }
            steps {
                script {
                    // Install Flake8 if not already installed
                    sh 'pip install -U flake8'

                    // Run Flake8 linting
                    sh 'flake8 "C:/DEV/JenkinsTest/jenkins"'
                }
            }
        }

        stage('Test') {
            steps {
                sh 'python3 -m pytest'
            }
        }

        
    }
}
