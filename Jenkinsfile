node() {
  stage('checkout') {
    deleteDir()
    checkout scm
  }
  stage('build') {
    sh "pylint.py"
  }
  stage('publish') {
    junit 'reports/*.xml'
  }
}
