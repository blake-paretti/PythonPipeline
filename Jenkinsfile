pipeline {
    agent { docker { image 'python:3.5.1' } }
    stages {
        stage('build') {
            steps {
                sh 'python --version'
            }
        }
        stage('Say Hello!'){
            steps{
                sh 'python HelloWorld.py'   
            }
        }
        
        stage('Unit Test?'){
            steps{
                sh 'python Unit_Test.py'   
            }
        }
        
        stage('Say Goodbye!'){
            steps{
                sh 'python GoodbyeWorld.py'   
            }
        }
    }
}
