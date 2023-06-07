# python-flask

```
codeql database create codeql-db --language=python --overwrite
codeql database analyze codeql-db codeql/python-queries:codeql-suites/python-security-experimental.qls --format=sarif-latest --output=codeql-results.sarif
```
