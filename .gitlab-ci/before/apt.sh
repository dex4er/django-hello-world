cat << END > /etc/apt/apt.conf.d/00no_install_recommends
APT::Install-Recommends "false";
END

apt-get update
