node() {
  stage('checkout') {
    deleteDir()
    checkout scm
  }
  stage('build') {
    sh "pylint"
  }
  stage('publish') {
    junit 'reports/*.xml'
  }
}
