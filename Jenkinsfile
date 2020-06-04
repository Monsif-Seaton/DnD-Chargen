pipeline {
    agent any

    stages{

            stage('Dependencies'){
                agent {label 'master'}
                steps{
                    sh 'chmod +x ./scripts/*'
                    sh 'bash ./scripts/before_installation.sh'
                    sh './scripts/installation.sh'
                }
            }

            stage('Deploying Docker Compose'){
                steps{
                    sh 'chmod +x ./scripts/*'
                    sh './script/docker.sh'
                }
            }

    }
}
