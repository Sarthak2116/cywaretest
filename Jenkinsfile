pipeline {
  environment {
    imagename = "sarthak321321/nginxtest"
    registryCredential = 'xxxxx'   // to be configured in jenkins
    dockerImage = ''
  }
  agent any
  stages {
    stage('Cloning Git') {
      steps {
        git([url: 'https://github.com/sarthak2116/cyware.git', branch: 'main', credentialsId: 'xxxxxx'])
 
      }
    }
    stage('Building image') {
      steps{
        script {
          dockerImage = docker.build imagename
        }
      }
    }
    stage('Running Unit tests') {
      steps{
        script {
          // Write unit tests here 
        }
      }
    }
    stage('Deploy Image') {
      steps{
        script {
          docker.withRegistry( '', registryCredential ) {
            dockerImage.push("$BUILD_NUMBER")
             dockerImage.push('latest')
          }
        }
      }
    }
    stage('Remove Unused docker image') {
      steps{
        sh "docker rmi $imagename:$BUILD_NUMBER"
         sh "docker rmi $imagename:latest"
 
      }
    }
  }
}