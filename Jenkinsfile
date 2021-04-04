// Uses Declarative syntax to run commands inside a container.
//

import groovy.json.JsonSlurper


def chartVars = ""

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
                            chartVars = readJSON file: "${WORKSPACE}/charts.json"
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

                    
                    repo_list.each{entry ->
                        println("$entry.key")
                        
                        dir("$entry.key"){
                          checkout([$class: 'GitSCM', branches: [[name: '*/master']], doGenerateSubmoduleConfigurations: false, extensions: [], submoduleCfg: [], userRemoteConfigs: [[credentialsId: 'sidhana-github', url: "https://github.com/harpaldhillon/${entry.key}.git"]]])
                        }
                    }

                    

                     
                    // dir('data'){
                    //     checkout([$class: 'GitSCM', branches: [[name: '*/master']], doGenerateSubmoduleConfigurations: false, extensions: [], submoduleCfg: [], userRemoteConfigs: [[credentialsId: 'sidhana-github', url: 'https://github.com/harpaldhillon/data.git']]])
                    // }
                    // sh "ls -lart ./*"
                }
            }
        }
    }
  }
