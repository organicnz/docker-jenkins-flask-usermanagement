pipeline {
  agent { docker { image 'python:3.7.6'} }
  // Setting the environment variables DISABLE_AUTH and DB_ENGINE
  environment {
    FLASK_APP = "app.py"
    FLASK_ENV = "development"
  }
  stages {
    stage('build') {
      steps('Make Virtual Env') {
        withEnv(["HOME=${env.WORKSPACE}"]) {
            sh 'pip3 install -r requirements.txt --user'
            sh 'pip3 install flask'
            sh 'pip3 install numpy pytest'
        }
      }
    }
    stage('test') {
      steps {
        withEnv(["HOME=${env.WORKSPACE}"]) {
            sh 'pytest -v'
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