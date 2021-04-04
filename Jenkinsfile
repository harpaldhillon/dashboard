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
                script {

                   def repo_list = chartVars["repo"]

                    repo_list.each { key, value ->
                    
                    println("************************")
                    
                    echo "$key"
                    echo "$value.name"
                    echo "$value.chart_path"
                    echo "$value.override_path"
                    
                    
                    dir("$key"){
                        checkout([$class: 'GitSCM', branches: [[name: '*/master']], doGenerateSubmoduleConfigurations: false, extensions: [], submoduleCfg: [], userRemoteConfigs: [[credentialsId: 'sidhana-github', url: "https://github.com/harpaldhillon/${key}.git"]]])
                    
                        ["bld", "int", "prd"].each {
                            def cmd = "helm template -f " + "$value.override_path" + "/" + "$value.name" + "-${it}.yaml" + " --output-dir out "  +  "$value.chart_path" + "/" + "$value.name"
                        
                            println(cmd)
                        }
                    }
                    }

                    sh "ls -lart ./*"
                }
            }
        }
    }
  }