pipeline {
    agent any

    stages {
        stage('AI Optimization Evaluation') {
            steps {
                script {
                    // Fetch the diff safely using returnStdout
                    def actualDiff = sh(
                        script: "git diff HEAD~1 HEAD || echo 'No diff available'",
                        returnStdout: true
                    ).trim()

                    if (!actualDiff) {
                        actualDiff = "No diff available or initial commit."
                    }

                    // Escape quotes for the JSON payload safely
                    def escapedDiff = actualDiff.replace('"', '\\"').replace('\n', '\\n').replace('\r', '')
                    def payload = "{\"code_diff\": \"${escapedDiff}\"}"

                    def approvedStages = []
                    try {
                        def jsonOutput = sh(
                            script: """curl -s -X POST -H 'Content-Type: application/json' -d '${payload}' http://host.docker.internal:8000/evaluate_stages""",
                            returnStdout: true
                        ).trim()

                        def matcher = jsonOutput =~ /"approved_stages"\s*:\s*\[(.*?)\]/
                        if (matcher) {
                            def stagesStr = matcher[0][1]
                            approvedStages = stagesStr.split(',').collect { it.trim().replaceAll('^"|"$', '') }.findAll { it }
                        } else {
                            approvedStages = []
                        }

                        echo "AI Approved Stages to run: ${approvedStages}"
                    } catch (err) {
                        echo "Warning: AI optimization service failed. Running fallback stages. Error: ${err.message}"
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

        stage('Validate') {
            when {
                expression { env.APPROVED_STAGES_STR.contains('Validate') }
            }
            steps {
                echo "Executing Validate..."
                sleep(time: 3, unit: 'SECONDS')
            }
        }

        stage('Validate base image signatures') {
            when {
                expression { env.APPROVED_STAGES_STR.contains('Validate base image signatures') }
            }
            steps {
                echo "Executing Validate base image signatures..."
                sleep(time: 4, unit: 'SECONDS')
            }
        }

        stage('Static code analysis') {
            when {
                expression { env.APPROVED_STAGES_STR.contains('Static code analysis') }
            }
            steps {
                echo "Executing Static code analysis..."
                sleep(time: 10, unit: 'SECONDS')
            }
        }

        stage('Start Database') {
            when {
                expression { env.APPROVED_STAGES_STR.contains('Start Database') }
            }
            steps {
                echo "Executing Start Database..."
                sleep(time: 5, unit: 'SECONDS')
            }
        }

        stage('Pod operations') {
            when {
                expression { env.APPROVED_STAGES_STR.contains('Pod operations') }
            }
            steps {
                echo "Executing Pod operations..."
                sleep(time: 6, unit: 'SECONDS')
            }
        }

        stage('Certificate') {
            when {
                expression { env.APPROVED_STAGES_STR.contains('Certificate') }
            }
            steps {
                echo "Executing Certificate..."
                sleep(time: 2, unit: 'SECONDS')
            }
        }

        stage('OSSG scan') {
            when {
                expression { env.APPROVED_STAGES_STR.contains('OSSG scan') }
            }
            steps {
                echo "Executing OSSG scan..."
                sleep(time: 8, unit: 'SECONDS')
            }
        }

        stage('Build') {
            when {
                expression { env.APPROVED_STAGES_STR.contains('Build') }
            }
            steps {
                echo "Executing Build..."
                sleep(time: 15, unit: 'SECONDS')
            }
        }

        stage('Push') {
            when {
                expression { env.APPROVED_STAGES_STR.contains('Push') }
            }
            steps {
                echo "Executing Push..."
                sleep(time: 7, unit: 'SECONDS')
            }
        }

        stage('Vulnerability scan') {
            when {
                expression { env.APPROVED_STAGES_STR.contains('Vulnerability scan') }
            }
            steps {
                echo "Executing Vulnerability scan..."
                sleep(time: 10, unit: 'SECONDS')
            }
        }

        stage('Sign container') {
            when {
                expression { env.APPROVED_STAGES_STR.contains('Sign container') }
            }
            steps {
                echo "Executing Sign container..."
                sleep(time: 3, unit: 'SECONDS')
            }
        }

        stage('Manage and sync with ArgoCD') {
            when {
                expression { env.APPROVED_STAGES_STR.contains('Manage and sync with ArgoCD') }
            }
            steps {
                echo "Executing Manage and sync with ArgoCD..."
                sleep(time: 5, unit: 'SECONDS')
            }
        }

        stage('Post deploy') {
            when {
                expression { env.APPROVED_STAGES_STR.contains('Post deploy') }
            }
            steps {
                echo "Executing Post deploy..."
                sleep(time: 4, unit: 'SECONDS')
            }
        }

        stage('Update APIHub') {
            when {
                expression { env.APPROVED_STAGES_STR.contains('Update APIHub') }
            }
            steps {
                echo "Executing Update APIHub..."
                sleep(time: 3, unit: 'SECONDS')
            }
        }

        stage('Dast passive scan') {
            when {
                expression { env.APPROVED_STAGES_STR.contains('Dast passive scan') }
            }
            steps {
                echo "Executing Dast passive scan..."
                sleep(time: 8, unit: 'SECONDS')
            }
        }

        stage('Dast cryptography scan') {
            when {
                expression { env.APPROVED_STAGES_STR.contains('Dast cryptography scan') }
            }
            steps {
                echo "Executing Dast cryptography scan..."
                sleep(time: 7, unit: 'SECONDS')
            }
        }

        stage('Promote image') {
            when {
                expression { env.APPROVED_STAGES_STR.contains('Promote image') }
            }
            steps {
                echo "Executing Promote image..."
                sleep(time: 5, unit: 'SECONDS')
            }
        }
    }
}