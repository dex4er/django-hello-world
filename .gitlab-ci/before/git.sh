apt-get install ca-certificates git git-lfs

git config --global user.email "gitlab-ci@$HOSTNAME"
git config --global user.name  "GitLab CI $CI_RUNNER_DESCRIPTION"
git config --global push.default current

git lfs install
git config --global lfs.locksverify false
