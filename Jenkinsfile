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
                        def str = "$entry.value"

                        def a = str.trim().replaceAll(~/^\[|\]$/, '').split(',').collect{ it.trim()}

                        println(a)

                        println(a.getClass())


                        //def obj = new groovy.json.JsonSlurper().parseText("$entry.value".toString())

                        //println(obj.getClass())

                        //println("$entry.value")


                        //for (i = 0; i < "${entry.value}".size(); i++){
                      
                        //     println("${entry.value}"[i])

                        //}

                        //println("${entry.value}".size())
                        
                        //dir("$entry.key"){
                        //  checkout([$class: 'GitSCM', branches: [[name: '*/master']], doGenerateSubmoduleConfigurations: false, extensions: [], submoduleCfg: [], userRemoteConfigs: [[credentialsId: 'sidhana-github', url: "https://github.com/harpaldhillon/${entry.key}.git"]]])
                        //}
                    }
                    sh "ls -lart ./*"
                }
            }
        }
    }
  }
