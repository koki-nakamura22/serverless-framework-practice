# test-service1

## Plugins

### Install
```sh
sls plugin install -n serverless-prune-plugin
sls plugin install -n serverless-offline
```

### Usage
Add installed plugin names to the plugins section in your serverless.yml.
e.g.
```yaml
plugins:
  - serverless-prune-plugin
  - serverless-offline
```

#### serverless-prune-plugin
Add settings to your serverless.yml that is like the bellow.
e.g.
```yaml
custom:
  prune:
    automatic: true # デプロイ時にserverless-prune-pluginを自動で動作させる
    number: 3 # AWS Lambda上で管理される世代の最大数
```

#### serverless-offline
```sh
serverless offline start --apiKey [Your API KEY]
```
