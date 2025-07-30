# -*- mode: ruby -*-
# vi: set ft=ruby :

unless Vagrant.has_plugin?("vagrant-vbguest", "0.30.0")
  system("vagrant plugin install vagrant-vbguest --plugin-version 0.30.0")
  puts "Dependencies installed, please try the command again."
  exit
end

Vagrant.configure("2") do |config|
    if Vagrant.has_plugin?("vagrant-vbguest")
        config.vbguest.auto_update = false
    end
    config.vm.box = "debian/bullseye64"

	# Configure VM Ram usage
    config.vm.provider :virtualbox do |v|
        v.memory = 4096
        v.customize ["modifyvm", :id, "--ioapic", "on"]
        v.cpus = 2
        v.customize ["modifyvm", :id, "--natdnshostresolver1", "on"]
        v.customize ["modifyvm", :id, "--natdnsproxy1", "on"]

    end


	# Forward a port from the guest to the host, which allows for outside
	# computers to access the VM, whereas host only networking does not.
	config.vm.network "forwarded_port", guest: 8000, host: 2255, auto_correct: true
    config.vm.network "forwarded_port", guest: 9200, host: 9200, auto_correct: true
    config.vm.network "forwarded_port", guest: 5432, host: 5432, auto_correct: true
    config.vm.network "forwarded_port", guest: 5601, host: 5601, auto_correct: true

	# Share an additional folder to the guest VM. The first argument is
	# an identifier, the second is the path on the guest to mount the
	# folder, and the third is the path on the host to the actual folder.
	config.vm.synced_folder ".", "/home/vagrant/smartshop"

	# Enable provisioning with a shell script.
	config.vm.provision :shell, :path => "etc/install/install.sh", :args => "smartshop", :binary => true
	config.vm.synced_folder ".", "/vagrant", disabled: true
	config.vm.synced_folder "etc/redis/", "/etc/redis/"
    config.vm.provision :shell, run: "always", :path => "etc/install/startup.sh", :privileged => false, :binary => true
end
