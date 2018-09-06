# Setting up jenkins



#### JENKINS Installation steps:
sudo add-apt-repository ppa:webupd8team/java
sudo apt update
sudo apt install oracle-java8-installer
sudo apt install oracle-java8-set-default
javac -version
cd /tmp && wget -q -O - https://pkg.jenkins.io/debian-stable/jenkins.io.key | sudo apt-key add -
echo 'deb https://pkg.jenkins.io/debian-stable binary/' | sudo tee -a /etc/apt/sources.list.d/jenkins.list
sudo apt update
sudo apt install jenkins
sudo systemctl stop jenkins.service
sudo systemctl start jenkins.service
sudo systemctl enable jenkins.service

#### Check your password:

cat /var/lib/jenkins/secrets/initialAdminPassword

#### Plugins You Need: 


#### Install aws cli & Configure:


	

#### Pip Packages:

open bashrc add

```
alias python=python3"
```
save and exit

```
# Pip Locale Setting
export LC_ALL="en_US.UTF-8"
export LC_CTYPE="en_US.UTF-8"
sudo dpkg-reconfigure locales

python -m pip install ecs-deploy
python -m pip install dokr
```

### Jenkins Plugin

+ Parameterized+Build
+ Git+Parameter+Plugin
+ Pre SCM BuildStep
+ Slack Notification

#### Refernce Link:

Installation Steps:
+ https://websiteforstudents.com/install-jenkins-on-ubuntu-16-04-17-10-18-04-lts-server/

Pip Locale Error: 
+ https://stackoverflow.com/questions/14547631/python-locale-error-unsupported-locale-setting
