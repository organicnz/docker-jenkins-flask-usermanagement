pipeline {
  agent { docker { image 'python:3.7.6'} }
  //Setting the environment variables DISABLE_AUTH and DB_ENGINE
  environment {
    FLASK_APP = "app.py"
    FLASK_ENV = "development"
  }
  stages {
    stage('build') {
      steps('Make Virtual Env') {
        withEnv(["HOME=${env.venv}"]) {
            sh 'pip3 install -r requirements.txt --user'
        }
      }
    }
    stage('test') {
      steps {
        withEnv(["HOME=${env.venv}"]) {
            sh 'flask run'
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