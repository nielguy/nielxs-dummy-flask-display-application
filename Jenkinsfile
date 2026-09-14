pipeline {
    agent any

    stages {
        stage('AI Optimization Evaluation') {
            steps {
                script {
                    def actualDiff = ""
                    try {
                        actualDiff = sh(
                            script: '''
                                if git rev-parse HEAD~1 >/dev/null 2>&1; then
                                    git diff HEAD~1 HEAD
                                else
                                    echo "No previous commit found."
                                fi
                            ''',
                            returnStdout: true
                        ).trim()
                    } catch (Exception e) {
                        actualDiff = "No diff available."
                    }

                    if (!actualDiff) {
                        actualDiff = "No diff available or initial commit."
                    }

                    // Securely inject Jenkins credentials using the credentials plugin to bypass CSRF via Basic Auth
                    withCredentials([usernamePassword(credentialsId: 'jenkins-api-token-creds', usernameVariable: 'JENKINS_USER', passwordVariable: 'JENKINS_TOKEN')]) {

                        // Construct callback URL embedding credentials for HTTP Basic Auth (which automatically bypasses CSRF in Jenkins 2.96+)
                        def callbackUrl = "http://${env.JENKINS_USER}:${env.JENKINS_TOKEN}@host.docker.internal:8080/job/${env.JOB_NAME}/${env.BUILD_NUMBER}/input/WebhookInput/proceed"

                        def payloadJson = groovy.json.JsonOutput.toJson([
                            code_diff: actualDiff,
                            callback_url: callbackUrl
                        ])
                        writeFile file: 'payload.json', text: payloadJson

                        // Submit task to FastAPI (Fire and Forget)
                        sh 'curl -s -X POST -H "Content-Type: application/json" -d @payload.json http://host.docker.internal:8000/evaluate_stages'

                        echo "AI Evaluation queued. Pausing pipeline with circuit breaker timeout..."

                        def approvedStages = []
                        try {
                            timeout(time: 5, unit: 'MINUTES') {
                                def aiResponse = input(
                                    id: 'WebhookInput',
                                    message: 'Waiting for AI Pipeline Optimizer Webhook...',
                                    parameters: [
                                        string(name: 'approved_stages', description: 'JSON string of approved stages from Celery webhook')
                                    ]
                                )
                                def parsed = new groovy.json.JsonSlurper().parseText(aiResponse)
                                approvedStages = parsed.approved_stages ?: []
                            }
                        } catch (org.jenkinsci.plugins.workflow.steps.FlowInterruptedException timeoutErr) {
                            echo "CRITICAL: AI optimization service timed out. Circuit breaker tripped: falling back to full pipeline execution."
                            approvedStages = [
                                "Validate", "Validate base image signatures", "Start Database",
                                "Pod operations", "Certificate", "Static code analysis", "OSSG scan",
                                "Build", "Push", "Vulnerability scan", "Sign container",
                                "Manage and sync with ArgoCD", "Post deploy", "Update APIHub",
                                "Dast passive scan", "Dast cryptography scan", "Promote image"
                            ]
                        } catch (err) {
                            echo "Warning: Webhook error encountered (${err.message}). Falling back to all stages."
                            approvedStages = [
                                "Validate", "Validate base image signatures", "Start Database",
                                "Pod operations", "Certificate", "Static code analysis", "OSSG scan",
                                "Build", "Push", "Vulnerability scan", "Sign container",
                                "Manage and sync with ArgoCD", "Post deploy", "Update APIHub",
                                "Dast passive scan", "Dast cryptography scan", "Promote image"
                            ]
                        }

                        env.APPROVED_STAGES_STR = approvedStages.join(',')
                    }
                }
            }
        }

        stage('Validate') {
            when {
                expression {
                    def approvedList = env.APPROVED_STAGES_STR ? env.APPROVED_STAGES_STR.split(',') as List : []
                    return approvedList.contains('Validate')
                }
            }
            steps {
                echo "Executing Validate..."
                sleep(time: 3, unit: 'SECONDS')
            }
        }

        stage('Validate base image signatures') {
            when {
                expression {
                    def approvedList = env.APPROVED_STAGES_STR ? env.APPROVED_STAGES_STR.split(',') as List : []
                    return approvedList.contains('Validate base image signatures')
                }
            }
            steps {
                echo "Executing Validate base image signatures..."
                sleep(time: 4, unit: 'SECONDS')
            }
        }

        stage('Static code analysis') {
            when {
                expression {
                    def approvedList = env.APPROVED_STAGES_STR ? env.APPROVED_STAGES_STR.split(',') as List : []
                    return approvedList.contains('Static code analysis')
                }
            }
            steps {
                echo "Executing Static code analysis..."
                sleep(time: 10, unit: 'SECONDS')
            }
        }

        stage('Start Database') {
            when {
                expression {
                    def approvedList = env.APPROVED_STAGES_STR ? env.APPROVED_STAGES_STR.split(',') as List : []
                    return approvedList.contains('Start Database')
                }
            }
            steps {
                echo "Executing Start Database..."
                sleep(time: 5, unit: 'SECONDS')
            }
        }

        stage('Pod operations') {
            when {
                expression {
                    def approvedList = env.APPROVED_STAGES_STR ? env.APPROVED_STAGES_STR.split(',') as List : []
                    return approvedList.contains('Pod operations')
                }
            }
            steps {
                echo "Executing Pod operations..."
                sleep(time: 6, unit: 'SECONDS')
            }
        }

        stage('Certificate') {
            when {
                expression {
                    def approvedList = env.APPROVED_STAGES_STR ? env.APPROVED_STAGES_STR.split(',') as List : []
                    return approvedList.contains('Certificate')
                }
            }
            steps {
                echo "Executing Certificate..."
                sleep(time: 2, unit: 'SECONDS')
            }
        }

        stage('OSSG scan') {
            when {
                expression {
                    def approvedList = env.APPROVED_STAGES_STR ? env.APPROVED_STAGES_STR.split(',') as List : []
                    return approvedList.contains('OSSG scan')
                }
            }
            steps {
                echo "Executing OSSG scan..."
                sleep(time: 8, unit: 'SECONDS')
            }
        }

        stage('Build') {
            when {
                expression {
                    def approvedList = env.APPROVED_STAGES_STR ? env.APPROVED_STAGES_STR.split(',') as List : []
                    return approvedList.contains('Build')
                }
            }
            steps {
                echo "Executing Build..."
                sleep(time: 15, unit: 'SECONDS')
            }
        }

        stage('Push') {
            when {
                expression {
                    def approvedList = env.APPROVED_STAGES_STR ? env.APPROVED_STAGES_STR.split(',') as List : []
                    return approvedList.contains('Push')
                }
            }
            steps {
                echo "Executing Push..."
                sleep(time: 7, unit: 'SECONDS')
            }
        }

        stage('Vulnerability scan') {
            when {
                expression {
                    def approvedList = env.APPROVED_STAGES_STR ? env.APPROVED_STAGES_STR.split(',') as List : []
                    return approvedList.contains('Vulnerability scan')
                }
            }
            steps {
                echo "Executing Vulnerability scan..."
                sleep(time: 10, unit: 'SECONDS')
            }
        }

        stage('Sign container') {
            when {
                expression {
                    def approvedList = env.APPROVED_STAGES_STR ? env.APPROVED_STAGES_STR.split(',') as List : []
                    return approvedList.contains('Sign container')
                }
            }
            steps {
                echo "Executing Sign container..."
                sleep(time: 3, unit: 'SECONDS')
            }
        }

        stage('Manage and sync with ArgoCD') {
            when {
                expression {
                    def approvedList = env.APPROVED_STAGES_STR ? env.APPROVED_STAGES_STR.split(',') as List : []
                    return approvedList.contains('Manage and sync with ArgoCD')
                }
            }
            steps {
                echo "Executing Manage and sync with ArgoCD..."
                sleep(time: 5, unit: 'SECONDS')
            }
        }

        stage('Post deploy') {
            when {
                expression {
                    def approvedList = env.APPROVED_STAGES_STR ? env.APPROVED_STAGES_STR.split(',') as List : []
                    return approvedList.contains('Post deploy')
                }
            }
            steps {
                echo "Executing Post deploy..."
                sleep(time: 4, unit: 'SECONDS')
            }
        }

        stage('Update APIHub') {
            when {
                expression {
                    def approvedList = env.APPROVED_STAGES_STR ? env.APPROVED_STAGES_STR.split(',') as List : []
                    return approvedList.contains('Update APIHub')
                }
            }
            steps {
                echo "Executing Update APIHub..."
                sleep(time: 3, unit: 'SECONDS')
            }
        }

        stage('Dast passive scan') {
            when {
                expression {
                    def approvedList = env.APPROVED_STAGES_STR ? env.APPROVED_STAGES_STR.split(',') as List : []
                    return approvedList.contains('Dast passive scan')
                }
            }
            steps {
                echo "Executing Dast passive scan..."
                sleep(time: 8, unit: 'SECONDS')
            }
        }

        stage('Dast cryptography scan') {
            when {
                expression {
                    def approvedList = env.APPROVED_STAGES_STR ? env.APPROVED_STAGES_STR.split(',') as List : []
                    return approvedList.contains('Dast cryptography scan')
                }
            }
            steps {
                echo "Executing Dast cryptography scan..."
                sleep(time: 7, unit: 'SECONDS')
            }
        }

        stage('Promote image') {
            when {
                expression {
                    def approvedList = env.APPROVED_STAGES_STR ? env.APPROVED_STAGES_STR.split(',') as List : []
                    return approvedList.contains('Promote image')
                }
            }
            steps {
                echo "Executing Promote image..."
                sleep(time: 5, unit: 'SECONDS')
            }
        }
    }
}