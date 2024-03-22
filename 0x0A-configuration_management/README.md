Puppet Configuration Management Example
This repository contains Puppet manifests to demonstrate basic configuration management tasks using Puppet. The provided manifests solve three tasks:

Task 1: Create a File
The manifest 0-create_a_file.pp creates a file named school in the /tmp directory with specific permissions, owner, group, and content.

To apply the manifest:

bash
Copy code
puppet apply 0-create_a_file.pp
Task 2: Install a Package
The manifest 1-install_a_package.pp installs the Flask package from pip3, ensuring that it is version 2.1.0.

To apply the manifest:

bash
Copy code
sudo puppet apply 1-install_a_package.pp
Task 3: Kill a Process
The manifest 2-kill_a_process.pp kills a process named killmenow using the pkill command.

To apply the manifest:

bash
Copy code
sudo puppet apply 2-kill_a_process.pp
Each manifest contains comments to explain the purpose and usage of the Puppet code. Additionally, the README provides instructions on how to apply each manifest to achieve the desired configuration management tasks.
