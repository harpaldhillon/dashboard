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

                    value.each{
                        //echo "$it.name"
                        //echo "$it.chart_path"
                        //echo "$it.override_path"

                        ["bld", "int", "prd"].each {item->
                            echo "$item:$it.name"

                            def cmd = "helm template -f " + "$it.override_path" + "/" + "$it.name" + "-${item}.yaml" + " --output-dir out "  +  "$it.chart_path" + "/" + "$it.name"
                        
                            println(cmd)
                        }
                    }
                    
                    
                    dir("$key"){
                        checkout([$class: 'GitSCM', branches: [[name: '*/master']], doGenerateSubmoduleConfigurations: false, extensions: [], submoduleCfg: [], userRemoteConfigs: [[credentialsId: 'sidhana-github', url: "https://github.com/harpaldhillon/${key}.git"]]])
                    
                        // ["bld", "int", "prd"].each {
                            
                        //     value.each{
                        //         def cmd = "helm template -f " + "$value.override_path" + "/" + "$value.name" + "-${it}.yaml" + " --output-dir out "  +  "$value.chart_path" + "/" + "$value.name"
                            
                        //         println(cmd)
                        //     }
                        // }
                    }
                    }

                    sh "ls -lart ./*"
                }
            }
        }
    }
  }