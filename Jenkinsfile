pipeline {
  agent { docker { image 'python:3.7.6'} }
  stages {
    stage('build') {
      steps('Make Virtual Env') {
        withEnv(["HOME=${env.WORKSPACE}"]) {
            sh 'pip3 install -r requirements.txt --user'
        }
      }
    }
    stage('test') {
      steps {
        withEnv(["HOME=${env.WORKSPACE}"]) {
            sh 'python3 testcalculator.py'
        }
      }
      post {
        always {
          junit 'test-reports/*.xml'
        }
      }
    }
  }
}