# serverless-framework-practice
## Environment
- Ubuntu 20.04 (WSL2)
- VS Code

## Requirements
- pyenv
- Python 3.8.7
- Yarn

## Troubleshooting
### Signature expired
```sh
Signature expired: 20211219T032530Z is now earlier than 20211219T040811Z (20211219T041311Z - 5 min.)
```
When displaying an error message that likes the above, execute the below command.
```sh
sudo ntpdate -v ntp.nict.jp
```
