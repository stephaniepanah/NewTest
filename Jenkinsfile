pipeline {
    
    //agent "LocalMachine"
    agent { node { label 'LocalMachine' } }
                
        stages {
               
            stage('Checkout') {
                steps {
                    checkout([$class: 'GitSCM', branches: [[name: 'main']], extensions: [], 
                    userRemoteConfigs: [[url: 'https://github.com/stephaniepanah/NewTest.git']]]) 
                }
            }
            
            stage('Run PyTest') {
                steps {
                    // Run your pre-commit checks here, for example:
                    sh 'echo "Running pre-commit checks"'
                    sh 'pip install pytest'
                    sh 'pytest' // Run your tests, replace 'pytest' with the actual command to run your tests
                    // Add more pre-commit checks as needed
                }
            }
                    
            stage('Run Pre-commit Checks') {
                steps {
                    // Install pre-commit
                    sh 'pip install pre-commit'
                    //sh '/usr/bin/pip install pre-commit'
                    
                    // Run pre-commit checks
                    //sh 'pre-commit run --all-files'
                    sh 'pre-commit run'
                    //sh '/usr/bin/python3 -m pre-commit run --all-files'
                    //sh 'trailing-whitespace'
                    //sh 'check_added_large_files'
                }
            }
                    
            // stage('Build') {
            //     steps {
            //         git branch: 'main', url: 'https://github.com/vastevenson/pytest-intro-vs.git'
            //         sh 'python3 ops.py'
            //     }
            // }
            
            stage('Flake8') {
                agent {
                    docker {
                        image 'python:3.11.4' // Use appropriate Python version
                    }
                }
                steps {
                    script {
                        // Install Flake8 if not already installed
                        sh 'pip install -U flake8'

                        // Run Flake8 linting
                        sh 'flake8 "C:/DEV/pipelines/newtest"'
                    }
                }
                // steps {
                //     script {
                //         // Install Flake8 if not already installed
                //         sh '/usr/bin/pip install flake8'

                //         // Run Flake8 linting
                //         //sh 'flake8 .'
                //         sh '/usr/bin/python3 -m flake8'
                //     }
                // }
            }
                    
            stage('Run PyLint') {
                steps {
                    //sh 'python3 -m pytest'
                    sh 'pylint .'
                }
            }
            
        }
}