pipeline {
  agent any
  stages {
    stage('build') {
      steps {
        echo 'Build..'
      }
    }
    stage('test') {
      steps {
        sh 'pytest --pylint'
      }   
    }
  }
}
