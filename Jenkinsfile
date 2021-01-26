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
        
        stage('Calculator Test'){
            steps{
                sh 'python Calculator.py'   
            }
        }
        
        stage('Say Goodbye!'){
            steps{
                sh 'python GoodbyeWorld.py'   
            }
        }
    }
}
