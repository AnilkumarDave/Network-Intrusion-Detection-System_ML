pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Run NIDS API Tests') {
            steps {
                dir('automation') {
                    sh 'mvn clean test'
                }
            }
        }
    }

    post {
        always {
            junit 'automation/target/surefire-reports/*.xml'
        }
    }
}
