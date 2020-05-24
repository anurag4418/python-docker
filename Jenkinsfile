node{
    stage('Python-Docker'){
        echo 'Hello World'
    }
    stage('SCM Checkout'){
        git 'https://github.com/anurag4418/python-docker.git'
    }
	stage('python-docker-build'){
	    sshPublisher(publishers: [sshPublisherDesc(configName: 'docker_host', transfers: [sshTransfer(cleanRemote: false, excludes: '', execCommand: 'docker build -t anuragjunghare/python-docker:${BUILD_NUMBER} .', execTimeout: 120000, flatten: false, makeEmptyDirs: false, noDefaultExcludes: false, patternSeparator: '[, ]+', remoteDirectory: '//home//anurag_junghare', remoteDirectorySDF: false, removePrefix: '', sourceFiles: 'Dockerfile, insert-script.py')], usePromotionTimestamp: false, useWorkspaceInPromotion: false, verbose: false)])
	}
	stage('python-docker-run'){
	    sshPublisher(publishers: [sshPublisherDesc(configName: 'docker_host', transfers: [sshTransfer(cleanRemote: false, excludes: '', execCommand: 'docker rm -f python-app || true', execTimeout: 120000, flatten: false, makeEmptyDirs: false, noDefaultExcludes: false, patternSeparator: '[, ]+', remoteDirectory: '//home//anurag_junghare', remoteDirectorySDF: false, removePrefix: '', sourceFiles: 'Dockerfile, insert-script.py'), sshTransfer(cleanRemote: false, excludes: '', execCommand: 'docker run -d --name python-app --link my-mysql anuragjunghare/python-docker:${BUILD_NUMBER}', execTimeout: 120000, flatten: false, makeEmptyDirs: false, noDefaultExcludes: false, patternSeparator: '[, ]+', remoteDirectory: '//home//lokesh', remoteDirectorySDF: false, removePrefix: '', sourceFiles: '')], usePromotionTimestamp: false, useWorkspaceInPromotion: false, verbose: false)])
	}
}
