these script allows transforming dextorm yaml files in command line argements and vice-versa

```bash
$ ./to_cli.py dextorm.yaml 
--app.instrumentedPackage=fr.pantheonsorbonne --app.sourceRootDir=src/main/java --app.publisher=console1 --app.issueCollector=basic-cli-uni --app.diffAlgorithm=g --differs.g.diffAlgorithm=GUMTREE --differs.g.methods=False --differs.g.instructions=True --differs.b.diffAlgorithm=BLAME --differs.b.methods=False --differs.b.instructions=True --issueCollectors.github.basic-cli-uni.gitHubRepoName=nh-group/basic-cli-uni --issueCollectors.github.basic-cli-uni.branch=master --issueCollectors.github.dummy.gitHubRepoName=nherbaut/dextorm-dummy-project --issueCollectors.github.dummy.repoAddress=file:///home/nherbaut/tmp/dextorm-dummy-project.git --issueCollectors.github.dummy.branch=master --publishers.grpcPublishers.grpc1.host=localhost --publishers.grpcPublishers.grpc1.port=8081 --publishers.filePublishers.console1.filePath=stdout --publishers.restPublishers.rest1.baseUrl=http://localhost:3000/coverage/issue/all
```

```bash
$ ./to_yaml.py --app.instrumentedPackage=fr.pantheonsorbonne --app.sourceRootDir=src/main/java --app.publisher=console1 --app.issueCollector=basic-cli-uni --app.diffAlgorithm=g --differs.g.diffAlgorithm=GUMTREE --differs.g.methods=False --differs.g.instructions=True --differs.b.diffAlgorithm=BLAME --differs.b.methods=False --differs.b.instructions=True --issueCollectors.github.basic-cli-uni.gitHubRepoName=nh-group/basic-cli-uni --issueCollectors.github.basic-cli-uni.branch=master --issueCollectors.github.dummy.gitHubRepoName=nherbaut/dextorm-dummy-project --issueCollectors.github.dummy.repoAddress=file:///home/nherbaut/tmp/dextorm-dummy-project.git --issueCollectors.github.dummy.branch=master --publishers.grpcPublishers.grpc1.host=localhost --publishers.grpcPublishers.grpc1.port=8081 --publishers.filePublishers.console1.filePath=stdout --publishers.restPublishers.rest1.baseUrl=http://localhost:3000/coverage/issue/all
```
```yaml
app:
  diffAlgorithm: g
  instrumentedPackage: fr.pantheonsorbonne
  issueCollector: basic-cli-uni
  publisher: console1
  sourceRootDir: src/main/java
differs:
  b:
    diffAlgorithm: BLAME
    instructions: 'True'
    methods: 'False'
  g:
    diffAlgorithm: GUMTREE
    instructions: 'True'
    methods: 'False'
issueCollectors:
  github:
    basic-cli-uni:
      branch: master
      gitHubRepoName: nh-group/basic-cli-uni
    dummy:
      branch: master
      gitHubRepoName: nherbaut/dextorm-dummy-project
      repoAddress: file:///home/nherbaut/tmp/dextorm-dummy-project.git
publishers:
  filePublishers:
    console1:
      filePath: stdout
  grpcPublishers:
    grpc1:
      host: localhost
      port: '8081'
  restPublishers:
    rest1:
      baseUrl: http://localhost:3000/coverage/issue/all
```
