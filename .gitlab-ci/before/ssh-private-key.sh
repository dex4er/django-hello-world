test -n "$SSH_PRIVATE_KEY" || exit 1

apt-get -y install openssh-client

mkdir -p ~/.ssh
printf "Host *\n\tStrictHostKeyChecking no\n\n" > ~/.ssh/config
set +x
echo "$SSH_PRIVATE_KEY" > ~/.ssh/id_rsa
set -x
chmod 600 ~/.ssh/id_rsa
eval $(ssh-agent -s)
ssh-add ~/.ssh/id_rsa