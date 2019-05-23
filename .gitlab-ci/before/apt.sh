cat << END > /etc/apt/apt.conf.d/00no_install_recommends
APT::Get::Assume-Yes "true";
APT::Get::Fix-Broken "true";
APT::Install-Recommends "false";
END

apt-get update
