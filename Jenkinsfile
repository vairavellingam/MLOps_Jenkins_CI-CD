@Library('jenkins-shared') _

pipeline {
    agent any
    environment {
        DOCKER_REPO = "vel23/mlops-jenkins-shared-library-project"
    }
    stages {
        stage('Checkout') {
            steps {
                gitCheckout('https://github.com/vairavellingam/MLOps_Jenkins_CI-CD.git','*/main','github-token')

            }
        }

        stage('Build & Push Image') {
            steps {
                dockerBuildAndPush(DOCKER_REPO,'dockerhub-token')
            }
        }

        stage('Install Kubectl') {
            steps {
               installKubectl()
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                k8sDeploy('kubeconfig')
            }
        }
    }
}