node() {
  stage('checkout') {
    deleteDir()
    checkout scm
  }
  stage('build') {
    sh 'virtualenv venv && . venv/bin/activate && pip install -r requirements.txt && python pylint.py'
  }
  stage('publish') {
    junit 'reports/*.xml'
  }
}
