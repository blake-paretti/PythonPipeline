pipeline {
    agent {
        docker {
            image 'node:6-alpine' 
            args '-p 8080:8080' 
        }
    }
    stages {
        stage('Run') { 
            steps {
                sh 'python HelloWorld.py' 
            }
        }
    }
}
