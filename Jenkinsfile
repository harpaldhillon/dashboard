// Uses Declarative syntax to run commands inside a container.
//
pipeline {
    agent {
        kubernetes {
            yaml '''
apiVersion: v1
kind: Pod
spec:
  containers:
  - name: helm
    image: alpine/helm
    command:
    - sleep
    args:
    - infinity
  - name: shell
    image: ubuntu
    command:
    - sleep
    args:
    - infinity
'''
            defaultContainer 'shell'
        }
    }
    stages {
        stage('Main') {
            steps {
                container('shell'){
                    script {
                        timestamps {
                            def chartVars = readJSON file: "${WORKSPACE}/charts.json"
                            print(chartVars)
                        }
                    }
                }
            }
        }
        stage('Checkout') {
            steps {
                script {

                    def repo_list = chartVars["repo"]

                    for (i = 0; i < repo_list.size(); i++)
                    {
                        print(repo_list[i])
                    }

                    // dir('cco'){
                    //     checkout([$class: 'GitSCM', branches: [[name: '*/master']], doGenerateSubmoduleConfigurations: false, extensions: [], submoduleCfg: [], userRemoteConfigs: [[credentialsId: 'sidhana-github', url: 'https://github.com/harpaldhillon/cco.git']]])
                    // }
                    // dir('data'){
                    //     checkout([$class: 'GitSCM', branches: [[name: '*/master']], doGenerateSubmoduleConfigurations: false, extensions: [], submoduleCfg: [], userRemoteConfigs: [[credentialsId: 'sidhana-github', url: 'https://github.com/harpaldhillon/data.git']]])
                    // }
                    // sh "ls -lart ./*"
                }
            }
        }
    }
  }
