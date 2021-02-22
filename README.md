# Interlink

Interlink is a way to remotely execute python scripts on a host machine.

## Installation
Clone the repository and modify the config files found in 'config/'
### config
- Username: valid usernames
- Password: valid passwords
- Dir: Directory of your python project folders
- Address: Host address
- Port: Port to open on host
### node-config
- Username: Username to log into the host with
- Password: Password to log into the host with
- Address: Address of the Host
- Port: Port of the Host

## Usage
### Host
Run 'host.py' on the remote server you want access to
### Node
Import 'node.py' on any machine you want to integrate host access to, for example
```Python
import node
node.send('command, *args')
```
### Terminal Access
Run 'terminal.py' to remotely log into the host

## Contributing
Contributing is greatly appreciated, please contact one of the team members to get started working on the codebase.
