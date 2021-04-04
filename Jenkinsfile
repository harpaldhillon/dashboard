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
                            chartVars = readJSON file: "${WORKSPACE}/charts.json", returnPojo: true
                            print(chartVars)
                        }
                    }
                }
            }
        }
        stage('Checkout') {
            steps {
                container('helm'){
                script {

                   def repo_list = chartVars["repo"]

                    repo_list.each { key, value ->          
                        dir("$key"){
                            checkout([$class: 'GitSCM', branches: [[name: '*/master']], doGenerateSubmoduleConfigurations: false, extensions: [], submoduleCfg: [], userRemoteConfigs: [[credentialsId: 'sidhana-github', url: "https://github.com/harpaldhillon/${key}.git"]]])
                        
                            value.each{
                                ["bld", "int", "prd"].each {item->
                                    

                                    def cmd = "helm template -f " + "$it.override_path" + "/" + "$it.name" + "-${item}.yaml" + " --output-dir out-dir "  +  "$it.chart_path" + "/" + "$it.name"
                                
                                    sh "ls -ltr"

                                    //sh "$cmd"
                                }
                            }
                        }
                    }

                    //sh "ls -lart ./*"
                }
            }
            }
        }
    }
  }