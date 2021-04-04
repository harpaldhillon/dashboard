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
                            
                            sh "ls -ltr"

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

                    //value.each{ key1,value1 ->
                    //echo "Walked through key $key1 and value $value1"
                    //}

                    }
                }
            }
        }
    }
  }