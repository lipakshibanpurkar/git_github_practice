pipeline{
agent any
stages{
stages('Clone Repo'){
steps{
git 'https://github.com/lipakshibanpurkar/git_github_practice.git'
}}
stage ('Insall Dependencies'){
step{
sh 'pip install -r requirement.txt'
}}
stage('Run Tests'){
step{
sh 'pytest'
}}

stage('Build'){
staps{
echo 'Build Successful'
}}
stage('Run App'){
    steps{
        sh 'nohup python app.py'
    }
}
}
}


