pipeline {
  agent { docker { image 'jenkins:later' } }
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
            sh 'python testcalsulator.py'
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