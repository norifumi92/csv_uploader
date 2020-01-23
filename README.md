### Setup Guidelines
---

If you use Vagrant, make sure the following version of Vagrant and Virtual Box was installed.

| Tables        | Link           |Version           |
| ------------- |:-------------:|:-------------:| 
| Vagrant      | https://www.vagrantup.com/downloads.html | 2.2.6 | 
| Virtualbox      | https://www.virtualbox.org/wiki/Download_Old_Builds_6_0      | 6.0.16 |

After running `vagrant up`, make sure the version of `python` and `sqlite3`:
 
```sh
$ vagrant ssh
# python version : 3.6
$ python --version
# sqlite3 version : 3.29.0
$ sqlite3 --version
```