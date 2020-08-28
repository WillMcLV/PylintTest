// Creating Pipeline
pipeline {
    // Set up the docker agent Jenkins will run on
    // agent { docker { image 'python:3.8' } }
    agent none
    environment {
        VERSION_NO         = '1.0'
        // repo User/RepoName
        repo               = "mariof/TP-Crucible"
        registryCredential = 'dockerhub'
        dockerImg          = ''

    }

    stages {
        stage('Initialize') {
            agent { dockerfile true }
            steps {
                script {
                    def dockerHome = tool 'myDocker'
                    env.PATH = "${dockerHome}/bin:${env.PATH}"
                }
            }
        }
        stage('Build') {
            agent { dockerfile true }
            steps {
                echo 'Building..'
                sh 'python --version'
            }
        }
        stage('Test') {
            agent { dockerfile true }
            steps {
                echo 'Testing..'
                // Run pylint
                sh 'pylint --junitxml=pylint.xml'
                // Run pycodestyle
                sh 'pycodestyle --junitxml=pycodestyle.xml'
                // Run pydocstyle
                sh 'pydocstyle --junitxml=pydocstyle.xml'
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
                // Push to dockerhub image repository with tags per mergeid/featurebranch or etc.
                script{
                    dockerImg = docker.build repo+":$BUILD_NUMBER"
                    docker.withRegistry( '', registryCredential ) {
                        dockerImg.push()
                    }
                    sh 'docker rmi $repo:BUILD_NUMBER'
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
