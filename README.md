Ansible Role: mplachter.swapfile
=========

This ansible role creates and configures Linux swapfiles.

Requirements
------------

Sufficient disk space to hold the swap file.

* Running
  * Ansible 2.3+
* Testing
  * Docker
  * Molecule = 1.2.5
    * Ansible 2.3.2.0 (Ansible-lint)

Role Variables
--------------

* `swapfile_Dir: /` : Directory where the swapfile will be created
* `swapfile_Name: swapfile` : Name of the swapfile
* `swapsize_MB: 1024` : Size of swapfile (MiB)
* `swap_swappiness: 30` : Set the value of vm.swappiness. [Linux Kernel Docs](https://www.kernel.org/doc/Documentation/sysctl/vm.txt)

Example Playbook
----------------


    - hosts: servers
      roles:
         - { role: mplachter.swapfile }

License
-------

MIT

Author Information
------------------

Matthew Plachter
