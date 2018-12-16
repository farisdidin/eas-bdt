# EAS Basis Data Terdistribusi 2018
### Muhammad Faris Didin Andiyar 

## Content :
### 1. Konfigurasi Server
### 2. Konfigurasi Aplikasi
### 3. Skenario Pengujian Beban


## Konfigurasi Server
### Arsitektur  
![alt text](asset/img/eas&#32;bdt.png)

### MySQL Cluster  
![Vagrantfile](mysql-cluster/Vagrantfile)  
Terdiri dari tiga buah node MySQL dan satu ProxySQL yang menggunakan box  ```bento/ubuntu-16.04```.
```ruby
# -*- mode: ruby -*-
# vi: set ft=ruby :

# All Vagrant configuration is done below. The "2" in Vagrant.configure
# configures the configuration version (we support older styles for
# backwards compatibility). Please don't change it unless you know what
# you're doing.

Vagrant.configure("2") do |config|
  
  # MySQL Cluster dengan 3 node
  (1..3).each do |i|
    config.vm.define "eas-db#{i}" do |node|
      node.vm.hostname = "eas-db#{i}"
      node.vm.box = "bento/ubuntu-16.04"
      node.vm.network "private_network", ip: "192.168.33.1#{i}"

      # Opsional. Edit sesuai dengan nama network adapter di komputer
      node.vm.network "public_network", bridge: "wlp2s0"
      
      node.vm.provider "virtualbox" do |vb|
        vb.name = "eas-db#{i}"
        vb.gui = false
        vb.memory = "512"
      end
  
      node.vm.provision "shell", path: "deployMySQL1#{i}.sh", privileged: false
    end
  end

  config.vm.define "eas-proxy2" do |proxy2|
    proxy2.vm.hostname = "eas-proxy2"
    proxy2.vm.box = "bento/ubuntu-16.04"
    proxy2.vm.network "private_network", ip: "192.168.33.10"
    proxy2.vm.network "public_network",  bridge: "wlp2s0"
    
    proxy2.vm.provider "virtualbox" do |vb|
      vb.name = "eas-proxy2"
      vb.gui = false
      vb.memory = "512"
    end

    proxy2.vm.provision "shell", path: "deployProxySQL.sh", privileged: false
  end

end

```  
[Provision node MySQL DB](mysql-cluster/deployMySQL11.sh)  
```bash
sudo apt-get update
sudo apt-get install libaio1
sudo apt-get install libmecab2
curl -OL https://dev.mysql.com/get/Downloads/MySQL-5.7/mysql-common_5.7.23-1ubuntu16.04_amd64.deb
curl -OL https://dev.mysql.com/get/Downloads/MySQL-5.7/mysql-community-client_5.7.23-1ubuntu16.04_amd64.deb
curl -OL https://dev.mysql.com/get/Downloads/MySQL-5.7/mysql-client_5.7.23-1ubuntu16.04_amd64.deb
curl -OL https://dev.mysql.com/get/Downloads/MySQL-5.7/mysql-community-server_5.7.23-1ubuntu16.04_amd64.deb
sudo debconf-set-selections <<< 'mysql-community-server mysql-community-server/root-pass password admin'
sudo debconf-set-selections <<< 'mysql-community-server mysql-community-server/re-root-pass password admin'
sudo dpkg -i mysql-common_5.7.23-1ubuntu16.04_amd64.deb
sudo dpkg -i mysql-community-client_5.7.23-1ubuntu16.04_amd64.deb
sudo dpkg -i mysql-client_5.7.23-1ubuntu16.04_amd64.deb
sudo dpkg -i mysql-community-server_5.7.23-1ubuntu16.04_amd64.deb
sudo ufw allow 33061
sudo ufw allow 3306
sudo cp /vagrant/my11.cnf /etc/mysql/my.cnf
sudo service mysql restart
sudo mysql -u root -padmin < /vagrant/cluster_bootstrap.sql
sudo mysql -u root -padmin < /vagrant/addition_to_sys.sql
sudo mysql -u root -padmin < /vagrant/create_proxysql_user.sql
```
