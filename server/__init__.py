import os, yaml

if os.environ.get('DEVELOPMENT_ENVIRONMENT') != 'production':
  file = open('config/secrets.yml')
  dataMap = yaml.load(file)
  file.close()
  for key, value in dataMap.items():
    os.environ[key] = value