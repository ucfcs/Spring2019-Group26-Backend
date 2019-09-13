# TODO: update to auto deploy on provision

# -*- mode: ruby -*-
# vi: set ft=ruby :


VAGRANTFILE_API_VERSION = "2"
Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|

  config.ssh.username = "vagrant"
  config.ssh.forward_agent = true
  config.vm.provision :shell, :path => "install.sh", :privileged => true

  name = "sd2"
  memory = "1024"
  cpus = "2"
  size = "50GB"


  config.vm.define "sd2", primary: true do |u64|
    #u64.vm.network "private_network", ip: "10.10.10.20"
    config.vm.network "forwarded_port", guest: 80, host: 8080, host_ip: "127.0.0.1"
    config.vm.network "forwarded_port", guest: 5000, host: 1337, host_ip: "127.0.0.1"
    u64.vm.provider "virtualbox" do |vb, override|
      override.vm.box ="ubuntu/bionic64"
      # Sync a folder between the host and all guests.
      # Uncomment this line (and adjust as you like)
      override.vm.synced_folder "../Spring2019-Group26-Backend/", "/home/vagrant/Spring2019-Group26-Backend", owner: "vagrant", group: "vagrant"

      # Change disksize to adjust storage space
      # Uncomment this line change size above to your liking
      #override.disksize.size = size
      vb.name = name
      vb.memory = memory
      vb.cpus = cpus

      vb.gui = false
    end
  end
end
