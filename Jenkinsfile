pipeline {
  agent any
  stages {
    stage('build') {
      steps {
        sh 'echo build'
      }
    }
    stage('testing') {
      parallel {
        stage('testing') {
          steps {
            sh 'echo test'
          }
        }
        stage('performance') {
          steps {
            sh 'echo performance'
          }
        }
      }
    }
    stage('static analysis') {
      steps {
        sh 'echo sonarqube'
      }
    }
    stage('deploy') {
      steps {
        sh 'echo deploy'
      }
    }
  }
}