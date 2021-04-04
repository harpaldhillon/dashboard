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

                           // def s = new File("${WORKSPACE}/charts.json").text

                           // def obj = new groovy.json.JsonSlurper().parseText(s)
                           // repos = obj["repo"]

                           // println(repos)

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
                    echo "Walked through key $key and value $value"

                   // value.each {key1,value1 ->
                    //echo "Walked through key $key1 and value $value1"
                    //}
            }

                    /*
                    repo_list.each{entry ->
                      //   println("$entry.key")
                     //   println("$entry.value"[0])

                        //println(str)

                        //def a = str.trim().replaceAll(~/^\[|\]$/, '').split(',').collect{ it.trim()}

                        //println(a)

                        //println(a.getClass())

                        //println(a[0])

                        // for (i = 0; i < a.size(); i++){
                        //     a[i].each{entry1 ->
                        //       println("$entry1")
                        //     }
                        // }

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
                    //}
                    sh "ls -lart ./*"
                }
            }
        }
    }
  }
