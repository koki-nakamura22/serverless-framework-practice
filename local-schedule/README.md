# local-schedule

## Plugins

### Install
```sh
sls plugin install -n serverless-local-schedule
sls plugin install -n serverless-dynamodb-local
sls dynamodb install
sls plugin install -n serverless-offline
```

### Usage

#### serverless-dynamodb-local
1. Install DynamoDB to local
```sh
sls dynamodb install
```

2. Launch DynamoDB on local.  
Only DynamoDB.
```sh
sls dynamodb start
```

With serverless-framework.
```sh
sls offline start
```

#### serverless-offline
Launch with dynamodb-local.
```sh
sls offline start --apiKey [Your API KEY]
```

## GUI Tools for DynamoDB Local
- NoSQL Workbench  
[Download NoSQL Workbench Link](https://docs.aws.amazon.com/ja_jp/amazondynamodb/latest/developerguide/workbench.settingup.html)  
[NoSQL Workbench Reference](https://docs.aws.amazon.com/ja_jp/amazondynamodb/latest/developerguide/workbench.html)  
This tool is for data display only.

- dynamodb-admin  
[dynamodb-admin](https://www.npmjs.com/package/dynamodb-admin)

## References
- [Serverless Local Schedule](https://www.serverless.com/plugins/serverless-local-schedule)
- [serverless-dynamodb-local](https://www.serverless.com/plugins/serverless-dynamodb-local)
