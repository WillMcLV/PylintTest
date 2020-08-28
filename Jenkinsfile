// Creating Pipeline
pipeline {
    // Set up the docker agent Jenkins will run on
    // agent { docker { image 'python:3.8' } }
    agent any
    
    stages {
        stage('Initialize') {
            steps {
                echo 'Building..'
            }
        }
        stage('Build') {
            steps {
                echo 'Building..'
                sh 'python --version'
            }
        }
        stage('Test') {
            steps {
                echo 'Testing..'
                // Run pylint
                sh 'pylint --junitxml=pylint.xml'
                // Run pycodestyle
                // sh 'pycodestyle --junitxml=pycodestyle.xml'
                // Run pydocstyle
                // sh 'pydocstyle --junitxml=pydocstyle.xml'
            }
            post {
                always {
                    junit 'pylint.xml'
                }
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying....'
                // Push to dockerhub image repository with tags per mergeid/featurebranch or etc
                }
            }                
        }
    }
}

// Scripted Pipeline
// node {
//      Stage 'Checkout'
//          echo 'Checkout Stage'
//          checkout scm

//      Stage 'Build'
//          echo 'Building Stage'
//          sh 'python --version'

//      Stage 'Test'
//          echo 'Test Stage'
//          //Pylint here

//      Stage 'Deploy'
//          echo 'Test Stage'

// }
