node() {
  stage('checkout') {
    deleteDir()
    checkout scm
  }
  stage('build') {
    sh 'pytest --pylint'
  }
  stage('publish') {
    junit 'reports/*.xml'
  }
