node() {
  stage('checkout') {
    deleteDir()
    checkout scm
  }
  stage('build') {
    sh "python pylint.py"
  }
  stage('publish') {
    junit 'reports/*.xml'
  }
}
