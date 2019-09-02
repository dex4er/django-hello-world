cat << END > /etc/apt/apt.conf.d/00no_install_recommends
APT::Get::Assume-Yes "true";
APT::Get::Fix-Broken "true";
APT::Install-Recommends "false";
END

. /etc/lsb-release

cat << END > /etc/apt/sources.list
deb ${APT_URL:-mirror://mirrors.ubuntu.com/mirrors.txt} ${DISTRIB_CODENAME} main restricted universe
deb ${APT_URL:-mirror://mirrors.ubuntu.com/mirrors.txt} ${DISTRIB_CODENAME}-updates main restricted universe
deb ${APT_URL:-mirror://mirrors.ubuntu.com/mirrors.txt} ${DISTRIB_CODENAME}-security main restricted universe
END

apt-get update
